def add_employees(): 
    id_no = input("enter id_no:")
    fname = input("enter the first name:")
    lname = input("enter the second name:")
    post  = input("enter post:")
    salary = input("enter salary:")
    email = fname+lname+"zoo.com"
    with open("../data_csv/employees.csv",'a') as f:
        f.write('\n')
        f.writelines([id_no,','+fname,','+lname,','+post,','+email+',',salary])
    
def add_animals():
    id_no = input("enter id_no:")
    name = input("enter Cname:")
    scientific_name = input("enter scientific name:")
    with open("../data_csv/animals_des.csv",'a') as f:
        f.write('\n')
        f.writelines([id_no+',', name+',', scientific_name])
        
def add_plants():
    id_no = input("enter id_no:")
    name = input("enter Cname:")
    scientific_name = input("enter the scientific name:")
    with open("../data_csv/plants.csv",'a') as f:
        f.write('\n')
        f.writelines([id_no+',' ,name+',' ,scientific_name])


def del_employee():
    id_no = input("enter the id_no of the object you want to remove:")
    f = open("../data_csv/employees.csv",'r')
    lines = f.readlines()
    for i in range(len(lines)):
        a = lines[i]
        b = a.split(',')
        c =b[0]
        if id_no == c:
            lines[i]=""
    f.close()
    f = open("../data_csv/employees.csv",'w')
    f.writelines(lines)
    f.close()    

def del_animals():
    id_no = input("enter the id_no of the object you want to remove:")
    f = open("../data_csv/animals_des.csv",'r')
    lines = f.readlines()
    for i in range(len(lines)):
        a = lines[i]
        b = a.split(',')
        c =b[0]
        if id_no == c:
            lines[i]=""
    f.close()
    f = open("../data_csv/animals_des.csv",'w')
    f.writelines(lines)
    f.close()            

def del_plants():
    id_no = input("enter the id_no of the object you want to remove:")
    f = open("../data_csv/plants.csv",'r')
    lines = f.readlines()
    for i in range(len(lines)):
        a = lines[i]
        b = a.split(',')
        c =b[0]
        if id_no == c:
            lines[i]=""
    f.close()
    f = open("../data_csv/plants.csv",'w')
    f.writelines(lines)
    f.close() 
   
