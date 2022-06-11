from typing import *

# change all the : signs to commas so the excel sheet can recognize the links

with open("./microsoft_interview_questions.txt", "r") as f:
    questions = f.readlines()

    result = ""
    for question in questions:
        index = question.find(":") # we find the first instance of the :
        #result += question[:index] + "," + question[index+2:]
        result += question[:index] + "\n"

with open("./cleaned.txt", "w") as f2:
    f2.write(result)
