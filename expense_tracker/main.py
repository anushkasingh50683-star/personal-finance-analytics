print(" | Welcome to Expense Tracker 🛒| ")

expenses=[]

while True:
    
    print("\n\n===============Menu===============")
    print("\n 1. Add Expenses 💸")
    print("\n 2. View All Expenses 🧾")
    print("\n 3. View Total Amount 💰")
    print("    \n 4. Exit 👋")
    
    choice=int(input("\n\n Please Enter your choice here : "))
    
    if choice==1:
        
        date=input("Enter the date of Expense (YY-MM-DD): ")
        category=input("Enter the category of expense :")
        desc=input("Enter some description of the expense :")
        amt=float(input("Enter the amount :"))
        
        expense={
            "date":date,
            "category":category,
            "description":desc,
            "amount":amt
        }
        
        expenses.append(expense)
        
        print("All your Expenses are added Sucessfully 📋 ")    
    
    elif choice==2:
    
        if len(expenses)==0:
            print("No expense")
        else:
            count=1
            
            for ur_expenses in expenses:
                
                print("\n \n Here are all your expenses 🗂️")
                # f string ke andar double quotes nhi lgate
                
                print(f"{count}->>\n"
                      f"Date - {ur_expenses['date']}\n"
                      f"Category - {ur_expenses['category']}\n"
                      f"Description - {ur_expenses['description']}\n"
                      f"Amount - {ur_expenses['amount']}"
                      )
                
                count+=1

    elif choice==3:
        
        total=0
        
        for ur_expenses in expenses:
            
            total+=ur_expenses["amount"]
        
        print("Total amount of your expenses is : ",total)
    
    elif choice==4:
        
        print(" || THANK YOU FOR VISITING OUR EXPENSE TRACKER 😊||")
        break
    
    else:
        print("Not a valid choice . Try again !!")