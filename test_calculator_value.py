from selenium import webdriver

chrome_driver = webdriver.Chrome()
chrome_driver.get('http://google.com')

search_input = chrome_driver.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_button = chrome_driver.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')

search_input.send_keys('Калькулятор')
search_button.click()

number_one = chrome_driver.find_element_by_xpath(
    '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[1]/div/div')

multi = chrome_driver.find_element_by_xpath(
    '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[3]/td[4]/div/div')

number_two = chrome_driver.find_element_by_xpath(
    '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[2]/div/div')

minus = chrome_driver.find_element_by_xpath(
    '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[4]/div/div')

number_three = chrome_driver.find_element_by_xpath(
    '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[4]/td[3]/div/div')

plus = chrome_driver.find_element_by_xpath(
    '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[4]/div/div')

equal_button = chrome_driver.find_element_by_xpath(
    '//*[@id="rso"]/div[1]/div/div/div[1]/div/div/div[3]/div/table[2]/tbody/tr[5]/td[3]/div/div')

calc_output = chrome_driver.find_element_by_xpath('//*[@id="cwos"]')

number_one.click()
multi.click()
number_two.click()
minus.click()
number_three.click()
plus.click()
number_one.click()
equal_button.click()


def test_calculator():
    assert int(calc_output.text) == 0
