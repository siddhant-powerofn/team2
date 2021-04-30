import db
from employee.controller import *

print("Type 1 if you want to insert record : ")
print("Type 2 if you want to update record : ")
print("Type 3 if you want to select record : ")
print("Type 4 if you want to delete record : ")
print("Type 5 if you want to select range of record : ")
input2 = int(input())

if(input2==1):
    insert_record()
elif(input2==2):
    update_record()
elif(input2==3):
    select_record()
elif(input2==4):
    delete_record()
elif(input2==5):
    select_range()


conn.close()