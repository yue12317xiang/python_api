import unittest
from selenium import webdriver
class SearchTest(unittest.TestCase):
    #打开网站操作
    def setUp(self): #优先执行的方法（初始化数值）
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('http://demo.magentocommerce.com/')
        #self.driver.get("http://demo.magentocommerce.com/")
    def test_search_by_category(self):
        #定位搜索框并清空搜索框中的内容
        self.search_field=self.driver.find_element_by_name("keys")
        # self.search_field.clear()
        #输入内容搜索
        # self.search_field.mouseenter("search-icon icon-container")
        self.search_field.send_keys("phones")
        self.search_field.submit()
        #xpath定位
        products = self.driver.find_element_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(2,len(products))
        #清空初始化值
    def tearDown(self):
            self.driver.quit()
        #调用main方法
if __name__ == '__main__':
            unittest.main(verbosity=2)
            
        