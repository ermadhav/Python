# Project :- 1
# try:
#     a = int(input("Enter the first num: "))
#     print("What kind of operation you want to perform : +,-,*,/ ")
#     o = input("Enter operation: ")
#     b = int(input("Enter the first num: "))

    
#     match o: 
#         case "+":
#             print(f"result = {a+b}")
#         case "-":
#             print(f"result = {a-b}")
#         case "*":
#             print(f"result = {a*b}")
#         case "/":
#             print(f"result = {a/b}")    

# except Exception as e:
#     print("enter a valid value of a and b")        

# Project:- 2

# questions = [
#     ["Who is Shah Rukh Khan?", "WWE Wrestler", "Plumber", "Actor", "Astronaut", 3],
#     ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
#     ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
#     ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2],
#     ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1],
#     ["What is the square root of 64?", "8", "10", "6", "12", 1],
#     ["Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 3],
#     ["Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 3],
#     ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
#     ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
#     ["What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 2]
# ]

# prizes = [100000, 320000, 400000, 450000,  500000, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000]

# i = 0 
# for question in questions:
#     print(question[0])
#     print(f"a. {question[1]}")
#     print(f"b. {question[2]}")
#     print(f"c. {question[3]}")
#     print(f"d. {question[4]}")

#     # Check whether the answer is correct or not
#     a = int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d\n"))
#     if(question[5] == a):
#         print("Correct Answer")
#     else:
#         print(f"Incorrect, the correct answer was {question[5]}")
#         print("Better luck next time!")
#         break 
#     print(f"You won {prizes[i]}")
#     i +=1    

# Project:- 3

# from PyPDF2 import PdfWriter
# merger = PdfWriter()
# pdfs = []
# n = int(input("How many pdf you want to merge \n"))

# for i in range (0,n):
#     name = input(f"Enter the name of pdf {i+1}: ")
#     pdfs.append(name)

# for pdf in pdfs:
#     merger.append(pdf)

# name = input("Enter the name of merged pdf you want: ")
# merger.write(f"{name}.pdf")
# print(f"{name}.pdf is downloaded")
# merger.close()


import requests
query = input("what type of news you are interested in today? ")
api = 'a1d43f4321ef488ca7d5a9f4bd49644f'

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-01-06&sortBy=publishedAt&apiKey=a1d43f4321ef488ca7d5a9f4bd49644f"

print(url)
r = requests.get(url)
data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index+1, article["title"], article["url"])
    print("\n****************************************\n")