import time
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
print("Chrome WebDriver initialized successfully.")

driver.get("https://www.kap.org.tr/en")
driver.implicitly_wait(10)

panel1 = driver.find_element(By.ID, "home-tab-financial")
panel1.click()

""""
text_to_paste = "AFYON NABER"
company_input = driver.find_element(By.ID, "search-input")
driver.execute_script("arguments[0].value = arguments[1];", company_input, text_to_paste)
driver.execute_script("arguments[0].dispatchEvent(new Event('input', { bubbles: true }));", company_input)
time.sleep(1)

ActionChains(driver).send_keys(Keys.ENTER).perform()


company_input = driver.find_element(By.ID, "search-input")
text_to_paste = "KONYA ŞEKER SANAYİ VE TİCARET A.Ş."
wait = WebDriverWait(driver, 10)
company_input = wait.until(EC.presence_of_element_located((By.ID, "search-input")))
company_input.click()
company_input.clear()
company_input.send_keys(text_to_paste)
time.sleep(1)
company_input.send_keys(Keys.ENTER)
"""

company_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-input")))
company_input.click()
company_input.clear()
time.sleep(0.5)
text_to_paste = "KONYA ŞEKER "
for char in text_to_paste:
    company_input.send_keys(char)
    time.sleep(0.1)  

time.sleep(2)

company_input.send_keys(Keys.ENTER)




year_dropdown_container = driver.find_element(By.XPATH, "//span[text()='Year']/following-sibling::div[contains(@class, 'custom-select')]")
year_button = year_dropdown_container.find_element(By.CLASS_NAME, "select-button")
year_button.click()
year_option = year_dropdown_container.find_element(By.XPATH, ".//label[text()='2025']")
year_option.click()
print("Year selected successfully.")



period_dropdown_container = driver.find_element(By.XPATH, "//span[text()='Period']/following-sibling::div[contains(@class, 'custom-select')]")
period_button = period_dropdown_container.find_element(By.CLASS_NAME, "select-button")
period_button.click()
period_option = period_dropdown_container.find_element(By.XPATH, ".//label[text()='All Periods']")
period_option.click()
print("Period selected successfully.")



#<div class="justify-between w-full"><label class="lg:block hidden font-normal text-sm mb-3 text-text-color">Şirket Ünvanı</label><input id="search-input" type="text" autocomplete="off" class=" border-0 text-dark text-sm block p-4 lg:py-4 py-3 w-full placeholder-dark rounded-md focus:border-transparent focus:ring-transparent  relative lg:hover:border lg:border lg:focus:ring-kap-gray lg:focus:border-kap-gray lg:border-transparent lg:hover:border-kap-gray lg:transition-border lg:ease-in-out lg:duration-300 lg:rounded-md" placeholder="Şirket Ünvanı" value=""><div id="select-dropdown" class="opacity-0 invisible absolute left-0 mt-1 w-full rounded-md z-50 p-4 max-h-300 shadow-lg bg-white overflow-y-auto transition-opacity duration-300" style="width:fit-content;min-width:35%"><div class="bg-light-gray rounded-xl grid gap-y-1 p-3"><ul class="bg-light-gray rounded-xl grid gap-y-1 p-3"></ul></div></div></div>
#<div class="justify-between w-full lg:w-fit"><span class="lg:block hidden font-normal text-sm mb-3 text-text-color">Yıl</span><div class="custom-select relative w-full lg:w-auto lg:border lg:hover:border lg:border-transparent lg:hover:border-kap-gray lg:transition-border lg:ease-in-out lg:duration-300 lg:rounded-md"><div class="select-button cursor-pointer flex justify-between 2xl:min-w-340 xl:min-w-304 lg:min-w-248 w-full items-center p-4 lg:py-4 py-3 text-dark font-normal bg-white rounded-lg"><span class="selected-value text-left text-sm" data-value="2024">2025</span><svg xmlns="http://www.w3.org/2000/svg" width="13" height="8" viewBox="0 0 13 8" fill="none"><path d="M11 1.75L6.5 6.25L2 1.75" stroke="#B12009" stroke-width="1.6" stroke-linecap="square"></path></svg></div><div class="opacity-0 invisible select-dropdown rounded-md z-50 mt-2.5 min-w-64 absolute text-sm w-full shadow-[0_12px_18px_rgba(0,0,0,0.2)] bg-white overflow-y-auto max-h-200 transition-[0.5s] duration-[ease] origin-[top_center]" role="listbox"><ul class="pt-0"><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">2026</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">2025</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">2024</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">2023</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">2022</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">2021</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">2020</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">2019</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">2018</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">2017</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">2016</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">2015</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">2014</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">2013</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">2012</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">2011</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">2010</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">2009</label></button></li></ul></div></div></div>
#<div class="justify-between  w-full lg:w-fit"><span class="lg:block hidden font-normal text-sm mb-3 text-text-color">Periyot</span><div class="custom-select relative w-full lg:w-auto lg:border lg:hover:border lg:border-transparent lg:hover:border-kap-gray lg:transition-border lg:ease-in-out lg:duration-300 lg:rounded-md"><div class="select-button cursor-pointer flex justify-between 2xl:min-w-340 xl:min-w-304 lg:min-w-248 w-full items-center p-4 lg:py-4 py-3 text-dark font-normal bg-white rounded-lg"><span class="selected-value text-left text-sm" data-value="">Yıllık</span><svg xmlns="http://www.w3.org/2000/svg" width="13" height="8" viewBox="0 0 13 8" fill="none"><path d="M11 1.75L6.5 6.25L2 1.75" stroke="#B12009" stroke-width="1.6" stroke-linecap="square"></path></svg></div><div class="opacity-0 invisible select-dropdown rounded-md z-50 mt-2.5 min-w-72 absolute text-sm w-full shadow-[0_12px_18px_rgba(0,0,0,0.2)] bg-white overflow-y-auto transition-[0.5s] duration-[ease] origin-[top_center]" role="listbox"><ul class="pt-0"><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">Tüm Dönemler</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">3 Aylık</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">6 Aylık</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">9 Aylık</label></button></li><li class="hover:bg-light-danger"><button class="w-full text-start"><label class="text-sm py-2 px-4 cursor-pointer block">Yıllık</label></button></li></ul></div></div></div>


