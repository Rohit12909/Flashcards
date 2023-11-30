from tkinter import *
import customtkinter as ctk
from main import flashcards

currentFile = ""


def clearFrame():
    for widgets in frame.winfo_children():
        widgets.destroy()

def nextCardButton():
    pass

def previousCardButton():
    pass

def flipCardButton():
    pass

def chooseSet():
    flashcards.call_files()

def createNewSet():
    setNameLabel = ctk.CTkLabel(frame, text="Set Name")
    setNameLabel.place(relx=0.37, rely=0.25)

    setNameVar = ctk.StringVar()
    setName = ctk.CTkEntry(frame, textvariable=setNameVar)
    setName.place(relx=0.45, rely=0.25)

    currentFile = str(setName.get())

    print(currentFile)

def saveToSet(term, definition):
    cards.create_New_Card(currentFile, term.get(), definition.get())
    term.delete(0, 'end')
    definition.delete(0, 'end')

def add_To_Set():
    clearFrame()
    cards.filename = currentFile

    termLabel = ctk.CTkLabel(frame, text="Term")
    termLabel.place(relx=0.4, rely=0.35)

    termVar = ctk.StringVar()
    term = ctk.CTkEntry(frame, textvariable=termVar)
    term.place(relx=0.45, rely=0.35)

    defLabel = ctk.CTkLabel(frame, text="Definition")
    defLabel.place(relx=0.37, rely=0.45)

    defVar = ctk.StringVar()
    definition = ctk.CTkEntry(frame, textvariable=defVar)
    definition.place(relx=.45, rely=0.45)
    #cards.term.place(relx=0.5, rely=0.35, anchor=CENTER)

    saveSet = ctk.CTkButton(master=frame, text="Save Set", command=lambda:saveToSet(term, definition))
    saveSet.place(relx=0.75, rely=0.75, anchor=CENTER)

    backToMenu = ctk.CTkButton(master=frame, text="Return to Main Menu", command=mainMenu)
    backToMenu.place(relx=0.5, rely=0.75, anchor=CENTER)


def mainMenu():
    clearFrame()
    frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    title = ctk.CTkLabel(master=frame, text="Flashcards", width=150, height=25, font=('Papyrus', 50))
    title.place(relx=0.5, rely=0.10, anchor=CENTER)

    newSet = ctk.CTkButton(master=frame, text="Create Set", command=createNewSet)
    newSet.place(relx=0.5, rely=.75, anchor=CENTER)

    pickSet = ctk.CTkButton(master= frame, text = "Choose existing set", command=chooseSet)
    pickSet.place(relx =.5, rely =.9, anchor= CENTER)

    addToSet = ctk.CTkButton(master=frame, text="Add to Set", command=add_To_Set)
    addToSet.place(relx=0.7, rely=0.75, anchor=CENTER)

    
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
    global root, frame, cards

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

    cards = flashcards("ds", "sd", 0, frame, "default")

    mainMenu()

    root.mainloop()

if __name__ == "__main__":
    main()



