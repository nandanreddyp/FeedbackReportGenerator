import os
import weasyprint
from datetime import datetime

def validate_json(json_data):
    """Validate student activity JSON data."""

    if not json_data:
        raise ValueError("JSON data is empty.")

    # Helper to validate a single student
    def validate_student(student):
        required_student_keys = {"student_id", "events"}
        required_event_keys = {"type", "created_time", "unit"}

        if not isinstance(student, dict):
            raise ValueError("Each student entry must be a dictionary.")

        missing = required_student_keys - student.keys()
        if missing:
            raise ValueError(f"Missing keys in student data: {', '.join(missing)}")

        for i, event in enumerate(student["events"]):
            if not isinstance(event, dict):
                raise ValueError(f"Event at index {i} is not a dictionary.")
            missing_event_keys = required_event_keys - event.keys()
            if missing_event_keys:
                raise ValueError(
                    f"Missing keys in event at index {i}: {', '.join(missing_event_keys)}"
                )

    if isinstance(json_data, dict):
        validate_student(json_data)
    elif isinstance(json_data, list):
        for idx, student in enumerate(json_data):
            try:
                validate_student(student)
            except ValueError as e:
                raise ValueError(f"Error in student at index {idx}: {e}")
    else:
        raise ValueError("Invalid format: Expected dict or list of dicts.")

    return True

def event_orders(events):
    """Handle events and return a string of event order."""
    event_order = ""
    morfed_events = [(datetime.fromisoformat(events['created_time']), int(events['unit'])) for events in events]
    morfed_events.sort(key=lambda x: x[1])
    unique_units = []; seen = set()
    for event in morfed_events:
        unit = event[1]
        if unit not in seen:
            seen.add(unit); unique_units.append(unit)
    labeled_units = {unit: f"Q{i}" for i, unit in enumerate(unique_units, start=1)}
    morfed_events.sort(key=lambda x: x[0])
    for i, event in enumerate(morfed_events):
        event_order += labeled_units[event[1]]
        if i != len(morfed_events) - 1:
            event_order += " -> "
    return event_order

def generate_html_from_json(json_data, filename=None):
    """Generate HTML from JSON data.
    """
    validate_json(json_data)

    def student_section(student, html_content):
        """Generate HTML for a single student."""
        html_content += f"<h1>Student ID: {student['student_id']}</h1>\n"
        # for event in student["events"]:
        #     html_content += f"<h2>Event Type: {event['type']}</h2>\n"
        #     html_content += f"<p>Created Time: {event['created_time']}</p>\n"
        #     html_content += f"<p>Unit: {event['unit']}</p>\n"
        html_content += f"<p>Event Order: {event_orders(student['events'])}</p>\n"
        return html_content
    
    html_content = "<html><body>\n"
    if isinstance(json_data, dict):
        html_content = student_section(json_data, html_content)
    elif isinstance(json_data, list):
        for student in json_data:
            html_content = student_section(student, html_content)
    html_content += "</body></html>"

    if filename:
        html_filepath = os.path.join("reports","files","htmls",f"{filename}.html")
        os.makedirs(os.path.dirname(html_filepath), exist_ok=True)
        with open(html_filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        return html_filepath
    return html_content

def generate_pdf_from_json(json_data, filename):
    """Generate a PDF from JSON data.
    """
    pdf_filepath = os.path.join("reports","files","pdfs",f"{filename}.pdf")
    os.makedirs(os.path.dirname(pdf_filepath), exist_ok=True)
    html_content = generate_html_from_json(json_data)
    weasyprint.HTML(string=html_content).write_pdf(pdf_filepath)
    return pdf_filepath



# ### test
# import json

# with open('../../student.json', 'r') as f:
#     json_data = json.load(f)

# html_content = generate_html_from_json(json_data, 'student')

# generate_pdf_from_json(html_content, 'student')
