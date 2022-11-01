import itertools

def main(start_size, start_count):
    # start_size - это доступное количество ячеек
    # start_count - начальное количество очков выживания

    equipment = {'в': (25, 3),  # 0
                 'п': (15, 2),  # 1
                 'б': (15, 2),  # 2
                 'а': (20, 2),  # 3
                 'и': (5, 1),  # 4
                 'н': (15, 1),  # 5
                 'т': (20, 3),  # 6
                 'о': (25, 1),  # 7
                 'ф': (15, 1),  # 8
                 'д': (10, 1),  # 9
                 'к': (20, 2),  # 10
                 'р': (20, 2)}  # 11

    def get_point_and_size(equipment):
        point = [equipment[i][0] for i in equipment]
        size = [equipment[i][1] for i in equipment]
        return point, size

    point, size = get_point_and_size(equipment)

    var = []  # Все возможные варианты оборудования
    mx = 0  # Максимальное возможное значение очков выживания
    entry_list = []  # Данные об выбранных предметах
    max_point = 0  # Общее количество очков выживания
    selected_equipment = []  # Выбранное оборудование

    for i in range(0, 12):
        max_point += point[i]

    for y in range(1, 11):
        val = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        com_set = itertools.combinations(val, y)
        for i in com_set:
            if 4 in i:  # Условие рассмотрения только тех вариантов, которые содержат инголятор
                var.append(i)

    for i in range(len(var)):
        count_size = 0
        count_point = 0
        for j in range(len(var[i])):
            count_size += size[var[i][j]]
            if count_size <= start_size:
                count_point += point[var[i][j]]
                if mx < count_point:
                    mx = count_point
                    v = i  # Записывает номер итоговой комбинации в переменную v

    for i in range(len(var[v])):
        entry_list.append((point[var[v][i]], size[var[v][i]]))  # Записываем размеры предметов которые были выбранны

    answer = 2 * mx - max_point + start_count  # Вычисляем итоговое количество очков выживания

    for key, y in equipment.items():  # Узнаем название использованных предметов
        for search in entry_list:
            count_repeat = search[1]
            if search == y and key not in selected_equipment and len(selected_equipment) < start_size:
                while count_repeat > 0:
                    count_repeat = count_repeat - 1
                    selected_equipment.append(key)

    selected_equipment_answer = []  # Правильный формат выбранное оборудование
    k = []

    for x in selected_equipment:
        for y in x:
            k.append(y)
            selected_equipment_answer.append(k)
            k = []

    print('Выбранные предметы:')
    for i in range(0, start_size):
        if i % 3 == 0:
            print(selected_equipment_answer[i:i + 3])
    print('Максимальное возможное количество очков выживания:')
    return answer


print('Основное задание', '\n')
print(main(9, 15), '\n')

print('Дополнительное задание для 7 ячеек', '\n')
print(main(7, 15))
