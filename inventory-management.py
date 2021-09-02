# THERE WILL BW 3 FILES 1 JUPYTER NOTEBOOK 1 RECORDS.JSON 1 SALES.JSON
# 1. RECORDS.JSON WILL HAVE THE ITEMS RECORD. THE ADMIN WILL CHANGE THE ITEMS ID AND ITS ATTRIBUTES,ETC
# 2. SALES.JSON THIS FILL WILL HAVE THE DETAILS OF THE PURCHASES LIKE NUMBER OF ITEMS PURCHASED ITEMS REMAINING,ETC
# 3. JUPYTER NOTEBOOK WILL CONTAIN THE CODE TO MANIPULATE THE SALES.JSON AND RECORDS.JSON FILES AND ALSO THEY WILL HAVE THE PREVILAGE PERFORM CRUD OPERATION ON THE RECORD.JSON DATA
# **********THE MORE FUNCTIONALITY YOU HAVE THE MORE POINTS YOU GET**********

# STEPS TO COMPLETE THE PROJECT
# 1. CREATE RECORD.JSON FILE WHICH WILL HAVE ALL THE PRE LOADED 30 RECORDS.
# 2. OPEN THIS FILE IN JUPYTER NTBK(CODE) SO THAT THE USER CAN PERFORM CRUD OPERATIONS.
# 3. WRITE SOME FUNCTIONALITIES
# 4. ASK THE USER IF THEY WISH TO SAVE THE CHANGES TO RECORDS.JSON FILE.
# 5. IF YES THEN CHANGE THE RECORDS.JSON FILE AND ALSO SALES.JSON FILES TO COMMIT THE CHANGES. IF NOT THEN MAKE NO CHANGES IN THE RECORDS.JSON AND SALES.JSON FILES.


#THIS PROJECT IS MADE BY REFERING THE INVENTORY OF A COMPANY MAKING CLOTHES

import json
recordsLength = 0
data = None
with open("records.json") as f:
    data = json.load(f)
    recordsLength = len(data)




#THIS IS LOGIN WHERE WE CHECK IF THE USER IS ADMIN COZ ADMIN IS HAVING COMPLETE PREVILAGE


def authenticate():
    userName = input("Enter your user name : ")
    password = input("Enter your password : ")
    return "admin" if (userName == "admin" and password == "admin123") else userName

# userIs = authenticate() #admin IF USER IS PASSING ADMIN'S USERNAME AND PASSWORD ELSE USERNAME
# print(userIs)

#DISPLAY METHOD WILL TAKE THE VALUES AND THEN DISPLAY THEM
def display():
    #1. EXPLAIN FROM HERE TO ....
    inputvalues = "1   , 2 ,, 3 ,, 25,".replace(" ","").split((",")) #input("1. Type\n2. Gender\n3. Item type\n4. Item\n5. Quantity\n6. Price\n7. Profit\n8. Max Quantity\nEnter the corresponding number(s) seperated using commas  :  ").replace(" ","").split((","))
    truelist = []
    print(inputvalues)
    for i in inputvalues:
        truelist.append(i) if (i.isnumeric() and int(i) <= 8 and int(i) > 0) else None
    print(truelist)
    #1. CONTINUE .... HERE THESE CODE WILL TACKLE INPUTS LIKE[(1   , 2 ,, 3),(2 5,55 4 ,),ETC] and number <= len(records.json)
    print(recordsLength)
    dispValLen = (input("Enter the Range : ") or str(recordsLength))
    mapValues = {"1":"type","2":"gender","3":"item_type","4":"item","5": "quantity","6":"price","7":"profit","8": "max_quantity"}
    getDictVal = ""
    for i in truelist:
        stri = "data['i']"
        stri += "['" + "{value}".format(value = mapValues[i]) + "']"
        getDictVal += stri + ","
    print(getDictVal)
    for i in range(1,int(dispValLen)+1):
        pass









display()







