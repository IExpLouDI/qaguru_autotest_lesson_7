import os.path

from pypdf import PdfReader

reader = PdfReader("tmp/Python Testing with Pytest (Brian Okken).pdf")

print(reader.pages)
print(len(reader.pages))

print(reader.pages[1].extract_text())

assert "Simple, Rapid, Effective, and Scalable" in reader.pages[1]
print(os.path.getsize(
	"../../../Downloads/qa_guru_python_9_7_files-master/tmp/Python Testing with Pytest (Brian Okken).pdf"))
assert os.path.getsize(
	"../../../Downloads/qa_guru_python_9_7_files-master/tmp/Python Testing with Pytest (Brian Okken).pdf") == 3035139