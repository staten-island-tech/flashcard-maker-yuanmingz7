import json
import random

class Teacher:
    @staticmethod 
    def flashcardmaker():
        try:
            with open("flashcards.json", "r") as file:
                flashcards = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError): 
            flashcards = {}

        while True:
            word = input("enter word for flashcard or type exit to quit: ")
            if word.lower() == 'exit': #lower makes it so its casw sensitive truns unto all lowercase
                break
            answer = input("Enter answer for flashcard: ")
            flashcards[word] = answer

            with open("flashcards.json", "w") as file:  #r means read, read whats inside of json
                json.dump(flashcards, file, indent=4)

        print(f"Flashcard for '{word}' has been added")



class Student:
    @staticmethod #make a variabl;e pitsode s,mt else
    def flashcardmaker():
        try:
            with open("flashcards.json", "r") as file:
                flashcards = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError): #wats gonna happen if its empty
            print("theres no flashcards")
            return
        
        print("type exit to quit, starting lashcards")
        keys = list(flashcards.keys())
        random.shuffle(keys)

        score = 0
        streak = 0
        points = 0

        for word in keys:
            print(f"flashcard: {word}")
            answer = input("aswer:")
            if answer.lower() == "exit":
                break
            if answer.lower() == flashcards[word].lower():
                streak +=1
                points +=1
                score += points
                print(f"correct)")
            else:
                print(f"youre wrong")
                streak == 0
                print(f"reseffed ur streak")

        print(f"ur total score is {score} with a streak of {streak}")
    
mode = input("teacher or student?: ").lower()

if mode == 'teacher':
    Teacher.flashcardmaker()
elif mode == 'student':
    Student.flashcardmaker()
