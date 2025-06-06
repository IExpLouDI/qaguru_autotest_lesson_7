import pytest
import os


@pytest.fixture(scope="function")
def clear_dir():
	file_path = ['']
	yield file_path
	os.remove(file_path[0])
