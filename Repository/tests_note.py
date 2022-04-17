import unittest
from Repository.nota_repo import nota_repository
from domain.entities import notare,disciplina,student
class TestCaseStud(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_repo = nota_repository()

    def test_add(self):
        stud = student(1, 'Popescu Adelina')
        dis = disciplina(101, 'fundamentele programarii', 'Mila Adriana')

        nota = notare(stud,dis, 7)
        self.__test_repo.add_nota(nota)
        self.assertIs (len(self.__test_repo.get_all_note()), 1)
        try:
            self.__test_repo.add_nota(nota)
            self.assertTrue( False)
        except ValueError:
            self.assertTrue( True)

    def test_dell(self):
        stud1=student(2,'Tibet Leo')
        dis1=disciplina(102,'analiza','Marian ion')
        dis = disciplina(101, 'fundamentele programarii', 'Mila Adriana')
        nota1=notare(stud1,dis1,9)
        nota3=notare(stud1,dis,9)
        self.__test_repo.add_nota(nota3)
        self.__test_repo.add_nota(nota1)
        self.assertIs(len(self.__test_repo.get_all_note()), 2)
        self.__test_repo.dell_nota(nota3)
        self.assertIs (len(self.__test_repo.get_all_note()),1)

    def test_modif(self):
        stud = student(1, 'Popescu Adelina')
        dis = disciplina(101, 'fundamentele programarii', 'Mila Adriana')
        nota = notare(stud, dis, 7)
        self.__test_repo.add_nota(nota)
        stud1 = student(2, 'Tibet Leo')
        dis1 = disciplina(102, 'analiza', 'Marian ion')
        dis = disciplina(101, 'fundamentele programarii', 'Mila Adriana')
        nota1 = notare(stud1, dis1, 9)
        self.__test_repo.add_nota(nota1)
        self.__test_repo.modif_nota(nota1,10)
        self.assertIs (nota1.getnota(),10)
        self.__test_repo.modif_nota(nota,8)
        self.assertIs(nota.getnota(),8)

    def tearDown(self) -> None:
        self.__test_repo.dell_all()

if __name__ == '__main__':
    unittest.main()