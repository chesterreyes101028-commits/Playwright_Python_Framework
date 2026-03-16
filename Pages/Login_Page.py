import os
from dotenv import load_dotenv
load_dotenv(override=True)

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_loc = page.get_by_role("textbox", name="Username")
        self.password_loc = page.get_by_role("textbox", name="Password")
        self.login_loc = page.get_by_role("button", name="Login")

    def navigate(self):
        self.page.goto(os.getenv("Base_URL"))

    def enter_username(self, username: str):
        self.username_loc.fill(username)

    def enter_password(self, password: str):
        self.password_loc.fill(password)

    def click_login(self):
        self.login_loc.click()

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()