import os


# directions
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CURRENT_DIR)
DIR_WITH_TESTS = os.path.join(ROOT_DIR, "tests")
DIR_WITH_RESOURCES = os.path.join(ROOT_DIR, "resources", "files")
DIR_WITH_RESOURCES_DOWNLOADS = os.path.join(ROOT_DIR, "resources", "files", "downloads")
