from zipfile import ZipFile
import os

from utils.paths import DIR_WITH_RESOURCES
from utils.command import check_result, file_content


def test_create_archive_and_check_in_directory():
	files_in_resources = [
		file for file in os.listdir(DIR_WITH_RESOURCES) if ("." in file and not file.startswith(".")
															and not file.endswith(".zip"))
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

	assert file_archive in os.listdir(DIR_WITH_RESOURCES)


def test_exists_zip_in_directory(save_dic_in_directory):
	files = os.listdir(DIR_WITH_RESOURCES)
	assert os.path.basename(save_dic_in_directory) in files


def test_files_in_zip_exists_in_dir(save_dic_in_directory):
	with ZipFile(save_dic_in_directory) as zip_file:
		files_in_zip = zip_file.namelist()

	files_in_resources = [
		file for file in os.listdir(DIR_WITH_RESOURCES) if ("." in file
															and not file.startswith(".")
															and not file.endswith(".zip")
															)
	]
	assert len(files_in_resources) == len(files_in_zip), ("Ожидаемое количество файлов в архиве\n"
														  "не соответствует фактическому.")

def test_check_content_pdf_file_in_archive(save_dic_in_directory):
	expected_params = {
			"expected_page_count": 10,
			"expected_page_text": "Тестовый PDF файл "
		}
	with ZipFile(save_dic_in_directory) as zip_file:  # открываем архив
		files_in_zip = zip_file.namelist()
		file = "".join([f for f in files_in_zip if f.endswith(".pdf")])

		with zip_file.open(file) as open_file:
			content = file_content(".pdf", open_file)

	assert content["page_count"] == expected_params["expected_page_count"], \
		(f"\nОжидаемое количество страниц - {expected_params['expected_page_count']}, не "
		 f"соответствует фактическому - {content['page_count']}")

	assert expected_params["expected_page_text"] in content["page_text"], \
	f"Ожидаемая подстрока '{expected_params['expected_page_text']}' не содержится в документе {file}"


def test_check_content_xls_file_in_archive(save_dic_in_directory):
	expected_params = {"page_count": 1,
	 "sheet_list": ["Sheet1"],
	 "column_count": 8,
	 "row_count": 10,
	 "value_9_1": "Vincenza"
	 }

	with ZipFile(save_dic_in_directory) as zip_file:  # открываем архив
		files_in_zip = zip_file.namelist()
		file = "".join([f for f in files_in_zip if f.endswith(".xls")])

		with zip_file.open(file) as open_file:
			content = file_content(".xls", open_file.read())

	assert expected_params["page_count"] == content["page_count"], \
		f'Ожидаемое значение {expected_params["page_count"]} не совпало с фактическим {content["page_count"]}.'

	assert expected_params["sheet_list"] == content["sheet_list"], \
		f'Ожидаемое значение {expected_params["sheet_list"]} не совпало с фактическим {content["sheet_list"]}.'

	assert expected_params["column_count"] == content["column_count"], \
		f'Ожидаемое значение {expected_params["column_count"]} не совпало с фактическим {content["column_count"]}.'

	assert expected_params["row_count"] == content["row_count"], \
		f'Ожидаемое значение {expected_params["row_count"]} не совпало с фактическим {content["row_count"]}.'

	assert expected_params["value_9_1"] == content["value_9_1"], \
		f'Ожидаемое значение {expected_params["value_3_2"]} не совпало с фактическим {content["value_3_2"]}.'


def test_check_content_xlsx_file_in_archive(save_dic_in_directory):
	expected_params = {"value_3_2": "Mara"}

	with ZipFile(save_dic_in_directory) as zip_file:  # открываем архив
		files_in_zip = zip_file.namelist()
		file = "".join([f for f in files_in_zip if f.endswith(".xlsx")])

		with zip_file.open(file) as open_file:
			content = file_content(".xlsx", open_file)

	assert expected_params["value_3_2"] == content["value_3_2"], \
		f'Ожидаемое значение {expected_params["value_3_2"]} не совпало с фактическим {content["value_3_2"]}.'
