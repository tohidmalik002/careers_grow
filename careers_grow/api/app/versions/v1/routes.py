ROUTES = {
    "login": {
        "func": "careers_grow.api.app.versions.v1.handlers.auth.login",
        "methods": ["POST"],
        "auth_required": False
    },
    "get_one": {
        "func": "careers_grow.api.app.versions.v1.handlers.utils.get_one",
        "methods": ["GET"],
        "auth_required": False
    }
}
