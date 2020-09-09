from tkinter import *
import requests
import json
from threading import Thread


background_color = "#1A1A1A"


window = Tk()
window.title("OG-Times User Informator 0.1")
window.geometry("735x575")
window.resizable(False,False)
window.configure(bg=background_color)
text_color = "#00ff00"
text_background = "#001a00"
button_bg = "#111111"  
label_bg = "#009900"

# Label

label_1 = Label(window, font=("Liberation Mono",15), bg=background_color, text="Username:", fg=text_color)
label_1.place(x=10, y=15)

label_2 = Label(window, width=30, font=("Liberation Mono",13), bg=label_bg, text="Username", fg="white")
label_2.place(x=10, y=65)

label_3 = Label(window, width=71, font=("Liberation Mono",13), bg=label_bg, text="Huge database search", fg="white")
label_3.place(x=10, y=320)

label_4 = Label(window, width=25, font=("Liberation Mono",13), bg=label_bg, text="Logs", fg="white")
label_4.place(x=325, y=192)


# Entry

entry_1 = Entry(window, borderwidth=0, highlightbackground=text_color,  width=59, fg=text_color, bg=text_background, font=("Liberation Mono",13))
entry_1.place(x=128, y=15)

# Text

text_1 = Text(window, width=30, height=10, borderwidth=0, highlightbackground=text_color,  fg=text_color, bg=text_background, font=("Liberation Mono",13))
text_1.place(x=10, y=90)

text_2 = Text(window, width=71, height=10, borderwidth=0, highlightbackground=text_color,  fg=text_color, bg=text_background, font=("Liberation Mono",13))
text_2.place(x=10, y=345)

text_3 = Text(window, width=25, height=4, borderwidth=0, highlightbackground=text_color,  fg=text_color, bg=text_background, font=("Liberation Mono",13))
text_3.place(x=325, y=216)




def clear():
    text_1.delete("1.0",END)
    text_2.delete("1.0",END)
    text_3.delete("1.0",END)
    entry_1.delete(0,END)

def cerere_server():
    username = entry_1.get().split()[0]
    text_3.insert(INSERT, "\n Online mode started\n User is {}\n".format(username))

    if len(username) < 3:
        print("Contul nu permite decat 3 caractere")
    else:
        proxies = {
                "http":"209.127.191.180:80"
            }

        url = "https://earthpanel.og-times.ro/search?name=" + username
        response = requests.get(url, proxies=proxies)
        if response.status_code != 200:
            text_3.insert(INSERT, " Status Status: 200\n")

        else:
            text_3.insert(INSERT, " Status Status: {}\n".format(response.status_code))
            data = response.json()
            
            users_usernames = []
            for users in data:
                username = users["nickname"]
                level = users["level"]
                text_1.insert(INSERT, "[{}] {}\n".format(level,username))
                users_usernames.append(username)            
        
            for user in users_usernames:
                file = open("users.txt", "r").readlines()
                for rand in file:
                    splited = rand.replace("'","").split(',')
                    if user in splited[0]:
                        text_2.insert(INSERT, "\n PanelUsername: {}\n Username: {}\n Password: {}\n ".format(user, splited[0], splited[1]))  

                
# Button

button_1 = Button(window, text="Clear", borderwidth=0, fg=text_color,  highlightbackground=text_color , bg=button_bg, width=37, font=("Liberation Mono",13), command=clear)

button_1.place(x=325, y=145)

button_2 = Button(window, text="Online Search", borderwidth=0, fg=text_color,  highlightbackground=text_color , bg=button_bg, width=37, font=("Liberation Mono",13), command=lambda : Thread(target=cerere_server).start())
button_2.place(x=325, y=65)

window.mainloop()

