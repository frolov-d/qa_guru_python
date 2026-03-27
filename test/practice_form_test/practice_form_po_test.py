from pathlib import Path

from selene import command, have
from selene.support.shared import browser


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.gender_male = browser.all('[name=gender]').element_by(have.value('Male'))
        self.user_number = browser.element('#userNumber')
        self.date_of_birth_input = browser.element('#dateOfBirthInput')
        self.month_select = browser.element('.react-datepicker__month-select')
        self.year_select = browser.element('.react-datepicker__year-select')
        self.subjects_input = browser.element('#subjectsInput')
        self.hobby_reading = browser.element('[for=hobbies-checkbox-2]')
        self.upload_picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit_button = browser.element('#submit')
        self.results_table = browser.element('.table')

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_first_name(self, value):
        self.first_name.type(value)

    def fill_last_name(self, value):
        self.last_name.type(value)

    def fill_email(self, value):
        self.user_email.type(value)

    def select_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    def fill_mobile_number(self, value):
        self.user_number.type(value)

    def fill_date_of_birth(self, year, month, day):
        self.date_of_birth_input.click()
        self.month_select.type(month)
        self.year_select.type(year)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def add_subject(self, subject):
        self.subjects_input.type(subject).press_enter()

    def select_hobby(self, hobby):
        if hobby == 'Reading':
            self.hobby_reading.perform(command.js.scroll_into_view)
            self.hobby_reading.click()

    def upload_picture_file(self, file_path):
        self.upload_picture.set_value(str(file_path))

    def fill_address(self, address):
        self.current_address.type(address)

    def select_state(self, state_name):
        self.state.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(state_name)
        ).click()

    def select_city(self, city_name):
        self.city.click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(city_name)
        ).click()

    def submit_form(self):
        self.submit_button.perform(command.js.click)

    def assert_registered_user_info(self, name, email, gender, telephone_number, date_of_birth,
                                   subject, hobby, photo, address, location):
        self.results_table.all('td').even.should(
            have.exact_texts(
                name,
                email,
                gender,
                telephone_number,
                date_of_birth,
                subject,
                hobby,
                photo,
                address,
                location
            )
        )


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Dmitry')
    registration_page.fill_last_name('F')
    registration_page.select_gender('Male')
    registration_page.fill_mobile_number('8005553535')
    registration_page.fill_email('test@test.test')
    registration_page.select_hobby('Reading')
    registration_page.fill_address('123 Main St.')
    registration_page.select_state('NCR')
    registration_page.select_city('Delhi')
    registration_page.fill_date_of_birth('1990', 'May', '11')
    registration_page.add_subject('Computer Science')
    registration_page.upload_picture_file(Path(__file__).parent.parent / 'resources' / 'picture.jpg')
    registration_page.submit_form()

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