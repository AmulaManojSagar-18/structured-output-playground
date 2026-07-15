import json

def parse_schema(schema_text):
    try:
        schema = json.loads(schema_text)
        return schema, None
    except Exception as e:
        return None, str(e)