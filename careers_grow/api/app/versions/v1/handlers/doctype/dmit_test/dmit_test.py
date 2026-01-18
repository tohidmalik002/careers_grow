import frappe

def get_dmit_test_data_from_token(payload):
    return {
        "multiple_intelligences": {
            "logical":"100%",
            "linguistic":"100%",
            "interpersonal":"100%",
            "naturalistic":"100%",
            "kinesthetic":"100%",
            "visual_spatial":"100%",
            "intrapersonal":"100%",
            "musical":"100%"
        },
        "personality_type":{
            "naturalistic":"100%",
            "musical":"100%"
        }
    }

def get_dmit_test_list(payload):

    user_details = frappe.local.jwt_payload

    res = frappe.db.sql("SELECT ue.entity_type, ue.entity " \
                            "FROM `tabApp User Entity` AS ue " \
                            "JOIN `tabApp User Entity Map` AS uem " \
                            "ON ue.name = uem.parent AND uem.parentfield = 'users' AND parenttype = 'App User Entity' " \
                            "WHERE uem.user = %(app_user)s", values = {'app_user': user_details['username']}, as_dict =1)
    if not res:
        return []
    entity_type, entity = res[0]["entity_type"], res[0]["entity"]

    entity_type_field_map = {
        "Student": "student_id",
        "Counsellor": "counsellor_id",
        "Franchise Partner": "franchise_id"
    }

    if not entity_type_field_map[entity_type]:
        frappe.throw("Invalid User Entity Type")
    

    filters = {entity_type_field_map[entity_type]: entity}


    dmit_list = frappe.get_all("DMIT Test", ['student_id', 'student_name', 'modified'], filters, order_by='modified desc')

    return dmit_list




    return {
        "multiple_intelligences": {
            "logical":"100%",
            "linguistic":"100%",
            "interpersonal":"100%",
            "naturalistic":"100%",
            "kinesthetic":"100%",
            "visual_spatial":"100%",
            "intrapersonal":"100%",
            "musical":"100%"
        },
        "personality_type":{
            "naturalistic":"100%",
            "musical":"100%"
        }
    }