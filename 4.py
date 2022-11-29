from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import time

driver = webdriver.Chrome()
driver.get("https://www.sociolla.com/2413-body-wash")
time.sleep(6)


try:
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "mainbody"))) #waits 10 seconds until element is located. Can have other wait conditions  such as visibility_of_element_located or text_to_be_present_in_element

    html = driver.page_source
    # print(html)
    soup = bs(html, 'html.parser')
    paging = soup.find("ul","pagination").find_all("li")
    # print(paging)
    lastPage = paging[len(paging)-1].text

    pages = list(range(1,int(lastPage)+1))
    for page in pages:
        url = "https://www.sociolla.com/2413-body-wash?page=%s" %(page)
        driver.get(url)
        time.sleep(3)
        soup = bs(driver.page_source, 'html.parser')
        
        list_products = soup.find_all('div', {'class': 'loaded-item'})
        for list in list_products:
            brandProduct = [x.text for x in list.find('a', {'class': 'product__brand'})]
            nameProduct = [x.text for x in list.find('p', {'class': 'product__name'})]
            priceProduct = [x.text for x in list.find('div', {'class': 'product-price__stroke'})]
            discountedPrice = [x.text for x in list.find('div', {'class': 'product__info-discount'})]
            productReviews = [x.text for x in list.find('span', {'class': 'product__reviews'})]
   
            print("brand :", brandProduct, "name :", nameProduct, "harga :", priceProduct, "harga diskon :", discountedPrice,"Product Reviews :",productReviews)

except:
    print("Couldnt locate element")