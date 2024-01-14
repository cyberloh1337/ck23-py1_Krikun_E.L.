# TODO Напишите функцию find_common_participants
def find_common_participants(a, b, spl = ','):
    a = set(a.split(spl))
    b = b.split(spl)
    a = list(a.intersection(b))
    a.sort()
    return (a)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))