def display_multiplication_table(number, upto):
    print(f"Multiplication table for {number}:")
    for i in range(1, upto + 1):
        print(f"{number} x {i} = {number * i}")

number = 2
upto = 12
display_multiplication_table(number, upto)
