from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

browser = webdriver.Chrome(r"C:\Users\Prasanna\Downloads\Compressed\chromedriver_win32\chromedriver.exe")
url ="https://www.youtube.com/channel/UCJM_TguIp5X2ldbQ9U_n3gA/featured"
browser.get(url)
browser.find_element_by_xpath("//*[@id='tabsContent']/paper-tab[2]/div").click()
browser.find_element_by_name
browser.find_element_by_class_name
browser.find_elements_by_id
keys.DOWN
keys.UP
keys.END
keys.delete

browser.close()
browser.fullscreen_window()
browser.switch_to_window()
browser.switch_to_frame()
browser.maximize_window()
i=0
while i<10:
    time.sleep(2)
    scroll = browser.find_element_by_xpath("/html").send_keys(Keys.END)
    i+=1
        
#scroll = browser.find_element_by_tag_name('body').send_keys(Keys.END)
links = list(browser.find_elements_by_id("video-title"))
print(len(links))
print(links.__getattribute__)
time.sleep(5)
browser.close()
