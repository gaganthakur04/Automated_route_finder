# import required modules
from selenium import webdriver
from time import sleep

# assign url in the webdriver object
driver = webdriver.Chrome("C:\\Users\\vin\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.google.co.in/maps/@10.8091781,78.2885026,7z")
sleep(2)

# search locations
def searchplace():
    Place = driver.find_element("id","searchboxinput")
    Place.send_keys("shimla")
    Submit = driver.find_element("xpath","/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div/div[2]/div[1]/button")
    Submit.click()
searchplace()

# get directions
def directions():
    sleep(10)
    directions = driver.find_element("xpath",
        "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button")
    directions.click()
directions()


def find():
    sleep(6)
    find = driver.find_element("xpath",
        "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
    find.send_keys("Delhi")
    sleep(2)
    search = driver.find_element("xpath",
        "/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    search.click()

find()

# get transportation details
def kilometers():
    sleep(5)
    Totalkilometers = driver.find_element("xpath",
        "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]")
    print("Total Kilometers:", Totalkilometers.text)
    sleep(5)
    Train = driver.find_element("xpath",
        "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div")
    print("Train Travel:", Train.text)
    sleep(7)
  
kilometers()

