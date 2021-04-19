from tkinter import *


margin = 15
start = 450
dol = 150

root = Tk()
root.title("E")
width = 1025
height = 550
root.geometry("1025x550")
c = Canvas(root, width=width, height=height, bg="black")


def draw(i, max, x, color, interest):
    if i <= max:
        size = 15
        x = x
        y = start - i * size
        c.create_text(x - 10, start + 5, anchor=NW, font="Arial",
                      text=f"{interest}", fill="white")
        c.create_rectangle(x, y, x - 20, y - size, fill=color, outline=color)
        print(x, y, x - 20, y - size)
        c.after(100, lambda: draw(i + 1, max, x, color, interest))

n_paying_interest = [1, 2, 3, 4, 6, 12, 24, 48, 182, 365]
colors = ['MediumPurple1', 'MediumPurple2', 'MediumPurple3', 'MediumPurple4', 'purple', 'violet red', 'VioletRed3',
          'medium violet red', 'VioletRed2', 'pale violet red']
print(len(colors))
limit = 0
s = 1  # доллар

for i in range(0, 10):
    interest = n_paying_interest[i]
    m = (1 + 1 / interest) ** interest
    summa = s * m
    if (summa) > limit:
        limit = s * m

    draw(0, summa * 10, 100 * i + 100, colors[i], interest)

c.create_text(350, 525, anchor=W, font="Arial",
              text=f"Аппроксимация экспоненты: {limit}", fill="fuchsia")
c.create_text(800, 485, anchor=NW, font="Arial",
              text="Кол-во начислений % в год", fill="white")
c.create_text(margin, 485, anchor=NW, font="Arial",
              text="Доллар", fill="white")
c.create_text(margin, margin, anchor=NW, font="Arial",
              text="\n сложная ставка 100% годовых \n Якоб Бернулли", fill="white")

print(limit)
c.create_rectangle(margin, dol - 15, width - margin, dol - 15, fill="fuchsia", outline="fuchsia")
c.create_rectangle(margin, start - (start - dol + 15) / 2, width - margin, start - (start - dol + 15) / 2,
                   fill="fuchsia",
                   outline="fuchsia")
c.create_rectangle(margin, start, width - margin, start, fill="fuchsia", outline="fuchsia")
c.pack()
root.mainloop()
