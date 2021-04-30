import sys
sys.path.append("/home/siddhant/Desktop/python")

from db import *

#SELECT RANGE FOR TWO EMPLOYEE ID
def select_range():
    start_emp_id = input("Enter the starting ID: ")
    end_emp_id = input("Enter the last employee ID: ")
    cur.execute("SELECT * FROM EMPLOYEE WHERE ID BETWEEN'"+start_emp_id+"'AND '"+end_emp_id+"'")

    data = cur.fetchall()

    for d in data:
        print(d)

#INSERT RECORD INTO TABLE
def insert_record():
    count_new_record = int(input("Type the total no of record you wnat to insert: \n"))

    for i in range(0,count_new_record,1):
        emp_id = input("Give the id name: \n")
        emp_name = input("Give the employee name: \n")
        emp_department = input("Give the employee department: \n")
        emp_active = (input("Give 1 if employee is still active, otherwise give 0: \n"))
        emp_gender = input("For female: press F and for male press M: \n")
        emp_role_id = input("Give the role id of employee: \n")

        #cur.execute("INSERT INTO EMPLOYEE (ID, NAME, DEPARTMENT, ACTIVE, GENDER, ROLE_ID) VALUES ('"+emp_id+"', '"+emp_name+"', '"+emp_department+"', '"+emp_active+"', '"+emp_gender+"', '"+emp_role_id+"')")
        sql = ("""INSERT INTO EMPLOYEE(ID, NAME, DEPARTMENT, ACTIVE, GENDER, ROLE_ID) VALUES(%s, %s, %s, %s, %s, %s)""")

        cur.execute(sql,(emp_id, emp_name, emp_department, emp_active, emp_gender, emp_role_id))
        conn.commit()
    print("Records created successfully")
    cur.close()

#SELECT ALL RECORD
def select_record():
    #for i in range(0,count_select, 1):
    #input1 = input("Give the employee id: \n")

    #cur.execute("SELECT * FROM EMPLOYEE WHERE ID = " + " '"+input1+"'")
    cur.execute("SELECT * FROM EMPLOYEE")

    data = cur.fetchall()

    for d in data:
        print(d)
    cur.close()

#UPDATE RECORD FOR  PARTICULAR EMPLOYEE ID
def update_record():
    update_emp_id=input("Provide with the correct id of row to be updated ")

    update_column=input("Provide with the column name to be updated: ")
    update_value=input("Provide with correct value for "+update_column+"\n")
    cur.execute("UPDATE EMPLOYEE SET "+update_column+" = '"+update_value+"' WHERE ID=" + " '"+update_emp_id+"'")
    conn.commit()
    cur.close()

#DELETE THER RECORD FOR PARTICULAR EMPLOYEE ID
def delete_record():
    delete_emp_id=input("Provide the employee id for deletion: ")
    cur.execute("DELETE FROM EMPLOYEE WHERE ID = " + " '"+delete_emp_id+"'")
    conn.commit()
    cur.close()