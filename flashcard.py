import json

class Teacher:
    @staticmethod #make a variabl;e pitsode s,mt else
    def flashcardmaker():
        try:
            with open("flashcards.json", "r") as file:
                flashcards = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError): #wats gonna happen if its emptty
            flashcards = {}

        while True:
            word = input("en5ter word for flashcard or type exit to quit: ")
            if word.lower() == 'exit': #lower makes it so its casw sensitive truns unto all lowercase
                break
            answer = input("Enter answer for flashcard: ")
            flashcards[word] = answer

            with open("flashcards.json", "w") as file:  #r means read, read whats inside of json
                json.dump(flashcards, file, indent=4)

        print(f"Flashcard for '{word}' has been added")

mode = input("teach oer student?: ").lower()

if mode == 'teacher':
    Teacher.flashcardmaker()


class Student:
    @staticmethod #make a variabl;e pitsode s,mt else
    def flashcardmaker():
        try:
            with open("flashcards.json", "r") as file:
                flashcards = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError): #wats gonna happen if its emptty
            flashcards = {}
    
    
while True:
    print(FlashCards.json)