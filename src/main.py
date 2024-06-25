import os
import pandas as pd
from pdf_parser import extract_text_from_pdf
from text_extraction import extract_name, extract_email, extract_phone, extract_location

def process_resumes(input_dir, output_path):
    data = []
    pdf_files = [file for file in os.listdir(input_dir) if file.endswith('.pdf')]

    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_dir, pdf_file)
        text = extract_text_from_pdf(pdf_path)

        name = extract_name(text)
        email = extract_email(text)
        phone = extract_phone(text)
        location = extract_location(text)

        data.append({
            'Name': name,
            'Email': email,
            'Phone': phone,
            'Location' : location,
        })

    # Here we are saving Data to Excel Sheet.
    columns = ['Name', 'Email', 'Phone', 'Location']  # Add other columns here...
    df = pd.DataFrame(data, columns=columns)
    df.to_excel(output_path, index=False)

if __name__ == '__main__':
    input_dir = 'data/input'
    output_path = 'data/output/resumes.xlsx'
    process_resumes(input_dir, output_path)
