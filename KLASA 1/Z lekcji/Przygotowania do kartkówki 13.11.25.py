# #Zadania z isdigit(); isalnum(); isalpha
# # Zadanie 1
# slowo = input('Podaj dowolne słowo: ')
# if slowo.isalpha():
#     print('Twoje słowo składa się wyłącznie z liter.')
# else:
#     print('Twoje słowo nie składa się wyłącznie z liter.')
#
# # Zadanie 2
# wiek = input('Podaj swój wiek: ')
# if wiek.isdigit():
#     print(f'Twój wiek to {wiek} lat.')
# else:
#     print('Wiek musi być liczbą!')
#
# # Zadanie 3
# login = input('Podaj login: ')
# if login.isalnum():
#     print(f'Twój login to: {login}')
# else:
#     print('Login zawiera niedozwolone symbole!')
#
# # Zadanie 4
# CiągZnakow = input('Podaj ciąg znaków: ')
# if CiągZnakow.isdigit():
#     print('To, co podałeś/aś, składa się tylko z cyfr.')
# elif CiągZnakow.isalpha():
#     print('To, co podałeś/aś, składa się tylko z liter.')
# elif CiągZnakow.isalnum():
#     print('To, co podałeś/aś, składa się z liter i cyfr.')
# else:
#     print('Użyłeś znaków, które nie powinny się tu znaleźć.')
#
# # Zadanie 5
# haslo = input('Podaj hasło, składające się tylko z liter i liczb: ')
# if not haslo.isalnum():
#     print('Hasło zawiera niedozwolone znaki!')
# elif haslo.isdigit():
#     print('Nie podałeś/aś żadnych liter.')
# elif haslo.isalpha():
#     print('Nie podałeś/aś żadnych liczb.')
# else:
#     print('Hasło podane poprawnie.')
#
# # Zadanie 6
# CiągZnakow2 = input('Podaj ciąg znaków: ')
# if CiągZnakow2.isdigit():
#     print(f'{CiągZnakow2} zawiera jedynie liczby.')
# elif CiągZnakow2.isalpha():
#     print(f'{CiągZnakow2} zawiera jedynie litery.')
# elif CiągZnakow2.isalnum():
#     print(f'{CiągZnakow2} zawiera zarówno litery, jak i liczby.')
# else:
#     print(f'{CiągZnakow2} zawiera inne znaki.')
#
# #Zadanie 7:
# znak = input('Podaj jedna literę: ')
# print(f'{znak} w systemie ASCII to {ord(znak)}')
#
# #Zadanie 8:
# kod = int(input('Podaj dowolny symbol w kodzie ASCII: '))
# print(f'{kod} w systemie ASCII to {chr(kod)}')
#
# #Zadanie 9:
# slowo = input('Podaj dowolne słowo: ')
# samogloski = 'aeiouyAEIOUY'
# tabela = slowo.maketrans(samogloski, '*' * len(samogloski))  #67
# print(f'{slowo.translate(tabela)}')

#Zadanie 10:

slowo2 = input('Podaj dowolne słowo: ')
print(f'Dużymi literami: {slowo2.upper()}')
print(f'Małymi literami: {slowo2.lower()}')

#Zadanie 11:
zdanie = input('Podaj dowolne zdanie: ')
print(f"Twoje zdanie po konfiguracji{zdanie.replace(' ', '_')}")

#Zadanie 12:
slowo3 = input('Podaj dowolne słowo: ')
print(f'posortowane słowo: {''.join(sorted(slowo3))}; odwrócone słowo: {slowo3[::-1]}')
