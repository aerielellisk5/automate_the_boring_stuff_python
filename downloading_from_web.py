import bs4, requests

def getAmazonPrice(productUrl):
    # res = requests.get(productUrl) --> Pretending to be a real browser by providing a User-Agent header would fix this particular issue: 
    # raise HTTPError(http_error_msg, response=self)
    # requests.exceptions.HTTPError: 503 Server Error: Service Unavailable for url:
    
    res = requests.get(productUrl, headers={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
})
    
    res.raise_for_status()
    # print(res.text)
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    print(soup.select('body > div.fabric-main-container.vs > main > div:nth-child(1) > div:nth-child(3) > div.sc-crHlIS.exYcBp.prism-layout-item-flex.prism-layout-item.sc-bDSnZ.fdOBjg > div > div:nth-child(1) > div.sc-crHlIS.exYcBp.prism-layout-item-flex.prism-layout-item.sc-QsvGH.fnApzZ > h2'))
    # print(soup.select('#corePrice_feature_div > div > span > span:nth-child(2) > span.a-price-whole'))
    # print(soup.select('a-price-whole'))
   
    #corePrice_feature_div > div > span > span.a-offscreen
    
    # print(elem)
    # return elem[0].text.strip()
    
   #corePrice_feature_div > div > span > span:nth-child(2) > span.a-price-whole
   
   
    


price = getAmazonPrice('https://www.victoriassecret.com/us/vs/bras-catalog/5000008267?brand=vs&collectionId=ffa700c2-fd93-4796-872d-ec589e693f3f&limit=12&priceType=regular&productId=df0d3fc1-ff7c-4349-a074-91bf387a5827&stackId=d8a03272-e4b1-4964-a2a1-0d7a8a4f9733&genericId=11206990&choice=1SJD')

# print('The price is ' + int(price)


