from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://irs.thsrc.com.tw/IMINT/")

button = driver.find_element_by_name('confirm')
button.click()

startStation = Select(driver.find_element_by_name('selectStartStation'))
startStation.select_by_value('2')

destinationStation = Select(driver.find_element_by_name('selectDestinationStation'))
destinationStation.select_by_value('7')

driver.find_element_by_id('trainCon:trainRadioGroup_0').click()

driver.find_element_by_id('seatRadio1').click()

driver.find_element_by_id('bookingMethod_1').click()

destinationStation = driver.find_element_by_name('toTrainIDInputField')
destinationStation.send_keys('mmj-2159')

# button = driver.find_element_by_id('SubmitButton')
# button.click()