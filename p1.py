a=121
if str(a)==str(a)[::-1]:
    print(a,"its palandrom")
else:
    print(a,"its not palandrom")


numbers = list(range(-25, 26))

positive_numbers = [num for num in numbers if num > 0]
negative_numbers = [num for num in numbers if num < 0]
zero = [num for num in numbers if num == 0]

print("Positive:", positive_numbers)
print("Negative:", negative_numbers)
print("zero:" , zero)
