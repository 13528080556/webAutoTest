# @Time    : 2019/12/12 10:31
# @Author  : Hugh
# @email   : 609799548@qq.com

from pageElement.base import Base


class LoginPage(Base):

    loc_input_username = ('id', 'username')
    loc_input_password = ('id', 'password')
    loc_login_button = ('class name', 'btn')

    def send_username(self, text):
        self.send(self.loc_input_username, text)

    def send_password(self, text):
        self.send(self.loc_input_password, text)

    def click_login_button(self):
        self.click(self.loc_login_button)



