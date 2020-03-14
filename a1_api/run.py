from httprquest import HttpRequest
from do_excel import Do_Excel
COOKIES = None
def runn(test_data,sheet_name):
    global COOKIES
    for item in test_data:
        res = HttpRequest().httrequest(item["url"],eval(item["data"]),item["method"],cookies=COOKIES)
        if res.cookies:
            COOKIES = res.cookies
        print("响应结果为：",res.json())
        Do_Excel().write_data("data.xlsx",sheet_name,item["code_id"]+1,str(res.json()))
test_data = Do_Excel().get_data("data.xlsx","denglu")
runn(test_data,"denglu")
test_data = Do_Excel().get_data("data.xlsx","zhuce")
runn(test_data,"zhuce")
test_data = Do_Excel().get_data("data.xlsx","chongzhi")
runn(test_data,"chongzhi")
        