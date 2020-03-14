import unittest
import HTMLTestRunner
from shopping_testhttprequest import Test_ShoppingHttpRequest
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(Test_ShoppingHttpRequest))
with open("test.html","wb") as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=1, title="这是购物项目", description="这是测试报告")
    runner.run(suite)