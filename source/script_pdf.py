import os.path
from pypdf import PdfReader
from utils.paths import DIR_WITH_RESOURCES


file_pdf = os.path.join(DIR_WITH_RESOURCES, "test.pdf")
reader = PdfReader(file_pdf)

print(reader.pages)
print(len(reader.pages))

# в файле только картинки, а библиотека не работает с ними
# print(reader.pages[1].extract_text())

page_count = 56

assert page_count == len(reader.pages)
print(os.path.getsize(file_pdf))

assert os.path.getsize(file_pdf) == 425786
