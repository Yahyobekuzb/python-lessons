def power(num):
    result = 1
    for i in range(num):
        result = result * num
    return result


power_num = 0
y = int(input("Enter a number: "))
for i in range(100):
    powered = power(i)
    if powered < y:
        power_num = i
    else:
        break
print(f"Maximum x = {power_num}")