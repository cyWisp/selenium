#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from time import sleep


if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(
        options=chrome_options,
    )

    driver.get('')

    user_name = driver.find_element(By.ID, 'uname')

    user_name.clear()
    user_name.send_keys('Shawna')

    pass_word = driver.find_element(By.ID, 'password')
    pass_word.clear()
    pass_word.send_keys('Palooka')

    # try:
    #     driver.find_element(By.XPATH,"//button[@type='submit' and @id='logon']").click()
    #     print('click was successful')
    #
    # except Exception as e:
    #     print(e)

    # sleep(3)

    driver.get_screenshot_as_file('test.png')
    driver.close()




