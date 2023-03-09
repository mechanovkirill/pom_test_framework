from pages.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators
from data.data import generated_person


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self) -> tuple[str, str, str, str]:
        person_data = next(generated_person())
        full_name: str = person_data.full_name
        email: str = person_data.email
        current_address: str = person_data.current_address
        permanent_address: str = person_data.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()

        return full_name, email, current_address, permanent_address

    def check_filled_form(self) -> tuple[str, str, str, str]:
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text
        email = self.element_is_present(self.locators.CREATED_EMAIL).text
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text
        full_name: str = full_name.split(':')[1]
        email: str = email.split(':')[1]
        current_address: str = current_address.split(':')[1]
        permanent_address: str = permanent_address.split(':')[1]

        return full_name, email, current_address, permanent_address




