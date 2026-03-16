from playwright.sync_api import Page, expect
from Pages.Login_Page import LoginPage


def test_example(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("Admin","admin123")

    page.get_by_role("link", name="Admin").click()
    page.get_by_role("textbox").nth(1).click()
    page.get_by_role("textbox").nth(1).fill("charon")
    page.get_by_role("button", name="Search").click()

    
