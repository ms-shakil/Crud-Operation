
def find_indx(list,id):
    found = False
    for i in list:
        if i["id"] == id:         
            found = True
            break
    return found

def insert_data():
    import json
    JSON_DATA = "./Players_data.json"
    DATA =[]
    with open(JSON_DATA,"r") as fd:
        DATA = json.load(fd)
        count = int(input("How many Players data you want insert:"))
        i = 0
        while i < count:
            people={
                "id":input("ID:"),
                "name":input("Name:"),
                "age":input("age"),
                "nat":input("Nat:"),
                "club":input("Club:")
            }
            if find_indx(DATA,people["id"]):
                print("Data already existes:")
            else:
                DATA.append(people)
                i+=1
                with open (JSON_DATA,"w") as fd:
                    json.dump(DATA,fd)    

