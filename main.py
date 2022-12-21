numerator = int(input("Enter a numerator: "))
denominator = int(input("Enter a denominator: "))
gcd_list = []
gcd = 0
if numerator > denominator:
    for i in range(denominator):
        if numerator % (i + 1) == 0 and denominator % (i + 1) == 0:
            gcd_list.append(i + 1)
else:
    for i in range(numerator):
        if numerator % (i + 1) == 0 and denominator % (i + 1) == 0:
            gcd_list.append(i + 1)
for i in gcd_list:
    if i > gcd:
        gcd = i
print(f"result: {numerator}/{denominator} = {numerator // gcd}/{denominator // gcd}")
