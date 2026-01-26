import frappe


def get_dmit_test_list(payload):
	user_details = frappe.local.jwt_payload

	entity_type, entity = user_details["entity_type"], user_details["entity"]

	entity_type_field_map = {
		"Student": "student_id",
		"Counsellor": "counsellor_id",
		"Franchise Partner": "franchise_id",
	}

	if not entity_type_field_map[entity_type]:
		frappe.throw("Invalid User Entity Type")

	filters = {entity_type_field_map[entity_type]: entity}

	dmit_list = frappe.get_all(
		"DMIT Test", ["student_id", "student_name", "modified"], filters, order_by="modified desc"
	)

	for r in dmit_list:
		r["student_id"] = f"({r['student_id']})"
		r["modified"] = str(r["modified"]).split(".")[0]

	return dmit_list


def get_dmit_test_data(payload):
	student_id = payload.get("student_id")
	if not student_id:
		frappe.throw("Student ID is required")
	student_id = student_id.replace("(", "").replace(")", "")

	user_details = frappe.local.jwt_payload

	entity_type, entity = user_details["entity_type"], user_details["entity"]

	filters = {}

	if entity_type == "Student":
		filters["student_id"] = entity
	elif entity_type == "Counsellor":
		filters["counsellor_id"] = entity
		filters["student_id"] = student_id
	elif entity_type == "Franchise Partner":
		filters["franchise_id"] = entity
		filters["student_id"] = student_id
	else:
		frappe.throw("Invalid User Entity Type")

	rec = frappe.get_value("DMIT Test", filters)

	if not rec:
		frappe.throw("No DMIT Test found")

	doc = frappe.get_doc("DMIT Test", rec)

	management_skills = {}
	for m in doc.management_skills:
		management_skills[
			m.management_skill.replace(" ", "_")
			.replace("-", "")
			.replace("(", "")
			.replace(")", "")
			.replace("/", "_")
			.replace("&", "and")
			.lower()
		] = m.score

	subject_selection = {}
	for s in doc.subject_selection_suitability:
		subject_selection[
			s.subject.replace(" ", "_")
			.replace("-", "")
			.replace("(", "")
			.replace(")", "")
			.replace("/", "_")
			.replace("&", "and")
			.lower()
		] = s.score

	department_suitability = {}
	for d in doc.departments:
		department_suitability[
			d.department.replace(" ", "_")
			.replace("-", "")
			.replace("(", "")
			.replace(")", "")
			.replace("/", "_")
			.replace("&", "and")
			.lower()
		] = d.score

	activity_interest = {}
	for a in doc.activity_interest:
		activity_interest[
			a.activity.replace(" ", "_")
			.replace("-", "")
			.replace("(", "")
			.replace(")", "")
			.replace("/", "_")
			.replace("&", "and")
			.lower()
		] = a.score

	res = {
		"student_name": doc.get("student_name"),
		"student_id": doc.get("student_id"),
		"counsellor_name": doc.get("counsellor_name"),
		"counsellor_id": doc.get("counsellor_id"),
		"franchise_name": doc.get("franchise_name"),
		"franchise_id": doc.get("franchise_id"),
		"mulitple_intelligences": {
			"logical": float_to_percentage_string(doc.get("mulitple_intelligence_logical")),
			"linguistic": float_to_percentage_string(doc.get("mulitple_intelligence_linguistic")),
			"interpersonal": float_to_percentage_string(doc.get("mulitple_intelligence_interpersonal")),
			"naturalistic": float_to_percentage_string(doc.get("mulitple_intelligence_naturalistic")),
			"kinesthetic": float_to_percentage_string(doc.get("mulitple_intelligence_kinesthetic")),
			"visual_spatial": float_to_percentage_string(doc.get("mulitple_intelligence_visual_spatial")),
			"intrapersonal": float_to_percentage_string(doc.get("mulitple_intelligence_intrapersonal")),
			"musical": float_to_percentage_string(doc.get("mulitple_intelligence_musical")),
		},
		"brain_dominance": {
			"left_brain": {
				"text": float_to_percentage_string(doc.get("left_brain")),
				"progress_value": doc.get("left_brain", 00.0) / 100,
			},
			"right_brain": {
				"text": float_to_percentage_string(doc.get("right_brain")),
				"progress_value": doc.get("right_brain", 00.0) / 100,
			},
			"trfc": doc.get("trfc", 00.0),
			"avg_trfc": doc.get("avg_trfc", 00.0),
		},
		"personality_type": {
			"naturalistic": float_to_percentage_string(doc.get("personality_type_naturalistic")),
			"musical": float_to_percentage_string(doc.get("personality_type_musical")),
		},
		"brain_lobes": {
			"pre_frontal": {
				"text": float_to_percentage_string(doc.get("pre_frontal_lobe")),
				"progress_value": doc.get("pre_frontal_lobe", 00.0) / 100,
			},
			"frontal": {
				"text": float_to_percentage_string(doc.get("frontal_lobe")),
				"progress_value": doc.get("frontal_lobe", 00.0) / 100,
			},
			"parietal": {
				"text": float_to_percentage_string(doc.get("parietal_lobe")),
				"progress_value": doc.get("parietal_lobe", 00.0) / 100,
			},
			"temporal": {
				"text": float_to_percentage_string(doc.get("temporal")),
				"progress_value": doc.get("temporal", 00.0) / 100,
			},
			"occipital": {
				"text": float_to_percentage_string(doc.get("occipital_lobe")),
				"progress_value": doc.get("occipital_lobe", 00.0) / 100,
			},
		},
		"neuron_distribution": {
			"left_brain": {
				"action": float_to_percentage_string(doc.get("left_brain_action")),
				"think": float_to_percentage_string(doc.get("left_brain_think")),
				"tactile": float_to_percentage_string(doc.get("left_brain_tactile")),
				"auditory": float_to_percentage_string(doc.get("left_brain_auditory")),
				"visual": float_to_percentage_string(doc.get("left_brain_visual")),
			},
			"right_brain": {
				"action": float_to_percentage_string(doc.get("right_brain_action")),
				"think": float_to_percentage_string(doc.get("right_brain_think")),
				"tactile": float_to_percentage_string(doc.get("right_brain_tactile")),
				"auditory": float_to_percentage_string(doc.get("right_brain_auditory")),
				"visual": float_to_percentage_string(doc.get("right_brain_visual")),
			},
		},
		"learning_style": {
			"auditory": {
				"text": float_to_percentage_string(doc.get("auditory")),
				"progress_value": doc.get("auditory", 00.0) / 100,
			},
			"kinesthetic": {
				"text": float_to_percentage_string(doc.get("kinesthetic")),
				"progress_value": doc.get("kinesthetic", 00.0) / 100,
			},
			"visual": {
				"text": float_to_percentage_string(doc.get("visual")),
				"progress_value": doc.get("visual", 00.0) / 100,
			},
		},
		"quotients": {
			"intelligence": float_to_percentage_string(doc.get("intelligence_quotient_iq")),
			"emotional": float_to_percentage_string(doc.get("emotional_quotient_eq")),
			"adversity": float_to_percentage_string(doc.get("adversity_quotient_aq")),
			"cultural": float_to_percentage_string(doc.get("cultural_quotient_cq")),
		},
		"management_skills": {
			"goal_setting": {
				"text": management_skills.get("goal_setting", 0),
				"progress_value": int_to_progress_value(management_skills.get("goal_setting")),
			},
			"crisis_management": {
				"text": management_skills.get("crisis_management", 0),
				"progress_value": int_to_progress_value(management_skills.get("crisis_management")),
			},
			"quality_adherence": {
				"text": management_skills.get("quality_adherence", 0),
				"progress_value": int_to_progress_value(management_skills.get("quality_adherence")),
			},
			"critical_observation": {
				"text": management_skills.get("critical_observation", 0),
				"progress_value": int_to_progress_value(management_skills.get("critical_observation")),
			},
			"creative_approach": {
				"text": management_skills.get("creative_approach", 0),
				"progress_value": int_to_progress_value(management_skills.get("creative_approach")),
			},
			"energy_level_drive": {
				"text": management_skills.get("energy_level_drive", 0),
				"progress_value": int_to_progress_value(management_skills.get("energy_level_drive")),
			},
			"strategic_planning": {
				"text": management_skills.get("strategic_planning", 0),
				"progress_value": int_to_progress_value(management_skills.get("strategic_planning")),
			},
			"leadership": {
				"text": management_skills.get("leadership", 0),
				"progress_value": int_to_progress_value(management_skills.get("leadership")),
			},
			"teamwork": {
				"text": management_skills.get("teamwork", 0),
				"progress_value": int_to_progress_value(management_skills.get("teamwork")),
			},
			"decision_making": {
				"text": management_skills.get("decision_making", 0),
				"progress_value": int_to_progress_value(management_skills.get("decision_making")),
			},
			"analytical_skills": {
				"text": management_skills.get("analytical_skills", 0),
				"progress_value": int_to_progress_value(management_skills.get("analytical_skills")),
			},
			"communication": {
				"text": management_skills.get("communication", 0),
				"progress_value": int_to_progress_value(management_skills.get("communication")),
			},
		},
		"subject_selection": {
			"civics": {
				"text": subject_selection.get("civics", 0),
				"progress_value": int_to_progress_value(subject_selection.get("civics")),
			},
			"humanities_ei": {
				"text": subject_selection.get("humanities_ei", 0),
				"progress_value": int_to_progress_value(subject_selection.get("humanities_ei")),
			},
			"foreign": {
				"text": subject_selection.get("foreign", 0),
				"progress_value": int_to_progress_value(subject_selection.get("foreign")),
			},
			"accounting": {
				"text": subject_selection.get("accounting", 0),
				"progress_value": int_to_progress_value(subject_selection.get("accounting")),
			},
			"visual_arts": {
				"text": subject_selection.get("visual_arts", 0),
				"progress_value": int_to_progress_value(subject_selection.get("visual_arts")),
			},
			"french": {
				"text": subject_selection.get("french", 0),
				"progress_value": int_to_progress_value(subject_selection.get("french")),
			},
			"english": {
				"text": subject_selection.get("english", 0),
				"progress_value": int_to_progress_value(subject_selection.get("english")),
			},
			"history": {
				"text": subject_selection.get("history", 0),
				"progress_value": int_to_progress_value(subject_selection.get("history")),
			},
			"management": {
				"text": subject_selection.get("management", 0),
				"progress_value": int_to_progress_value(subject_selection.get("management")),
			},
			"geography": {
				"text": subject_selection.get("geography", 0),
				"progress_value": int_to_progress_value(subject_selection.get("geography")),
			},
			"chemistry": {
				"text": subject_selection.get("chemistry", 0),
				"progress_value": int_to_progress_value(subject_selection.get("chemistry")),
			},
			"physics": {
				"text": subject_selection.get("physics", 0),
				"progress_value": int_to_progress_value(subject_selection.get("physics")),
			},
		},
		"department_suitability": {
			"purchase": {
				"text": department_suitability.get("purchase", 0),
				"progress_value": int_to_progress_value(department_suitability.get("purchase")),
			},
			"manufacturing": {
				"text": department_suitability.get("manufacturing", 0),
				"progress_value": int_to_progress_value(department_suitability.get("manufacturing")),
			},
			"r_and_d": {
				"text": department_suitability.get("r_&_d", 0),
				"progress_value": int_to_progress_value(department_suitability.get("r_&_d")),
			},
			"administration": {
				"text": department_suitability.get("administration", 0),
				"progress_value": int_to_progress_value(department_suitability.get("administration")),
			},
			"legal": {
				"text": department_suitability.get("legal", 0),
				"progress_value": int_to_progress_value(department_suitability.get("legal")),
			},
			"operations": {
				"text": department_suitability.get("operations", 0),
				"progress_value": int_to_progress_value(department_suitability.get("operations")),
			},
			"planning": {
				"text": department_suitability.get("planning", 0),
				"progress_value": int_to_progress_value(department_suitability.get("planning")),
			},
			"hr": {
				"text": department_suitability.get("hr", 0),
				"progress_value": int_to_progress_value(department_suitability.get("hr")),
			},
			"finance": {
				"text": department_suitability.get("finance", 0),
				"progress_value": int_to_progress_value(department_suitability.get("finance")),
			},
			"mktg_and_sales": {
				"text": department_suitability.get("mktg_&_sales", 0),
				"progress_value": int_to_progress_value(department_suitability.get("mktg_&_sales")),
			},
			"management": {
				"text": department_suitability.get("management", 0),
				"progress_value": int_to_progress_value(department_suitability.get("management")),
			},
		},
		"activity": {
			"cycling": {
				"text": activity_interest.get("cycling", 0),
				"progress_value": int_to_progress_value(activity_interest.get("cycling")),
			},
			"trekking": {
				"text": activity_interest.get("trekking", 0),
				"progress_value": int_to_progress_value(activity_interest.get("trekking")),
			},
			"outdoor_games": {
				"text": activity_interest.get("outdoor_games", 0),
				"progress_value": int_to_progress_value(activity_interest.get("outdoor_games")),
			},
			"photography": {
				"text": activity_interest.get("photography", 0),
				"progress_value": int_to_progress_value(activity_interest.get("photography")),
			},
			"musical": {
				"text": activity_interest.get("musical", 0),
				"progress_value": int_to_progress_value(activity_interest.get("musical")),
			},
			"drawing_painting": {
				"text": activity_interest.get("drawing/painting", 0),
				"progress_value": int_to_progress_value(activity_interest.get("drawing/painting")),
			},
			"dramatics": {
				"text": activity_interest.get("dramatics", 0),
				"progress_value": int_to_progress_value(activity_interest.get("dramatics")),
			},
			"debate": {
				"text": activity_interest.get("debate", 0),
				"progress_value": int_to_progress_value(activity_interest.get("debate")),
			},
			"cookery": {
				"text": activity_interest.get("cookery", 0),
				"progress_value": int_to_progress_value(activity_interest.get("cookery")),
			},
			"computers": {
				"text": activity_interest.get("computers", 0),
				"progress_value": int_to_progress_value(activity_interest.get("computers")),
			},
			"chess": {
				"text": activity_interest.get("chess", 0),
				"progress_value": int_to_progress_value(activity_interest.get("chess")),
			},
			"calligraphy": {
				"text": activity_interest.get("calligraphy", 0),
				"progress_value": int_to_progress_value(activity_interest.get("calligraphy")),
			},
			"aerobics": {
				"text": activity_interest.get("aerobics", 0),
				"progress_value": int_to_progress_value(activity_interest.get("aerobics")),
			},
			"dairy_writing": {
				"text": activity_interest.get("dairy_writing", 0),
				"progress_value": int_to_progress_value(activity_interest.get("dairy_writing")),
			},
		},
	}
	return res


def int_to_progress_value(value):
	return (value or 0) / 10


def float_to_percentage_string(value):
	return f"{float(value or 00.0):.2f}%"
