from auth import check
from disp import detail_zoo, detail_ani

print("welcome!!!")

def initial():
    enter_code = input("press e to enter or x to exit or d for details:") 
    if enter_code == "E" or enter_code == "e":
        check()
    elif enter_code == "x" or enter_code =="X":
        print("you have exited")
    elif enter_code == "D" or enter_code =="d":
        print("\n")
        detail_zoo()  
        detail_ani()    
    else:
        print("try again")
        initial()

if __name__=="__main__":
    initial() 

