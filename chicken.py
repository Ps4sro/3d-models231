
import random
import tkinter as tk

class Pet:
    def __init__(self, window):
        self.window = window
        self.x = 800
        self.cycle = 0
        self.check = 1
        self.event_number = random.randrange(1, 3, 1)

        # GIF frames
        self.idle_frames = [tk.PhotoImage(file='idle.gif', format=f'gif -index {i}') for i in range(2)]
        self.walk_frames = [tk.PhotoImage(file='walk.gif', format=f'gif -index {i}') for i in range(8)]

        # Window configuration
        self.window.config(highlightbackground='black')
        self.window.overrideredirect(True)
        self.window.wait_visibility(window)
        self.window.wm_attributes('-alpha', 0.1)

        self.label = tk.Label(window, bd=0, bg='black')
        self.label.pack()

        self.update()

    def gif_work(self, cycle, frames, first_num, last_num):
        if cycle < len(frames) - 1:
            cycle += 1
        else:
            cycle = 0
            self.event_number = random.randrange(first_num, last_num + 1, 1)
        return cycle

    def update(self):
        if self.event_number == 1:
            frame = self.idle_frames[self.cycle]
            self.cycle = self.gif_work(self.cycle, self.idle_frames, 1, 2)
        elif self.event_number == 2:
            frame = self.walk_frames[self.cycle]
            self.cycle = self.gif_work(self.cycle, self.walk_frames, 1, 2)
            self.x -= 3

        self.window.geometry(f'100x100+{self.x}+800')
        self.label.configure(image=frame)
        self.window.after(100, self.update)

if __name__ == "__main__":
    window = tk.Tk()
    pet = Pet(window)
    window.mainloop()
