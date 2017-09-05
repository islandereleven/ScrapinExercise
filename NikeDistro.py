# I pull prices from the French nike running shoe selection and simply plot their distribution 

from lxml import html
import numpy as np
import matplotlib.pyplot as plt

import requests 

# get page and extract html/xml
page = requests.get('https://store.nike.com/fr/fr_fr/pw/homme-running-chaussures/7puZ8yzZoi3?ipp=81')
tree = html.fromstring(page.content)


#pull all prices 
prices = tree.xpath('//span[@class="local nsg-font-family--base"]/text()')
counter = 0 
#print prices
pricelist = []
for price in prices: 
	convertedprice = ''.join(c for c in price.encode('utf-8') if (c.isdigit() or c == ","))
	convertedprice = convertedprice.replace(",",".")
	pricelist.append(float(convertedprice))

print pricelist
plt.hist(pricelist, bins=range(0,300,20))
plt.show()
