def get_even_numbers(list):
    list = [4,6,7,8]
    result = []
    for number in list:
        if number % 2 == 0:
            result.append(number)
    print(result)
get_even_numbers(list)