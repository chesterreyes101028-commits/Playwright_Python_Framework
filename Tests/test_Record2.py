from playwright.sync_api import Page, expect
from Pages.Login_Page import LoginPage


def test_example(page: Page):
    login_page = LoginPage(page)
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

    page.get_by_role("link", name="Admin").click()
    page.get_by_role("textbox").nth(1).click()
    page.get_by_role("textbox").nth(1).fill("charon")
    page.get_by_role("button", name="Search").click()
    page.wait_for_timeout(5000)