def get_even_numbers(list):
    result = []
    for number in list:
        if type(number) == int:
            if number % 2 == 0:
                result.append(number)
        else :
            print("numar non int")
    return result
print(get_even_numbers([4,6,7,8,35,34]))


