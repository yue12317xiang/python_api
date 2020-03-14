import unittest
from ddt import ddt,data
from httprquest import HttpRequest
from shopping_excel import Doo_Excel
from read_config import Read_Config
from my_log import Mylog
test_data = Doo_Excel().get_data("data.xlsx")
COOKIE = None
@ddt
class Test_ShoppingHttpRequest(unittest.TestCase):
    @data(*test_data)
    def test_httrequest(self,item):
        global COOKIE
        res = HttpRequest().httrequest(item["url"],eval(item["data"]),item["method"],cookies=COOKIE)
        if res.cookies:#获取cookies
            COOKIE = res.cookies
        try:
            self.assertEqual(item["code"],res.json()["code"]) #添加断言
            print("-------------------",item["url"],"-----------")
            print("-------------------",item["data"],"-----------")

            print("获取到的结果是：",res.json())
            qiwang = "PASS"
        except Exception as e:
            qiwang = "Failed"
            print("执行用例失败",e)
            raise e
        finally:
             Doo_Excel().write_data("data.xlsx",item["sheet_name"],item["code_id"]+1,str(res.json()),qiwang)
    