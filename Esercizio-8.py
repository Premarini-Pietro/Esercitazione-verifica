def my_function(*kids):
    if len(kids) >= 4:
        print(kids[2])
        print(kids[3])
    elif len(kids) == 3:
        print(kids[2])
    else:
        print("Nessuno")
    print("#######")

my_function("Emil", "Tobias", "Linus", "Antonino","Marietto")
