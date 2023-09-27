ucheniki = {}
predmet = {'Предметы': {'Математика': None, 'Английский': None,
'Программирование': None}}

def new_class():
    class_add = input('Введите номер и букву класса(большая буква) без пробела: ')
    name_uchenik = input('Введите имя ученика: ')
    ucheniki[class_add] = {'Ученики': {name_uchenik: predmet}}
    print(ucheniki)

def new_schoolboy():
    select_class = input('В какой класс добавить ученика?: ')
    if select_class in ucheniki:
        name_uchenik = input('Введите имя ученика: ')
        if name_uchenik in ucheniki[select_class]['Ученики']:
            print('Такой ученик уже есть')
        else:
            ucheniki[select_class]['Ученики'][name_uchenik] = predmet
            print(ucheniki)
    else:
        print('Такого класса нет')
        new_schoolboy()

def replace_schoolboy():
    select_class = input('В каком классе заменить ученика?: ')
    if select_class in ucheniki:
        name = input('Введите имя ученика которого хотите заменить: ')
        if name in ucheniki[select_class]['Ученики']:
            new_name = input('Введите имя нового ученика: ')
            if new_name in ucheniki[select_class]['Ученики']:
                print(f'В {select_class} уже есть такой ученик')
                replace_schoolboy()
            else:
                del ucheniki[select_class]['Ученики'][name]
                ucheniki[select_class]['Ученики'][new_name] = predmet
                print(ucheniki)
        else:
            print(f'В {select_class} классе нет такого ученика')
            replace_schoolboy()
    else:
        print('Такого класса нет')
        replace_schoolboy()

def delete_schoolboy():
    select_class = input('В каком классе удалить ученика?: ')
    if select_class in ucheniki:
        name = input('Введите имя ученика которого хотите удалить: ')
        if name in ucheniki[select_class]['Ученики']:
            del ucheniki[select_class]['Ученики'][name]
            print(f'{name} успешно удален из {select_class} класса')
            print(ucheniki)
        else:
            print(f'В {select_class} классе нет такого ученика')
            delete_schoolboy()
    else:
        print('Такого класса нет')
        delete_schoolboy()

def add_teacher():
    select_class = input('В какой класс добавить преподавателя?: ')
    if select_class in ucheniki:
        name_teacher = input('Введите Имя и Отчество нового преподавателя: ')
        if 'Преподаватель' in ucheniki[select_class]:
            print(f'В {select_class} уже есть преподаватель')
            add_teacher()
        else:
            ucheniki[select_class]['Преподаватель'] = name_teacher
            print(ucheniki)
    else:
        print('Такого класса нет')
        add_teacher()

def replace_teacher():
    select_class = input('В каком классе заменить преподавателя?: ')
    if select_class in ucheniki:
        name = input('Введите Имя и Отчество преподавателя которого хотите заменить: ')
        if name in ucheniki[select_class]['Преподаватель']:
            new_name = input('Введите Имя и Отчество нового преподавателя: ')
            ucheniki[select_class]['Преподаватель'] = new_name
            print(ucheniki)
        else:
            print(f'В {select_class} нет такого преподавателья')
            replace_teacher()
    else:
        print('Такого класса нет' )
        return replace_teacher()

def delete_teacher():
    select_class = input('В каком классе удалить преподавателя?: ')
    if select_class in ucheniki:
        name = input('Введите Имя и Отчество преподавателя которого хотите удалить: ')
        if name in ucheniki[select_class]['Преподаватель']:
            del ucheniki[select_class]['Преподаватель']
            print(f'Преподаватель {name} успешно удален из {select_class} класса')
            print(ucheniki)
        else:
            print(f'В {select_class} классе нет такого преподавателя')
            delete_teacher()
    else:
        print('Такого класса нет')
        delete_teacher()


def add_mark():
    name = input('Введите имя ученика для выставления оценки: ')
    class_add = input('В каком он классе?: ')
    if name in ucheniki[class_add]['Ученики']:
        lesson = input('По какому предмету выставить оценку (Математика, Английский, Программирование)?: ')
        mark = int(input("Введите оценку: "))
        if lesson == 'Математика':
            ucheniki[class_add]['Ученики'][name]['Предметы'][lesson] = mark
            print(ucheniki)
        elif lesson == 'Английский':
            ucheniki[class_add]['Ученики'][name]['Предметы'][lesson] = mark
            print(ucheniki)
        elif lesson == 'Программирование':
            ucheniki[class_add]['Ученики'][name]['Предметы'][lesson] = mark
            print(ucheniki)
        else:
            print('Такого предмета нет')
            add_mark()
    else:
        print(f'В {class_add} нет такого ученика')
        add_mark()

def replace_mark():
    class_add = input('В каком классе ученик, которому вы хотите изменить оценку?: ')
    if class_add in ucheniki:
        name = input('Введите имя ученика для изменения оценки: ')
        if name in ucheniki[class_add]['Ученики']:
            lesson = input('По какому предмету изменить оценку (Математика, Английский, Программирование)?: ')
            new_mark = int(input("Введите оценку: "))
            if lesson == 'Математика':
                ucheniki[class_add]['Ученики'][name]['Предметы'][lesson] = new_mark
                print(ucheniki)
            elif lesson == 'Английский':
                ucheniki[class_add]['Ученики'][name]['Предметы'][lesson] = new_mark
                print(ucheniki)
            elif lesson == 'Программирование':
                ucheniki[class_add]['Ученики'][name]['Предметы'][lesson] = new_mark
                print(ucheniki)
            else:
                print('Такого предмета нет')
                add_mark()
        else:
            print(f'В {class_add} нет такого ученика')
            add_mark()
    else:
        print('Нет такого класса')
        replace_mark()

def delete_mark():
    class_add = input('В каком классе ученик, которому хотите удалить оценку?: ')
    if class_add in ucheniki:
        name = input('Ведите имя ученика: ')
        if name in ucheniki[class_add]['Ученики']:
            lesson = input('По какому предмету удалить оценку (Математика, Английский, Программирование)?: ')
            if lesson in ucheniki[class_add]['Ученики'][name]['Предметы']:
                new_mark = None
                ucheniki[class_add]['Ученики'][name]['Предметы'][lesson] = new_mark
                print(f'Оценка по предмету {lesson} успешно удалена у {name} из {class_add} класса')
                print(ucheniki)
            else:
                print('Введите название предмета корректно')
                delete_mark()
        else:
            print(f'В {class_add} классе нет такого ученика')
            delete_mark()
    else:
        print('Такого класса нет')
        delete_mark()

while True:
    admin = int(input('Введите действие (цифра): Создание класса: 1'
                      '\nДобавление учеников: 2, Изменение учеников: 3, Удаление учеников: 4'
                      '\nДобавление преподавателя: 5, Удаление преподавателя: 6'
                      '\nИзменение преподавателя: 7, Выставление оценок: 8'
                      '\nИзменение оценок: 9, Удаление оценок: 10: '))
    if admin == 1:
        new_class()
    elif admin == 2:
        new_schoolboy()
    elif admin == 3:
        replace_schoolboy()
    elif admin ==4:
        delete_schoolboy()
    elif admin == 5:
        add_teacher()
    elif admin == 6:
        replace_teacher()
    elif admin == 7:
        delete_teacher()
    elif admin == 8:
        add_mark()
    elif admin == 9:
        replace_mark()
    elif admin == 10:
        delete_mark()
    else:
        print('Не корректно введено действие, попробуйте заново')




    