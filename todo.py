Todo_list= [] # Declated a empty list

while True :

    user_prompt= input("enter add. show, edit, delet, or exit: ")

    match user_prompt :
        case "add" :
            todos= input("write your things to do: ")
            Todo_list.append(todos)
        
        case "show" :
            print(Todo_list)

        case "exit" :
            break

        