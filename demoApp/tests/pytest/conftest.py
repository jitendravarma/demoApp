import os
import time
import pytest

from selenium import webdriver

from selenium.webdriver.chrome.options import Options


options = Options()
# options.add_argument('--headless')


@pytest.fixture(scope='session')
def setup(request):
    chromedriver = os.popen('which chromedriver').read().strip()
    print("\nInitiating chrome driver")
    driver = webdriver.Chrome(chromedriver, options=options)
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    driver.implicitly_wait(30)
    yield driver
    time.sleep(2)
    driver.close()
