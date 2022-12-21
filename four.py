def boundary(elements, size):
    for jj in range(size):
        print("+" + "-" * elements, end="")
        if jj == size - 1:
            print("+")


def internal(elements, size):
    for ii in range(elements):
        for jj in range(size):
            print("|" + " " * elements, end="")
            if jj == size - 1:
                print("|")


N = int(input("Enter the size of each elements: "))
n = int(input("Enter a number of elements: "))
for i in range(n + 2):
    for j in range(N):
        if i == 0 or i == n + 1:
            print("+" + "-" * n, end="")
            if j == N - 1:
                print("+")
        else:
            print("|" + " " * n, end="")
            if j == N - 1:
                print("|")

num_elements = int(input("Enter the number of elements: "))
num_size = int(input("Enter the size of each element: "))
boundary(num_elements, num_size)
internal(num_elements, num_size)
boundary(num_elements, num_size)