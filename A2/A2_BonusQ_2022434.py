# Saksham Singh
# 2022434
# Section B,  Group 7
# IP Assignment 02

#--------------BonusQ------------------
# Elwin Babu 2022182 
# Namit Bhadana 2022313 
# Saksham Singh 2022434

import requests
import webbrowser
def random():
    url="https://api.unsplash.com/photos/random?client_id=MVk7gR14Wd9u_9lKNC-lu_hzkVSKlitUKb8gZNVzoaY"
    resp=requests.get(url)
    data=resp.json()
    download=data["links"]["download"]
    webbrowser.open_new_tab(download)

def searchcoll():
    baseurl="https://api.unsplash.com/search/collections?query="
    query=input("Enter Query:")
    apikey="MVk7gR14Wd9u_9lKNC-lu_hzkVSKlitUKb8gZNVzoaY"
    count = "&per_page="+input("Enter no of search results: ")
    url=baseurl+query+"&client_id="+apikey+count
    resp=requests.get(url)
    data=resp.json()
    for i in data["results"]:
        webpage=(i["links"]["html"])
        webbrowser.open_new_tab(webpage)

def searching():
    api_url = "https://api.unsplash.com/search/photos?query="
    search_query = input("Enter what do you want to search for: ")
    count = "&per_page="+input("Enter no of search results: ")
    api_key = "&client_id=MVk7gR14Wd9u_9lKNC-lu_hzkVSKlitUKb8gZNVzoaY"
    orientation = "&orientation="+input("Enter orientation (landscape, portrait, squarish):" )
    resp = requests.get(api_url+search_query+count+orientation+api_key)
    data = resp.json()
    for i in data["results"]:
        webbrowser.open_new_tab((i["urls"]["raw"]))

while True:
    print("""        1.Search for an image
        2.Search for a premade collection of images
        3.Open a random image
        4.Exit""")
    n=int(input("Enter number corresponding to option:"))
    if n==1:
        searching()
    elif n==2:
        searchcoll()
    elif n==3:
        random()
    elif n==4:
        break

