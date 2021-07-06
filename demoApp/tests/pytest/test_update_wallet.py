import time

import pytest
from utils import BASE_URL, Utils


@pytest.mark.usefixtures("setup")
class TestLogin(Utils):

    def test_login(self):
        """ to test login and find user name in after the login
        edit as per your email and name"""
        driver = self.driver
        driver.get(f"{BASE_URL}/login/")
        self.login("test@admin.com", "test123")

        # check if the url is okay
        assert (self.crashes(BASE_URL) == 200)

        assert (self.page_contains("Jitendra") is not None)
