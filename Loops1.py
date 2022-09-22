# Ex1:
numbers = [12, 75, 150, 180, 145, 525, 50]
ruslt_numbers = []
for i in numbers:
    if i % 5 == 0 and i <= 150:
        ruslt_numbers.append(i)
    if i > 500:
        break
print(ruslt_numbers)
