Data Extarction from pdf.

## Description
This project is designed to extract structured information from resume PDFs and save it in an Excel sheet. 
It uses `pdfplumber` for PDF parsing and `pandas` for data handling.

-----------------------------------------------------------------------------------------------------------
1. pip install pdfminer.six 

Pdfminer.six is a community maintained fork of the original PDFMiner. 
It is a tool for extracting information from PDF documents. 
It focuses on getting and analyzing text data. 
Pdfminer.six extracts the text from a page directly from the sourcecode of the PDF. 
It can also be used to get the exact location, font or color of the text.

It is built in a modular way such that each component of pdfminer.six can be replaced easily. 
You can implement your own interpreter or rendering device that uses 
the power of pdfminer.six for other purposes than text analysis.

https://pypi.org/project/pdfminer.six/

2. pip install PyPDF2

PyPDF2 is a free and open-source pure-python PDF library capable of splitting, 
merging, cropping, and transforming the pages of PDF files. 
It can also add custom data, viewing options, and passwords to PDF files. 
PyPDF2 can retrieve text and metadata from PDFs as well.

https://pypi.org/project/PyPDF2/

3. pip install pyMuPDF

PyMuPDF is a high performance Python library for data extraction, analysis, conversion & manipulation of PDF (and other) documents.