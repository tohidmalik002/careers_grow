// Copyright (c) 2025, Touhid Mullick and contributors
// For license information, please see license.txt

frappe.ui.form.on("DMIT Test", {
	refresh(frm) {
		setup_table(frm, "management_skills", "Management Skill", "management_skill");
		setup_table(frm, "subject_selection_suitability", "Subject", "subject");
		setup_table(frm, "departments", "Department Suitability", "department");
		setup_table(frm, "activity_interest", "Activity Interest", "activity");
	},
});

function setup_table(frm, table_field, master_doctype, link_field) {
	// Disable Row addition and deletion
	frm.set_df_property(table_field, "cannot_add_rows", true);
	frm.set_df_property(table_field, "cannot_delete_rows", true);

	// Force refresh to ensure properties invoke
	frm.refresh_field(table_field);

	if (frm.is_new() || !frm.doc[table_field]?.length) {
		frappe.call({
			method: "frappe.client.get_list",
			args: {
				doctype: master_doctype,
				fields: ["name"],
				order_by: "name asc",
			},
			callback: function (r) {
				if (r.message) {
					frm.clear_table(table_field);
					r.message.forEach((record) => {
						let row = frm.add_child(table_field);
						row[link_field] = record.name;
						row.score = 0;
					});
					frm.refresh_field(table_field);
				}
			},
		});
	}
}
