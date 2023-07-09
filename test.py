#visa management system

import mysql.connector
from mysql.connector import Error
import csv


while True:
    print("")
    print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t WELCOME TO HALEEB")
    print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t            MAIN MENU              ")
    print("")
    print("\t1)ADMIN LOGIN")
    print("\t2)CUSTOMER LOGIN")
    print("\t3)DELIVERY LOGIN")
    print("\t4)SUPPLIER LOGIN")
    print("\t5)NEW CUSTOMER")
    print("\t6)Exit")
    print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    ch=int(input("enter choice = :"))
    if ch==1:
        while True:
            print("")
            print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\t ADMIN LOGIN")
            print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            username=input("Enter admin username :")
            try :
                connection = mysql.connector.connect(host='localhost',
                                             database='haleeb',
                                             user='root',
                                             password='root')
                cursor = connection.cursor()
                st=("SELECT EXISTS(SELECT * from admin WHERE username = '%s')")%username
                cursor.execute(st)
                data=cursor.fetchall()
                for row in data:
                    if row[0] == 1:
                        password = input("Enter password : ")
                        st2 = ("SELECT password from admin WHERE username = '%s'")%username
                        cursor.execute(st2)
                        data=cursor.fetchall()
                        for row in data:
                            if row[0] == password :
                                print("Welcome admin!!")
                                id_query = ("SELECT admin_id from admin WHERE username = '%s'")%username
                                cursor.execute(id_query)
                                aid_list = cursor.fetchall()
                                aid = aid_list[0][0]
                                while True:
                                    print("")
                                    print("\t~~~~~~~~~~~~~")
                                    print("\t ADMIN")
                                    print("\t~~~~~~~~~~~~~")
                                    print("\t1) Add Product")
                                    print("\t2) Add Category")
                                    print("\t3) View Categories")
                                    print("\t4) View Suppliers")
                                    print("\t5) Add Supplier")
                                    print("\t6) Update Supplier")
                                    print("\t7) Delete Supplier")
                                    print("\t8) View Distributors")
                                    print("\t9) Add Distributor")
                                    print("\t10) Update Distributor")
                                    print("\t11) Delete Distributor")
                                    print("\t12) View Branch Stock")
                                    print("\t13) View Sales")
                                    print("\t14) View Orders")
                                    print("\t15) Restock request")
                                    print("\t16) Return to MAIN MENU")
                                    print("~~~~~~~~~~~~~")
                                    ch = int(input("Enter choice = :"))
                                    if ch == 1:
                                        connection = mysql.connector.connect(host='localhost',
                                                                        database='haleeb',
                                                                        user='root',
                                                                        password='root')
                                        cursor = connection.cursor()
                                        p_catno = int(input("Enter category_no : "))
                                        p_name = input("Enter product name : ")
                                        p_desc = input("Enter product description : ")
                                        p_price = int(input("Enter product price : "))
                                        query = "select exists (select * from category where category_id = '%s');"%(p_catno)
                                        cursor.execute(query)
                                        data2 = cursor.fetchall()
                                        for row in data2:
                                            if row[0] == 0:
                                                query = "insert into products values (%s,%s,%s,%s);"
                                                record_tuple = (p_catno, p_name, p_desc, p_price)
                                                cursor.execute(query, record_tuple)
                                                connection.commit()
                                            else:
                                                print("This category_no doesn't exist.")
                                    elif ch == 2:
                                        connection = mysql.connector.connect(host='localhost',
                                                                        database='haleeb',
                                                                        user='root',
                                                                        password='root')
                                        cursor = connection.cursor()
                                        c_name = input("Enter category name : ")
                                        c_desc = input("Enter category description : ")
                                        query = "insert into category values (%s,%s);"
                                        record_tuple = (c_name, c_desc)
                                        cursor.execute(query, record_tuple)
                                        connection.commit()
                                    elif ch == 3:
                                        connection = mysql.connector.connect(host='localhost',
                                                                        database='haleeb',
                                                                        user='root',
                                                                        password='root')
                                        cursor = connection.cursor()
                                        query = "SELECT * FROM category;"
                                        cursor.execute(query)
                                        data = cursor.fetchall()
                                        print("Categories:")
                                        print("ID | Name | Description")
                                        for row in data:
                                            print(row)

                                    elif ch == 4:
                                        connection = mysql.connector.connect(host='localhost',
                                                                        database='haleeb',
                                                                        user='root',
                                                                        password='root')
                                        cursor = connection.cursor()
                                        query = "SELECT * FROM supplier;"
                                        cursor.execute(query)
                                        data = cursor.fetchall()
                                        print("Suppliers:")
                                        print("ID | Name | Phone | Address | Email | Branch No")
                                        for row in data:
                                            print(row)

                                    elif ch == 5:
                                        connection = mysql.connector.connect(host='localhost',
                                                                        database='haleeb',
                                                                        user='root',
                                                                        password='root')
                                        cursor = connection.cursor()
                                        name = input("Enter supplier name: ")
                                        ph_no = input("Enter supplier phone number: ")
                                        address = input("Enter supplier address: ")
                                        email = input("Enter supplier email: ")
                                        b_no = int(input("Enter branch number: "))

                                        mySql_insert_query = """INSERT INTO supplier (name, ph_no, address, email, b_no) 
                                                                VALUES (%s, %s, %s, %s, %s)"""
                                        recordTuple = (name, ph_no, address, email, b_no)
                                        cursor.execute(mySql_insert_query, recordTuple)
                                        connection.commit()
                                        print(cursor.rowcount, "Record inserted successfully into supplier table")

                                    elif ch == 6:
                                        connection = mysql.connector.connect(host='localhost',
                                                                        database='haleeb',
                                                                        user='root',
                                                                        password='root')
                                        cursor = connection.cursor()
                                        supplier_id = int(input("Enter supplier ID to update: "))
                                        new_name = input("Enter new supplier name: ")
                                        new_ph_no = input("Enter new supplier phone number: ")
                                        new_address = input("Enter new supplier address: ")
                                        new_email = input("Enter new supplier email: ")
                                        new_b_no = int(input("Enter new branch number: "))

                                        mySql_update_query = """UPDATE supplier SET name=%s, ph_no=%s, address=%s, email=%s, b_no=%s WHERE supplier_id=%s"""
                                        recordTuple = (new_name, new_ph_no, new_address, new_email, new_b_no, supplier_id)
                                        cursor.execute(mySql_update_query, recordTuple)
                                        connection.commit()
                                        print(cursor.rowcount, "Record updated successfully into supplier table")
                                        connection.commit()
                                        print(cursor.rowcount, "Record updated successfully in supplier table")

                                    elif ch == 7:
                                        connection = mysql.connector.connect(host='localhost',
                                                                        database='haleeb',
                                                                        user='root',
                                                                        password='root')
                                        cursor = connection.cursor()
                                        supplier_id = int(input("Enter supplier ID to delete: "))

                                        mySql_delete_query = """DELETE FROM supplier WHERE supplier_id=%s"""
                                        recordTuple = (supplier_id,)
                                        cursor.execute(mySql_delete_query, recordTuple)
                                        connection.commit()
                                        print(cursor.rowcount, "Record deleted successfully from supplier table")

                                    elif ch == 8:
                                        connection = mysql.connector.connect(host='localhost',
                                                                        database='haleeb',
                                                                        user='root',
                                                                        password='root')
                                        cursor = connection.cursor()
                                        query = "SELECT * FROM distributor;"
                                        cursor.execute(query)
                                        data = cursor.fetchall()
                                        print("Distributors:")
                                        print("ID | Name | Phone | Branch No")
                                        for row in data:
                                            print(row)

                                    elif ch == 9:
                                        connection = mysql.connector.connect(host='localhost',
                                                                        database='haleeb',
                                                                        user='root',
                                                                        password='root')
                                        cursor = connection.cursor()
                                        name = input("Enter distributor name: ")
                                        ph_no = input("Enter distributor phone number: ")
                                        branch_no = int(input("Enter branch number: "))

                                        mySql_insert_query = """INSERT INTO distributor (name, ph_no, branch_no) 
                                                                VALUES (%s, %s, %s)"""
                                        recordTuple = (name, ph_no, branch_no)
                                        cursor.execute(mySql_insert_query, recordTuple)
                                        connection.commit()
                                        print(cursor.rowcount, "Record inserted successfully into distributor table")

                                    elif ch == 10:
                                        connection = mysql.connector.connect(host='localhost',
                                                                        database='haleeb',
                                                                        user='root',
                                                                        password='root')
                                        cursor = connection.cursor()
                                        distributor_id = int(input("Enter distributor ID to update: "))
                                        new_name = input("Enter new distributor name: ")
                                        new_ph_no = input("Enter new distributor phone number: ")
                                        new_branch_no = int(input("Enter new branch number: "))

                                        mySql_update_query = """UPDATE distributor SET name=%s, ph_no=%s, branch_no=%s WHERE distributor_id=%s"""
                                        recordTuple = (new_name, new_ph_no, new_branch_no, distributor_id)
                                        cursor.execute(mySql_update_query, recordTuple)
                                        connection.commit()
                                        print(cursor.rowcount, "Record updated successfully in distributor table")

                                    elif ch == 11:
                                        connection = mysql.connector.connect(host='localhost',
                                                                        database='haleeb',
                                                                        user='root',
                                                                        password='root')
                                        cursor = connection.cursor()
                                        distributor_id = int(input("Enter distributor ID to delete: "))

                                        mySql_delete_query = """DELETE FROM distributor WHERE distributor_id=%s"""
                                        recordTuple = (distributor_id,)
                                        cursor.execute(mySql_delete_query, recordTuple)
                                        connection.commit()
                                        print(cursor.rowcount, "Record deleted successfully from distributor table")

                                    elif ch == 12:
                                        connection = mysql.connector.connect(host='localhost',
                                                database='haleeb',
                                                user='root',
                                                password='root')
                                        cursor = connection.cursor()
                                        print("Branch_id | stock")
                                        qu = ("""SELECT product_id, stock
                                                FROM location_inventory
                                                where loc_id = '%s';""")%aid
                                        cursor.execute(qu)
                                        data2=cursor.fetchall()
                                        print("product_id | stock")
                                        for row2 in data2:
                                            print(row2)
                                    elif ch == 13:
                                        connection = mysql.connector.connect(host='localhost',
                                                database='haleeb',
                                                user='root',
                                                password='root')
                                        cursor = connection.cursor()
                                        qu = ("""select sum(amount)
                                                from payment, orders
                                                where payment.payment_id = orders.payment_id and orders.branch_id = '%s';""")%aid
                                        cursor.execute(qu)
                                        data2=cursor.fetchall()
                                        print("Total sales of this branch is : ")
                                        for row2 in data2:
                                            print(row2[0])
                                    elif ch == 14:
                                        connection = mysql.connector.connect(host='localhost',
                                                database='haleeb',
                                                user='root',
                                                password='root')
                                        cursor = connection.cursor()
                                        print("order_id | date_of_order | status | branch_id | payment_id | cust_id")
                                        qu = ("""SELECT * from orders where branch_id = '%s';""")%aid
                                        cursor.execute(qu)
                                        data2=cursor.fetchall()
                                        for row2 in data2:
                                            print(row2)
                                    elif ch == 15:
                                        try:
                                            connection = mysql.connector.connect(host='localhost',
                                                                        database='haleeb',
                                                                        user='root',
                                                                        password='root')
                                            cursor = connection.cursor()
                                            product_id = int(input("Enter product_id to restock : "))
                                            quantity = int(input("Enter quantity: "))
                                            insert_query = ("INSERT INTO restock_request (product_id, supplier_id, quantity, b_no) VALUES (%s, %s, %s, %s)")
                                            insert_data = (product_id, aid, quantity, aid)
                                            cursor.execute(insert_query, insert_data)
                                            connection.commit()
                                            print("Restock request created.")
                                        except Error as e:
                                            print("Error while connecting to MySQL", e)
                                        finally:
                                            if (connection.is_connected()):
                                                cursor.close()
                                                connection.close()
                                                print("MySQL connection is closed")
                                    elif ch == 16:
                                        break
                                    
                            else :
                                print("Password you entered is incorrect.")
                    else :
                        print("Username doesn't exist")
                break
            except:
                print("error")
            break
    elif ch==2:
        while True:
            print("")
            print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\t CUSTOMER LOGIN")
            print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            username=input("Enter customer username :")
            try :
                connection = mysql.connector.connect(host='localhost',
                                             database='haleeb',
                                             user='root',
                                             password='root')
                cursor = connection.cursor()
                st=("SELECT EXISTS(SELECT * from customer WHERE username = '%s')")%username
                cursor.execute(st)
                data=cursor.fetchall()
                for row in data:
                    if row[0] == 1:
                        password = input("Enter password : ")
                        st2 = ("SELECT password from customer WHERE username = '%s'")%username
                        cursor.execute(st2)
                        data=cursor.fetchall()
                        for row in data:
                            if row[0] == password :
                                print("Welcome customer!!")
                                id_query = ("SELECT customer_id from customer WHERE username = '%s'")%username
                                cursor.execute(id_query)
                                cid_list=cursor.fetchall()
                                cid = cid_list[0][0]
                                while True:
                                    print("")
                                    print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\t CUSTOMER")
                                    print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("\t1)Browse Products")
                                    print("\t2)Add item to cart")
                                    print("\t3)View cart")
                                    print("\t4)Checkout Cart")
                                    print("\t5)Update quantity/Remove items in cart")
                                    print("\t6)Cancel order")
                                    print("\t7)View previous orders")
                                    print("\t8)Return to MAIN MENU")
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    ch=int(input("enter choice = :"))
                                    if ch == 1:
                                        while True:
                                            print("")
                                            print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\t CUSTOMER")
                                            print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\t1)See best selling item")
                                            print("\t2)Browse category wise")
                                            print("\t3)See catalogue")
                                            print("\t4)Return")
                                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            ch2=int(input("enter choice = :"))
                                            if ch2 == 1:
                                                connection = mysql.connector.connect(host='localhost',
                                                 database='haleeb',
                                                 user='root',
                                                 password='root')
                                                cursor = connection.cursor()
                                                qu = ("""select * 
                                                    from products, (select product_id
                                                    from location_inventory
                                                    where loc_id = '%s'
                                                    order by stock asc
                                                    limit 3) as table2
                                                    where products.product_id = table2.product_id;""")%cid
                                                cursor.execute(qu)
                                                data2=cursor.fetchall()
                                                for row2 in data2:
                                                    print(row2)
                                            elif ch2 == 2:
                                                connection = mysql.connector.connect(host='localhost',
                                                 database='haleeb',
                                                 user='root',
                                                 password='root')
                                                cursor = connection.cursor()
                                                qu = ("""select * from category;""")
                                                cursor.execute(qu)
                                                data2=cursor.fetchall()
                                                for row2 in data2:
                                                    print(row2)
                                                cat_id = int(input("Enter category ID to browse: "))
                                                st=("select exists (select * from category where category_id = '%s');")%cat_id
                                                cursor.execute(st)
                                                data=cursor.fetchall()
                                                print("product_id category_no name description price")
                                                for row in data:
                                                    if row[0] == 1:
                                                        qu = ("""select * from products where category_no = '%s';""")%cat_id
                                                        cursor.execute(qu)
                                                        data2=cursor.fetchall()
                                                        for row2 in data2:
                                                            print(row2)
                                                    else:
                                                        print("Invalid category ID")
                                                        break
                                            elif ch2 == 3:
                                                connection = mysql.connector.connect(host='localhost',
                                                 database='haleeb',
                                                 user='root',
                                                 password='root')
                                                cursor = connection.cursor()
                                                qu = ("""SELECT products.product_id, products.name, price
                                                    FROM products
                                                    JOIN category ON products.category_no = category.category_id order by products.product_id asc;""")
                                                cursor.execute(qu)
                                                data2=cursor.fetchall()
                                                for row2 in data2:
                                                    print(row2)
                                            elif ch2 == 4:
                                                break
                                    elif ch == 2:
                                        connection = mysql.connector.connect(host='localhost',
                                             database='haleeb',
                                             user='root',
                                             password='root')
                                        cursor = connection.cursor()
                                        pid = int(input("Enter product id : "))
                                        quantity = int(input("Enter quantity : "))
                                        mySql_insert_query = """INSERT INTO cart_items(cust_id, product_id, quantity)
                                                      VALUES (%s ,%s ,%s) """
                                        recordTuple=(cid, pid, quantity)
                                        cursor.execute(mySql_insert_query,recordTuple)
                                        connection.commit()
                                        print(cursor.rowcount, "Record inserted successfully into products table")
                                    elif ch == 3:
                                        connection = mysql.connector.connect(host='localhost',
                                             database='haleeb',
                                             user='root',
                                             password='root')
                                        cursor = connection.cursor()
                                        mySql_insert_query = ("""select products.product_id, products.name, quantity, price*quantity as total_price
                                                    from cart_items, products where cust_id = '%s' and products.product_id=cart_items.product_id;""")%(cid)
                                        cursor.execute(mySql_insert_query)
                                        data2 = cursor.fetchall()
                                        print("Product_id  Name Quantity  Price ")
                                        for row2 in data2:
                                            print(row2)
                                    elif ch == 4:
                                        connection = mysql.connector.connect(host='localhost',
                                             database='haleeb',
                                             user='root',
                                             password='root')
                                        cursor = connection.cursor()
                                        print("Total amount to pay = ", end = '')
                                        mySql__query = ("""select sum(price*quantity)
                                                                from cart_items, products
                                                                where cart_items.product_id = products.product_id and cust_id = '%s';""")%cid
                                        cursor.execute(mySql__query)
                                        price_list = cursor.fetchall()
                                        amount = 0
                                        for row in price_list:
                                            amount = int(row[0])
                                            print(row[0])
                                        mode = input("Enter mode of payment (Credit Card, Debit Card, Cash, Net Banking) : ")
                                        mySql_insert_query = ("insert into payment(mode, amount, cust_id) values(%s, %s, %s)")
                                        record_tuple = (mode, amount, cid)
                                        cursor.execute(mySql_insert_query, record_tuple)
                                        connection.commit()
                                        print()
                                        del_query = ("""delete from cart_items where cust_id = '%s'""")%(cid)
                                        cursor.execute(del_query)
                                        connection.commit()
                                        up_query = ("""update cart set no_of_items = 0 where cust_id = '%s'""")%(cid)
                                        cursor.execute(up_query)
                                        connection.commit()
                                        print("Successfully placed order.")
                                    elif ch == 5:
                                        connection = mysql.connector.connect(host='localhost',
                                             database='haleeb',
                                             user='root',
                                             password='root')
                                        cursor = connection.cursor()
                                        print("Items in cart are :-")
                                        mySql_insert_query = ("""select products.product_id, products.name, quantity, price*quantity as total_price
                                                    from cart_items, products where cust_id = '%s' and products.product_id=cart_items.product_id;""")%(cid)
                                        cursor.execute(mySql_insert_query)
                                        data2 = cursor.fetchall()
                                        print("Product_id  Name Quantity  Price ")
                                        for row2 in data2:
                                            print(row2)
                                        while True:
                                            print("")
                                            print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\t Update Items Quantity")
                                            print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            print("\t1)Decrease quantity")
                                            print("\t2)Add quantity")
                                            print("\t3)Remove product")
                                            print("\t4)Return to MAIN MENU")
                                            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                            ch2=int(input("enter choice = :"))

                                            if (ch2 == 1):
                                                r_pid = int(input("Enter product_id of item to decrease quantity : "))
                                                st=(""" select exists (select cust_id, product_id, quantity 
                                                         from cart_items where cust_id = '%s' and product_id = '%s');""")
                                                record_tuple = (cid, r_pid)
                                                cursor.execute(st, record_tuple)
                                                data=cursor.fetchall()
                                                for row in data:
                                                    if row[0] == 1:
                                                        st=(""" select * from cart_items where cust_id = '%s' and product_id = '%s';""")
                                                        record_tuple = (cid, r_pid)
                                                        cursor.execute(st, record_tuple)
                                                        data=cursor.fetchall()
                                                        print(data[0])
                                                        og_quantity = data[0][2]
                                                        r_quantity = int(input("Enter quantity to remove : "))
                                                        if (r_quantity > og_quantity):
                                                            print("You are removing more items than there are in the cart.")
                                                        elif (r_quantity < og_quantity and r_quantity>0):
                                                            st=(""" update cart_items set quantity = '%s' where cust_id = '%s' and product_id = '%s';""")
                                                            record_tuple = (og_quantity-r_quantity, cid, r_pid)
                                                            cursor.execute(st, record_tuple)
                                                            connection.commit()
                                                        elif r_quantity == og_quantity:
                                                            print("Delete item instead.")
                                                        elif r_quantity<0 :
                                                            print("You cannot remove negative items.")
                                                    else:
                                                        print("You don't have this product in cart.")
                                                        break
                                            elif ch2 == 2:
                                                r_pid = int(input("Enter product_id of item to increase quantity : "))
                                                st=(""" select exists (select cust_id, product_id, quantity 
                                                         from cart_items where cust_id = '%s' and product_id = '%s');""")
                                                record_tuple = (cid, r_pid)
                                                cursor.execute(st, record_tuple)
                                                data=cursor.fetchall()
                                                for row in data:
                                                    if row[0] == 1:
                                                        st=(""" select * from cart_items where cust_id = '%s' and product_id = '%s';""")
                                                        record_tuple = (cid, r_pid)
                                                        cursor.execute(st, record_tuple)
                                                        data=cursor.fetchall()
                                                        og_quantity = data[0][2]
                                                        r_quantity = int(input("Enter quantity to add : "))
                                                        if (r_quantity>0):
                                                            st=(""" update cart_items set quantity = '%s' where cust_id = '%s' and product_id = '%s';""")
                                                            record_tuple = (og_quantity+r_quantity, cid, r_pid)
                                                            cursor.execute(st, record_tuple)
                                                            connection.commit()
                                                        elif r_quantity<0 :
                                                            print("You cannot add negative or zero item.")
                                                    else:
                                                        print("You don't have this product in cart.")
                                                        break
                                            elif ch2 == 3:
                                                r_pid = int(input("Enter product_id of item to remove : "))
                                                st=(""" select exists (select cust_id, product_id, quantity 
                                                         from cart_items where cust_id = '%s' and product_id = '%s');""")
                                                record_tuple = (cid, r_pid)
                                                cursor.execute(st, record_tuple)
                                                data=cursor.fetchall()
                                                for row in data:
                                                    if row[0] == 1:
                                                        st=(""" delete from cart_items where cust_id = '%s' and product_id = '%s';""")
                                                        record_tuple = (cid, r_pid)
                                                        cursor.execute(st, record_tuple)
                                                        connection.commit()
                                                    else:
                                                        print("You don't have this product in cart.")
                                                        break
                                            elif ch2 == 4:
                                                break
                                            else:
                                                print("Invalid input. Try again.")
                                    elif ch == 6:
                                        connection = mysql.connector.connect(host='localhost',
                                             database='haleeb',
                                             user='root',
                                             password='root')
                                        cursor = connection.cursor()
                                        mySql_insert_query = ("""select * from orders where cust_id = '%s' and status = "In Transit";""")%cid
                                        print("Order ID | Date of order | Status | Branch ID | Payment ID | Customer ID")
                                        cursor.execute(mySql_insert_query)
                                        data2 = cursor.fetchall()
                                        for row2 in data2:
                                            print(row2)
                                        d_oid = int(input("Enter order_id to delete : "))
                                        st=(""" select exists (select * from orders where cust_id = '%s' and status = "In Transit" and order_id = '%s');""")
                                        record_tuple = (cid, d_oid)
                                        cursor.execute(st, record_tuple)
                                        data=cursor.fetchall()
                                        for row in data:
                                            if row[0] == 1:
                                                st=("""delete from orders where order_id = '%s';""")%d_oid
                                                cursor.execute(st)
                                                connection.commit()
                                            else:
                                                print("The order is not yours/ order_id doesn't exist/ order is already delivered.")
                                                break
                                    elif ch == 7:
                                        connection = mysql.connector.connect(host='localhost',
                                             database='haleeb',
                                             user='root',
                                             password='root')
                                        cursor = connection.cursor()
                                        print("Order ID | Date of order | Status")
                                        mySql_insert_query = ("""select order_id, date_of_order, status from orders where cust_id = '%s';""")%cid
                                        cursor.execute(mySql_insert_query)
                                        data2 = cursor.fetchall()
                                        for row2 in data2:
                                            print(row2)
                                    elif ch == 8:
                                        break
                            else :
                                print("Password you entered is incorrect.")
                    else :
                        print("Username doesn't exist")
                break
            except mysql.connector.Error as err:
                print("Something went wrong: {}".format(err))
    elif ch == 3:
        print("")
        print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\t DISTRIBUTOR LOGIN")
        print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        username=input("Enter distributor name :")
        try :
            connection = mysql.connector.connect(host='localhost',
                                             database='haleeb',
                                             user='root',
                                             password='root')
            cursor = connection.cursor()
            st=("SELECT EXISTS(SELECT * from distributor WHERE name = '%s')")%username
            cursor.execute(st)
            data=cursor.fetchall()
            for row in data:
                if row[0] == 1:
                    print("Welcome distributor!!")
                    id_query = ("SELECT distributor_id from distributor WHERE name = '%s'")%username
                    cursor.execute(id_query)
                    did_list = cursor.fetchall()
                    did = did_list[0][0]
                    while True: 
                        print("")
                        print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("\t DISTRIBUTOR")
                        print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("\t1)See all orders")
                        print("\t2)See pending orders")
                        print("\t3)Change status of order to delivered")
                        print("\t4)See Orders delivered")
                        print("\t5)Return to MAIN MENU")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        ch=int(input("enter choice = :"))
                        if ch == 1:
                            connection = mysql.connector.connect(host='localhost',
                                             database='haleeb',
                                             user='root',
                                             password='root')
                            cursor = connection.cursor()
                            qu = ("select * from orders where branch_id = '%s';")%did
                            cursor.execute(qu)
                            data2=cursor.fetchall()
                            for row2 in data2:
                                print(row2)
                        elif ch == 2:
                            connection = mysql.connector.connect(host='localhost',
                                             database='haleeb',
                                             user='root',
                                             password='root')
                            cursor = connection.cursor()
                            qu = ("""select * from orders where branch_id = '%s' and status = "In Transit";""")%did
                            cursor.execute(qu)
                            data2=cursor.fetchall()
                            for row2 in data2:
                                print(row2)
                        elif ch == 3:
                            connection = mysql.connector.connect(host='localhost',
                                             database='haleeb',
                                             user='root',
                                             password='root')
                            cursor = connection.cursor()
                            oid = int(input("Enter order id : "))
                            qu = ("""update orders set status = "Delivered" where order_id = '%s';""")%oid
                            cursor.execute(qu)
                            connection.commit()
                            print("Status updated successfully!")
                        elif ch == 4:
                            connection = mysql.connector.connect(host='localhost',
                                             database='haleeb',
                                             user='root',
                                             password='root')
                            cursor = connection.cursor()
                            qu = ("""select * from orders where branch_id = '%s' and status = "Delivered";""")%did
                            cursor.execute(qu)
                            data2=cursor.fetchall()
                            for row2 in data2:
                                print(row2)
                        elif ch == 5:
                            break
                else :
                    print("Username doesn't exist")
                    break
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
    elif ch == 4:
        while True:
            print("")
            print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\t SUPPLIER LOGIN")
            print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            username=input("Enter supplier name :")
            try :
                connection = mysql.connector.connect(host='localhost',
                database='haleeb',
                user='root',
                password='root')
                cursor = connection.cursor()
                st=("SELECT EXISTS(SELECT * from supplier WHERE name = '%s')")%username
                cursor.execute(st)
                data=cursor.fetchall()
                for row in data:
                    if row[0] == 1:
                        print("Welcome supplier!!")
                        id_query = ("SELECT supplier_id from supplier WHERE name = '%s'")%username
                        cursor.execute(id_query)
                        sid_list = cursor.fetchall()
                        sid = sid_list[0][0]
                        while True:
                            print("")
                            print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("\t SUPPLIER")
                            print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                            print("\t1) View Restocking Requests")
                            print("\t2) Accept Restocking Request")
                            print("\t3) Return to Main Menu")
                            ch2 = int(input("Enter choice: "))
                            if ch2 == 1:
                                try:
                                    connection = mysql.connector.connect(host='localhost',
                                                                database='haleeb',
                                                                user='root',
                                                                password='root')
                                    cursor = connection.cursor()
                                    restock_query = ("SELECT * from restock_request WHERE supplier_id = %s")
                                    cursor.execute(restock_query, (sid,))
                                    restock_data = cursor.fetchall()
                                    print("Restocking Requests:")
                                    print("ID | Product ID | Supplier ID | Quantity | b_no")
                                    for row in restock_data:
                                        print(row)
                                except Error as e:
                                    print("Error while connecting to MySQL", e)
                                finally:
                                    if (connection.is_connected()):
                                        cursor.close()
                                        connection.close()
                                        print("MySQL connection is closed")
                            elif ch2 == 2:
                                connection = mysql.connector.connect(host='localhost',
                                                                database='haleeb',
                                                                user='root',
                                                                password='root')
                                cursor = connection.cursor()
                                request_id = int(input("Enter the restock request ID: "))
                                restock_query = ("SELECT * from restock_request WHERE id = '%s'")%request_id
                                cursor.execute(restock_query)
                                restock_data = cursor.fetchall()
                                for row in restock_data:
                                    quantity = row[3]
                                    loc_id = row[4]
                                    pro_id = row[1]
                                accept_query = ("update location_inventory set stock = stock + '%s' where loc_id = '%s' and product_id = %s;")
                                record_tuple = (quantity, loc_id, pro_id)
                                cursor.execute(accept_query, record_tuple)
                                connection.commit()
                                print("Restock request accepted.")

                            elif ch2 == 3:
                                break
                            else:
                                print("Invalid input")
                    else :
                        print("Username doesn't exist")
                        break
            except mysql.connector.Error as err:
                print("Something went wrong: {}".format(err))
                break
    elif ch == 5:
        connection = mysql.connector.connect(host='localhost',
                    database='haleeb',
                    user='root',
                    password='root')
        cursor = connection.cursor()
        c_id = int(input("Enter customer_id : "))
        c_name = input("Enter customer name : ")
        c_email = input("Enter email : ")
        c_username = input("Enter username : ")
        c_password = input("Enter password : ")
        query = "select exists (select * from customer where customer_id = '%s');"%(c_id)
        cursor.execute(query)
        data = cursor.fetchall()
        for row in data:
            if row[0] == 0:
                query = "select exists (select * from customer where email = '%s');"%(c_email)
                cursor.execute(query)
                data2 = cursor.fetchall()
                for row2 in data2:
                    if row2[0] == 0:
                        query = "select exists (select * from customer where username = '%s');"%(c_username)
                        cursor.execute(query)
                        data3 = cursor.fetchall()
                        for row2 in data3:
                            if row2[0] == 0:
                                query = "insert into customer(name, email, username, password) values (%s,%s,%s,%s,%s);"
                                record_tuple = (c_id, c_name, c_email, c_username, c_password)
                                cursor.execute(query, record_tuple)
                                connection.commit()
                            else:
                                print("This username already exist. Try another.")
                    else:
                        print("This email already exist. Try another.")
            else:
                print("This customer_id already exists.")
    elif ch == 6:
        break

            

