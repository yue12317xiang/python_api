import unittest
import HTMLTestRunner
from test_httprqust import Test_HttpRequest
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(Test_HttpRequest))
with open("test.html","wb") as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=1, title="这是购物项目", description="这是测试报告")
    runner.run(suite)
