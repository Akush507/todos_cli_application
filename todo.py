Todo_list= [] # Declated a empty list

while True :

    user_prompt= input("enter prompts: add. show, edit, delete, or exit: ")

    match user_prompt :
        case "add" :
            todos= input("write your things to do: ")
            Todo_list.append(todos.title())
        
        case "show" :
            print("-" *50)
            for i in range(0, len(Todo_list)):
                print(f"{i+1}. {Todo_list[i]}")
            print("-" *50)

        case "delete" :
            ndx= int(input("enter index of todo items "))

            if 1 <= ndx <= len(Todo_list): 
                Todo_list.pop(ndx-1)
                print("deleted")

            else :
                print(f"invalid index index cant be greater than length of list")

        case "edit" :
            ndx= int(input("index of todo items to edit: "))

            if 1 <= ndx <= len(Todo_list) :
                newtodo= input("change your todo: ")
                Todo_list[ndx-1]=newtodo.title()

            else:
                print("Invalid index")

        case "exit" :
            break

        case _:
            print("Invalid prompt \n valid ones are add, show, edit, delete, or exit")

        