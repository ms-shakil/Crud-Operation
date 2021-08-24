
def find_indx(list,id):
    for indx in range(len(list)):
        if list[indx]["id"] == id:
            return indx
    return "ID NOT MESS"   
      
def update_data():
    import json
    JSON_DATA ="./Players_data.json"
    DATA = None
    with open(JSON_DATA,"r") as fd:
        DATA =json.load(fd)
        ind = -1
        while ind == -1:
            id_ = input("Enter an your ID:")
            ind = find_indx(DATA["Information"],id_) 
            data_list =[]
            for j in DATA["Information"][ind].keys():
                if j != id:
                    data_list.append(j)
            feild =""
            while feild == "":
                upd =input("What do you want update{}:".format(",".join(data_list)))
                if upd in data_list:
                    feild = upd
            new_val = input("Enter an value:")   
            DATA["Information"][ind][feild] = new_val
    with open(JSON_DATA,"w") as fd:
        json.dump(DATA,fd)             
          