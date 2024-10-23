import  random
secretNum = random.randint(1,100)
attempts = 0
answers = set()
while True:
    try:
        guess = int(input("введите ваше число"))
        attempts += 1
        answers.add(guess)
        if guess < secretNum:
            print("больше")
        elif guess > secretNum:
            print("меньше")
        else:
            print(f"вы угадали число {secretNum} за {attempts} попыток")
            break
    except ValueError:
        print("ввод некоректный")
with open('random.txt', 'w', encoding='utf-8') as file:
    file.write("ващи попытки: \n")
    for guess in  answers:
        file.write(str(guess) + '\n')