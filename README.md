# PDF Text Extraction

The PDF Text Extraction is a Python program designed to extract and analyze patient information from PDF documents, specifically medical charts. It uses the `pdfplumber` library to extract textual data from PDF files and provides insights into patient data such as age, date of birth, and EKG validity.

## Features

- Extracts patient information from PDF medical charts.
- Calculates and displays patient age based on date of birth.
- Determines if a patient has a valid EKG.
- Outputs patient details to the console.

## Prerequisites

- Python 3.7 and up
- `pdfplumber` library (`pip install pdfplumber`)

## How to Use

1. Place your PDF files in the same directory as the program.
2. Run the program (`python your_program_name.py`).
3. The program will analyze each PDF file in the directory.
4. Patient details, including age, date of birth, and EKG validity, will be displayed in the console.

## Sample Output Of My PDFs

Age: 52.00  
Dob: 02/02/1971  
has_valid_ekg : False  
Name: “John Doe The Second”
