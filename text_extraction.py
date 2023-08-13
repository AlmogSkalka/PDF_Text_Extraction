import os
import pdfplumber
from typing import List, Dict
from dataclasses import dataclass
from datetime import datetime


@dataclass
class TextualWord:
    x0: float
    x1: float
    text: str


class Chart:
    name: str
    dob: datetime
    has_valid_ekg: bool

    def __init__(self, patient_name: str, patient_dob: datetime, has_valid_ekg: bool):
        self.name = patient_name
        self.dob = patient_dob
        self.has_valid_ekg = has_valid_ekg

    @property
    def age(self) -> float:
        if self.dob is not None:
            today = datetime.today()
            birthdate = self.dob
            age = (
                today.year
                - birthdate.year
                - ((today.month, today.day) < (birthdate.month, birthdate.day))
            )
            return age


PagesToWords = Dict[int, List[TextualWord]]


# took this out of 'populate_chart' to orgnize and have better vision for myself
# There might be an extra foor loop ATM, but we can omit it as the data is relativley small in my examples
def get_pdf_lines(page_to_words: PagesToWords) -> list:
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
                name_list = line[index + 1 :]
                name = " ".join(name_list)
                break
            if "DOB:" in word:
                dob_list = line[index + 1 :]
                dob = datetime.strptime(dob_list[0], "%d/%m/%Y").date()
            if "EKG" in word:
                has_valid_ekg = " ".join(line[index + 2 :])

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
                page_words.append(text_word)
            pageNumToContent[pageNum] = page_words
            pageNum += 1
    return pageNumToContent


def main():
    # check for each pdf file in the directory
    pdf_files_folder = os.path.dirname(__file__)

    for file_name in os.listdir(pdf_files_folder):
        if file_name.endswith(".pdf"):
            pdf_path = os.path.join(pdf_files_folder, file_name)
            page_content = get_pdf_content(pdf_path)
            chart = populate_chart(page_content)
            if chart.age is not None:
                print(f"Age: {chart.age:.2f}")
                print(f"Dob: {chart.dob.strftime('%m/%d/%Y')}")
                print(f"has_valid_ekg: {chart.has_valid_ekg}")
                print(f"Name: {chart.name}")
                print("\n")
        else:
            print("This is not a PDF file!\n")


if __name__ == "__main__":
    main()
