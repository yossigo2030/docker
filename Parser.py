from lxml import etree as Et

TAGS = ["browser_type", "excepted_title", "first_name", "mail", "password", "password_confirm"]

# dict = {"browser_type": "edge", "excepted_title":"BUYME אתר המתנות והחוויות הגדול בישראל | Gift Card",
#         "first_name": "first_name", "mail": "garygaryyh@gmail.com",
#        "password": "garyP123@", "password_confirm":"garyP123@" }


class Parser:

    def __init__(self, file_name):
        # pass
        self.__tree = Et.parse(file_name).getroot()

    def get_text(self, tag_name):
        # return dict[tag_name]
        return self.__tree.find(tag_name).text