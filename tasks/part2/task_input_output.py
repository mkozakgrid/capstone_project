def read_numbers(n: int) -> str:
    numbers = []
    input_numbers = input("Enter numbers (0 to exit): ")
    while input_numbers != 0:
        numbers.append(int(input_numbers))
        input_numbers = input("Enter numbers (0 to exit): ")
    
    for i in range(n):
        sum = 0
        count = 0
        if numbers[i].isdigit():
            sum += numbers[i]
            count += 1
    average = round(sum / count, 2)
    message = f"Avg: {average}"
    return message

