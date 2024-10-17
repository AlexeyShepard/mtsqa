import pytest
import allure
from playwright.sync_api import Playwright, expect

@pytest.fixture()
def form_data():
    return {
        'number':'9186253416',
        'name':'Алексей'
    }


def browser_emulate(playwright, form_data):
    with allure.step('Создаем экземпляр браузера'):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
    with allure.step('Переходим на страницу mts.ru'):
        page.goto("https://moskva.mts.ru/personal")
    with allure.step('Переходим в раздел тарифов'):
        page.locator("mts-ecosystem-navigation-widget a").filter(has_text="Тарифы").click()
        page.locator("[id=\"\\34 704357\"] a").click()
    with allure.step('Открываем форму отправки заявки на оформление тарифа'):
        page.locator("mts-product-header-connection").get_by_text("Подключить").click()
    with allure.step('Ожидаем, когда все элементы формы прогрузятся в DOM'):
        page.wait_for_selector('div.mm-web-button__text:has-text("Оставить заявку")', state='attached')
        page.wait_for_selector('input[placeholder="XXX XXX XX XX"]', state='attached')
        page.wait_for_selector('input#username[placeholder="Ваше имя"]', state='attached')
    with allure.step('Заполняем номер телефона'):
        page.get_by_role("textbox", name="XXX XXX XX XX").click()
        page.get_by_role("textbox", name="XXX XXX XX XX").fill(form_data['number'])
    with allure.step('Заполняем имя клиента'):
        page.get_by_role("textbox", name="Ваше имя").click()
        page.get_by_role("textbox", name="Ваше имя").fill(form_data['name'])
    with allure.step('Отправляем данные'):
        page.get_by_role("button", name="Оставить заявку").click()
    with allure.step('Ожидаем, что на странице куда нас перенаправит будет текст "Заявка отправлена" '):
        expect(page.get_by_text("Заявка отправлена")).to_be_visible()

        context.close()
        browser.close()


@allure.epic('Оставить заявку на оформление тарифа')
@allure.story('Пошагово переходим на форму заполнения данных и оправляем их')
class TestLeaveRequest():
    @staticmethod
    @allure.title('Тест для отправления заявки с данными которых нету в базе данных')
    def test_positive(playwright: Playwright, form_data) -> None:
        browser_emulate(playwright, form_data)

    @staticmethod
    @allure.title('Тест для отправления заявки с данными, которые уже есть в базе данных')
    def test_negative(playwright: Playwright, form_data) -> None:
        browser_emulate(playwright, form_data)

