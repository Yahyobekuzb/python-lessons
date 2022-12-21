def prime_number(num):
    dividers = 0
    for i in range(2, num):
        if num % i == 0:
            dividers += 1
    if dividers > 0:
        return False
    else:
        return True


m = int(input("Enter a number: "))
print(f"The prime numbers <= {m} are:", end=" ")
for i in range(2, m + 1):
    if prime_number(i):
        print(i, end=" ")