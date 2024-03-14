import os, allure
from selene import browser, have


def test_filling_form():
    with allure.step("Открыть страницу регистрации"):
        browser.open('automation-practice-form')

    with allure.step("Заполнить форму и отправить"):
        browser.element('#firstName').type('Gercog')
        browser.element('#lastName').type('Perkins')
        browser.element('#userEmail').type('Chester@mail.com')
        browser.element('[for="gender-radio-1"]').click()
        browser.element('#userNumber').type('7890005670')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('[value="0"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('[value="1950"]').click()
        browser.element('.react-datepicker__day--016').click()
        browser.element('#subjectsInput').type('M')
        browser.element('#react-select-2-option-1').click()
        browser.element('[for="hobbies-checkbox-2"]').click()
        browser.element('#uploadPicture').send_keys(os.path.abspath('Chester-Mills.jpeg'))
        browser.element('#currentAddress').type('Chester-Mills, Center')
        browser.element('#react-select-3-input').type('Haryana').press_enter()
        browser.element('#react-select-4-input').type('Karnal').press_enter()
        browser.element('#submit').click()

    with allure.step("Проверить, что отправленная форма содержит корректные данные"):
        browser.element('.table').should(have.text('Gercog Perkins'))
        browser.element('.table').should(have.text('Chester@mail.com'))
        browser.element('.table').should(have.text('Male'))
        browser.element('.table').should(have.text('7890005670'))
        browser.element('.table').should(have.text('16 January,1950'))
        browser.element('.table').should(have.text('Chemistry'))
        browser.element('.table').should(have.text('Reading'))
        browser.element('.table').should(have.text('Chester-Mills.jpeg'))
        browser.element('.table').should(have.text('Chester-Mills, Center'))
        browser.element('.table').should(have.text('Haryana Karnal'))
