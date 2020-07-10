# L3, Ex.2
print('Enter the user data:')
firstName = input('first name: ')
lastName = input('last name: ')
yearB = int(input('year of birth: '))
city = input('city: ')
telephone = input('telephone number: ')
email = input('email: ')


def userData(fn, ln, yob, city,tel, mail):
    return fn, ln, yob, city,tel, mail


print(*userData(fn=firstName, ln=lastName, yob=yearB, city=city, tel=telephone, mail=email))