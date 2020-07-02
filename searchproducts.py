from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://demo.magentocommerce.com/")
search_filed=driver.find_element_by_name("q")
search_filed.clear()
search_filed.send_keys("phones")
search_filed.submit()
products = driver.find_element_by_xpath("//h2[@class='product-name']/a")
print("Found"+str(len(products))+"products:")
for product in products:
    print(product.text)
driver.quit()