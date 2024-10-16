import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://moskva.mts.ru/personal")
    page.locator("mts-ecosystem-navigation-widget a").filter(has_text="Тарифы").click()
    page.locator("[id=\"\\34 704357\"] a").click()
    page.locator("mts-product-header-connection").get_by_text("Подключить").click()
    page.get_by_role("textbox", name="XXX XXX XX XX").click()
    page.get_by_role("textbox", name="XXX XXX XX XX").fill("9186253419")
    page.get_by_role("textbox", name="Ваше имя").click()
    page.get_by_role("textbox", name="Ваше имя").fill("Прохор")
    page.get_by_role("button", name="Оставить заявку").click()
    actual_text = page.get_by_text("Заявка отправлена").inner_text()

    print(actual_text)

    # ---------------------
    context.close()
    browser.close()

    assert actual_text == 'Заявка отправлена'


with sync_playwright() as playwright:
    run(playwright)
