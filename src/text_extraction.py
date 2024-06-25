import re
import string

def extract_name(text):
    # Simplistic approach, assumes name is at the beginning of the resume
    lines = text.split('\n')
    return lines[0].strip()

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else None

def extract_phone(text):
    match = re.search(r'\+?\d[\d -]{8,12}\d', text)
    return match.group(0) if match else None

def extract_location(text):
    # Example keywords for cities or states (can be expanded)
    locations = ["Bengaluru","Bangalore,India", "Mumbai", "Delhi", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad"]
    for location in locations:
        if location.lower() in text.lower():
            return location
    return None