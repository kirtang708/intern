
class category:
    def __init__(self,name,code,no_of_code):
        self.name = name
        self.code = code
        self.no_of_products = no_of_code


a=category("baby_shampoo","t1t1",77)
b=category("baby_powder","t2t2",108)
c=category("baby_cream","t3t3",69)

print(a.name,a.code,a.no_of_products)
print(b.name,b.code,b.no_of_products)
print(c.name,c.code,c.no_of_products)
            
class product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price
        
    def __repr__(self):
        return'({},{},{},{})'.format(self.name,self.code,self.category,self.price)
        
        
product_1=product("blushers",'k11','cosmetic_1',100)
product_2=product("face_powder",'k22','cosmetic_2',120)
product_3=product("foundation",'k33','cosmetic_3',125)
product_4=product("lipstick",'k44','cosmetic_4',130)
product_5=product("makeup_bases",'k55','cosmetic_5',80)
product_6=product("lotion",'k66','cosmetic_6',130)
product_7=product("moisturizer",'k77','cosmetic_7',90)
product_8=product("cream",'k88','cosmetic_8',80)
product_9=product("shampoo",'k99','cosmetic_9',50)
product_10=product("hair_oil",'k110','cosmetic_10',40)

list = [product_1, product_2, product_3, product_4, product_5, 
        product_6, product_7, product_8, product_9, product_10]


def sortlist_price(p):
    return p.price

sorted_products_price= sorted(list, key= sortlist_price)
sorted_products_price_= sorted(list, key= sortlist_price, reverse=True)
#print(list)
 

print("Object sorted by price(low to high):\n", sorted_products_price)

print("Object sorted by price(high to low):", sorted_products_price_)








    
  
  
  
  
  
  
  
   


  
