from behave import *
from appium import webdriver

@given(u'appium is setup')
def step_impl(context):
    #This is the config I used in my android simulator.
    context.desired_caps = {
    "deviceName":"Pixel_3a_API_30_x86",
    "platformName":"Android",
    #Path where your app is
    "app":"~/PunkApp.apk"
}

@given(u'the main page is shown')
def step_impl(context):
    #Instance of webdriver
    context.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', context.desired_caps)
    #Wait by default 10 secs for any element.
    context.driver.implicitly_wait(10)

@when(u'the user enters in alpha dog')
def step_impl(context):
    #I had to do a relative Xpath because there were so many generic elements.
    beer = context.driver.find_element_by_xpath("//*[contains(@text,'Alpha Dog')]")
    beer.click()

@then(u'the description is correct')
def step_impl(context):
    #I used alpha dog.
    alpha_dog_description = "A fusion of caramel malt flavours and punchy New Zealand hops. A session beer you can get your teeth into."
    #Get the description of the element.
    description = context.driver.find_element_by_id("com.ijikod.punkapp:id/description_txt")

    #For you to see in the console, asserting won't give you any feedback on the console unless false.
    print(description.text == alpha_dog_description)
    assert description.text == alpha_dog_description

    context.driver.quit()
