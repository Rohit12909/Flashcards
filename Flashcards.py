from tkinter import *
import customtkinter as ctk



def clearFrame():
    for widgets in frame.winfo_children():
        widgets.destroy()

def nextCardButton():
    pass

def previousCardButton():
    pass

def flipCardButton():
    pass

def mainMenu():
    clearFrame()
    frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    title = ctk.CTkLabel(master=frame, text="Flashcards", width=150, height=25, font=('Papyrus', 50))
    title.place(relx=0.5, rely=0.10, anchor=CENTER)

def interface():
    nextCard = ctk.CTkButton(master=frame, text="Next Card", command=nextCardButton)
    nextCard.place(relx=0.3, rely=0.5, anchor=CENTER)

    previousCard = ctk.CTkButton(master=frame, text="Previous Card", command=previousCardButton)
    previousCard.place(relx=0.1, rely=0.5, anchor=CENTER)

    flipCard = ctk.CTkButton(master=frame, text="Flip Card", command=flipCardButton)
    flipCard.place(relx=0.5, rely=0.5, anchor=CENTER)

    menu = ctk.CTkButton(master=frame, text="Main Menu", command=mainMenu)
    menu.place(relx=0.75, rely=0.5, anchor=CENTER)

def main():
    global root, frame

    root = ctk.CTk()
    frame = ctk.CTkFrame(root)
    frame.pack(side="top", expand=True, fill="both")
    root.title('Flashcards')
    root.geometry("800x500")
    root.resizable(width=1000, height=500)
    #root.configure(bg=bgColor)
    root.grid_rowconfigure(0, weight=3)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)

    interface()

    root.mainloop()

if __name__ == "__main__":
    main()



