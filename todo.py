while True :

    user_prompt= input("Enter prompts: add, show, edit, complete, or exit: ")
    user_prompt = user_prompt.strip()

    match user_prompt :
        case "add" :
            
            todos = input("Enter your todos: ") + "\n"  
            
            with open("todos.txt", "r") as file :
                todo = file.readlines()                   
            
            todo.append(todos.title())                     
            
            with open("todos.txt", "w") as file :
                file.writelines(todo)

            print("The todo is added\n")

        case "show" :
            with open('todos.txt', 'r') as file :      
                todos_list= file.readlines()         
            
            todos= [w.strip("\n") for w in todos_list]      
            
            for i, list_element in enumerate(todos, start=1):      
                print(i, list_element) 

            print("\n")

        case "edit" :
            ndx= int(input("Number of todo items to edit: "))
            ndx= ndx-1

            with open("todos.txt", "r") as file :
                todos= file.readlines()
            
            new_todos = input("Enter new todo: ")
            todos[ndx]= new_todos.title() +'\n'

            with open('todos.txt', 'w') as file :
                file.writelines(todos)
            
            print(f"The todo no {ndx+1} was changed type 'show' to see.\n")

        case "complete" :
            
            ndx= int(input("Enter number of todo items you completed: "))
            ndx= ndx-1
            
            with open('todos.txt','r') as file :
                todos= file.readlines()
            
            removed_todo= todos[ndx]
            todos.pop(ndx)

            with open('todos.txt','w') as file :
                file.writelines(todos)
            
            print(f'The todo-item "{removed_todo.strip()}" was removed from the list \n')

        case "exit" :
            break

        case _:
            print("Invalid prompt \n valid ones are add, show, edit, delete, or exit")    