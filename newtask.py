def duty():
    duties = [] #empty list
    print("--WELCOME TO MANAGE YOUR DUTIES---")

    whole_task=int(input("Enter how many duties you want to add:"))
    for i in range(1,whole_task+1):
        duties_name = input(f"Enter duties{i}=")
        duties.append(duties_name)

    print(f"yor today's duties are\n{duties}")
    while True:
        jobs  = int(input("Enter 1 - ADD\n2 - UPDATE\n3 - DELETE \n4 - VIEW\n5 - EXIT"))
        if jobs ==1:
            ADD = input("enter duty you want to add =")
            duties.append(ADD)
            print(f"Duty{ADD} has been successfully added")
        elif jobs ==2:
            UPDATE_val = input("enter the duty you want to change =")
            if UPDATE_val in duties:
                change = input("Enter new duty = ")
                index = duties.index(UPDATE_val)
                duties[index] = change
                print(f"UPDATED VALUE{change} ")

        elif jobs ==3:
            del_val=input("which task you want to delete=")
            if del_val in duties:
                index= duties.index(del_val)
                del duties[index]
                print(f"DUTIES{del_val}has been deleted")

        elif jobs == 4:
            print(f"Total jobs={duties}")

        elif jobs == 5:
            print(f"stop the programme----")
            break
        
        else:
            print("invalid input")
duty()
            