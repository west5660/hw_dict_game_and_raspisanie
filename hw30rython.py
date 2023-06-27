#Задание 1
import random

# Списки предметов для каждого класса
class13 = ['Чтение', 'Пение', 'Рисование', 'Математика']
class58 = ['Математика', 'Музыка', 'Физика', 'Геометрия', 'Химия', 'Биология', 'Физкультура', 'Русский язык']
class911 = ['Математика', 'Музыка', 'Физика', 'Геометрия', 'Литература', 'Русский язык', 'Физкультура', 'ОБЖ', 'Химия', 'Биология', 'География', 'Статистика']

def f1(class_number):
    if class_number in [1, 2, 3]:
        subjects = class13
        lessons = 3
    elif class_number in [5, 6, 7, 8]:
        subjects = class58
        lessons = 4
    elif class_number in [9, 10, 11]:
        subjects = class911
        lessons = 5
    else:
        print("Некорректный номер класса.")
        return None

    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']

    # Создаем расписание на основе выбранного класса
    raspisanie = {}
    for day in days:
        # Используем функцию random.sample для выбора случайных предметов
        # из списка subjects в количестве lessons
        raspisanie[day] = random.sample(subjects, lessons)

    return raspisanie

# Пример использования:
class_number = int(input("Введите номер класса (1-11): "))
raspisanie = f1(class_number)

if raspisanie:
    # Выводим расписание на экран
    for day, subjects in raspisanie.items():
        print(day + ":", subjects)

#Задание 2

import random

def character_hero(character_class, name, race):
    # Определение характеристик в зависимости от класса персонажа
    if character_class == 'маг':
        stats = ['Сила', 'Выносливость', 'Ловкость', 'Харизма', 'Интеллект', 'Удача']
        stats_lim = [1, 2, 3, 4, 10, 10]
    elif character_class == 'лучник':
        stats = ['Сила', 'Выносливость', 'Ловкость', 'Харизма', 'Интеллект', 'Удача']
        stats_lim = [3, 4, 5, 6, 2, 10]
    elif character_class == 'воин':
        stats = ['Сила', 'Выносливость', 'Ловкость', 'Харизма', 'Интеллект', 'Удача']
        stats_lim = [5, 6, 1, 2, 3, 10]
    else:
        print("Некорректный класс персонажа.")
        return None

    # Генерация случайных характеристик суммой 30
    stats_generate = random.sample(range(1, 11), 6)
    while sum(stats_generate) != 30:
        stats_generate = random.sample(range(1, 11), 6)

    if race == 'эльф':
        stats_generate[2] += 5
        race_stat = 'Ловкость'
    elif race == 'орк':
        stats_generate[0] += 9
        race_stat = 'Сила'
    elif race == 'человек':
        stats_generate[5] += 3
        race_stat = 'Удача'
    elif race == 'нежить':
        stats_generate[4] += 7
        race_stat = 'Интеллект'

    # Вывод информации о персонаже
    print("Ваш персонаж:", 'Имя', name, 'класс', character_class, 'вид', race)
    for i in range(len(stats)):
        if stats[i] == race_stat:
            print(f"{stats[i]:<12} {stats_generate[i]} (+{stats_generate[i] - 5} 'бонус вида')")
        else:
            print(f"{stats[i]:<12} {stats_generate[i]}")

    # Возвращаем созданного персонажа
    character = {'name': name,'class': character_class,'race': race,'stats': dict(zip(stats, stats_generate))}
    return character

# Пример использования:
character_class = input("Выберите класс персонажа (маг, лучник, воин): ")
character_name = input("Введите имя персонажа: ")
character_race = input("Введите расу персонажа (эльф, орк, человек, нежить): ")

character = character_hero(character_class, character_name, character_race)
