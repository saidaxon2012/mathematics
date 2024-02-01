import random

result = []
sum = 0 
start = -9
stop = 9
for i in range(5):
    num = random.randint(start, stop + 1)
    result.append(num)
    sum = sum + num 
    print(num)    
answer = int(input("Javobini kiriting: "))
if answer == sum:
    print("Barakalla. To`g`ri topdingiz 🎉 !")
else:
    print("Afsuski javob to`g`ri emas ❌ !")
    
# print(result)


