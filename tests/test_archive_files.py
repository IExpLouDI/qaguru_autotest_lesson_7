from zipfile import ZipFile
from config import DIR_WITH_RESOURCES
import os


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


def test_check_files_in_archive():
	pass
