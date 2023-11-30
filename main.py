# import cards
import os
import pickle
import customtkinter as ctk
global file_number


file_number = 0


#loop that allows user to create flashcard sets that store the terms and definitions to a text file 

class flashcards:
    def __init__(self, term, definition, file_number):
        self.term = term
        self.definition = definition  
        self.file_number = file_number      
    def __str__(self):
        return self.term+ ' ' +self.definition
    def create_New_Set(self, name):
        file_name = str(name) + str(file_number) + ".txt"
        gate = 1
        with open (file_name, "a") as file1:
            while gate == 1:
                term = input("enter a term: ")
                definition = input("enter the definition: ")
                file1.write(term + "*"+ definition)
                file1.write("\n")
                gate = int(input("enter 0 to escape, enter 1 to continue entering terms/definition: "))
            file1.flush()
            self.file_number += 1
            file1.close() 
    def call_files():
            #reads all the files in the folder 
        # folder path
        dir_path = r'C:/Users/Admin/Desktop/repos/Flashcard/Flashcards/Sets'

        # list to store files
        res = []

        # Iterate directory
        for path in os.listdir(dir_path):
            # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                res.append(path)
        print(res)










flash_cards = []


exit = False 

# while exit == False:
     



# file1 = open("testFile.txt", "r")
# Lines = file1.readlines()
# x = len(file1.readlines())
# for line in Lines:
#     string = line
#     words = string.split('*') 
#     print(words[1])
#     flash_cards.append(flashcards(words[0], words[1]))
# # with open("testFile.txt", "a") as file1:
# #     # Writing data to a file
# #     file1.write(flashCard1.term)
# #     file1.write(" ")
# #     file1.write(flashCard1.definition)
# for element in flash_cards:
#     print(element.term)
#     print(element.definition)



