import frappe

from careers_grow.api.app.versions.base import BaseVersion
from careers_grow.api.app.versions.v2.routes import ROUTES

class V2(BaseVersion):
    version = "v2"
    routes = ROUTES
