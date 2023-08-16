import os
import pdfplumber
from typing import List, Dict
from datetime import datetime
from Model.TextualWord import TextualWord
from Model.Chart import Chart

PagesToWords = Dict[int, List[TextualWord]]


# took this out of 'populate_chart' to organize and have better vision for myself
# There might be an extra for loop ATM, but we can omit it as the data is relatively small in my examples
def get_pdf_lines(page_to_words: PagesToWords) -> list:
    #get_pdf_lines is not completed yet. The logic listed is not correct yet.
    lines = []
    first_x0 = -1
    for page, words in page_to_words.items():
        line = []
        for word in words:
            if first_x0 == -1:
                first_x0 = word.x0
            elif first_x0 == word.x0:
                lines.append(line)
                line = []
            line.append(word.text)
    return lines


def populate_chart(page_to_words: PagesToWords) -> Chart:
    name = ""
    dob = None
    has_valid_ekg = False
    rows = get_pdf_lines(page_to_words)

    for line in rows:
        for index, word in enumerate(line):
            if "Name:" in word:
                name_list = line[index + 1:]
                name = " ".join(name_list)
                break
            if "DOB:" in word:
                dob_list = line[index + 1:]
                dob = datetime.strptime(dob_list[0], "%d/%m/%Y").date()
            if "EKG" in word:
                has_valid_ekg = " ".join(line[index + 2:])

    return Chart(name, dob, has_valid_ekg)


def get_pdf_content(pdf_folder: str) -> PagesToWords:
    pageNumToContent: PagesToWords = {}
    with pdfplumber.open(pdf_folder) as pdf:
        pageNum = 0
        for page in pdf.pages:
            words = page.extract_words()
            page_words = []
            for word in words:
                text_word = TextualWord(x0=word["x0"], x1=word["x1"], text=word["text"])
                print("word: ")
                print(word)
                page_words.append(text_word)
            pageNumToContent[pageNum] = page_words
            pageNum += 1
    return pageNumToContent


def print_chart_data(chart_obj: Chart):
    if chart_obj.age is not None:
        print(f"Age: {chart_obj.age:.2f}")
        print(f"Dob: {chart_obj.dob.strftime('%m/%d/%Y')}")
        print(f"has_valid_ekg: {chart_obj.has_valid_ekg}")
        print(f"Name: {chart_obj.name}")
        print("\n")


def main():
    # check for each pdf file in the directory
    pdf_files_folder = os.path.dirname(__file__)

    for file_name in os.listdir(pdf_files_folder):
        if file_name.endswith(".pdf"):
            pdf_path = os.path.join(pdf_files_folder, file_name)
            page_content = get_pdf_content(pdf_path)
            chart = populate_chart(page_content)
            print_chart_data(chart)


if __name__ == "__main__":
    main()
