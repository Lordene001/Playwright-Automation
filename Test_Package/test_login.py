
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def DCU_Dig_Banking_Login_Validation(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.locator("body").click()
    page.goto("https://app-qa.dcu.org/login")
    page.get_by_label("Username").fill("bhard61381")
    page.get_by_role("textbox", name="Password").fill("QAtest2024!")
    page.get_by_role("button", name="SIGN IN").click()
    page.get_by_label("profile").click()
    page.get_by_role("option", name=" Profile Settings").click()
    element = page.get_by_role("heading", name="Contact Information")
    expect(element).to_have_text("Contact Information")
    # page.pause()

    # To get a list of elements (in this case links)
    # all_links = page.get_by_role("link").all()
    # for  link in all_links:
    #     if link.text_content() == 'expected value of element':
    #         link.click()



    context.close()
    browser.close()


with sync_playwright() as playwright:
    DCU_Dig_Banking_Login_Validation(playwright)
