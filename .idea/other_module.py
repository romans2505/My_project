def is_lady(name):
    if (name == 'Аня') or (name == 'Вика') or (name == 'Валя'):
        return True
    else:
     return False

def count_lady(persons):
    count = 0
    for name in persons:
        if is_lady(name):
            count += 1
    return count

persons = ['Аня', 'Петя', 'Валя', 'Серёжа']
print(count_lady(persons))
