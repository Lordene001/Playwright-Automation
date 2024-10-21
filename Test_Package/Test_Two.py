import re
from playwright.sync_api import Playwright, sync_playwright, expect
from page_Package.HomePage_Page import HomePage


def API_University(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.apisecuniversity.com/")

    hp = HomePage(page)
    hp.SignIn('emmanuelene4@gmail.com','Mindlesskid@001')
    element = hp.Login_Validation_Element
    expect(element).to_have_text("Courses")
    page.pause()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    API_University(playwright)
