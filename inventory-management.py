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
    #1. EXPLAIN FROM HERE TO ....
    display = "1. Type\n2. Gender\n3. Item type\n4. Item\n5. Quantity\n6. Price\n" + f"{'7. Profit' if userIs == 'trueadmin' else ''}" + "\n" + f"{'8. Max Quantity' if userIs == 'trueadmin' else ''}" + "\n9. Go Back\n10. Quit"
    inputvalues = input("{display} \nEnter the corresponding number(s) seperated using commas  :  ".format(display=display)).replace(" ", "").split((","))
    truelist = []
    print(inputvalues)
    for i in inputvalues:
        truelist.append(i) if (i.isnumeric() and int(i) <= 8 and int(i) > 0) else None
        list(set(truelist)).sort() #    TO MAKE LIST UNIQUE AND SORTED
        if userIs != "trueadmin":
            truelist.remove('7') if '7' in truelist else ""
            truelist.remove('8') if '8' in truelist else ""
    print(truelist)
    if '10' in inputvalues:
        quit()
    if '9' in inputvalues:
        welcome(userIs)

    #1. CONTINUE .... HERE THESE CODE WILL TACKLE INPUTS LIKE[(1   , 2 ,, 3),(2 5,55 4 ,),ETC] and number <= len(records.json)
    print(recordsLength)
    dispValLen = (input("Enter the Range (Press Enter to see full list) : ") or str(recordsLength))
    print(f"{'     TYPE   ' if ('1' in truelist) else '', 'GENDER' if ('2' in truelist) else '', 'ITEM TYPE' if ('3' in truelist) else '', ' ITEM ' if ('4' in truelist) else '', 'QUANTITY' if ('5' in truelist) else '', 'PRICE' if ('6' in truelist) else '', 'PROFIT' if ('7' in truelist) else '', 'MAX QUANTITY' if ('8' in truelist) else ''}")
    for i in range(1,int(dispValLen)+1):
        check = f"{data[str(i)]['type'] if ('1' in truelist) else '', data[str(i)]['gender'] if ('2' in truelist) else '', data[str(i)]['item_type'] if ('3' in truelist) else '', data[str(i)]['item'] if ('4' in truelist) else '', data[str(i)]['quantity'] if ('5' in truelist) else '', data[str(i)]['price'] if ('6' in truelist) else '', data[str(i)]['profit'] if ('7' in truelist) else '', data[str(i)]['max_quantity'] if ('8' in truelist) else ''}"
        print(check)






def buying():
    pass










userIs = authenticate() #admin IF USER IS PASSING ADMIN'S USERNAME AND PASSWORD ELSE USERNAME

with open("records.json") as f:
    data = json.load(f)
    recordsLength = len(data)

welcome(userIs)

