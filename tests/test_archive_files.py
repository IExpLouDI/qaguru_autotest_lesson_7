from zipfile import ZipFile
import os

from utils.paths import DIR_WITH_RESOURCES
from utils.command import check_result


def test_create_archive_and_check_in_directory():
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

	assert file_archive in os.listdir(DIR_WITH_RESOURCES)


def test_exists_zip_in_directory(save_dic_in_directory):
	files = os.listdir(DIR_WITH_RESOURCES)
	assert 1 == 1

def test_check_files_in_archive(get_instructions):

	zip_in_directory = [file for file in os.listdir(DIR_WITH_RESOURCES) if file.endswith(".zip")]
	assert len(zip_in_directory) == 1 , f"В дирректории {DIR_WITH_RESOURCES} более одного архива {zip_in_directory}"

	with ZipFile(os.path.join(DIR_WITH_RESOURCES, zip_in_directory[0])) as zip_file:  # открываем архив
		files_in_zip = zip_file.namelist()

		for _i, file in enumerate(files_in_zip):
			f_type = "." + file.split(".")[1]
			with zip_file.open(file) as opened_file:
				# не всё так просто с .xls
				if f_type != '.xls':
					check = check_result(f_type, get_instructions[f_type], opened_file)
				else:
					check = check_result(f_type, get_instructions[f_type], opened_file.read())

				assert True == check[0], check[1]
