my_dict = {'Sahsa':1976, 'Kolya': 1995, 'Vova': 1954} # словарь
print('Dict: ',my_dict)                             # печать словаря
print('Existing value: ',my_dict['Kolya'])          # год рождения Kolya
print('Not existing value: ',my_dict.get('Robert'))  # Robert - не существующий ключ
my_dict.update({'Tolya': 2001, 'Vitya': 2008})      # добавил ключи Tolya и Vitya
a = my_dict.pop('Tolya')                            # удаление Tolya и вызов его значения
print('Delited value: ',my_dict)
print('Modified dictionari:', a)

my_set = {3, 'Диван', 3.14, 3, 'Диван'}             # первоначальное множество
print('Set: ', my_set)                              #печать уникальных значений
print(my_set.add(15))                               #добавдение 15
print(my_set.add('Vova'))                           #добавление Vova
print(my_set.remove('Диван'))                       #ндаляем Диван
print('Modified set: ', my_set)                     # печать нового множества






