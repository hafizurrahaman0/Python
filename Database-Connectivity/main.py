import mysql.connector

# Make sure the connection to the MySQL database is established
while True:
    print("""
    ================================
    Welcome To Tanu Malik Cafe
    ================================
    """)
    try:
        import mysql.connector
    except ModuleNotFoundError:
        print("MySQL Connector not found. Please install it using 'pip install mysql-connector-python'.")
        break

    passwd = "root"
    try:
        mysql = mysql.connector.connect(
            host="localhost", port=3306, user="root", passwd=passwd)
        mycursor = mysql.cursor()
        mycursor.execute("create database if not exists city_cafe")
        mycursor.execute("use city_cafe")

        # Creating tables for cafe management
        mycursor.execute(
            "create table if not exists customer_details(name varchar(30) primary key, contact varchar(15), order_history text)")
        mycursor.execute(
            "create table if not exists staff_details(name varchar(30) primary key, role varchar(40), age int(3), address varchar(50), contact varchar(15), monthly_salary int(10))")
        mycursor.execute(
            "create table if not exists menu_items(item_name varchar(30) primary key, category varchar(30), price decimal(10,2))")
        mycursor.execute(
            "create table if not exists orders(order_id int primary key auto_increment, customer_name varchar(30), item_name varchar(30), quantity int, order_date date)")
        mycursor.execute(
            "create table if not exists user_data(username varchar(30) primary key, password varchar(30) default '000')")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        break

    while True:
        print("""
        1. Sign In
        2. Registration
        """)
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 2:
            print("""
            =======================================
            !!!!!!!!!!Register Yourself!!!!!!!!
            =======================================
            """)
            u = input("Input your username: ")
            p = input("Input your password (Password must be strong!!!): ")
            try:
                mycursor.execute("insert into user_data(username, password) values(%s, %s)", (u, p))
                mysql.commit()
                print("Registration Done Successfully!")
            except mysql.connector.Error as err:
                print(f"Error: {err}")

        elif choice == 1:
            un = input("Enter Username: ")
            ps = input("Enter Password: ")
            mycursor.execute("select password from user_data where username=%s", (un,))
            row = mycursor.fetchone()
            if row and row[0] == ps:
                while True:
                    print("""
                    1. Manage Staff
                    2. Manage Customers
                    3. Manage Menu
                    4. Manage Orders
                    5. Sign Out
                    """)
                    try:
                        action = int(input("Enter your choice: "))
                    except ValueError:
                        print("Please enter a valid number.")
                        continue
                    if action == 5:
                        break
                    elif action == 1:
                        while True:
                            print("""
                            1. Add Staff
                            2. Remove Staff
                            3. View Staff Details
                            4. Go Back
                            """)
                            action = int(input("Enter your choice: "))
                            if action == 1:
                                staffName = str(input("Enter Staff Name: "))
                                staffRole = str(input("Enter Role: "))
                                staffAge = int(input("Enter Staff Age: "))
                                staffAddress = str(input("Enter Address: "))
                                staffContact = str(input("Enter Contact: "))
                                staffSalary = int(input("Enter Salary: "))

                                sql = "INSERT INTO staff_details (name, role, age, address, contact, monthly_salary) VALUES (%s, %s, %s, %s, %s, %s)"
                                val = (staffName, staffRole, staffAge, staffAddress, staffContact, staffSalary)

                                mycursor.execute(sql, val)
                                mysql.commit()

                                print("New Staff Added!..")

                            elif action == 2:
                                staffName = str(input("Enter staff name to remove: "))

                                sql = "DELETE FROM staff_details WHERE name = %s"
                                val = (staffName,)

                                mycursor.execute(sql, val)
                                mysql.commit()

                                print(f"Staff member '{staffName}' has been removed.")

                            elif action == 3:
                              mycursor.execute("SELECT * FROM staff_details")
                              staffs = mycursor.fetchall()
                              for staff in staffs:
                                  print(f"Name: {staff[0]}, Role: {staff[1]}, Age: {staff[2]}, Address: {staff[3]}, Contact: {staff[4]}, Monthly Salary: {staff[5]}")
                                  
                            elif action == 4:
                              break


                    elif action == 2:  # Manage Customers
                        while True:
                            print("""
                            1. Add Customer
                            2. Remove Customer
                            3. View Customer Details
                            4. Go Back
                            """)
                            action = int(input("Enter your choice: "))
                            
                            if action == 1:  # Add Customer
                              customerName = str(input("Enter Customer Name: "))
                              customerContact = str(input("Enter Customer Contact: "))
                              customerOrderHistory = str(input("Enter Order History: "))

                              sql = "INSERT INTO customer_details (name, contact, order_history) VALUES (%s, %s, %s)"
                              val = (customerName, customerContact, customerOrderHistory)

                              mycursor.execute(sql, val)
                              mysql.commit()

                              print(f"Customer '{customerName}' added successfully.")

                              # Add an initial order when the customer is added (if necessary)
                              orderItem = str(input("Enter the item ordered by the customer: "))
                              orderQuantity = int(input("Enter quantity of the item ordered: "))
                              orderDate = input("Enter the order date (YYYY-MM-DD): ")

                              # Insert order data
                              sql = "INSERT INTO orders (customer_name, item_name, quantity, order_date) VALUES (%s, %s, %s, %s)"
                              val = (customerName, orderItem, orderQuantity, orderDate)

                              mycursor.execute(sql, val)
                              mysql.commit()

                              print(f"Order added for customer '{customerName}'.")

                            elif action == 2:  # Remove Customer
                              customerName = str(input("Enter customer name to remove: "))

                              # Delete associated orders
                              sql = "DELETE FROM orders WHERE customer_name = %s"
                              val = (customerName,)

                              mycursor.execute(sql, val)
                              mysql.commit()

                              # Delete the customer
                              sql = "DELETE FROM customer_details WHERE name = %s"
                              val = (customerName,)

                              mycursor.execute(sql, val)
                              mysql.commit()

                              print(f"Customer '{customerName}' and their orders have been removed.")

                            elif action == 3:
                                mycursor.execute("SELECT * FROM customer_details")
                                customers = mycursor.fetchall()
                                for customer in customers:
                                    print(f"Name: {customer[0]}, Contact: {customer[1]}, Order History: {customer[2]}")

                            elif action == 4:
                                break

                    elif action == 3:  # Manage Menu
                        while True:
                            print("""
                            1. Add Menu Item
                            2. Remove Menu Item
                            3. View Menu Items
                            4. Go Back
                            """)
                            action = int(input("Enter your choice: "))
                            if action == 1:
                                itemName = str(input("Enter Item Name: "))
                                itemCategory = str(input("Enter Category: "))
                                itemPrice = float(input("Enter Price: "))

                                sql = "INSERT INTO menu_items (item_name, category, price) VALUES (%s, %s, %s)"
                                val = (itemName, itemCategory, itemPrice)

                                mycursor.execute(sql, val)
                                mysql.commit()

                                print(f"Menu Item '{itemName}' added successfully.")

                            elif action == 2:
                                itemName = str(input("Enter menu item name to remove: "))

                                sql = "DELETE FROM menu_items WHERE item_name = %s"
                                val = (itemName,)

                                mycursor.execute(sql, val)
                                mysql.commit()

                                print(f"Menu item '{itemName}' has been removed.")

                            elif action == 3:
                                mycursor.execute("SELECT * FROM menu_items")
                                menu = mycursor.fetchall()
                                for item in menu:
                                    print(f"Item: {item[0]}, Category: {item[1]}, Price: {item[2]}")

                            elif action == 4:
                                break

                    elif action == 4:  # Manage Orders
                        while True:
                            print("""
                            1. View Orders
                            2. Go Back
                            """)
                            action = int(input("Enter your choice: "))
                            if action == 1:
                                mycursor.execute("SELECT * FROM orders")
                                orders = mycursor.fetchall()
                                for order in orders:
                                    print(order)
                                    print(f"Order ID: {order[0]}, Customer Name: {order[1]}, Item: {order[2]}, Quantity: {order[3]}, Date: {order[4]}")
                            elif action == 2:
                                break

            else:
                print("Invalid username or password")
        else:
            break
