# pyrefly: ignore [missing-import]
import streamlit as st
import json

from gemini_client import generate_json
from schema_parser import parse_schema
from evaluator import evaluate

st.title("Structured Output Playground")

text_input = st.text_area(
    "Enter Unstructured Text",
    height=200
)

schema_input = st.text_area(
    "Enter JSON Schema",
    value='''
{
  "name": "",
  "skills": [],
  "experience": 0
}
''',
    height=200
)

if st.button("Generate JSON"):

    schema, error = parse_schema(schema_input)

    if error:
        st.error(error)

    else:

        with st.spinner("Generating..."):
            output = generate_json(
                text_input,
                schema_input
            )

        try:
            output_json = json.loads(output)

            result = evaluate(
                output_json,
                schema
            )

            st.success(
                f"Schema Compliance Score: {result['score']}/100"
            )

            if result["missing_fields"]:
                st.warning(
                    f"Missing fields: {result['missing_fields']}"
                )

            st.json(output_json)

        except Exception:
            st.error(
                "Gemini returned invalid JSON."
            )

            st.code(output)