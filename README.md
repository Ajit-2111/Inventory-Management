# Inventory-Management

This repo contains the assignments and project files for the ETG Internship ( Python ).This project will help in managing the inventory. There are two types of user in this project i.e the **ADMIN** and **NORMAL USER**. Both of them are given different previleges.

## FILES
The files required to run the code in your machines are :

**1. Inventory Management.py file :** This file has all the python code.

**2. records.json file :** This file containe some dummy record. Tde data stored in this json files are stored in the form:

{"1": {"type": "raw_materials", "gender": "null", "item_type": "thread", "item": "cotton_thread", "quantity": "959", "price": "150", "profit": "15", "max_quantity": "500"}}

This is an example of which type of data and how the data is stored in the records.json file.

**2. sales.json file :** This file contains the sales details in json format.

{"1": {"time": "06-Sep-2021-Mon-17:11:40", "buyer": "genesis", "order": {"jeans": 2, "track_pants": 2, "denim_shirt": 1, "t_shirt": 2}, "paid": 3653, "tax": "12%"}}

This is an example of which data and how the data is stored in this sales.json file.


## Features for Admin (For Admin Previlages use username = admin and password = admin123)
1. Display Record
2. Buy Items
3. Delete Records
4. Update Records
5. Add to Records
6. Display Sales
7. Quit

## Features for Normal User (All non admin user are Normal User)
1. Display Record
2. Buy Items
3. Quit

**NOTE : OPTION 1,2 ARE ALMOST SAME FOR BOTH TYPES OF USER**

## 1. Display Records

Here the user can see all the records. When user selects this function they will see different options to see different types of records. The user is given the option of :
1. SHOW ALL 
2. Type
3. Gender
4. Item type
5. Item
6. Quantity
7. Price
8. Profit
9. Max Quantity
10. Go Back
11. Quit



