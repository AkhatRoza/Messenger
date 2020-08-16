def max_number(numbers):
    m = numbers[0]

    for number in numbers:
        if number >= m:
            m = number
    return m


print(max_number([12,15,56,5,57,99,12569,346,66666]))
print(max_number([12,1,56,5,9,125,34,66]))

def more_then_k(numbers,k):
    result=[]

    for number in numbers:
        if number >= k:
            result.append(number)
    return result

print(more_then_k([12,15,56,5,57,99,12569,346,66666],33))
print(more_then_k([12,1,56,5,9,125,34,66],44))