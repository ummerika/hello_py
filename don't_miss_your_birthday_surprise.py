import tkinter as tk
import random
import time
import threading
import math

root = tk.Tk()
root.title("The Magic Birthday Sky")
root.geometry("800x600")
root.config(bg="black")

canvas = tk.Canvas(root, width=800, height=600, bg="black", highlightthickness=0)
canvas.pack()

stars = []
for _ in range(60):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    s = canvas.create_oval(x, y, x+2, y+2, fill="white", outline="")
    stars.append(s)

def twinkle_stars():
    while True:
        for s in stars:
            color = random.choice(["#ffffff", "#ffe5b4", "#fffacd", "#b0e0e6"])
            canvas.itemconfig(s, fill=color)
        canvas.update()
        time.sleep(0.2)

balloons = []
colors = ["#FF6B6B", "#FFD93D", "#6BCB77", "#4D96FF", "#F473B9", "#E36414"]

def create_balloons():
    for _ in range(10):
        x = random.randint(50, 750)
        y = random.randint(550, 650)
        color = random.choice(colors)
        b = canvas.create_oval(x, y, x+40, y+60, fill=color, outline="")
        balloons.append(b)

def animate_balloons_up():
    for _ in range(220):
        for b in balloons:
            canvas.move(b, 0, -3)
            x, y, _, _ = canvas.coords(b)
            if y < -60:
                canvas.move(b, 0, 650)
        canvas.update()
        time.sleep(0.03)

def type_text(text, x, y, color="#FFD93D", size=38, delay=0.1):
    text_id = canvas.create_text(x, y, text="", fill=color, font=("Comic Sans MS", size, "bold"))
    full = ""
    for ch in text:
        full += ch
        canvas.itemconfig(text_id, text=full)
        canvas.update()
        time.sleep(delay)
    return text_id

def fireworks():
    for _ in range(5):
        x = random.randint(100, 700)
        y = random.randint(150, 350)
        color = random.choice(colors)
        for r in range(5, 60, 5):
            c = canvas.create_oval(x-r, y-r, x+r, y+r, outline=color)
            canvas.update()
            time.sleep(0.03)
            canvas.delete(c)
        time.sleep(0.3)
def animate_scene():
    create_balloons()

    threading.Thread(target=twinkle_stars, daemon=True).start()

    animate_balloons_up()

    type_text("🎉 Happy Birthday 🎉", 400, 250, "#FFD93D", 40, 0.1)
    time.sleep(1)
    type_text("Wishing you a sky full of dreams", 400, 310, "#00FFAA", 20, 0.05)
    time.sleep(1.5)

    fireworks()

    animate_balloons_up()
    canvas.delete("all")
    type_text("💫 May your year sparkle with joy 💫", 400, 300, "#FFB6C1", 30, 0.08)
    time.sleep(2)
    canvas.delete("all")

def start_animation():
    threading.Thread(target=animate_scene, daemon=True).start()

start_btn = tk.Button(
    root, text="🎁 Begin the Magic 🎁",
    font=("Comic Sans MS", 16, "bold"),
    bg="#FFD93D", fg="black",
    relief="flat", padx=15, pady=8,
    command=start_animation
)
start_btn.place(relx=0.5, rely=0.9, anchor="center")

root.mainloop()



