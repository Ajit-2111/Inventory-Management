#THIS PROJECT IS MADE BY REFERING THE INVENTORY OF A COMPANY MAKING CLOTHES

import json

#THIS IS LOGIN WHERE WE CHECK IF THE USER IS ADMIN COZ ADMIN IS HAVING COMPLETE PREVILAGE
def authenticate():
    userName = input("Enter your user name : ")
    password = input("Enter your password : ")
    return ('trueadmin' if (userName =='admin' and password == 'admin123') else userName)

def welcome(user):
    print("Hello ",user)
    print("What do you want to do ?\n1. Display Record\n2. Buy Items\n3. Quit")
    userchoice = input("Enter the corresponding number  : ")
    if userchoice == '1':
        display()
    elif userchoice == '2':
        buying()
    elif userchoice == '3':
        quit()



#DISPLAY METHOD WILL TAKE THE VALUES AND THEN DISPLAY THEM
def display():
    if userIs != "trueadmin":
        productlist = []
        for i in data.values():
            if i['type'] == 'products':
                productlist.append(i)
        inputvalues = input("1. SHOW ALL \n2. Type\n3. Gender\n4. Item type\n5. Item\n6. Quantity\n7. Price\n8. Go Back\n9. Quit\nEnter the corresponding number(s) seperated using commas  :  ").replace(" ", "").split((","))
        truelist = []
        for i in inputvalues:
            truelist.append(i) if (i.isnumeric() and int(i) <= 9 and int(i) > 0) else None
            list(set(truelist)).sort() #    TO MAKE LIST UNIQUE AND SORTED
        quit() if '9' in truelist else welcome(userIs) if '8' in truelist else ''
        dispValLen = (input("Enter the Range (Press Enter to see full list) : ") or str(len(productlist)))
        if '1' in truelist:
            truelist=['2','3','4','5','6','7']
        print(' TYPE ' if ('2' in truelist) else '', 'GENDER' if ('3' in truelist) else '', 'ITEM TYPE' if ('4' in truelist) else '', ' ITEM ' if ('5' in truelist) else '', 'QUANTITY' if ('6' in truelist) else '', 'PRICE' if ('7' in truelist) else '')
        for i in range(0,int(dispValLen)):
            #check = f"{productlist[i]['type'] if ('2' in truelist) else '', productlist[i]['gender'] if ('3' in truelist) else '', productlist[i]['item_type'] if ('4' in truelist) else '', productlist[i]['item'] if ('5' in truelist) else '', productlist[i]['quantity'] if ('6' in truelist) else '', productlist[i]['price'] if ('7' in truelist) else ''}"
            print(productlist[i]['type'] if ('2' in truelist) else '', productlist[i]['gender'] if ('3' in truelist) else '', productlist[i]['item_type'] if ('4' in truelist) else '', productlist[i]['item'] if ('5' in truelist) else '', productlist[i]['quantity'] if ('6' in truelist) else '', productlist[i]['price'] if ('7' in truelist) else '')

    if userIs == "trueadmin":
        #1. EXPLAIN FROM HERE TO ....
        inputvalues = input("1. SHOW ALL \n2. Type\n3. Gender\n4. Item type\n5. Item\n6. Quantity\n7. Price\n8. Profit\n9. Max Quantity\n10. Go Back\n11. Quit\nEnter the corresponding number(s) seperated using commas  :  ").replace(" ", "").split((","))
        truelist = []
        for i in inputvalues:
            truelist.append(i) if (i.isnumeric() and int(i) <= 11 and int(i) > 0) else None
            list(set(truelist)).sort() #    TO MAKE LIST UNIQUE AND SORTED
        if '11' in inputvalues:
            quit()
        if '10' in inputvalues:
            welcome(userIs)
        if '1' in truelist:
            truelist=['2','3','4','5','6','7','8','9']
        #1. CONTINUE .... HERE THESE CODE WILL TACKLE INPUTS LIKE[(1   , 2 ,, 3),(2 5,55 4 ,),ETC] and number <= len(records.json)
        dispValLen = (input("Enter the Range (Press Enter to see full list) : ") or str(recordsLength))
        print('     TYPE   ' if ('2' in truelist) else '', 'GENDER' if ('3' in truelist) else '', 'ITEM TYPE' if ('4' in truelist) else '', ' ITEM ' if ('5' in truelist) else '', 'QUANTITY' if ('6' in truelist) else '', 'PRICE' if ('7' in truelist) else '', 'PROFIT' if ('8' in truelist) else '', 'MAX QUANTITY' if ('9' in truelist) else '')
        for i in range(1,int(dispValLen)+1):
            print(data[str(i)]['type'] if ('2' in truelist) else '', data[str(i)]['gender'] if ('3' in truelist) else '', data[str(i)]['item_type'] if ('4' in truelist) else '', data[str(i)]['item'] if ('5' in truelist) else '', data[str(i)]['quantity'] if ('6' in truelist) else '', data[str(i)]['price'] if ('7' in truelist) else '', data[str(i)]['profit'] if ('8' in truelist) else '', data[str(i)]['max_quantity'] if ('9' in truelist) else '')




def buying():
    productlist = []
    for i in data.values():
        if i['type'] == 'products':
            itemlist = [i['gender'],i["item"],i["price"],i["quantity"]]
            productlist.append(itemlist)
    for i in range(len(productlist)):
        print("No. : ",i+1,'  ','Gender : ',productlist[i][0],'  ','Item : ',productlist[i][1],"  ",'Price : ',productlist[i][2])
    print('Enter the corresponding numbers of items which you want to buy : ')
    cart=[]
    commit = ''
    while commit != 'y':
        additemtocart = int(input('Enter the item number : '))
        itemquantity = int(input('Enter the item quantyity : '))
        cart.append([additemtocart,itemquantity])
        buymore = input('Do you want to buy more products (y / n) : ')
        if buymore == 'y':
            continue
        commit = input('Do you want to buy these products (y / n) : ')
        print("CART : ",cart)
        bill(cart,productlist)


def bill(cart,prodlist):
    finalprice = []
    for i in range(len(cart)):
        cartithkey = cart[i][0]
        cartithvalue = cart[i][1]
        productprice = int(prodlist[cartithkey - 1][2])
        productquantity = int(prodlist[cartithkey - 1][3])
        print("productprice : ",productprice,"productquantity :",productquantity)
        if cartithvalue > productquantity:
            print('We have ',productquantity," ",prodlist[cartithkey - 1][1]," only.")
            quantityless = input('Do you want to buy them ? ( y / n) : ')
            if quantityless == 'y':
                cart[i][1]= productquantity
                prodlist[cartithkey - 1][3] = 0
                finalprice.append(productprice * productquantity)
                continue
            else:
                continue
        finalprice.append(productprice * cartithvalue)
        print("FINAL PRICE : ",finalprice)
    print('paid value = ',finalprice)



    print('\n\n---------  ',userIs,"'s  Bill  ---------\n")
    print(" Item   Quantity   Price")
    for i in range(len(cart)):
        print(prodlist[cart[i][0] - 1][1],"  ", cart[i][1],"  ",finalprice[i])
    print("\nTotal Price =  Rs. ",sum(finalprice))
    print('\n\n---------  Abc Clothings  ---------\n')











userIs = authenticate() #admin IF USER IS PASSING ADMIN'S USERNAME AND PASSWORD ELSE USERNAME

with open("records.json", "r") as f:
    data = json.load(f)
    recordsLength = len(data)

welcome(userIs)

