import os
import time

import requests
from selene import query
from selene.support.shared import browser
from selenium import webdriver
from config import DIR_WITH_RESOURCES_DOWNLOADS
# from selenium.webdriver.chrome.service import Service убран по ненадобности
# from webdriver_manager.chrome import ChromeDriverManager убран по ненадобности


def test_text_in_downloaded_file_by_click(clear_dir):
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": DIR_WITH_RESOURCES_DOWNLOADS,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    browser.config.driver = driver

    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
    browser.element("[data-testid='download-raw-button']").click()
    time.sleep(4)

    clear_dir[0] = DIR_WITH_RESOURCES_DOWNLOADS + "/README.rst"

    with open(f"{clear_dir[0]}") as file:
        file_content_str = file.read()
        assert "test_answer" in file_content_str


def test_text_in_downloaded_file_by_saving_file_from_api_url():
    browser.open("https://github.com/pytest-dev/pytest/blob/main/README.rst")
    download_url = browser.element("[data-testid='raw-button']").get(query.attribute("href"))

    content = requests.get(url=download_url).content
    with open(os.path.join(DIR_WITH_RESOURCES_DOWNLOADS, "readme2.rts"), 'wb') as file:
        file.write(content)

    with open(f"{DIR_WITH_RESOURCES_DOWNLOADS}/readme2.rst") as file:
        file_content_str = file.read()
        assert "test_answer" in file_content_str
