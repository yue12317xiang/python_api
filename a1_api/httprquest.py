import requests
from my_log import Mylog
class HttpRequest:
    def httrequest(self,url,data,method,**kwargs):
        try:
            if method == "GET":
                res = requests.get(url,data,**kwargs)
            elif method == "POST":
                res = requests.post(url,data,**kwargs)
            else:
                Mylog().info("给的请求方式不正确")
        except Exception as e:
            Mylog().error("请调整请求方式")
            raise e
        return res
if __name__ == '__main__':
    register_url = "http://localhost:3000/users/register"
    register_data = {"userName":"admin111","password":"123123"}
    login_url = "http://localhost:3000/users"
    login_data = {"userName":"admin111","password":"123123"}
    pay_url = "http://localhost:3000/users/topUp"
    pay_data = {"money":"50"}
    register_res = requests.post(register_url,register_data,"POST")
    login_res = requests.post(login_url,login_data,"POST")
    pay_res = requests.post(pay_url,pay_data,"POST",cookies=login_res.cookies)
    print("充值结果为：",pay_res.json())
    
