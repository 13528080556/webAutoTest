# @Time    : 2019/12/12 10:38
# @Author  : Hugh
# @email   : 609799548@qq.com

from pageElement.base import Base


class BBSPage(Base):

    loc_nav_bbs = ('link text', '论坛')
    loc_content = ('css selector', 'ul.article-list > li:nth-child(%s)')
    loc_page_number = ('css selector', 'ul.pageOutside > li:nth-child(%s)')
    loc_publish_button = ('class name', 'publish')

    def click_nav_bbs(self):
        self.click(self.loc_nav_bbs)

    def click_content(self, number):
        loc = (self.loc_content[0], self.loc_content[1] % number)
        self.click(loc)

    def click_publish(self):
        self.click(self.loc_publish_button)

    def click_page_number(self, number):
        loc = (self.loc_page_number[0], self.loc_page_number[1] % number)
        self.click(loc)

