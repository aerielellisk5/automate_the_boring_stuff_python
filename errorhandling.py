

# def boxPrint(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception('"symbol" needs to a string of length 1.')
#     if (width < 2) or (height < 2):
#         raise Exception('"widht or height is less than 2"')
#     print(symbol * width)
    
#     for i in range(height -2):
#         print(symbol + (' ' * (width - 2)) + symbol)
        
#     print(symbol * width)
    
# # boxPrint('*', 15, 5)
# # boxPrint('O', 5, 16)
    
# boxPrint('O', 1, 16)    

market_2nd = {'ns' : 'green', 'ew' : 'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red'
print(market_2nd)            
switchLights(market_2nd)
print(market_2nd)  