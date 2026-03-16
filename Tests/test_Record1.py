import re
from playwright.sync_api import Page, expect
from Pages.Login_Page import LoginPage


def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = LoginPage(page)
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    #page.get_by_role("button",name="Login").click()
    login_page.click_login()
    page.get_by_role("link", name="Admin").click()
    page.get_by_role("button", name="Search").click()
    print("hotdog")
    #expect(page.locator("#app")).to_contain_text("(13) Records Found")
