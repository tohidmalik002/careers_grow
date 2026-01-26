# Copyright (c) 2025, Touhid Mullick and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class DMITTest(Document):
	def validate(self):
		for field in self.meta.fields:
			if field.fieldtype == "Percent":
				value = self.get(field.fieldname)
				if value is not None and (value < 0 or value > 100):
					frappe.throw(_("Value for {0} must be between 0 and 100").format(field.label))

		child_tables = [
			"management_skills",
			"subject_selection_suitability",
			"departments",
			"activity_interest",
		]
		for table in child_tables:
			for row in self.get(table) or []:
				if row.score is not None and (row.score < 0 or row.score > 10):
					frappe.throw(
						_("Score in table {0} row {1} must be between 0 and 10").format(table, row.idx)
					)
