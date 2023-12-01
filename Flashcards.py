from tkinter import *
import customtkinter as ctk
from main import flashcards

currentSet = []
flashcardSets = []
clicked_set =""

def clearFrame():
    for widgets in frame.winfo_children():
        widgets.destroy()

def nextCardButton():
    pass

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

  
def previousCardButton():
    pass

def flipCardButton():
    pass

def chooseSet():

    clearFrame()

    sets = flashcards.call_files()
    clicked_set = StringVar()
    clicked_set.set(sets[0])
    # Create Dropdown menu 
    drop = ctk.CTkComboBox( frame , variable= clicked_set , values=sets ) 
    drop.pack() 

    clicked_set.set(str(drop))

    # clicked_set = ctk.CTkOptionMenu(master=frame,
    #                                    values=sets,
    #                                    command=optionmenu_callback,
    #                                    variable=clicked_set)
    
    print(clicked_set.get())
    back_To_Menu = ctk.CTkButton(master = frame, text = "back to main menu", command = mainMenu)
    back_To_Menu.place(relx =.5, rely =.7, anchor= CENTER)
    select_set = ctk.CTkButton(master = frame, text = "continue with selected set", command =learn_flashCards )
    select_set.place(relx =.5, rely = .8, anchor = CENTER)
    
    

def createNewSet():
    cards = flashcards("ds", "sd", 0).create_New_Set("set 1")
    print(cards)

def mainMenu():
    clearFrame()
    frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
    title = ctk.CTkLabel(master=frame, text="Flashcards", width=150, height=25, font=('Papyrus', 50))
    title.place(relx=0.5, rely=0.10, anchor=CENTER)
    newSet = ctk.CTkButton(master=frame, text="Create Set", command=createNewSet)
    newSet.place(relx=0.5, rely=.5, anchor=CENTER)
    pickSet = ctk.CTkButton(master= frame, text = "Choose existing set", command=chooseSet)
    pickSet.place(relx =.5, rely =.7, anchor= CENTER)
    
def interface():
    nextCard = ctk.CTkButton(master=frame, text="Next Card", command=nextCardButton)
    nextCard.place(relx=0.3, rely=0.5, anchor=CENTER)

    previousCard = ctk.CTkButton(master=frame, text="Previous Card", command=previousCardButton)
    previousCard.place(relx=0.1, rely=0.5, anchor=CENTER)

    flipCard = ctk.CTkButton(master=frame, text="Flip Card", command=flipCardButton)
    flipCard.place(relx=0.5, rely=0.5, anchor=CENTER)

    menu = ctk.CTkButton(master=frame, text="Main Menu", command=mainMenu)
    menu.place(relx=0.75, rely=0.5, anchor=CENTER)
def learn_flashCards():
    clearFrame()
    print(clicked_set)



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

    mainMenu()

    root.mainloop()

if __name__ == "__main__":
    main()



