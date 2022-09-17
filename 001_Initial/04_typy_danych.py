#####
#####
#str - string zmienne tekstowe
#####
#####

name1 = 'Arek\'s program'
print(name1)

name2 = "Tak się wstawia\n\ndwa ENTERY"
print(name2)

name3 = """Można też tak wstawić


dwa ENTERY"""
print(name3)

#####
#####
#int - interger liczby całkowite, float - liczby zmiennoprzecinkowe
#####
#####

#int
a = 10
#float
b = 15.5
#int
c = 1_000_000

print(a + b + c)

#####
#####
#bool - typ logiczny (przyjmujący wartości true albo false)
#####
#####

#Konwencja kilku słów w jednej zmiennej w Pythonie - piszemy z podkreśleniami - snake_case
is_sky_blue = True
is_sun_blue = False

print(is_sky_blue)
print(is_sun_blue)


#####
#Sprawdzene typu zmiennej
#####

print(type(name2))
print(type(a))
print(type(b))
print(type(is_sky_blue))

#####
#Zmiana typu zmiennej
#####

first = 5
second = "2"

print(first + int(second))