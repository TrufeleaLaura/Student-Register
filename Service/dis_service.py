from domain.entities import disciplina
from Validators.validators import discValidator
from Repository.dis_repo import dis_repository
from Validators.validatori import *

class disciplina_service():
    """
    Este responsabil de efectuarea operatiilor cerute de utilizator
    """
    def __init__(self,repo,validator):
        """
        Initializeaza service
        :param
        repo: obiect de tip repo care ajuta la gestionarea listei de disciplina
        repo: dis_repository
        validator: validator pentru verificarea disciplinei
        """
        self.__repo=repo
        self.__validator=validator

    def adaugare_dis(self, id, numedis, numeprof):
        """
        Adauga serial
        :param id:id disciplina
        :param nume: nume disciplina
        :return: obiectul de tip disciplina creat
        :raises: ValueError daca disciplina are date invalide
        """
        dis=disciplina(id,numedis,numeprof)
        self.__validator.validatedis(dis)
        self.__repo.add_dis(dis)
        return dis

    def stergere_dis(self,value,poz):
        """
        Sterge disciplina
        value:data dupa care se va identifica disciplina stearsa
        poz:pozitia in entitAte
        """
        validator2(value,poz)
        self.__repo.dell_dis(value,poz)

    def update_dis(self, id, value,poz):
        """
        Modifica datele disciplinei
        :param id: id-ul disciplinei de modificat
        value-data cu care se va schimba,poz-ce se va schimba
        :return: se modifica disciplina
        :raises: ValueError daca noile date nu sunt valide
        """
        validator2(value,poz)
        return self.__repo.update_dis(id, value,poz)

    def cautare_dis(self, value,poz):
        """Returneaza disciplina cautata dupa criteriul dat"""

        validator2(value,poz)
        if poz=='0':
            return self.__repo.findDis(value)
        if poz=='1':
            return self.__repo.find1Dis(value)
        if poz=='2':
            return self.__repo.find2Dis(value)

    def adauga_random(self):
        id = random.randint(101, 150)
        numedis = random_string_generator(7)
        numeprof=random_string_generator(10)
        d = disciplina(id, numedis,numeprof)
        self.__repo.add_ran(d)
        return d

    def get_all_discipline(self):
        """
        Returneaza o lista cu toate disciplinele
        """
        return self.__repo.get_discipline()






































