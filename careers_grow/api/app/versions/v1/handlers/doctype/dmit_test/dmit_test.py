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