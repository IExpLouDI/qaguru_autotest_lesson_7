from zipfile import ZipFile
import pytest
import os

from utils.paths import DIR_WITH_RESOURCES


@pytest.fixture(scope="function")
def clear_dir():
	"""Зачистка директории после скачивания файла"""
	file_path = ['']
	yield file_path
	os.remove(file_path[0])


@pytest.fixture(scope="function")
def get_instructions():
	"""Проверка содержимого файлов после открытия архива"""
	instructions = {".xls": {"page_count": 1,
							 "sheet_list": ["Sheet1"],
							 "column_count": 8,
							 "row_count": 10,
							 "value_9_1": "Vincenza"
					},
					".xlsx": {"value_3_2": "Mara"
					},
					".pdf": {
						"page_count": 2
					}
	 }
	return instructions


@pytest.fixture(scope="session")
def save_dic_in_directory():
	files_in_resources = [
		file for file in os.listdir(DIR_WITH_RESOURCES) if ("." in file and not file.startswith("."))
	]
	file_archive = "result_archive.zip"
	path_file_archive = os.path.join(DIR_WITH_RESOURCES, file_archive)

	if file_archive in files_in_resources:
		os.remove(path_file_archive)

	with ZipFile(path_file_archive, "w") as zip_f:
		for file in files_in_resources:
			if "zip" not in file:
				zip_f.write(os.path.join(DIR_WITH_RESOURCES, file), arcname=file)
	zip_f.close()

	yield path_file_archive

	os.remove(path_file_archive)
