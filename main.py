mini project- expense tracker

expenses = [] # list of all expenses in form of dictionary

print("welcome to expense tracker : khrcha kam kiya karo")

while True:
    print("===MENU===")
    print("1. add expense")
    print("2. view all expenses")
    print("3. view total khrcha")
    print("4. exit")

    choice= int(input("please enter your choice :"))


# ADD EXPENSE
    if(choice ==1):
        DATE= input("kis date par khrcha kiya tha?")
        category= input("kis type ka khrcha kiya? (food,travel,makeup,books)")
        description= input("aur detail do")
        amount= float(input("kitnai ka khrcha tha: "))

        expense= {
            "DATE": DATE,
            "category": category,
            "description": description,
            "amount": amount

        }

        expenses.append(expense)
        print(" \n DONE BRO. expense is added successfully")

        #VIEW ALL EXPENSES
    elif(choice == 2):
        if(len(expenses)==0 ):
                print("no expenses added. jao pehlai khrcha karo. ")
        else:
                print("===Yeh hai apka sara expense===")
                count= 1
                for eachKhrcha in expenses:
                    print(f"khrcha number {count} -> {eachKhrcha["DATE"]}, {eachKhrcha["category"]}, {eachKhrcha["description"]}, {eachKhrcha["amount"]}")
                    count= count+1

        # 3. view total spending
        if(choice ==3):
                total= 0
                for eachKhrcha in expenses:
                    total= total + eachKhrcha["amount"]

                    print("\n total khrcha =", total)

#4. exit
    elif(choice == 4):
        print("thank you for using our system")
        break

    else:
        print("invalid choice. try again")
