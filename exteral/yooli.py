import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_argument("--headless")

base_url = "https://www.yooli.com/dingcunbao/detail/101.html"
#对应的chromedriver的放置目录
driver = webdriver.Chrome(executable_path=('/home/jim/.local/bin/chromedriver'), chrome_options=chrome_options)

driver.get(base_url)

start_time=time.time()
print('this is start_time ',start_time)

driver.find_element_by_xpath("//*[@id='investTabs']/li[3]").click()

# driver.execute_script("arguments[0].scrollIntoView(true)", driver.find_element_by_xpath("//div[@id='loanInvsetRecordPager']/div/a[last()-1]")); 

page = True

while page:
	datas = driver.find_element_by_id("financePlanInvestorTable")
	datas = datas.find_elements_by_tag_name("ul")
	for data in datas:
		print('name:', data.find_element_by_xpath("li[@class='col_1']/span").text, end='\t')
		print('amount:', data.find_element_by_xpath("li[@class='col_2']").text, end='\t')
		print('time:', data.find_element_by_xpath("li[@class='col_3']").text, end='\n')
	# driver.save_screenshot('screen.png')
	js="var q=document.documentElement.scrollTop=5000"
	driver.execute_script(js)
	time.sleep(1)
	page_index = driver.find_element_by_xpath("//*[@id='financePlanInvestorTablePager']/div/a[last()]")
	page_st = page_index.text
	print(page_st)
	if '>' not in page_st:
		page = False
	else:
		#js="var q=document.documentElement.scrollTop=5000"  
		#driver.execute_script(js)
		#time.sleep(2)
		#ActionChains(driver).move_to_element(page_index).perform()
		page_index.click()
		time.sleep(1)

driver.close()

end_time=time.time()
print('spent time: ',end_time-start_time)