import frappe

from careers_grow.api.app.versions.base import BaseVersion
from careers_grow.api.app.versions.v1.routes import ROUTES
from careers_grow.api.app.versions.v1.handlers.auth import authenticate_request

class V1(BaseVersion):
    version = "v1"
    routes = ROUTES

    def authenticate(self, route):
        if route.get("auth_required") != False:
            authenticate_request()

    def dispatch(self, route, payload):
        func = frappe.get_attr(route["func"])
        return func(payload)