
import requests

from bs4 import BeautifulSoup



from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def write_txt(myFunc, myString):
    with open("{}.txt".format(myFunc), "w", encoding="utf-8") as text_file:
        text_file.write(myString)


def amazon_lamps():
    #Can't access Amazon using simple requests. 
    url = "https://www.amazon.com/s?k=lamp"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    print(soup.findAll('a'))


def github_python():
    #In this function, we are looking to pull contextual information from github repos
    #We search the github searchbar for 
    #class mt-n1

    #Nagivate to github homepage
    driver = webdriver.Firefox()
    driver.get("https://github.com")
    search_bar = driver.find_element_by_name("q") #pull out search bar
    search_bar.send_keys("Python") #Type query into search bar
    search_bar.send_keys(Keys.RETURN) #Mimic hitting the enter key

    # url = "https://github.com/search?q=python"
    # response = requests.get(url)
    # print(response.status_code)
    # soup = BeautifulSoup(response.text, "html.parser")
    print(driver.page_source)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    list_items = soup.findAll('div', class_="mt-n1")
    for item in list_items:
        repo_name = ''.join(map(lambda x: x.string, item.a.contents)) #Gets the name of the repo by pulling in the first instance of the <a> in the div element. Some extra formatting required 
        print(repo_name)

    # write_txt(github_python.__name__, soup.prettify())

 

    
    


if __name__ =="__main__":
    import timeit #Package for timing function execution

    # print(timeit.timeit("main()", globals=locals(), number=1))
    # amazon_lamps()
    github_python()
    

    