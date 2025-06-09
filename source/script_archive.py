import os.path
from zipfile import ZipFile
from config import DIR_WITH_RESOURCES_DOWNLOADS


add_file = os.path.join(DIR_WITH_RESOURCES_DOWNLOADS + "hello.zip")

with ZipFile(add_file) as zip_file:
    print(zip_file.namelist())
    text = zip_file.read('Hello.txt')
    print(text)
    zip_file.extract('Hello.txt', path="../../../Downloads/qa_guru_python_9_7_files-master/tmp")
