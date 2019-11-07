import os
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open('image.jpg')
text = pytesseract.image_to_string(img)


print("\nWelcome to the line memory machine alpha program. Here you can enter a word and we can help you remember it!\n")

print(text)
print("\n")
cont = input("Press Enter to continue")

#response0 = input("Type a word that you want to remember?   ")
#response1 = input("\nType it's definition and read it until you think you have it in your short term memory, then press enter. \n \n ")

words = text.split()
letters = [word[0] for word in words]
print("\n")
print (" ".join(letters))
print("\n")















print("Look at each letter and try to remember the word that goes with it. \n")

print("Once you're confident that you can remember the phrase. Close your eyes and try to repeat the definition. \n")

#print("Now go do something else and try to remember it one minute from now. \n")





#print("Welcome to the line memory machine alpha program. Here you can enter some text and we can help you remember it!")

#response1 = input("Type a sentence you want to remember?   ")

#words = response1.split()
#letters = [word[0] for word in words]
#print (" ".join(letters))