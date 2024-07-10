#tkinter try
import tkinter as tk
import requests


root = tk.Tk()
root.title("notify system")
root.geometry("300x200")

def button_click():
    #tokenとenrtyを入手．
    token = entry_token.get()
    message = entry_text.get("1.0", tk.END).strip()
    line_header  = {
    'Content-Type' : 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer' + ' ' + token }
    line_message = 'message=' + message 
    req = requests.post('https://notify-api.line.me/api/notify', headers = line_header, data = line_message)
    req.close()


label_token = tk.Label(text="enter your token")
entry_token = tk.Entry(width=26)
label_notify = tk.Label(text="enter notification")
entry_text = tk.Text(width=30,height=5)
button = tk.Button(text="SEND",width=10,command=button_click)

label_token.place(x=55,y=15)
entry_token.place(x=55,y=40)
label_notify.place(x=55,y=65)
entry_text.place(x=55,y=87)
button.place(x=105,y=165)


root.mainloop()

