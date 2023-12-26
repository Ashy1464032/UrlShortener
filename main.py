# Imports
import requests

# Constants
API_KEY = ''
BASE_URL = 'https://cutt.ly/api/api.php'


# shorten link function
def shorten_link(link, name):
    # payload
    payload = {'key': API_KEY, 'short': link, 'name': name}
    request = requests.get(BASE_URL, params=payload)
    data = request.json()

    #exception handling
    try:
        title = data["url"]["title"]
        link = data["url"]["shortLink"]

        print("Title: ", title)
        print("Link: ", link)
    except:
        status = data['url']['status']
        print("Error status code: ", status)



# call function

url = input("Enter your url: ")
alias = input("Enter the url name: ")

shorten_link(url, alias)
