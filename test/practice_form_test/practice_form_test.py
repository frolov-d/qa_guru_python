from pathlib import Path

from selene.support.shared import browser
from selene import have, by
from selene import command

import test
from test import resources


def test_student_registration_form():
    browser.open('/automation-practice-form')
    browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
        have.size_greater_than_or_equal(3)
    )
    browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    # WHEN
    browser.element('#firstName').type('Dmitry')
    browser.element('#lastName').type('F')
    browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()
    browser.element('#userNumber').type('8005553535')
    browser.element('#userEmail').type('test@test.test')
    browser.element('[for=hobbies-checkbox-2]').perform(command.js.scroll_into_view)
    browser.element('[for=hobbies-checkbox-2]').click()

    browser.element('#currentAddress').type('123 Main St.')

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('NCR')
    ).click()

    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('Delhi')
    ).click()

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type('May')
    browser.element('.react-datepicker__year-select').type('1990')
    browser.element(f'.react-datepicker__day--0{11}:not(.react-datepicker__day--outside-month)').click()

    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('#uploadPicture').set_value(
        str(Path(__file__).parent.parent / 'resources' / 'picture.jpg')
    )

    browser.element('#submit').perform(command.js.click)

    # THEN
    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'Dmitry F',
            'test@test.test',
            'Male',
            '8005553535',
            '11 May,1990',
            'Computer Science',
            'Reading',
            'picture.jpg',
            '123 Main St.',
            'NCR Delhi'
        )
    )