from Parser import Parser
from BuyMe import BuyMe
import unittest
import time

class MyTestCase(unittest.TestCase):
    __title = None
    __filePath = "/usr/workspace/config_buy_me_ex.xml"
    # __filePath = "C:\\Users\\gary\\school\\portland\\buy_me_docker\\config_buy_me_ex.xml"
    __buy_me = None
    __parser = None

    @classmethod
    def setUpClass(cls):
        cls.__parser = Parser(cls.__filePath)
        cls.__buy_me = BuyMe(cls.__parser.get_text("browser_type"))
        cls.__title = cls.__buy_me.get_title()
        cls.__buy_me.register_sign_up_item()
        cls.__buy_me.register_item()
        cls.__buy_me.name_item()
        cls.__buy_me.mail_item()
        cls.__buy_me.password_item()
        cls.__buy_me.confirm_password_item()
        cls.__buy_me.sign_up_item()
        cls.__title = cls.__buy_me.getDriver().title

    def test_title(self):
        self.assertEqual(self.__parser.get_text("excepted_title"), self.__title, "titles don't match!")

    def test_registration(self):
        self.assertTrue(self.register(), "Failed to register!")

    def register(self):
        self.__buy_me.send_keys_name_item(self.__parser.get_text("first_name"))
        self.__buy_me.send_keys_mail_item(self.__parser.get_text("mail"))
        self.__buy_me.send_keys_password_item(self.__parser.get_text("password"))
        self.__buy_me.send_keys_password_confirm_item(self.__parser.get_text("password"))
        try:
            self.__buy_me.get_sign_up_item().click()
            self.__buy_me.getDriver().find_element_by_css_selector("img[class = 'arrow']")
            time.sleep(2)
            return True
        except:
            return False

    @classmethod
    def tearDownClass(self):
        self.__buy_me.end()


if __name__ == '__main__':
    log_file = 'log_file.txt'
    with open(log_file, "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)