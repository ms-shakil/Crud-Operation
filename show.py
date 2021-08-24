def find_indx(list,id):

    for i in range(len(list)):
        if list[i]["id"] == id:
            return i
            break
    return "x"    
def show_data():
    import json
    JSON_DATA ="./Players_data.json"
    DATA =[]
    with open(JSON_DATA,"r") as fd:
        DATA =json.load(fd)
        id_ = input("Enter an your id:")
        idx = find_indx(DATA["Information"],id_)
        print(DATA["Information"][idx])