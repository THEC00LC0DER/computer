import random

MyNum = []

for i in range(100):
    num = random.randint(1, 1000)
    MyNum.append(num)
EndCounter = 99

NoMoreSwaps = True

while EndCounter >= 1 and NoMoreSwaps:
    NoMoreSwaps = True
    for Counter in range(EndCounter):
        if MyNum[Counter+1] < MyNum[Counter]:  # changed from > to <
            MyNum[Counter], MyNum[Counter +
                                  1] = MyNum[Counter + 1], MyNum[Counter]
            NoMoreSwaps = False
    EndCounter -= 1
print(MyNum)
