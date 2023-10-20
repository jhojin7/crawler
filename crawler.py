from bs4 import BeautifulSoup
import time
import random

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import exceptions


def run(idx):
    q = f"examtopics-aws-dva-c02-{idx}"
    url = f"https://www.google.com/search?q={q}"
    # xpath = '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/span/a'
    # selector = "#rso > div:nth-child(1) > div > div > div > div > div > span"
    selector = "h3"

    chromedriver_autoinstaller.install()
    opt = Options()
    # opt.add_argument("--headless=new")
    driver = webdriver.Chrome(options=opt)
    wait = WebDriverWait(driver, random.uniform(1, 2))
    driver.get(url)

    # elem = driver.find_element(By.CSS_SELECTOR, css2)
    # wait.until(lambda _: elem.is_displayed())
    # driver.implicitly_wait(5)

    # driver.implicitly_wait(100.0)
    elem = driver.find_element(by=By.CSS_SELECTOR, value=selector)
    # elems = driver.find_elements(by=By.XPATH, value=xpath)
    wait.until(lambda _: elem.is_displayed())
    print(q)

    # click on search result
    time.sleep(random.uniform(1, 2))
    # elem = elems[0]
    elem.click()

    time.sleep(random.uniform(1, 2))
    elem = driver.find_element(by=By.CSS_SELECTOR, value="div.question-body")
    wait.until(lambda _: elem.is_displayed())

    print(driver.current_url)
    with open(f"{q}.html", 'w') as f:
        # f.write(elem.get_attribute("innerHTML"))
        f.write(driver.page_source)
    time.sleep(random.uniform(1, 2))
    driver.quit()
    return

    # for elem in elems:
    for i in range(len(elems)):
        elems = driver.find_elements(
            by=By.CSS_SELECTOR, value="li.Nlist_item > a")
        elem = elems[i]
        wait.until(lambda _: elem.is_displayed())
        print(elem.text)
        try:
            elem.click()
        except exceptions.ElementClickInterceptedException as e:
            driver.execute_script(
                "document.querySelector(arguments[0]).click()", "li.Nlist_item > a")
        else:
            exit()

        h2 = driver.find_element(By.CSS_SELECTOR, "h2")
        wait.until(lambda _: h2.is_enabled(), "aaaaaaaaaaaa")
        print(h2.text)
        driver.back()


for i in range(110, 140):
    run(i)
