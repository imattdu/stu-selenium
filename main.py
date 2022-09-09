import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    # 长截图配置
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    driver.get(
        "https://www.selenium.dev/zh-cn/documentation/webdriver/browser/windows/#%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE")
    time.sleep(1)

    # 用js获取页面的宽高，如果有其他需要用js的部分也可以用这个方法
    width = driver.execute_script("return document.documentElement.scrollWidth")

    height = driver.execute_script("return document.documentElement.scrollHeight")

    # 获取页面宽度及其宽度
    print(width, height)

    # 将浏览器的宽高设置成刚刚获取的宽高
    driver.set_window_size(width, height)

    time.sleep(5)

    driver.save_screenshot('./224.png')
    driver.quit()
