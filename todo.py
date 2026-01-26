# return elements from text file as list
def read_file():
     with open("todos.txt", "r") as file :
            return file.readlines()

# writes the argument to files as todos   
def writeto_file(todos):
    with open("todos.txt","w") as file:
        file.writelines(todos)



while True :

    user_prompt= input("Enter prompts: add <your-todos>, show, edit <todos-index>, complete <todos-index>, or exit: ")
    user_prompt = user_prompt.strip()

    parts= user_prompt.split(maxsplit=1)
    
    command= parts[0]
    argument = parts[1] if len(parts)>1 else ""

    if "add" == command :
        
        todos = argument + "\n"  
        todo = read_file()                   
        
        todo.append(todos.title())                     
        
        writeto_file(todo)

        print("The todo is added\n")

    elif "show" == command :
                
            todos_list=  read_file()           
            todos= [w.strip("\n") for w in todos_list] 

            for i, list_element in enumerate(todos, start=1):      
                print(i, list_element)     

    elif "edit" == command :
        try:
            ndx= int(argument)
            ndx= ndx-1

            todos=  read_file()
            
            new_todos = input("Enter new todo: ")
            todos[ndx]= new_todos.title() +'\n'

            writeto_file(todos)
            
            print(f"The todo no {ndx+1} was changed type 'show' to see.\n")

        except ValueError:
            print("Invalid syntax please try again:\n")
            continue
        except IndexError:
            print("Invalid index please try again:\n")
            continue

    elif "complete" == command :
        try:
            ndx= int(argument)
            ndx= ndx-1
            
            todos=  read_file()
            
            removed_todo= todos[ndx]
            todos.pop(ndx)

            writeto_file(todos)
             
            print(f'The todo-item "{removed_todo.strip()}" was removed from the list \n')

        except ValueError:
            print("Invalid syntax please try again")
            continue
        except IndexError:
            print("Invalid index please try again:\n")
            continue

    elif "exit" == command :
        break

    else :
        print("Invalid prompt \n valid ones are add, show, edit, delete, or exit")    