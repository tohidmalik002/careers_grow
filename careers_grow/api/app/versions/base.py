import frappe

class BaseVersion:
    version = None
    routes = {}

    def get_route(self, method):
        return self.routes.get(method)

    def authenticate(self, route):
        raise NotImplementedError

    def success(self, data):
        frappe.local.response.update({
            "success": True,
            "data": data
        })

    def error(self, message, status=500):
        frappe.local.response["http_status_code"] = status
        frappe.local.response.update({
            "success": False,
            "message": message
        })

    def dispatch(self, route, request):
        raise NotImplementedError