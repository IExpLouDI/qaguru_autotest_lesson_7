from zipfile import ZipFile

with ZipFile("tmp/hello.zip") as zip_file:
    print(zip_file.namelist())
    text = zip_file.read('Hello.txt')
    print(text)
    zip_file.extract('Hello.txt', path="../../../Downloads/qa_guru_python_9_7_files-master/tmp")