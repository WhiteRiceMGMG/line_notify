import tkinter as tk
import requests

class Application():
    def __init__(self, master):
        self.master = master
        self.master.title("notify system") 
        self.master.geometry("300x200")  
        self.widget()

    def widget(self):
        # ウィジェットの作成
        self.label_token = tk.Label(text="enter your token")
        self.entry_token = tk.Entry(width=26)
        self.label_notify = tk.Label(text="enter notification")
        self.entry_text = tk.Text(width=30, height=5)
        self.button = tk.Button(text="SEND", width=10, command=self.button_click)

        # ウィジェットの配置
        self.label_token.place(x=55, y=15)
        self.entry_token.place(x=55, y=40)
        self.label_notify.place(x=55, y=65)
        self.entry_text.place(x=55, y=87)
        self.button.place(x=105, y=165)

    def button_click(self):
        token = self.entry_token.get()
        message = self.entry_text.get("1.0", tk.END).strip()
        line_header  = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Bearer ' + token
        }
        line_message = {'message': message}
        req = requests.post('https://notify-api.line.me/api/notify', headers=line_header, data=line_message)
        req.close()

def main():
    root = tk.Tk()
    app = Application(master=root)
    root.mainloop()

if __name__ == "__main__":
    main()
