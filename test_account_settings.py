    import time

import pytest
from time import sleep

from locators.create_account_locators import email_address
from pages.account_settings import account_settings
from pages.account_settings import Edit



@pytest.mark.usefixtures("setup")
class TestEdit:
  def test_to_verify_the_two_step_verification(self):
        edit_driver = Edit(self.driver)
        edit_driver.open_login_page()
        edit_driver.enter_username('unique56@yopmail.com')
        edit_driver.enter_password('Sak@1421')
        edit_driver.clicking_on_sign_in()