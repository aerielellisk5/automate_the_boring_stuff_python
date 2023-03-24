import bs4, requests

def getAmazonPrice(productUrl):
    # res = requests.get(productUrl) --> Pretending to be a real browser by providing a User-Agent header would fix this particular issue: 
    # raise HTTPError(http_error_msg, response=self)
    # requests.exceptions.HTTPError: 503 Server Error: Service Unavailable for url:
    
    res = requests.get(productUrl, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
})
    
    res.raise_for_status()
    print(res.text)
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    print(soup.select('#corePrice_feature_div > div > div > span > span:nth-child(2) > span.a-price-whole'))
    # print(soup.select('#corePrice_feature_div > div > span > span:nth-child(2) > span.a-price-whole'))
    # print(soup.select('a-price-whole'))
   
    #corePrice_feature_div > div > span > span.a-offscreen
    
    # print(elem)
    # return elem[0].text.strip()
    
   #corePrice_feature_div > div > span > span:nth-child(2) > span.a-price-whole
    


price = getAmazonPrice('https://www.amazon.com/AmazonBasics-Mattress-Foundation-Tool-Free-Assembly/dp/B082T8QCZS?ref_=ast_sto_dp&th=1&psc=1')

# print('The price is ' + int(price)


