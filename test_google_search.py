from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "path/to/chromedriver.exe"


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)


driver.get("https://www.google.com/en")


search_box = driver.find_element("name", "q")
search_box.send_keys("Mercedes A Class")
search_box.send_keys(Keys.RETURN)


search_results = driver.find_elements("css selector", ".tF2Cxc")

target_result = None
target_page_number = None


for page_number, result in enumerate(search_results, start=1):
    if "engine/horsepower" in result.text.lower() and "specifications" in result.text.lower():
        target_result = result
        target_page_number = page_number
        break

assert target_result is not None, "Target result not found in search results"


print(f"Target result found on page: {target_page_number}")


driver.quit()
