#Todo list app made for sample challenge

import sys               #to get commands from cmd window
import datetime          #for date and time


args = sys.argv
tasks = []              #list to store tasks to be done
done = []               #list to store tasks that are completed


try:
        command = args[1]   
except IndexError:
        print("Usage :- ")
        print("todo.py add `todo item` # Add a new todo")
        print("todo.py ls              # show remaining todos")
        print("todo.py del NUMBER      # Delete a todo")
        print("todo.py done NUMBER     # Complete a todo")
        print("todo.py help            # Show usage")
        print("todo.py report          # Statistics")
        sys.exit(1)



if command not in ("add","del","ls","done","help","report"):
        print("Usage :- ")
        print("todo.py add `todo item` # Add a new todo")
        print("todo.py ls              # show remaining todos")
        print("todo.py del NUMBER      # Delete a todo")
        print("todo.py done NUMBER     # Complete a todo")
        print("todo.py help            # Show usage")
        print("todo.py report          # Statistics")
        sys.exit(1)


#to add in the todo list
if command == "add":
        task = args[2]
        print('Added todo: "{}"'.format(task))
        file = open("tasks.txt", "a")
        file.write(task+"\n")
        file.close()

        f = open("done.txt", "a")
        f.close()

#to delete from the list
elif command == "del":
        try:
                file = open("tasks.txt", "r")
        except IOError as e:
                print(str(e))
                sys.exit(1)

        #to read all the lines from the file and store them in list
        tasks = file.readlines()
        tasks = [task.strip() for task in tasks]
       
        digit = int(args[2])-1
        tasks.pop(digit)        #to remove the item from the list
        print("Deleted todo #{}".format(args[2]))

        #updating the tasks.txt file
        file = open("tasks.txt", "w")
        tasks = [task + "\n" for task in tasks]
        file.writelines(tasks)
        file.close()
        
#to view what's in the list       
elif command == "ls":
        try:
                file = open("tasks.txt", "r")
        except IOError as e:
                print(str(e))
                sys.exit(1)
                
        tasks = file.readlines()
        if len(tasks) == 0:
                print("there are no tasks!")
        else:
                tasks = [task.strip() for task in tasks]
                tasks = tasks[::-1]
                j=len(tasks)
                for i in range(len(tasks)):
                        content = tasks[i]
                        print("[{0}] {1}".format(j, content))
                        j=j-1

        file.close()

        
elif command == "help":
        print("Usage :- ")
        print("todo.py add `todo item` # Add a new todo")
        print("todo.py ls              # show remaining todos")
        print("todo.py del NUMBER      # Delete a todo")
        print("todo.py done NUMBER     # Complete a todo")
        print("todo.py help            # Show usage")
        print("todo.py report          # Statistics")
        sys.exit(1)

#to mark the items as done and delete them from the tasks file and append in done.txt file       
elif command == "done":
        try:
                file = open("tasks.txt", "r")
                f = open("done.txt", "r")
        except IOError as e:
                print(str(e))
                sys.exit(1)
        
        tasks = file.readlines()
        tasks = [task.strip() for task in tasks]
        
        digit = int(args[2])-1
        value = tasks[digit]
        date_object = datetime.date.today()
        insert = "x "+str(date_object)+" " +value

        #updating the done.txt file
        f = open("done.txt", "a")
        f.write(insert +"\n")
        f.close()
        
        tasks.pop(digit)
        
        print("Marked todo #{} as done.".format(args[2]))

        #updating the tasks.txt file
        file = open("tasks.txt", "w")
        tasks = [task + "\n" for task in tasks]
        file.writelines(tasks)
        file.close()

        
#to get the report 
elif command == "report":
        try:
                file = open("tasks.txt", "r")
                f = open("done.txt", "r")
        except IOError as e:
                print(str(e))
                sys.exit(1)
        
        tasks = file.readlines()
        tasks = [task.strip() for task in tasks]

        
        done = f.readlines()
        done = [t.strip() for t in done]
        
        #for showing date and time
        d = datetime.datetime.now() 
        date = str(d.day)+"/"+str(d.month)+"/"+str(d.year)
        print("{0} Pending : {1} Completed : {2}".format(date,len(tasks), len(done)))
        
else:
        print("invalid command!")
