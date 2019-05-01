from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv
import time

url = 'https://restructuring.primeclerk.com/pge/Home-ClaimInfo'

driver = webdriver.Chrome()
driver.implicitly_wait(300)
driver.get(url)

with open('claims.csv', 'w') as f:
    csv_w = csv.writer(f)
    csv_w.writerow(['creditor', 'debtor', 'claim'])

    while True:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        time.sleep(1)
        rows = soup.select('tbody .jqgrow :nth-child(n + 6)')

        creditors = [val.get_text() for val in rows[::3]]
        debtors = [val.get_text() for val in rows[1::3]]
        claims = [val.get_text() for val in rows[2::3]]

        for creditor, debtor, claim in zip(creditors, debtors, claims):
            csv_w.writerow([creditor, debtor, claim])

        new_page_button = driver.find_element_by_id('next_pager1')
        attrs = new_page_button.get_attribute('class').split(' ')
        if 'ui-state-disabled' not in attrs:
            new_page_button.click()
        else:
            break

driver.quit()
