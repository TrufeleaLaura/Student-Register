import unittest
from Repository.dis_repo import dis_repository
from Service.dis_service import disciplina_service
from domain.entities import disciplina
from Validators.validators import discValidator

class TestCaseStud(unittest.TestCase):
    def setUp(self) -> None:
        repo = dis_repository()
        validator=discValidator()
        self.__test_srv=disciplina_service(repo,validator)

    def test_adaug(self):
        added_dis = self.__test_srv.adaugare_dis('121', 'Engleza', 'Maria Ana')
        self.assertTrue (added_dis.getprofesor() == 'Maria Ana')
        self.assertTrue (added_dis.getIdDisciplina() == '121')

        self.assertTrue (len(self.__test_srv.get_all_discipline()) == 1)

        try:
            added_st = self.__test_srv.adaugare_dis('2', ' ', '')
            self.assertTrue( False)
        except ValueError:
            self.assertTrue(True)

    def test_del(self):
        st1 = self.__test_srv.adaugare_dis('111', 'Educatie fizica', 'Ciobanu Cristina')
        st2 = self.__test_srv.adaugare_dis('101', 'Fundamentele programarii', 'Maria Andreea')
        st3 = self.__test_srv.adaugare_dis('105', 'Geometrie', 'Carla Antonia')

        self.__test_srv.stergere_dis('111', '0')
        self.__test_srv.stergere_dis('Geometrie', '1')
        self.assertTrue( len(self.__test_srv.get_all_discipline()) == 1)

    def test_update(self):
        st1 = self.__test_srv.adaugare_dis('111', 'Educatie fizica', 'Ciobanu Cristina')
        st2 = self.__test_srv.adaugare_dis('101', 'Fundamentele programarii', 'Maria Andreea')
        st3 = self.__test_srv.adaugare_dis('105', 'Geometrie', 'Carla Antonia')

        self.__test_srv.update_dis('111', 'Andreea Macel', '2')
        self.assertTrue( st1.getprofesor() == 'Andreea Macel')
        self.__test_srv.update_dis('105', '117', '0')
        self.assertTrue( st3.getIdDisciplina() == '117')
        try:
            self.__test_srv.update_dis('1', '117', '0')
            self.assertTrue( False)
        except ValueError:
            self.assertTrue(True)

    def test_caut(self):
        st1 = self.__test_srv.adaugare_dis('111', 'Educatie fizica', 'Ciobanu Cristina')
        st2 = self.__test_srv.adaugare_dis('101', 'Fundamentele programarii', 'Maria Andreea')
        st3 = self.__test_srv.adaugare_dis('105', 'Geometrie', 'Carla Antonia')

        caut_st1 = self.__test_srv.cautare_dis('111', '0')
        self.assertTrue( caut_st1.getprofesor() == 'Ciobanu Cristina')
        caut_st2 = self.__test_srv.cautare_dis('Fundamentele programarii', '1')
        self.assertTrue(caut_st2.getIdDisciplina() == '101')

    def test_getall(self):
        st1 = self.__test_srv.adaugare_dis('111', 'Educatie fizica', 'Ciobanu Cristina')
        st2 = self.__test_srv.adaugare_dis('101', 'Fundamentele programarii', 'Maria Andreea')
        st3 = self.__test_srv.adaugare_dis('105', 'Geometrie', 'Carla Antonia')

        self.assertTrue (type(self.__test_srv.get_all_discipline()) == list)
        self.assertTrue (len(self.__test_srv.get_all_discipline()) == 3)