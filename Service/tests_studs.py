import unittest
from Service.stud_service import student_service
from Repository.stud_repo import stud_repository
from Validators.validators import studValidator
from domain.entities import notare,disciplina,student
class TestCaseStud(unittest.TestCase):
    def setUp(self) -> None:
        repo=stud_repository()
        validator = studValidator()
        self.__test_srv = student_service(repo,validator)

    def test_filter_by_prefix(self):
        self.__test_srv.adaugare_student('1', 'Urlici marian')
        self.__test_srv.adaugare_student('2', 'Boba Cas')
        self.__test_srv.adaugare_student('3', 'Borl Curea')

        filtered_list = self.__test_srv.filter_by_prefix('Bo')
        self.assertEqual(len(filtered_list),2)

    def test_adaugare(self):
        added_st = self.__test_srv.adaugare_student('1','Truf Andreea')
        self.assertIs (added_st.getnume(), 'Truf Andreea')
        self.assertIs (added_st.getIdstudent(),'1')

        self.assertEqual (len(self.__test_srv.get_all_students()), 1)

        try:
            added_st = self.__test_srv.adaugare_student('2',' ')
            self.assertTrue( False)
        except ValueError:
            self.assertTrue(True)

    def test_delete(self):
        st1 = self.__test_srv.adaugare_student('1', 'Truf Andreea')
        st2 = self.__test_srv.adaugare_student('2', 'Maria anabela')
        st3 =self.__test_srv.adaugare_student('3','Mara Antonia')

        self.__test_srv.stergere_student('1','0')
        self.__test_srv.stergere_student('3','0')
        self.assertTrue( len(self.__test_srv.get_all_students())==1)

    def test_update(self):
        st1 = self.__test_srv.adaugare_student('1', 'Truf Andreea')
        st2 = self.__test_srv.adaugare_student('2', 'Maria anabela')
        st3 = self.__test_srv.adaugare_student('3', 'Mara Antonia')

        self.__test_srv.update_stud('1','Andreea Macel','1')
        self.assertTrue( st1.getnume()=='Andreea Macel')
        self.__test_srv.update_stud('3','5','0')
        self.assertTrue( st3.getIdstudent()=='5')

    def test_cautare(self):
        st1 = self.__test_srv.adaugare_student('1', 'Truf Andreea')
        st2 = self.__test_srv.adaugare_student('2', 'Maria anabela')
        st3 = self.__test_srv.adaugare_student('3', 'Mara Antonia')

        caut_st1=self.__test_srv.cautare_stud('1','0')
        self.assertTrue( caut_st1.getnume()=='Truf Andreea')
        caut_st2=self.__test_srv.cautare_stud('3','0')
        self.assertTrue( caut_st2.getnume()=='Mara Antonia')

    def test_getall(self):
        st1 = self.__test_srv.adaugare_student('1', 'Truf Andreea')
        st2 = self.__test_srv.adaugare_student('2', 'Maria anabela')
        st3 = self.__test_srv.adaugare_student('3', 'Mara Antonia')
        self.assertTrue (type(self.__test_srv.get_all_students()) == list)
        self.assertTrue (len(self.__test_srv.get_all_students()) == 3)

if __name__ == '__main__':
    unittest.main()