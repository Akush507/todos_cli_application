while True :

    user_prompt= input("Enter prompts: add <your-todos>, show, edit <todos-index>, complete <todos-index>, or exit: ")
    user_prompt = user_prompt.strip()

    parts= user_prompt.split(maxsplit=1)
    
    command= parts[0]
    argument = parts[1] if len(parts)>1 else ""

    if "add" == command :
        
        todos = argument + "\n"
        
        with open("todos.txt", "r") as file :
            todo = file.readlines()                   
        
        todo.append(todos.title())                     
        
        with open("todos.txt", "w") as file :
            file.writelines(todo)

        print("The todo is added\n")

    elif "show" == command :
        with open('todos.txt', 'r') as file :      
            todos_list= file.readlines()         
        
        todos= [w.strip("\n") for w in todos_list] 

    
        for i, list_element in enumerate(todos, start=1):      
            print(i, list_element) 
        
    elif "edit" == command :
        ndx= int(argument)
        ndx= ndx-1

        with open("todos.txt", "r") as file :
            todos= file.readlines()
        
        new_todos = input("Enter new todo: ")
        todos[ndx]= new_todos.title() +'\n'

        with open('todos.txt', 'w') as file :
            file.writelines(todos)
        
        print(f"The todo no {ndx+1} was changed type 'show' to see.\n")

    elif "complete" == command :
        
        ndx= int(argument)
        ndx= ndx-1
        
        with open('todos.txt','r') as file :
            todos= file.readlines()
        
        removed_todo= todos[ndx]
        todos.pop(ndx)

        with open('todos.txt','w') as file :
            file.writelines(todos)
        
        print(f'The todo-item "{removed_todo.strip()}" was removed from the list \n')

    elif "exit" == command :
        break

    else :
        print("Invalid prompt \n valid ones are add, show, edit, delete, or exit")    