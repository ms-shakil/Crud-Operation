from insert import insert_data,find_indx
from show import show_data,find_indx
from update import update_data,find_indx
from delete import delete_data,find_indx
try:

    A = input("What Do you Want:\n(insert,\nupdate,\nshow,\ndelete,)\n\nWrite here:")

    if A == "insert":
        insert_data()
    elif A == "update":
        update_data() 
    elif A == "show":
        show_data()
    elif A == "delete":
        delete_data()
    else: 
        print("Data Not Found:")    
except Exception  as e:
    print(e)                  