
def find_indx(list,id):
    for i in range(len(list)):
        if list[i]["id"]==id:
            return i
    return "x"

def delete_data():
    import json
    JSON_DATA ="./Players_data.json"
    DATA =[]
    with open(JSON_DATA,"r") as fd:
        DATA =json.load(fd)
        try:
            id_= input("Enter an your ID:")
            idx =find_indx(DATA,id_)
            DATA.pop(idx)
        except Exception:
            print("ID ERROR")
        with open(JSON_DATA,"w") as fd:
            json.dump(DATA,fd)
                