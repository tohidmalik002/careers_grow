// Copyright (c) 2025, Touhid Mullick and contributors
// For license information, please see license.txt

frappe.ui.form.on("App User", {
	refresh(frm) {},
	entity: function (frm) {
		if (frm.doc.entity && frm.doc.entity_type) {
			frappe.db.get_value(frm.doc.entity_type, frm.doc.entity, "full_name").then((r) => {
				if (r && r.message && r.message.full_name) {
					frm.set_value("full_name", r.message.full_name);
				}
			});
		}
	},
});
