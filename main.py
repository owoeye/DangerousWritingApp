import re
from tkinter import *

TIME = 60


class WritingApp:
    def __init__(self, writing_app):
        # creating GUI
        self.writing_app = writing_app
        self.writing_app.title("Dangerous Writing App")
        self.writing_app.config(bg="white")
        # window size
        self.writing_app.geometry("800x600")
        # Set default font for all widgets
        self.writing_app.option_add("*font", "helvetica 12")
        # create writing area
        self.text_box = Text(self.writing_app, placeholder="...", bd=0)
        self.text_box.insert("1.0", "Start Writing ...")
        self.text_box.place(relx=0.5, rely=0.6, anchor=CENTER, relheight=1)

        # create word count
        self.wordcount = Label(self.writing_app, text="0 words", bg="white")
        self.wordcount.place(relx=0.5, rely=0.05)

        # timer variable
        self.time = TIME
        # create Timer
        self.timerOfLabel = Label(self.writing_app, text=f"{self.time // 60:02d}:{self.time % 60:02d}", bg="white")
        self.timerOfLabel.place(relx=0.8, rely=0.05, anchor=N)
        # after some time
        self.timer_id = self.writing_app.after(1000, self.update_timer, self.time)
        # recognize keystrokes
        self.writing_app.bind("<Key>", self.reset_timer)
        # create RETRY button
        self.retryButton = Button(self.writing_app)
        self.retryButton.pack_forget()

    def reset_timer(self, event):
        # wordcount
        words = self.text_box.get('1.0', 'end-1c')
        self.wordcount.config(text=f'{len(words.split())} words')
        # time
        self.time = TIME
        self.writing_app.after_cancel(self.timer_id)  ## cancel old after event based on id
        self.update_timer(self.time)

    def update_timer(self, time):
        time -= 1
        if TIME >= time > 0:
            self.timerOfLabel.configure(text=f"{time // 60:02d}:{time % 60:02d}")
            self.timer_id = self.writing_app.after(1000, self.update_timer, time)
        else:
            self.stop()

    def stop(self):
        self.writing_app.after_cancel(self.timer_id)  ## stop timer
        self.text_box.delete("1.0", "end")  ## clear textbox
        self.text_box.place_forget()  ## hide widgets not in use
        # Show button for reply
        self.retryButton.configure(text="RETRY", height=2, width=20, command=self.restart, font=("helvetica", 32, "bold"))
        self.retryButton.place(relx=0.5, rely=0.3, anchor=CENTER)

    def restart(self):

        self.retryButton.place_forget() ## hide retry widgets and retry button
        # reset up
        self.text_box.insert("1.0", "Start Writing ...")  ## reinsert starting text
        self.text_box.place(relx=0.5, rely=0.6, anchor=CENTER, relheight=1)
        self.time = TIME
        self.update_timer(self.time)


if __name__ == "__main__":
    writing_app = Tk()
    app = WritingApp(writing_app)
    writing_app.mainloop()
