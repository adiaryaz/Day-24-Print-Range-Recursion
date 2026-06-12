def print_range(start, end):
    if start > end:
        return
    print(start)
    print_range(start + 1, end)

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
print_range(start, end)