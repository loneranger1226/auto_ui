from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time

from selenium.webdriver.support.wait import WebDriverWait


def open_browser(browser_type):
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_experimental_option('useAutomationExtension', False)
    try:
        driver = getattr(webdriver, browser_type)(options=option)
    except Exception as e:
        print(e)
        driver = webdriver.Chrome(options=option)
    return driver


class Key(object):
    def __init__(self, browser_type):
        self.driver = open_browser(browser_type)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # def __init__(self, browser_type, log):
    #     self.driver = open_browser(browser_type)
    #     self.driver.maximize_window()
    #     self.log = log
    #     self.driver.implicitly_wait(10)

    def open(self, url):
        self.driver.get(url)

    def locate(self, name, value):
        # if len(self.driver.window_handles) > 1:
        #     self.driver.switch_to.window(self.driver.window_handles[-1])
        #     self.switch_to_iframe()
        return self.driver.find_element(name, value)

    # 输入
    def input(self, name, value, text):
        self.locate(name, value).send_keys(text)

    # 点击
    def click(self, name, value):
        self.locate(name, value).click()
        time.sleep(1)

    # 显示等待
    def web_el_wait(self, name, value):
        return WebDriverWait(self.driver, 10, 0.5).until(
            lambda el: self.locate(name, value), message="元素查找失败"
        )

    # 切换Iframe
    def switch_to_iframe(self, value, name=None):
        if not name:
            self.driver.switch_to.frame(value)
        self.driver.switch_to.frame(self.locate(name, value))

    # 切换句柄
    def switch_handle(self, close=False, index=1):
        handles = self.driver.window_handles
        if close:
            self.driver.close()
        self.driver.switch_to.window(handles[index])

    # 切换default窗口
    def switch_default(self):
        self.driver.switch_to.default_content()

    def wait(self, sleep_time):
        time.sleep(sleep_time)

    def assert_text(self, name, value, expect):
        try:
            text = self.locate(name, value).text
            assert text == expect, "断言失败，实际结果为：{}".format(text)
            return True
        except Exception as e:
            self.log.exception("出现异常，断言失败：实际结果与预期不符：{}".format(e))
            return False

    # 退出
    def quit(self):
        self.driver.quit()
