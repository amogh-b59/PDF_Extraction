from flask import Flask, request, redirect, url_for, render_template, flash
import os
from werkzeug.utils import secure_filename
import pandas as pd
from src.pdf_parser import extract_text_from_pdf
from src.text_extraction import extract_name, extract_email, extract_phone, extract_location

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'supersecretkey'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
            'Location': location,
        })
        
    columns = ['Name', 'Email', 'Phone', 'Location']  # Add other columns here...
    df = pd.DataFrame(data, columns=columns)
    df.to_excel(output_path, index=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Process the uploaded file
        process_resumes(app.config['UPLOAD_FOLDER'], 'data/output/resumes.xlsx')
        
        flash('File successfully uploaded and processed')
        return redirect(url_for('index'))
    else:
        flash('Allowed file types are pdf')
        return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)
