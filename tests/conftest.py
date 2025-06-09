import pytest
import os


@pytest.fixture(scope="function")
def clear_dir():
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
