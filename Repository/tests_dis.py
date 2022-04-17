import unittest
from Repository.dis_repo import dis_repository
from domain.entities import disciplina

class TestCaseStud(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_repo = dis_repository()
        self.setup_test_repo_dis()

    def setup_test_repo_dis(self):
            dis1 = disciplina('101', 'Fundamentele programarii', 'Maria Andreea')
            dis2 = disciplina('102', 'Analiza', 'Boba Leo')
            dis3 = disciplina('103', 'Geografie', 'Carnu Maria')
            dis4 = disciplina('104', 'Algebra', 'Darda Leo')
            dis5 = disciplina('105', 'Geometrie', 'Carla Antonia')
            dis6 = disciplina('106', 'Psihologie', 'Marian Claudiu')
            dis7 = disciplina('107', 'Logica', 'Andrei Fasiu')

            self.__test_repo.add_dis(dis1)
            self.__test_repo.add_dis(dis2)
            self.__test_repo.add_dis(dis3)
            self.__test_repo.add_dis(dis4)
            self.__test_repo.add_dis(dis5)
            self.__test_repo.add_dis(dis6)
            self.__test_repo.add_dis(dis7)

    def test_findDis(self):
        p = self.__test_repo.findDis('101')
        self.assertIs (p.getprofesor(),'Maria Andreea')

        p1 = self.__test_repo.findDis('112')
        self.assertIsNone (p1)

        p2 = self.__test_repo.find1Dis('Analiza')
        self.assertIs (p2.getprofesor(),'Boba Leo')

        p3 = self.__test_repo.find2Dis('Marian Claudiu')
        self.assertIs( p3.getIdDisciplina(), '106')

    def test_sizedis(self):
        self.assertEqual (self.__test_repo.sizedis(),7)

        self.__test_repo.dell_dis('107', '0')
        self.assertEqual( self.__test_repo.sizedis(),6)

        self.__test_repo.add_dis(disciplina('111', 'Educatie fizica', 'Ciobanu Cristina'))
        self.assertEqual(self.__test_repo.sizedis(),7)

    def test_get_all(self):
        crt_dis = self.__test_repo.get_discipline()
        self.assertIs (type(crt_dis), list)
        self.assertEqual (len(crt_dis), 7)

        self.__test_repo.dell_dis('107', '0')
        crt_dis = self.__test_repo.get_discipline()
        self.assertEqual (len(crt_dis), 6)

    def test_add_dis(self):
        dis1 = disciplina('120', 'Algebra', 'Serena Andreea')
        self.__test_repo.add_dis(dis1)
        self.assertEqual (self.__test_repo.sizedis(), 8)

        try:
            # duplicate id
            #test_repo.add_dis(dis2)
            self.__test_repo.add_dis(dis1)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

    def test_dell_dis(self):
        self.__test_repo.dell_dis('101', '0')
        self.assertEqual (self.__test_repo.sizedis(), 6)
        try:
            self.__test_repo.dell_dis('wrk', '0')
            self.assertTrue( False)
        except ValueError:
            self.assertTrue( True)

    def test_update(self):
        self.__test_repo.update_dis('105', 'Carla Maria', '2')
        dis1=self.__test_repo.findDis('105')
        self.assertIs(dis1.getprofesor(),'Carla Maria')
        self.__test_repo.update_dis('104', 'Programare', '1')
        dis2 = self.__test_repo.find1Dis('Programare')
        self.assertIs( dis2.getIdDisciplina(), '104')

    def tearDown(self) -> None:
        self.__test_repo.dell_all()

if __name__ == '__main__':
        unittest.main()