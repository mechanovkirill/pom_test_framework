import time

from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box_positive(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            name, email, curr_address, per_address = text_box_page.fill_all_fields()
            output_name, output_email, output_curr_address, output_per_address = text_box_page.check_filled_form()
            print(text_box_page.fill_all_fields())
            print(text_box_page.check_filled_form())
            # assert name == output_name
            # assert email == output_email
            # assert curr_address == output_curr_address
            # assert per_address == output_per_address
            time.sleep(6)
