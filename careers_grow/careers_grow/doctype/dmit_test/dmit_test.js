// Copyright (c) 2025, Touhid Mullick and contributors
// For license information, please see license.txt

frappe.ui.form.on("DMIT Test", {
	refresh(frm) {
		setup_table(frm, "management_skills", "Management Skill", "management_skill");
		setup_table(frm, "subject_selection_suitability", "Subject", "subject");
		setup_table(frm, "departments", "Department Suitability", "department");
		setup_table(frm, "activity_interest", "Activity Interest", "activity");
	},
	validate(frm) {
		frm.meta.fields.forEach((field) => {
			if (field.fieldtype === "Percent") {
				const value = frm.doc[field.fieldname];
				if (value != null && (value < 0 || value > 100)) {
					frappe.msgprint(__("Value for {0} must be between 0 and 100", [field.label]));
					frappe.validated = false;
				}
			}
		});

		const child_tables = [
			"management_skills",
			"subject_selection_suitability",
			"departments",
			"activity_interest",
		];
		child_tables.forEach((table) => {
			(frm.doc[table] || []).forEach((row) => {
				if (row.score != null && (row.score < 0 || row.score > 10)) {
					frappe.msgprint(
						__("Score in table {0} row {1} must be between 0 and 10", [table, row.idx])
					);
					frappe.validated = false;
				}
			});
		});
	},
});

function setup_table(frm, table_field, master_doctype, link_field) {
	// Disable Row addition and deletion
	frm.set_df_property(table_field, "cannot_add_rows", true);
	frm.set_df_property(table_field, "cannot_delete_rows", true);

	frappe.call({
		method: "frappe.client.get_list",
		args: {
			doctype: master_doctype,
			fields: ["name"],
			order_by: "name asc",
		},
		callback: function (r) {
			if (r.message) {
				const existing_rows = frm.doc[table_field] || [];
				const existing_ids = new Set(existing_rows.map((row) => row[link_field]));

				r.message.forEach((record) => {
					if (!existing_ids.has(record.name)) {
						let row = frm.add_child(table_field);
						row[link_field] = record.name;
						row.score = 0;
					}
				});

				// Sort by link field
				if (frm.doc[table_field]) {
					frm.doc[table_field].sort((a, b) => {
						return (a[link_field] || "").localeCompare(b[link_field] || "");
					});

					// Update idx
					frm.doc[table_field].forEach((row, index) => {
						row.idx = index + 1;
					});

					frm.refresh_field(table_field);
				}
			}
		},
	});
}
