import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "rammsat")
@allure.feature("Задача")
@allure.story("Доступность задачи пользователю")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps():
    open_main_page()
    search_for_repository()
    go_to_repository()
    open_issue_tab()
    should_see_issue_with_number("#76")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")
    browser.driver.maximize_window()


@allure.step("Найти репозиторий")
def search_for_repository():
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys("eroshenkoam/allure-example")
    browser.element('.header-search-input').submit()


@allure.step("Перейти к репозиторию")
def go_to_repository():
    browser.element(by.link_text("eroshenkoam/allure-example")).click()


@allure.step("Перейти в Issue")
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step("Найти Issue с номером {number}")
def should_see_issue_with_number(number):
    assert browser.element(by.partial_text(number)).should(be.visible)
