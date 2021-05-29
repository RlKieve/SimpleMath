# Simple Math.py
# author: Roddy
# date: 11.07.20

import random

name=input("What is your name?")
score=0
question=0
prompt = input("Ready? Yes or No")

while prompt == 'Yes':
    for question_num in range(1, 11): #Number of questions + 1. e.g 20 questions = 20+1=21
        ops = ['+', '-', '*','/'] #operations +,-, and *
        rand=random.randint(3,10) #Range of random number 1
        rand2=random.randint(3,10) #Range of random number 2
        operation = random.choice(ops)
        if rand >= rand2:
            maths = eval(str(rand) + operation + str(rand2))
            print('\nQuestion number: {}'.format(question_num))
            print ("The question is",rand,operation,rand2)
            question=question+1

            while True:
                try:
                    d=int(input ("What is your answer:"))
                except ValueError:
                    print("\nENTER A NUMBER!!!")
                    print('Question number: {}'.format(question_num))
                    print ("The question is",rand,operation,rand2)
                    continue
                else:
                    if d==maths:
                        print ("Correct")
                        score=score+1
                    else:
                        print ("Wrong, The answer is:",maths)
                    break
        else:
            maths = eval(str(rand2) + operation + str(rand))
            print('\nQuestion number: {}'.format(question_num))
            print ("The question is",rand2,operation,rand)
            question=question+1

            while True:
                try:
                    d=int(input ("What is your answer:"))
                except ValueError:
                    print("\nENTER A NUMBER!!!")
                    print('Question number: {}'.format(question_num))
                    print ("The question is",rand2,operation,rand)
                    continue
                else:
                    if d==maths:
                        print ("Correct")
                        score=score+1
                    else:
                        print ("Wrong, The answer is:",maths)
                    break
print ("\n===============",name + "\'s","total score is:",score,"/",question,"===============")
