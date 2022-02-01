from unittest import result
import requests
from bs4 import BeautifulSoup


URL_BASE  = "https://vizeo.eu/"
URL_CAM  = "Cameras.html"
page = requests.get(URL_BASE + URL_CAM)
result_product_per_page = []


def recover_all_producd():
    if page.status_code == 200:
            soup = BeautifulSoup(page.content, "html.parser")
            result = soup.find_all('a', href=True)
            hrefs = []
            for link in result:
                hrefs.append(link['href'])
            # print(hrefs)
            sub_string = "FicheProduit-"
            for ref_page_prod in hrefs:
                if sub_string in ref_page_prod:
                    result_product_per_page.append(ref_page_prod)
    else:
        print(f"Page not found : {page.status_code}")

def change_page():
    for page_cam in result_product_per_page:
        page = requests.get(URL_BASE + page_cam)
        soup = BeautifulSoup(page.content, "html.parser")
        scrap_data(soup)
        

def scrap_data(soup):
    title = soup.title.text
    price = soup.select_one('span[class*=prod-fiche-refonte-code]').text
    desc = soup.find_all('div', class_='prod_fiche_designation pt-5')
    # desc = soup.select_one('div[class*=prod_fiche_designation pt-5]').text
    img = soup.select_one('.img-fluid')
    img_link = img['src']
    # img = soup.find_all('img', class_='img-fluid')
    print(title)   
    print(price)   
    print(desc)   
    print(img_link)   
    print("------")   

print("go")
recover_all_producd()
print("next")
change_page()
print("end")

