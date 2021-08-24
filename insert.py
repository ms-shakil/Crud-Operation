
def find_indx(list,id):
    found = False
    for i in list:
        if i["id"] == id:         
            found = True
            break
    return found

def insert_data():
    import json
    import re
    Age = re.compile("^\d{1,3}$")
    Phone = re.compile(r"^01[3-9]\d{8}$")
    Gmail = re.compile(r"\w+@\w+\.\w{3,5}$")
    JSON_DATA = "./Players_data.json"

    with open(JSON_DATA,"r") as fd:
        DATA = json.load(fd)
        count = int(input("How many Players data you want insert:"))
        i = 0
        while i < count:
            people={}
            id_ = input("Enter the ID:")
            people["id"] = id_
            name = input("Enterthe Name:")
            people["name"]= name
            coun = input("Enter Country  Name:").upper()
            people["Country"] = coun
            while True:
                Ag = input("Enter tha Age:")
                age_ = Age.search(Ag)
                if age_ != None:
                    people["age"]=age_.group()
                    break
            while True:
                phone = input("Enter the Phone Number::")
                phn = Phone.search(phone)
                if phn != None:
                    people["Phone number"] = phn.group()
                    break
            while True:
                gmail = input("Enter the Gmail:")
                gml = Gmail.search(gmail)
                if gml != None:
                    people["Email"] = gml.group()
                    break
            if find_indx(DATA["Information"],people["id"]):
                print("Data already existes:")
            else:
                DATA["Information"].append(people)
                i+=1

        DATA["Total_player"] = len(DATA["Information"])
        My_dic ={}
        My_arr =[]
        for i in DATA["Information"]:
            dic = i["Country"]
            if dic in My_dic:
                My_dic[dic] +=1
            else:
                My_dic[dic] =1
    
        for name,count in  My_dic.items():
            My_arr.append({
              "name":name,
              "count":count
            })
        DATA["Country"]    = My_arr
       

    with open (JSON_DATA,"w") as fd:
        json.dump(DATA,fd)    
