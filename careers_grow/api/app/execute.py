import frappe
from careers_grow.api.app.versions import VERSION_MAP

@frappe.whitelist(allow_guest=True)
def run():
    try:
        http_method = frappe.local.request.method
        payload = frappe.request.args.to_dict() if http_method == "GET" else (frappe.request.json or {})
        version_key = payload.get("version", "v1")
        method = payload.get("method")

        version = VERSION_MAP.get(version_key)
        if not version:
            frappe.throw("Unsupported API version")

        if not method:
            frappe.throw("Missing API Method")

        route = version.get_route(method)
        if not route:
            frappe.throw("Unknown API path")

        if http_method not in route.get("methods", []):
            frappe.throw("Method not allowed")

        version.authenticate(route)

        result = version.dispatch(route, payload)
        return version.success(result)

    except Exception as e:
        frappe.db.rollback()
        frappe.log_error(frappe.get_traceback(), "Dynamic API Executor Error")
        version = VERSION_MAP.get(version_key) or VERSION_MAP.get('v1')
        return version.error(str(e), getattr(e, "http_status_code", 500))