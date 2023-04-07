from tkinter import *
import requests
# GUI
root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

def get_chat():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)
    
    URL = "https://api.openai.com/v1/chat/completions"
    message = e.get().lower()

    open_ai_key = # Personal open AI
    payload = {
        "model":"gpt-3.5-turbo",
        "messages":[{"role":"user","content":message}],
        "temperature":1,
        "top_p":1,
        "n":1,
        "stream":False,
        "presence_penalty":0.0,
        "frequency_penalty":0.0,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {open_ai_key}",
    }   
    
    response = requests.request("POST", URL, headers=headers, json=payload)
    data = response.json()
    quote = data['choices'][0]['message']['content']
      
    # inserts new data into the TextBox
    txt.insert(END, "\n" + "Bot -> "+quote)
    e.delete(0, END)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=get_chat).grid(row=2, column=1)

root.mainloop()
