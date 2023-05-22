n = int(input("Введите количество чисел: "))
max_even = None

for i in range(n):
    num = int(input(f"Введите число {i+1}: "))
    
    if num % 2 == 0 and (max_even is None or num > max_even):
        max_even = num

if max_even:
    print(f"Наибольшее четное число: {max_even}")
else:
    print("В последовательности нет четных чисел") 
