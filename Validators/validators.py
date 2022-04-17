from domain.entities import student,disciplina,notare
from Validators.validatori import containsNumber
class studValidator:
    def validatestud(self, student):
        errors = []
        if int(student.getIdstudent()) <=0 or int(student.getIdstudent()) >100 or student.getIdstudent().isdigit()!=True :
            errors.append('Id-ul trebuie sa fie mai mare decat 0 si mai mic decat 100')
        if len(student.getnume())< 2 or containsNumber(student.getnume())==True:
            errors.append('Studentul trebuia sa aiba minim 2 caractere si sa nu contina cifre')
        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)

class discValidator:
    def validatedis(self, disciplina):
        errors = []
        if  int(disciplina.getIdDisciplina()) <101 or int(disciplina.getIdDisciplina())>150  :
            errors.append('Id-ul trebuie sa fie mai mare decat 101')
        if len(disciplina.getnumedis())< 1 or containsNumber(disciplina.getnumedis())==True:
            errors.append('Disciplina trebuie sa nu fie lipsa si sa nu contina cifre')
        if len(disciplina.getprofesor()) < 2 or containsNumber(disciplina.getprofesor())==True:
            errors.append('Profesorul  trebuie sa aiba minim 2 caractere si sa nu contina cifre')
        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)

class noteValidator:
    def validatenot(self, nota):
        errors = []
        if int(nota.getnota()) < 0 or int(nota.getnota()) > 10:
            errors.append('Nota nu este valida')
        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)
"""
def test_student_validator():
    test_valid=studValidator()
    stud1=student("kdd",'123')
    try:
        test_valid.validatestud(stud1)
        assert False
    except ValueError:
        assert True
    stud2=student(0,'Marian Iulia')
    try:
        test_valid.validatestud(stud2)
        assert False
    except ValueError:
        assert True
def test_disciplina_validator():
    test_valid=discValidator()
    dis1=disciplina(101,'Fp','Mihut Alex')
    try:
        test_valid.validatedis(dis1)
        assert True
    except ValueError:
        assert False
    dis2=disciplina(201,'0 2','KKK')
    try:
        test_valid.validatedis(dis2)
        assert False
    except ValueError:
        assert True

def test_notare():
    test_valid=noteValidator()
    stud = student(1, 'Popescu Adelina')
    dis = disciplina(101, 'fundamentele programarii', 'Mila Adriana')
    nota = notare(stud, dis, 8)
    test_valid.validatenot(nota)

    nota1= notare(stud, dis, 15)
    try:
        test_valid.validatenot(nota1)
        assert False
    except ValueError:
        assert True

test_disciplina_validator()
test_disciplina_validator()
test_notare()
"""
