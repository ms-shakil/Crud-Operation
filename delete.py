
def find_indx(list,id):
    for i in range(len(list)):
        if list[i]["id"]==id:
            return i
    return "x"

def delete_data():
    import json
    JSON_DATA ="./Players_data.json"
    
    with open(JSON_DATA,"r") as fd:
        DATA =json.load(fd)
        try:
            id_= input("Enter an your ID:")
            idx =find_indx(DATA["Information"],id_)
            DATA["Information"].pop(idx)
        except Exception:
            print("ID ERROR")

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
    with open(JSON_DATA,"w") as fd:
        json.dump(DATA,fd)
         