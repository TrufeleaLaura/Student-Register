from Validators.validators  import *
import unittest
class TestCaseValid(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = studValidator()
        self.__validator1=discValidator()
        self.__validator2=noteValidator()

    def test_student_validator(self):

        stud1=student('15kj','123')
        try:
            self.__validator.validatestud(stud1)
            self.assertTrue( False)
        except ValueError:
            self.assertTrue(True)
        stud2 = student('0', 'Marian Iulia')
        try:
            self.__validator.validatestud(stud2)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    def test_disciplina_validator(self):
        dis1=disciplina(101,'Fp','Mihut Alex')
        try:
            self.__validator1.validatedis(dis1)
            self.assertTrue(True)
        except ValueError:
            self.assertTrue(False)
        dis2=disciplina(201,'0 2','KKK')
        try:
            self.__validator1.validatedis(dis2)
            self.assertTrue( False)
        except ValueError:
            self.assertTrue(True)

    def test_notare(self):
        stud= student(1, 'Popescu Adelina')
        dis= disciplina(101, 'fundamentele programarii', 'Mila Adriana')
        nota = notare(stud, dis, 8)
        self.__validator2.validatenot(nota)

        nota1= notare(stud, dis, 15)
        try:
            self.__validator2.validatenot(nota1)
            self.assertTrue( False)
        except ValueError:
            self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
