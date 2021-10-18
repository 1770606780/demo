'''
    实现前程贷项目：
        注册
        认证：（实名认证，修改手机号，修改登陆密码）
        添加银行卡：
'''
from selenium import webdriver
import time

driver= webdriver.Chrome()

# 注册
driver.get("http://8.129.91.152:8765/")
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/span[1]").click()
driver.find_element_by_xpath("//*[@id='phone']").send_keys("17656851495")
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[4]/input").send_keys("liuhao0.0")
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[5]/label/input").click()
# 断掉
time.sleep(20)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/form/div[6]/button").click()
driver.find_element_by_xpath("//*[@id='layui-layer2']/div[3]/a[1]").click()
time.sleep(5)

# 认证
driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/span[3]/a").click()
driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]/a/img").click()
driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/ul/li[1]/a").click()
driver.find_element_by_xpath("//*[@id='layui-layer1']/div[2]/div/form/div[1]/div/input").send_keys("孙老头")
driver.find_element_by_xpath("//*[@id='layui-layer2']/div[2]/div/form/div[2]/div/input").click()
driver.find_element_by_xpath("//*[@id='layui-layer2']/div[2]/div/form/div[3]/div/button").click()
driver.find_element_by_xpath("//*[@id='layui-layer3']/span").click() #点击x
time.sleep(5)

# 修改手机号
driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/ul/li[2]/a").click()
driver.find_element_by_xpath("//*[@id='layui-layer4']/div[2]/div/form/div[1]/a").click()
time.sleep(15)
driver.find_element_by_xpath("//*[@id='layui-layer4']/div[2]/div/form/div[3]/button").click()

# 修改密码
driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/ul/li[4]/a").click()
driver.find_element_by_xpath("//*[@id='layui-layer5']/div[2]/div/form/div[1]/input").send_keys("liuhao0.0")
driver.find_element_by_xpath("//*[@id='layui-layer5']/div[2]/div/form/div[2]/input").send_keys("") #新密码
driver.find_element_by_xpath("//*[@id='layui-layer5']/div[2]/div/form/div[3]/input").send_keys("") #新密码
driver.find_element_by_xpath("//*[@id=l'ayui-layer5']/div[2]/div/form/div[5]/button[1]").click()
time.sleep(5)

# 添加银行卡
driver.find_element_by_xpath("/html/body/div/div[2]/ul/li[2]/a").click()
driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div/a").click()
########################################################################



























