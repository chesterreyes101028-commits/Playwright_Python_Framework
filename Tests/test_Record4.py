import os
from playwright.sync_api import Page, expect
from Pages.Login_Page import LoginPage
from dotenv import load_dotenv
load_dotenv()


def test_example(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(os.getenv("Username"),os.getenv("Password"))
    page.wait_for_timeout(5000)
    Dashboard = page.get_by_role("heading",name="Dashboard").text_content()

    if Dashboard == 'Hotdog':
        print("Champoy")
    else:
        print(Dashboard)
 
    page.get_by_role("link", name="Admin").click()
    page.get_by_role("textbox").nth(1).click()
    page.get_by_role("textbox").nth(1).fill("charon")
    page.get_by_role("button", name="Search").click()

