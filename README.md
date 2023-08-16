# PDF Text Extraction

The PDF Text Extraction is a Python program designed to extract and analyze patient information from PDF documents, specifically medical charts. It utilizes Object-Oriented Programming (OOP) principles and data structures to efficiently process and organize the extracted data, along to utilizing external Python library, `pdfplumber` for data extraction.

## Features

- Extracts patient information from PDF medical charts.
- Calculates and displays patient age based on date of birth.
- Determines if a patient has a valid EKG.
- Outputs patient details to the console.

## Prerequisites

- Python 3.7+
- `pdfplumber` library (`pip install pdfplumber`)
- To install the required dependencies for this project, you can use the `requirements.txt` file. Run the following command in your virtual environment:

```bash
pip install -r requirements.txt
```

## Object-Oriented Approach

The program employs an Object-Oriented approach to represent patient charts and their data. The `Chart` class encapsulates patient attributes such as name, date of birth, and EKG validity. This design promotes code organization, readability, and reusability.

## Data Extraction and Organization

The program uses data structures to efficiently organize extracted text data from PDF files. The `PagesToWords` dictionary maps page numbers to lists of `TextualWord` objects, representing individual words with associated coordinates. This data structure enables effective grouping and analysis of patient information.

## How to Use

1. Place your PDF files in the same directory as the program.
2. Run the program (`python your_program_name.py`).
3. The program will analyze each PDF file in the directory.
4. Patient details, including age, date of birth, and EKG validity, will be displayed in the console.

## Data Extraction

The program utilizes the `pdfplumber` library to extract textual data from PDF files. It makes use of the following attributes:

- `x0`: Distance of the left side of a character from the left side of the page.
- `x1`: Distance of the right side of a character from the left side of the page.

These attributes are used to identify and organize patient information within the PDF medical charts. This way, we are able to determine if a word is located at the start of a new text line or not.

### Example Output of 'get_pdf_content':

_0: [TextualWord(x0=72.025, x1=108.875, text='Patient')_

## Sample Output

Age: 53.00
Dob: 01/15/1969
has_valid_ekg: valid
Name: John Doe

Age: 42.00
Dob: 07/21/1979
has_valid_ekg: not valid
Name: Jane Smith

## Note

- PDF files must be properly formatted medical charts with relevant patient information.
- The program assumes a specific format for patient details, including "Name:", "DOB:", and "EKG".

```

```
