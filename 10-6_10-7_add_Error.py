# TC 2020/10/10

print("Give me two numbers,and I'll add them.")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst number:\n")
    if first_number == 'q':
        break
    second_number = input("\nSceond number:\n")
    if second_number =='q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("String can't add,please input two number\n")
    else:
        print(answer)