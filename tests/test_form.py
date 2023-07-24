import os

from selene import browser, have


# Тест для заполнения и отправки формы

def test_fill_and_submit_form(setup_browser):

    browser.open('/automation-practice-form')

    # Заполнение полей формы
    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Doe')
    browser.element('#userEmail').type('johndoe@example.com')
    browser.element('//label[text()="Male"]').click()
    browser.element('#userNumber').type('1234567890')

    # Выбор даты рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys('June')  # Июнь
    browser.element('.react-datepicker__year-select').send_keys('1990')
    browser.element(f'.react-datepicker__day--0{15}').click()  # Выбираем 15-е число

    # Выбор предметов
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('//label[text()="Sports"]').click()

    # Загрузка файла
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture/Streets.png'))

    # Ввод текущего адреса
    browser.element('#currentAddress').type('123 Street, City, Country')

    # Выбор штата и города
    browser.element('#state').click()
    browser.all("#state div").element_by(have.exact_text("NCR")).click()
    browser.element('#city').click()
    browser.all("#city div").element_by(have.exact_text("Delhi")).click()

    # Отправка формы
    browser.element('#submit').click()

    # Ожидание появления модального окна перед выполнением проверок
    browser.element('.modal-title').should(have.exact_text('Thanks for submitting the form')).wait_until(
        have.exact_text('Thanks for submitting the form'))

    # Проверка успешной отправки формы
    browser.element('.table').all('td:nth-of-type(2)').should(
        have.texts(
            'John Doe',
            'johndoe@example.com',
            'Male',
            '1234567890',
            '15 June,1990',
            'Maths',
            'Sports',
            'Streets.png',
            '123 Street, City, Country',
            'NCR Delhi',
        )
    )
