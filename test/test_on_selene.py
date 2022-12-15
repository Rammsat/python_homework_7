from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "rammsat")
@allure.feature("Задача")
@allure.story("Доступность задачи пользователю")
@allure.link("https://github.com", name="Testing")
def test_on_selene():
    browser.open('https://github.com')

    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys("eroshenkoam/allure-example")
    browser.element('.header-search-input').submit()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element('#issues-tab').click()

    assert browser.element(by.partial_text("#76")).should(be.visible)
