from appium import webdriver

#This is the config I used in my android simulator.
desired_caps = {
    "deviceName":"Pixel_3a_API_30_x86",
    "platformName":"Android",
    #Path where your app is
    "app":"~/PunkApp.apk"
}

#I used alpha dog because the one you proposed couldn't be loaded.
alpha_dog_description = "A fusion of caramel malt flavours and punchy New Zealand hops. A session beer you can get your teeth into."

#Instance of webdriver
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#Wait by default 10 secs for any element.
driver.implicitly_wait(10)

#I had to do a relative Xpath because there were so many generic elements.
beer = driver.find_element_by_xpath("//*[contains(@text,'Alpha Dog')]")
beer.click()

#Get the description of the element.
description = driver.find_element_by_id("com.ijikod.punkapp:id/description_txt")

#For you to see in the console, asserting won't give you any feedback on the console unless false.
print(description.text == alpha_dog_description)
assert description.text == alpha_dog_description
driver.quit()