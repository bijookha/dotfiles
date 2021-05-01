import pprint
import random

skills=[['qqq','cold snap'],
['qqw','ghost walk'],
['qqe','ice wall'],
['www','emp'],
['wwq','tornado'],
['wwe','alacrity'],
['eee','sunstrike'],
['eeq','forge spirit'],
['eew','chaos meter'],
['qwe','deafening blast']]

number=int(input('Number of questions?\n'))
print('______\n')
answersheet=[]
score=0

def answer_matches(answer,correct):
    if len(answer)!= len(correct):
        return False
    for c in answer:
        if not c in correct and answer.count(c)!=correct.count(c):
            return False
    return True

for i in range(0,number):
    rand=random.randint(0,10)-1
    question=skills[rand][1]
    correct_answer=[c for c in skills[rand][0]]
    answer=str(input('{}:\t{}? '.format(i+1,question)))
    answer=[c for c in answer]

    correct='False'
    if answer_matches(answer,correct_answer):
        correct='True'
        score=score+1
    answersheet.append([answer, correct_answer, correct, question])
    print(correct)

            

print('______')
pprint.pprint(answersheet)
print('______')
print('score{}/{}\n'.format(score,number))
print('______')
pprint.pprint(skills)
