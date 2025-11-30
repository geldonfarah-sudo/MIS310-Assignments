def main():
    # lists for days and sales
    week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    sale_list = [50, 75, 150, 125, 100]

    # assume first value is the largest
    max_sale = sale_list[0]
    max_day = week_list[0]

    # loop to find largest sale and matching day
    for list in range(len(sale_list)):
        if sale_list[list] > max_sale:
            max_sale = sale_list[list]
            max_day = week_list[list]

    # output results
    print(f"The Max sales is ${max_sale}")
    print(f"The Max sales day is {max_day}")

main()

# problem 2 (fixed)

def main():
    numbers = []

    # first prompt (as shown in sample)
    one = float(input("Enter value: "))
    if one != 0:
        numbers.append(one)

        # subsequent prompts until 0
        while True:
            num = float(input("Enter value (or 0 to end): "))
            if num == 0:
                break
            numbers.append(num)

    print(numbers)

    # compute range safely
    if len(numbers) == 0:
        range_value = 0.0
    else:
        smallest = numbers[0]
        largest = numbers[0]
        for numb in numbers:
            if numb < smallest:
                smallest = numb
            if numb > largest:
                largest = numb
        range_value = largest - smallest

    print(f"Range= {range_value}")

main()
