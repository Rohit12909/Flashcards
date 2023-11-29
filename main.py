# import cards
import pickle


class flashcards:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition
    def __str__(self):
        return self.term+ ' ' +self.definition
    




flash_cards = []


exit = False 

# while exit == False:
file_number = 0
file_name = "testFile" + str(file_number) + ".txt"
gate = 1
with open (file_name, "a") as file1:
    while gate == 1:
        term = input("enter a term")
        definition = input("enter the definition")
        file1.write(term + "*"+ definition)
        gate = input("enter 0 to escape, enter 1 to continue entering terms/definition")

        



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



