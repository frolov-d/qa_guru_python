from pathlib import Path

from selene import command
from selene import have
from selene.support.shared import browser


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_day_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def assert_registered_user_info(self, name, email, gender, telephone_number, date_of_birth, subject, hobby,
                                    photo, address, location):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                name,
                email,
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


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Dmitry')


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

    registration_page.fill_day_of_birth('1990', 'May', '11')

    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('#uploadPicture').set_value(
        str(Path(__file__).parent.parent / 'resources' / 'picture.jpg')
    )

    browser.element('#submit').perform(command.js.click)

    # THEN
    registration_page.assert_registered_user_info(
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
    