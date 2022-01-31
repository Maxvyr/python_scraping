from unittest import result
import requests
from bs4 import BeautifulSoup


URL  = "https://vizeo.eu/Cameras.html"
page = requests.get(URL)
resultProductPage = []

if page.status_code == 200:
        soup = BeautifulSoup(page.content, "html.parser")
        result = soup.find_all('a', href=True)
        hrefs = []
        for link in result:
            hrefs.append(link['href'])
        # print(hrefs)
        subString = "FicheProduit-"
        for refProd in hrefs:
            if subString in refProd:
                # print(refProd)
                resultProductPage.append(refProd)
        print(resultProductPage)
else:
    print(f"Page not found : {page.status_code}")