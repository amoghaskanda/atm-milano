import logger

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep

def wait_time(fermata):

    # For Chrome/Chromium use webdriver.Chrome()
    driver = webdriver.Edge()

    driver.get("https://giromilano.atm.it/#/home/")
    driver.refresh()

    print("Displaying wait time for first solution only", end="")
    sleep(1)
    print(".", end="")
    sleep(1)
    print(".", end="")
    sleep(1)
    print(".")

    cerca_fermata = WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"span[translate='lblCercaFermata']")))

    cerca_fermata.click()

    # Locating input
    fermata_input = WebDriverWait(driver,10)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[id='txtFermata']")))

    # Sending our function's parameters as input to the text box
    fermata_input.send_keys(fermata)
    fermata_input.send_keys(Keys.ENTER)

    # Clicking only on the first solution (can be changed later)
    first_solution = WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[class='rowLinea']")))
    first_solution.click()

    # Printing the stop name and route number
    stop_name = WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='divPopupLine ng-binding']")))
    print(stop_name.text)

    # Printing wait time every 30s
    try:
        waiting_time = WebDriverWait(driver, 10)\
            .until(EC.element_to_be_clickable
                                              ((By.CSS_SELECTOR, "span[class ='fontBold pull-right ng-binding']")))\
            .text

        print("Waiting time: " + waiting_time)
    except Exception as e:
        logger.error(e, msg="")


if __name__ == '__main__':
    fermata = input("Enter stop/via/piazza: ")
    wait_time(fermata)
