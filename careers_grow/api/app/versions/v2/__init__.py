import frappe

from careers_grow.app.api.versions.base import BaseVersion
from careers_grow.app.api.v2.routes import ROUTES

class V2(BaseVersion):
    version = "v2"
    routes = ROUTES
