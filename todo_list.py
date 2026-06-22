tasks=[]
while True:

     print("To-Do List")
     print("\n1. Add Task")
     print("2. View Tasks")
     print('3. Exit')
     choice=input("Enter your choice:")
     if choice=="1":
         
         task=input("Enter a task:")
         tasks.append(task)
         print("Task added succesfully!")
     elif choice=="2":
         if len(tasks)==0:
             print("No tasks available.")
         else:
             print("\n/Your Tasks:")
             for task in tasks:
                  print("-",task)
     elif choice=="3":
         print("Goodbye!")
         break
     else:
         print("Invalid choice!")