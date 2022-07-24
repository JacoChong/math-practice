import random
import time

score = 0

data = {'questions':[]}

while True:
    tried = 0
    print(f"--------------------\nScore: {score}")
    num1 = random.randrange(2, 10)
    num2 = random.randrange(2, 10)
    ans = num1 * num2
    try:
        starttime = time.time()
        fb = int(input(f"--------------------\n\n{num1} x {num2} = "))
        tried += 1
        if fb == 123456789:
            break
        if fb == ans:
            endtime = time.time() 
            usedtime = round((endtime - starttime), 1)
            print(f"√     +2     {usedtime}\n")
            isCorrect = True
            acc = f'{1 / tried * 100}%'
            score += 2
            data['questions'].append({
                'ques': f'{num1} x {num2}',
                'time':usedtime,
                'acc': acc,
                'tries': tried
                })
            continue
        elif fb != ans:
            print("X     -1\n")
            isCorrect = False
            score -= 1
    except ValueError:
        print("--\n")
        isCorrect = False

    while isCorrect == False:
        try:
            fb = int(input(f"{num1} x {num2} = "))
            tried += 1
            if fb == ans:
                endtime = time.time()
                usedtime = round((endtime - starttime), 1)
                print(f"√     --     {usedtime}\n")
                isCorrect = True
                acc = f'{1 / tried * 100}%'
                data['questions'].append({
                    'ques': f'{num1} x {num2}',
                    'time': usedtime,
                    'acc': acc,
                    'tries': tried
                    })
                break
            elif fb != ans:
                print("X     -1\n")
                score -= 1
                continue
        except ValueError:
            print("--\n")
            continue

data["questions"].sort(key=lambda v:v['time'], reverse=True)

print("\n--------------------\n\nScore: {score}") #                                     --100.0% (  )-
print(f'  # | Question | Avg Time Used | Avg Accuracy \n----|----------|---------------|--------------')
for i in range(len(data["questions"])):
    print(f' {i+1:>2} | {data["questions"][i]["ques"]:^8} | {((data["questions"][i]["time"])/(data["questions"][i]["tries"])):>13} |  {((data["questions"][i][acc])/(data["questions"][i][tried])):>6} ({data["questions"][i][tried]}) ')