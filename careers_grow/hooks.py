app_name = "careers_grow"
app_title = "Careers Grow"
app_publisher = "Touhid Mullick"
app_description = "Careers Grow"
app_email = "tohidmalik002@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "careers_grow",
# 		"logo": "/assets/careers_grow/logo.png",
# 		"title": "Careers Grow",
# 		"route": "/careers_grow",
# 		"has_permission": "careers_grow.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/careers_grow/css/careers_grow.css"
# app_include_js = "/assets/careers_grow/js/careers_grow.js"

# include js, css files in header of web template
# web_include_css = "/assets/careers_grow/css/careers_grow.css"
# web_include_js = "/assets/careers_grow/js/careers_grow.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "careers_grow/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "careers_grow/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "careers_grow.utils.jinja_methods",
# 	"filters": "careers_grow.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "careers_grow.install.before_install"
# after_install = "careers_grow.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "careers_grow.uninstall.before_uninstall"
# after_uninstall = "careers_grow.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "careers_grow.utils.before_app_install"
# after_app_install = "careers_grow.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "careers_grow.utils.before_app_uninstall"
# after_app_uninstall = "careers_grow.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "careers_grow.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"careers_grow.tasks.all"
# 	],
# 	"daily": [
# 		"careers_grow.tasks.daily"
# 	],
# 	"hourly": [
# 		"careers_grow.tasks.hourly"
# 	],
# 	"weekly": [
# 		"careers_grow.tasks.weekly"
# 	],
# 	"monthly": [
# 		"careers_grow.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "careers_grow.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "careers_grow.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "careers_grow.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["careers_grow.utils.before_request"]
# after_request = ["careers_grow.utils.after_request"]

# Job Events
# ----------
# before_job = ["careers_grow.utils.before_job"]
# after_job = ["careers_grow.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"careers_grow.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
