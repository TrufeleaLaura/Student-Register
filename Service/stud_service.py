from domain.entities import student
from Validators.validators import studValidator
from Repository.stud_repo import stud_repository
from Validators.validatori import *
import random

class student_service():
    """
    Este responsabil de efectuarea operatiilor cerute de utilizator
    """
    def __init__(self,repo,validator):
        """
        Initializeaza service
        :param
        repo: obiect de tip repo care ajuta la gestionarea listei de studenti
        repo: stud_repository
        validator: validator pentru verificarea studentilor
        """
        self.__repo=repo
        self.__validator=validator

    def adaugare_student(self, id, nume):
        """
        Adauga serial
        :param id:id student
        :param nume: nume student
        :return: obiectul de tip Student creat
        :raises: ValueError daca studentul are date invalide
        """
        s=student(id,nume)
        self.__validator.validatestud(s)
        self.__repo.add_student(s)
        return s

    def stergere_student(self,value,poz):
        """
        Sterge studentul
        value:data dupa care se va identifica studentul sters
        poz:pozitia in entitAte
        """
        validator1(value,poz)
        self.__repo.dell(value,poz)

    def update_stud(self, id, value,poz):
        """
        Modifica datele studentului
        :param id: id-ul student de modificat
        value-data cu care se va schimba,poz-ce se va schimba
        :return: se modifica studentul
        :raises: ValueError daca noile date nu sunt valide
        """

        validator1(value,poz)
        return self.__repo.update(id, value,poz)

    def cautare_stud(self,value,poz):
        """Returneaza studentul cautat dupa  criteriul dat"""
        if poz=='0':
            return self.__repo.find(value)
        if poz=='1':
            return self.__repo.find1(value)

    def filter_prefix(self,prefix,nume):
         """
         Verifica daca prefixul face parte din numele studentului
         :return: True or False
         """
         l1=[]#litere prefix
         l2=[]#litere nume student
         for lit in prefix:
            l1.append(lit)
         val=True
         for lit in nume:
            l2.append(lit)
         for lit in range(len(l1)):
            if(l1[lit]!=l2[lit]):
                val=False
         return val

    def filter_by_prefix(self, prefix):
        """
        Returneaza lista de studenti care contin prefixul acela in nume
        :return: lista de studenti care indeplinesc criteriul
        """
        all_students = self.get_all_students()
        filt_list = [stud for stud in all_students if self.filter_prefix(prefix,stud.getnume())==True]
        return filt_list

    def adauga_random(self):
        """
        Genereaza valori random pt id,nume
        """
        id=random.randint(1,100)
        nume=random_string_generator(7)
        s=student(id,nume)
        self.__repo.add_ran(s)
        return s


    def get_all_students(self):
        """
        Returneaza o lista cu toti studentii
        """
        return self.__repo.get_all_students()

