import random
import pytest
import allure
from playwright.sync_api import Playwright, expect, Page
from Task2.models import FormData
from Task2.utils import random_number


def go_to_homepage(page):
    with allure.step('Переходим на страницу mts.ru'):
        page.goto("https://moskva.mts.ru/personal")

def go_to_tariffs(page):
    with allure.step('Нажать на кнопку "Тарифы"'):
        page.locator("mts-ecosystem-navigation-widget a").filter(has_text="Тарифы").click()


def go_to_tariff_description(page):
    with allure.step('Нажать кнопку "Подробнее" на карточке "Тариф №1"'):
        page.locator("[id=\"\\34 704357\"] a").click()

def go_to_connect_the_tariff_form(page):
    with allure.step('Нажать на кнопку "Подключить"'):
        page.locator("mts-product-header-connection").get_by_text("Подключить").click()

def fill_the_form(page, add_form_data):
    # Перед вводом в форму, ждем когда все элементы будут загружены
    page.wait_for_selector('input[placeholder="XXX XXX XX XX"]', state='attached')
    page.wait_for_selector('input#username[placeholder="Ваше имя"]', state='attached')
    with allure.step(f'Заполняем номер телефона, number: {add_form_data["number"]}'):
        page.get_by_role("textbox", name="XXX XXX XX XX").click()
        page.get_by_role("textbox", name="XXX XXX XX XX").fill(add_form_data['number'])
    with allure.step(f'Заполняем имя клиента: {add_form_data["name"]}'):
        page.get_by_role("textbox", name="Ваше имя").click()
        page.get_by_role("textbox", name="Ваше имя").fill(add_form_data['name'])

def send_data(page):
    with allure.step(f'Отправляем форму'):
        page.wait_for_selector('div.mm-web-button__text:has-text("Оставить заявку")', state='attached')
        page.get_by_role("button", name="Оставить заявку").click()

@pytest.fixture()
def add_form_data():
    return FormData(
        number=random_number(),
        name=''
    ).model_dump()

@pytest.fixture(scope="session")
def context_browser(playwright: Playwright) -> Page:
    with allure.step('Создаем экземпляр браузера'):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        return page

@allure.epic('Оставить заявку на оформление тарифа')
@allure.story('Позитивные тесты')
class TestLeaveRequestPositive():
    @staticmethod
    @allure.title('Перейти на страницу https://moskva.mts.ru/personal')
    def test_go_to_mts_page(context_browser):
        go_to_homepage(context_browser)
        expect(context_browser.get_by_text("Пополнение и оплата")).to_be_visible()

    @staticmethod
    @allure.title('Переходим в раздел тарифов')
    def test_go_to_tariffs(context_browser):
        go_to_tariffs(context_browser)
        expect(context_browser.get_by_text("Тариф №1")).to_be_visible()

    @staticmethod
    @allure.title('Переход к тарифу №1')
    def test_go_to_tariff_description(context_browser):
        go_to_tariff_description(context_browser)
        expected_result = 'Тариф с мобильной связью, домашним интернетом, ТВ и онлайн-кинотеатром KION'
        expect(context_browser.get_by_text(expected_result)).to_be_visible()

    @staticmethod
    @allure.title('Переход к форме заполнения заявки')
    def test_go_to_connect_the_tariff_form(context_browser):
        go_to_connect_the_tariff_form(context_browser)
        expect(context_browser.get_by_text("Заявка на подключение")).to_be_visible()

    @staticmethod
    @allure.title('Заполнение формы заявки')
    def test_fill_the_form(context_browser, add_form_data):
        fill_the_form(context_browser, add_form_data)
        warnings = ["Заполните поле", "Укажите Ваше имя"]
        expect(context_browser.get_by_text("Заявка на подключение")).not_to_have_text(warnings)

    @staticmethod
    @allure.title('Отправить заявку')
    def test_send_the_data(context_browser):
        send_data(context_browser)
        expect(context_browser.get_by_text("Заявка отправлена")).to_be_visible()






