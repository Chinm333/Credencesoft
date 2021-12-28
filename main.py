from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.chewy.com/b/dog-288")

ans = response.text
soup = BeautifulSoup(ans, "lxmi")
category = soup.find(name="a", class_="subcat")
category_text = category.getText()
# # print(category_text)
#
# # response = requests.get(url="https://www.chewy.com/b/wet-food-293")
wet_food = soup.find(name="a", class_="facet_selection")
we_text = wet_food.getText()
# # print(we_text)

response = requests.get(url="https://www.chewy.com/pedigree-adult-complete-nutrition/dp/141438")
ans = response.text
soup = BeautifulSoup(ans, "html.parser")
title = soup.find(name="h1")
title_text = title.getText()
print(title_text)

descrip = soup.find(name="div", class_="descriptions__content cw-tabs__content--left")
des_text = descrip.getText()
print(des_text)

size = soup.find(name="div", class_="attribute-selection")
size_text = size.getText()

ingrediant = soup.find(name="id", class_="cw-table__cell")
ingrediant_text = ingrediant.getText()

bene = soup.find(name="div", class_="cw-type__h2")
bene_text = bene.getText()

brand = soup.find(name="h2",class_="pdp-ext-content")
brand_text = brand.getText()

price = soup.find(name="span", class_="ga-eec__price")
price_text = price.getText()

