import cng
from disp import display

def check():
    name = input("enter your username\n")+"\n"
    mail = input("enter your mail\n")+"\n"
    password = input("enter your password\n")+"\n"
    
    with open("../info/admin.txt", "r") as f: 
        na = f.readline()
        em = f.readline()
        pa = f.readline()    
        
        if name == na and mail == em and password == pa:
            print("welcome",name)
            val = input("press m to make changes to your data and d to display your data:")
            if val == "m" or val =="M":
                make_changes()
            elif val == "D" or val== "d":
                display()
            else:
                print("bye!!")
        else:     
            print("\nsorry!! wrong information")
            print("do you want to try again?")
            print("y:yes" + "any other key to exit")
            ver = input()
            if ver == "y" or ver == "Y":    
                check()
            else:
                print("bye!!")
                
                
def make_changes():
    string = input("where would you like to make the changes:")
    if string == "Employees" or string == "employees":
        val= input("press a to add and d to delete:")
        if val == "A" or val == "a":
            cng.add_employees()
        elif val =="D" or val == "d":
            cng.del_employee()
        else:
            print("exited")
    
    elif string == "Animals" or string == "animals":
        val= input("press a to add and d to delete:")
        if val == "A" or val == "a":
            cng.add_animals()
        elif val =="D" or val == "d":
            cng.del_animals()
        else:
            print("exited")
    
    elif string == "Plants" or string == "plants":
        val= input("press a to add and d to delete:")
        if val == "A" or val == "a":
            cng.add_plants()
        elif val =="D" or val == "d":
            cng.del_plants()
        else:
            print("exited")
    else:
        foo = input("press y to try again or press any other key to exit:")
        if foo == "y" or foo =="Y":
            make_changes()
        else:
            print("exited")


        