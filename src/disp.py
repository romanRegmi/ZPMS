def display():
    string = str(input("which data would you like to display:"))
    if string == "Employees" or string == "employees":
        from prettytable import from_csv
        f = "../data_csv/employees.csv"
        csv_file = open(f)
        emp = from_csv(csv_file)
        print(emp)
    elif string == "Animals" or string == "animals":
        from prettytable import from_csv
        f = "../data_csv/animals_des.csv"
        csv_file = open(f)
        ani = from_csv(csv_file)
        print(ani)
    elif string == "Plants" or string == "plants": 
        from prettytable import from_csv
        f = "../data_csv/plants.csv"
        csv_file = open(f)
        pla = from_csv(csv_file)
        print(pla)
    else:
        ver = input("press Y/y to try again or press any other key to exit:")
        if ver == "y" or ver =="Y":
            display()
        else:
            print("Bye")

def detail_zoo():
    with open("../info/details.txt","r") as f:
        for line in f:
            print(line, end="")

def detail_ani():
    from prettytable import from_csv
    f = "../data_csv/animals.csv"
    csv_file = open(f)
    ani = from_csv(csv_file)
    print(ani)