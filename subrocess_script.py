from subprocess import Popen, CREATE_NEW_CONSOLE
import time



def sub_console():
    p_list = []
    try:
        p_list.append(Popen("python server_message.py", creationflags=CREATE_NEW_CONSOLE))
    except:
        pass

    while True:
        user = input("Create 5 clients - 's'\nDestroy - 'x'\nEscape - 'q'" )
        
        if user == "q":
            break
        elif user == "s":
            for i in range(5):
                time.sleep(1)
                p_list.append(Popen("python client_messege.py", creationflags=CREATE_NEW_CONSOLE))
            print("5 consoles started")
        elif user == "x":
            for p in p_list:
                p.kill()
            p_list.clear()  

if __name__ == "__main__":
    sub_console()
    
