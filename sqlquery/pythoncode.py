import mysql.connector
from mysql.connector import Error 

#Initialise the cursor
def connect_cursor(host_name,user_name,user_password,db_name):
    connection=None
    try:
        connection=mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
        
    except Error as e:
        print(f"The error '{e}' occured")
        
    return connection


def create_table():
    sql='''CREATE TABLE IF NOT EXISTs users(
        id INT,
        name VARCHAR(255) NOT NULL,
        age INT,
        gender VARCHAR(50),
        nationality VARCHAR(50)
        )'''
    try:
        cursor.execute(sql)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"Error '{e}' as occured")    
    
        
def check_user(id):
    sql="SELECT * FROM users WHERE id=%s"
    cursor.execute(sql,(id,))
    cursor.fetchall()
    return cursor.rowcount == 1

def add_user():
    id=input("Enter the id : ")
    if check_user(id):
        print("User already exist choose other user Id")
        return 
    Name=input("enter the name of the User : ")
    age=input("Enter the Age of User : ")
    gender=input("Enter the gender of User : ")
    nationality=input("Enter the nationality of User : ")
    
    sql="INSERT INTO users (id,name,age,gender,nationality) VALUES (%s,%s,%s,%s,%s)"
    data=(id,Name,age,gender,nationality)    
    try:
        cursor.execute(sql,data)
        connection.commit()
        print("User successfully added")
    except Error as e:
        print(f"An error '{e}' as occured")
        connection.rollback()
        
def remove_user():
    id=input("Enter the id : ")
    if not check_user(id):
        print("User does not exist. Please try again.")
        return 
    
    sql="DELETE FROM users WHERE id=%s"
    try:
        cursor.execute(sql,(id,))
        connection.commit()
        print("User successfully removed")
    except Error as e:
        print(f"An error '{e}' as occured")
        connection.rollback()
        
def change_detail():
    id=input("Enter the id : ")
    if not check_user(id):
        print("User does not exist. Please try again.")
        return 
    try:
        chng=input("Enter the value to be change : ")
        val=input("enter changed value : ")
        sql="UPDATE users SET %s=%s WHERE id=%s"
        data=(chng,val,id)
        cursor.execute(sql,data)
        connection.commit()
        print("Succeddsully changed the data")
    except Error as e:
        print(f"Error : '{e}'")
        connection.rollback()
        
def display_data():
    try:
        sql="SELECT * FROM users"
        cursor.execute(sql)
        user=cursor.fetchall()
        for usr in user:
            print("\nUser Id :",usr[0])
            print("User Name :",usr[1])
            print("User Age :",usr[2])
            print("User Gender :",usr[3])
            print("User nationality :",usr[4])
            print("------------------------------------")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def main():
    while True:
        print("\nWelcome to User register Record")
        print("Press:")
        print("1 to Add User")
        print("2 to Remove User")
        print("3 to Change User Details")
        print("4 to Display User")
        print("5 to Exit")
                
        ch = input("Enter your Choice: ")

        if ch == '1':
            add_user()
        elif ch == '2':
            remove_user()
        elif ch == '3':
            change_detail()
        elif ch == '4':
            display_data()
        elif ch == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid Choice! Please try again.")
            
if __name__=="__main__": 
    connection=connect_cursor('localhost','root','Sungjinwoo123','db')
    cursor=connection.cursor()
    create_table()
    main()
       