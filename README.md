# Inventory-Management

This repo contains the assignments and project files for the ETG Internship ( Python ).This project will help in managing the inventory. There are two types of user in this project i.e the **ADMIN** and **NORMAL USER**. Both of them are given different previleges.

## FILES
The files required to run the code in your machines are :

**1. Inventory Management.py file :** This file has all the python code.

**2. records.json file :** This file containe some dummy record. Tde data stored in this json files are stored in the form:

{"1": {"type": "raw_materials", "gender": "null", "item_type": "thread", "item": "cotton_thread", "quantity": "959", "price": "150", "profit": "15", "max_quantity": "500"}}

This is an example of which type of data and how the data is stored in the records.json file.

**3. sales.json file :** This file contains the sales details in json format.

{"1": {"time": "06-Sep-2021-Mon-17:11:40", "buyer": "genesis", "order": {"jeans": 2, "track_pants": 2, "denim_shirt": 1, "t_shirt": 2}, "paid": 3653, "tax": "12%"}}

This is an example of which data and how the data is stored in this sales.json file.


At first the program will ask for username and password you can type anything but For Admin Previlages use username = admin and password = admin123.

## Features for Admin 
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

**SHOW ALL  :** If the user selects this option then the output will display all the details.

If the user select other option they will see only that data. **Don't understand what does this mean ?** See the following images to understand more.

![display 1 1](https://user-images.githubusercontent.com/77968856/132240104-af9852df-0da9-46c3-af16-6666c206b463.jpg)
![display 1 2](https://user-images.githubusercontent.com/77968856/132240251-e4ac3fb0-b6b7-4285-b031-996e92b68024.jpg)

In the the first image i have only entered 2 as input and the program only displayed me the Type of the products.

In the second image I have entered the numbers 2,3,5 this showed me the recods of the product type the gender for which the product is manufactured and teh product name. You can select multiple options by seperating each of them with ' , '(comma).


## 2. Buy Items

When the user selects the option to buy items the are shown all the products that are available ( product number, displays only gender, item and price ). After that the user needs to enter the product number and the the quantity. If you want to shop more then dont worry there is an option " Do you want to buy more ? " you must answer it either "y" or "n". For those user who type "y" the will again the product number and the quantity. This will go on until the user enters "n" for buying more option. After that the program will ask " Do you want to buy these products (y / n) " if you enter "y" then your bill will be prepared, if you enter "n" then you will be taken back to welcome function. If the user enters the products more than it is present in the records the will be given an option to buy all the remaining products.

![bill](https://user-images.githubusercontent.com/77968856/132242912-6223e900-5501-4b54-a46e-ca7930949a37.jpg)

This is the bill, here user with username Genesis will get this bill.

## 3. Delete Records

When the Admin selects this option then he will be provided with whole record and then the user has to enter the record number to delete it. Type "DELETEALL" to delete all record.

## 4. Update Records

Adin will see all the record and then he will be asked to enter the record number to edit and then type the attribute to edit with the new value. If the admin wants to edit more records then they have to enter "y" for edit more question.
![update](https://user-images.githubusercontent.com/77968856/132244069-fa4e19a8-8fb1-44cc-aa93-859f867aef36.jpg)
 

## 5. Add to Records
![add record](https://user-images.githubusercontent.com/77968856/132244480-2b16de21-76d1-4681-9dd9-2b5724dcdeb6.jpg)

The admin has to provide all these details to create a new record element. The attribute which will be left blank will get the null value in the record.

## 6. Display Sales

![sales](https://user-images.githubusercontent.com/77968856/132244887-21c61212-e83b-4838-8993-7310923a50da.jpg)

Admin can see the details for months, years , price ,all. For months, years , price option they must provide start and end of the range to display the sales.


If you face any problem you can contact me on :
Gmail Account : ajitcc07@gmail.com

Linkedin : www.linkedin.com/in/ajitchoudhary

















