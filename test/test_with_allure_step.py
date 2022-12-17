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
def test_with_allure_step():
    with allure.step("Открыть github"):
        browser.open('https://github.com')
        browser.driver.maximize_window()

    with allure.step("Найти репозиторий"):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').send_keys("eroshenkoam/allure-example")
        browser.element('.header-search-input').submit()

    with allure.step("Перейти в репозиторий"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Перейти в Issue"):
        browser.element('#issues-tab').click()

    with allure.step("Найти Issue с номером 76"):
        assert browser.element(by.partial_text("#76")).should(be.visible)
