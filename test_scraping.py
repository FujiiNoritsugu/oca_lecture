import time
from selenium import webdriver

def main():
    driver = webdriver.Chrome('/home/fujii/oca_lecture/scraping/chromedriver')
    driver.get('https://www.google.co.jp')
    time.sleep(5)
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5)
    driver.quit()
    
if __name__ == '__main__':
    main()
