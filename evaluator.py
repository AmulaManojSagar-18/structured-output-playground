import json

def evaluate(json_output, schema):

    score = 100
    missing_fields = []

    for field in schema.keys():
        if field not in json_output:
            score -= 20
            missing_fields.append(field)

    return {
        "score": max(score, 0),
        "missing_fields": missing_fields,
        "valid_json": True
    }
