import unittest
from ddt import ddt,data
from httprquest import HttpRequest
from do_excel import Do_Excel
from read_config import Read_Config
from my_log import Mylog
test_data = Do_Excel().get_data("data.xlsx")
COOKIE = None
@ddt
class Test_HttpRequest(unittest.TestCase):
    @data(*test_data)
    def test_httrequest(self,item):
        global COOKIE
        res = HttpRequest().httrequest(item["url"],eval(item["data"]),item["method"],cookies=COOKIE)
        if res.cookies:#获取cookies
            COOKIE = res.cookies
        try:
            self.assertEqual(item["code"],res.json()["code"]) #添加断言
            # print("-------------------",item["data"],"-----------")
            print("获取到的结果是：",res.json())
            qiwang = "PASS"
        except Exception as e:
            qiwang = "Failed"
            print("执行用例失败",e)
            raise e
        finally:
             Do_Excel().write_data("data.xlsx",item["sheet_name"],item["code_id"]+1,str(res.json()),qiwang)
    