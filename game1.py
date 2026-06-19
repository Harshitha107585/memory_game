import tkinter as tk
from PIL import Image, ImageTk
import random

cards = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
random.shuffle(cards)

buttons = []
first = None
second = None
lock = False

def on_click(index):
    global first, second, lock
    if lock:
        return

    btn = buttons[index]
    btn.config(text=cards[index])

    if first is None:
        first = index
    elif second is None and index != first:
        second = index
        lock = True
        root.after(1000, check_match)

def check_match():
    global first, second, lock

    if cards[first] == cards[second]:
        buttons[first].config(state="disabled")
        buttons[second].config(state="disabled")
    else:
        buttons[first].config(text="?")
        buttons[second].config(text="?")

    first = None
    second = None
    lock = False

    
root = tk.Tk()
root.title("Memory Matching Game")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = screen_width // 2
window_height = screen_height // 2
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

start_frame = tk.Frame(root)
start_frame.pack(fill = "both",expand =True)

bg_image = Image.open("bg.jpg")
bg_image = bg_image.resize((window_width,window_height))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(start_frame,image = bg_photo)
bg_label.place(x=0,y=0,relwidth =1,relheight=1)
# prevent python from deleting the image
bg_label.image = bg_photo

start_label = tk.Canvas(start_frame,width=window_width,height=window_height,highlightthickness=0 )
start_label.pack(fill = "both",expand = True)
start_label.create_image(0,0,image=bg_photo,anchor = 'nw')
start_label.create_text(
    window_width // 2,
    window_height // 3,
    text="Welcome to Memory Game!",
    font=("Comic Sans MS", 36, "bold"),
    fill="black"
)



def start_game():
    start_frame.pack_forget() 
    game_canvas.pack(fill ="both",expand = True)          

start_button = tk.Button(
    start_frame,
    text="Start",
    font=("Comic Sans MS", 20, "bold"),  
    fg="black", 
    bg="#7FDC83",  
    activebackground="#7FDC83",  
    activeforeground="black",  
    bd=5,  
    relief="raised", 
    command=start_game
)
start_label.create_window( window_width // 2,window_height // 2,window=start_button)

game_canvas = tk.Canvas(
    root,
    width=window_width,
    height=window_height,
    highlightthickness=0
)


game_bg_img = Image.open("game_bg.jpg")
game_bg_img = game_bg_img.resize((window_width, window_height))
game_bg_photo = ImageTk.PhotoImage(game_bg_img)

game_canvas.create_image(0, 0, image=game_bg_photo, anchor="nw")
game_canvas.image = game_bg_photo

cols = 4
rows = 4
card_w = 70
card_h = 70
gap = 30

grid_width = cols * card_w + (cols - 1) * gap
grid_height = rows * card_h + (rows - 1) * gap

start_x = (window_width - grid_width) // 2
start_y = (window_height - grid_height) // 2



for i in range(16):
    btn = tk.Button(root, text="?", width=6, height=3,font=("Arial",16,"bold"),bg="#64E664",      
    fg="black",         
    activebackground="#13E11A",  
    activeforeground="Black",
                    command=lambda i=i: on_click(i))
    
    x = start_x + (i % cols) * (card_w + gap) + card_w // 2
    y = start_y + (i // cols) * (card_h + gap) + card_h // 2

    game_canvas.create_window(x, y, window=btn)
    
   
    buttons.append(btn)

root.mainloop()
