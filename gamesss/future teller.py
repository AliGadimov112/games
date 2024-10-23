import random
with open("questions.txt", 'r', encoding= 'utf-8') as file:
    questions = file.readlines()
    print(questions)
    questions = [question.strip()for question in questions]
with open("response.txt", 'r' , encoding= 'utf-8') as file:
    responses = file.readlines()
    responses = [response.strip() for response in responses]
    randIndex = random.randint(0, len(questions) - 1)
    print(questions[randIndex])
    print(responses[randIndex])