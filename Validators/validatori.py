import random
import string
def validator1(value,poz):
    """
    Valideaza o valoare ce trebuie sa fie parametru al unui obiect de tip student
    raise ValueError daca datele nu sunt valide
    """
    errors=[]
    if poz==0 and (value.isdigit()!=True or (int(value)<0 or int(value)>100)):
        errors.append('Id-ul trebuie sa fie mai mare decat 0 si mai mic decat 100')
    elif poz==1 and ( len(value)< 2 or containsNumber(value)==True) :
        errors.append('Studentul trebuia sa aiba minim 2 caractere si sa nu contina cifre')
    if len(errors) > 0:
        errors_string = '\n'.join(errors)
        raise ValueError(errors_string)

def validator2(value,poz):
    """"
    valideaza o valoare ce trebuie sa fie parametru al unui obiect de tip disciplina
    raise ValueError daca datele nu sunt valide
    """
    errors=[]
    if poz==0 and (int(value) < 101 or int(value) > 150 or value.isdigit()!=True):
        errors.append('Id-ul trebuie sa fie mai mare decat 101')
    if  poz==1 and (len(value) < 1 or containsNumber(value)==True):
        errors.append('Disciplina incorecta')
    if poz==2 and (len(value) < 2 or containsNumber(value)==True):
            errors.append('Numele Profesorului  trebuie sa aiba minim 2 caractere')
    if len(errors) > 0:
        errors_string = '\n'.join(errors)
        raise ValueError(errors_string)

def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False
def random_string_generator(length):
    result = ''.join((random.choice(string.ascii_lowercase) for x in range(length)))
    return result