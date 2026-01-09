import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path
import configparser

def pytest_addoption(parser):
    parser.addoption("--device", action="store", default="Pixel 7")
    
@pytest.fixture(scope="function")
def web_driver_01(request):
    chrome_options = Options()
    if request.config.getoption("--device") == 'Pixel 7':
        chrome_options.add_argument("--window-size=412,915")
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36")
    
    elif request.config.getoption("--device") == 'iPhone SE':
        chrome_options.add_argument("--window-size=375,667")
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.5 Mobile/15E148 Safari/604.1")
    else:
        chrome_options.add_argument("--window-size=412,915")
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()



@pytest.fixture(scope='session')
def test_config(request):
    config = configparser.ConfigParser()
    p = Path()
    pytest.root_folder = str(p.cwd())
    config_location = pytest.root_folder + '/config.ini'
    config.read(config_location)

    return config