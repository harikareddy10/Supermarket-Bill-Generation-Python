print("-----------------Welcome to Harika Supermarket-------------------")
name = input("Enter your name: ")
list = int(input("For list of items press 1: "))
s = '''
Rice        20/kg
Sugar       35/kg
Wheat floor 20/kg
oil         80/kg
Paneer      200/kg
Maggi       5/pck
colgate     89/1pc
ice cream   150/pck
'''

qlist = []
plist = []

d = {"rice": 20,"sugar":35,"wheat floor":20,"oil":80,"paneer":200,"maggi":5,"colgate":89,"ice cream":150}
amount = 0
if list == 1:
    print(s)
    for i in range(len(d)):
        purchase = []
        buy = int(input("If you wanna buy something,Press 1/Wanna exit, press 2: "))
        if buy ==2:
            print("Thank you {}! Visit Again".format(name))
            break
        elif buy==1:
            item = input("Enter the item: ").lower()
            if item in d.keys():
                quantity = int(input("Enter the Quantity: "))
                bill = input("Can I bill the items?yes or no: ").lower()
                if bill == "yes":
                   amount = float(amount+ (d.get(item)*quantity))
                   purchase.append(item)
                   qlist.append(quantity)
                   plist.append(amount)
                   gst = 19.00
                   total_price = gst+amount
                   print(25*"*","Harika Supermarket",25*"*")
                   print(25*" ","  Muddireddy")
                   print("Name:",name)
                   print(50*"--")
                   print("s.no",8*" ","items",8*" ","quantity",8*" ","price of item",8*" ","Tax",8*" ","Payable Amount")
                   if total_price!=0:
                       for i in range(len(purchase)):
                           print(i+1,12*" ",purchase[i],12*" ",qlist[i],15*" ",plist[i],15*" ",gst,10*" ",total_price)
                           print(50*"--")
            else:
                print("Sorry!, The entered item is out of stock.")
        else:
            print("Please enter correct input")
        
            
                    
        
            
                   
                    
                    
                
                
                