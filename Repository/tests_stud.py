import unittest
from Repository.stud_repo import stud_repository
from domain.entities import student
class TestCaseStud(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_repo = stud_repository()
        self.setup_test_repo()

    def setup_test_repo(self):
        st1 = student('1', 'Truf Andreea')
        st2 = student('2', 'Boba Leo')
        st3 = student('3', 'Carnu Maria')
        st4 = student('4', 'Darda Leo')
        st5 = student('5', 'Carla Antonia')
        st6 = student('6', 'Marian Claudiu ')
        st7 = student('7', 'Andrei Fasiu')
        st8 = student('8', 'Gheorghe Andra' )
        st9 = student('9', 'Valentin Bogdan')
        st10 =student('10', 'Vali Mihai')

        self.__test_repo.add_student(st1)
        self.__test_repo.add_student(st2)
        self.__test_repo.add_student(st3)
        self.__test_repo.add_student(st4)
        self.__test_repo.add_student(st5)
        self.__test_repo.add_student(st6)
        self.__test_repo.add_student(st7)
        self.__test_repo.add_student(st8)
        self.__test_repo.add_student(st9)
        self.__test_repo.add_student(st10)

    def test_getall(self): #BLACK BOX TESTING
        lst=self.__test_repo.get_all_students()
        self.assertIsNot(lst,[])
        self.assertTrue(type(lst),list)
        self.assertTrue(lst[0].getIdstudent()=='1')
        self.assertTrue(lst[1].getnume()=='Boba Leo')

    def test_find(self):
        p = self.__test_repo.find('10')
        self.assertTrue(p.getnume(),'Vali Mihai')

        p1 = self.__test_repo.find('12')
        self.assertIs (p1, None)

    def test_size(self):
        self.assertEqual (self.__test_repo.size(), 10)
        self.__test_repo.dell('5','0')
        self.__test_repo.dell('Andrei Fasiu','1')

        self.assertEqual (self.__test_repo.size(),8)

        self.__test_repo.add_student(student('11', 'Ciobanu Cristina'))
        self.assertEqual (self.__test_repo.size(), 9)

    def test_get_all_students(self):
        crt_stud = self.__test_repo.get_all_students()
        self.assertIs (type(crt_stud),list)
        self.assertEqual (len(crt_stud), 10)

        self.__test_repo.dell('5', '0')
        self.__test_repo.dell('Andrei Fasiu', '1')

        crt_stud = self.__test_repo.get_all_students()
        self.assertEqual (len(crt_stud), 8)


    def test_add_student(self):
        st1 = student('20', 'Serena Andreea')
        self.__test_repo.add_student(st1)

        self.assertEqual (self.__test_repo.size(),11)
        st2 = student('21', 'Kim Mariana')
        self.__test_repo.add_student(st2)

        try:
            # duplicate id
            self.__test_repo.add_student(st2)
            self.assertTrue( False)
        except ValueError:
            self.assertTrue(True)

    def test_dell(self):
        st2 = student('21', 'Kim Mariana')
        self.__test_repo.add_student(st2)

        deleted_stud = self.__test_repo.dell('21','0')
        self.assertEqual (self.__test_repo.size(),10)

        stud = self.__test_repo.find('1')
        self.assertIs (stud.getnume(),'Truf Andreea')

        try:
            self.__test_repo.dell('wrk','0')
            self.assertTrue( False)
        except ValueError:
            self.assertTrue(True)

    def test_update(self):
        self.__test_repo.update('1','Carla Maria','1')
        stud=self.__test_repo.find('1')
        self.assertIs(stud.getnume(),'Carla Maria')
        self.__test_repo.update('5','Andra','1')
        stud1=self.__test_repo.find('5')
        self.assertIs(stud1.getnume(),'Andra')


    def tearDown(self) -> None:
        self.__test_repo.dell_all()

if __name__ == '__main__':
    unittest.main()