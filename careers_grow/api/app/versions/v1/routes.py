ROUTES = {
	"login": {
		"func": "careers_grow.api.app.versions.v1.handlers.auth.login",
		"methods": ["POST"],
		"auth_required": False,
	},
	"get_one": {
		"func": "careers_grow.api.app.versions.v1.handlers.utils.get_one",
		"methods": ["GET"],
		"auth_required": True,
	},
	"get_dmit_test_data": {
		"func": "careers_grow.api.app.versions.v1.handlers.doctype.dmit_test.dmit_test.get_dmit_test_data",
		"methods": ["GET"],
		"auth_required": True,
	},
	"get_dmit_test_list": {
		"func": "careers_grow.api.app.versions.v1.handlers.doctype.dmit_test.dmit_test.get_dmit_test_list",
		"methods": ["GET"],
		"auth_required": True,
	},
}
