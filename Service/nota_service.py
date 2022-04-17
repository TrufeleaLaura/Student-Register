from domain.entities import notare,student,disciplina
from Validators.validators import noteValidator
from Repository.nota_repo import nota_repository
from Repository.stud_repo import stud_repository
from Repository.dis_repo import dis_repository
from domain.reports_entities import disnota,medie,total_dis
import random

class nota_service:
    def __init__(self, nt_repo, nt_val, stud_repo, dis_repo):
        self.__nt_repo = nt_repo
        self.__nt_val = nt_val #validator
        self.__stud_repo = stud_repo
        self.__dis_repo = dis_repo

    def adaugare_nota(self, stud_id, dis_id, no):
        """
        Creeaza o notare si o sadauga in lista de notari
        :param stud_id: id-ul studentului evaluat
        :param dis_id: id-ul disciplinei la care studentul sete evaluat

        :param nota: nota atribuita
        :return: notarea creat cu datele date
        """
        stud = self.__stud_repo.find(stud_id)
        if stud is None:
            raise ValueError("Nu exista student cu acest id")

        dis = self.__dis_repo.findDis(dis_id)

        if dis is None:
            raise ValueError("Nu exista disciplina cu acest id")

        nota = notare(stud, dis,no)
        self.__nt_val.validatenot(nota)
        self.__nt_repo.add_nota(nota)
        return nota

    def stergere_nota(self,stud_id, dis_id,no):
        """
        Creeaza o notare si sterge din lista daca se regaseste
        """
        stud = self.__stud_repo.find(stud_id)
        if stud is None:
            raise ValueError("Nu exista student cu acest id")

        dis = self.__dis_repo.findDis(dis_id)

        if dis is None:
            raise ValueError("Nu exista disciplina cu acest id")

        nota = notare(stud, dis, no)
        self.__nt_val.validatenot(nota)
        self.__nt_repo.dell_nota(nota)

    def modific_nota(self,stud_id,dis_id,no,value):
        """

        Modifica nota studentului la o disciplina
        """
        stud = self.__stud_repo.find(stud_id)
        if stud is None:
            raise ValueError("Nu exista student cu acest id")

        dis = self.__dis_repo.findDis(dis_id)

        if dis is None:
            raise ValueError("Nu exista disciplina cu acest id")

        nota = notare(stud, dis, no)
        self.__nt_val.validatenot(nota)
        self.__nt_repo.modif_nota(nota,value)

    def adauga_ran(self,nrnote):
        stud=self.__stud_repo.get_all_students()
        dis=self.__dis_repo.get_discipline()
        li=[]
        if len(dis)==0:
            raise ValueError("Nu exista discipline")
        if len(stud)==0:
            raise ValueError("Nu exista studenti")
        for _nrno in range(nrnote):
            s=random.choice(stud) #se alege random student
            d=random.choice(dis)
            n=str(random.randint(1,10))
            nota=notare(s,d,n)
            self.__nt_repo.add_nota(nota)
            li.append(nota)
        return li

    def get_all(self):
        return self.__nt_repo.get_all_note()

    def get_all_pt_dis(self, id_dis):
        """
        Returneaza o lista cu toate notele pentru o disciplina data
        :return: lista cu toate notele existente pentru disciplina data
        """
        all_note = self.__nt_repo.get_all_note()
        dis_note = []
        for no in all_note:
            if no.getdis().getIdDisciplina() == id_dis:
                dis_note.append(no)
        return dis_note

    def bubbleSort(self,lista,cmp,reverse=False):
        """
        Functia sorteaza crescator o lista dupa o functie cmp
        :param lista: lista care trebuie sortata
        :param cmp: functia de comparare dupa care se sorteaza
        :return: lista sortata
        """
        n = len(lista)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                    if cmp(lista[j] ,lista[j + 1])==False:
                        lista[j], lista[j + 1] = lista[j + 1], lista[j]
        if reverse==False:
            return lista
        else:
            lista.reverse()
            return lista

    def cmpnume(self,a,b):
        if a.getstudent().getnume()<b.getstudent().getnume():
            return True
        return False
    def cmpnota(self,a,b):#dublu criteriu
        if a.getnota()<b.getnota():
            return True
        elif a.getnota()==b.getnota() and a.getstudent().getIdstudent()<b.getstudent().getIdstudent():
            return True
        return False
    def cmpavg(self,a,b):
        if a.getavgnote()<b.getavgnote():
            return True
        return False

    def cmpavg1(self,a,b):#dublu criteriu
        if a.getavg()<b.getavg():
            return True
        elif a.getavg()==b.getavg() and a.getprof()<b.getprof():
            return True
        return False

    def shellsort(self,li, n,cmp,reverse=False):
        h = n // 2
        while h > 0:
            for i in range(h, n):
                t = li[i]
                j = i
                while j >= h and cmp(li[j - h],t)==False:
                    li[j] = li[j - h]
                    j -= h
                li[j] = t
            h = h // 2
        if reverse == False:
            return li
        else:
            li.reverse()
            return li

    def get_sortnume(self,id_dis):
        """
        Returneaza lista sortata cu studentii si notele la o disciplina data
        :return: lista ordonata alfabetic dupa nume
        :raises: ValueError daca nu exista disciplina cu id dat

        """
        dis = self.__dis_repo.findDis(id_dis)
        if dis is None:
            raise ValueError("Nu exista disciplina cu acest id")

        note_dis = self.get_all_pt_dis(id_dis) #lista cu elementele de obiect nota care au nota la disciplina data
        #sorted_stud = sorted(note_dis, key=lambda x: x.getstudent().getnume(), reverse=False)
        sorted_stud=self.shellsort(note_dis,len(note_dis),cmp=self.cmpnume,reverse=False)
        result = []
        for nota in sorted_stud:
            sorted_stud_dto = disnota(nota.getstudent().getnume(), nota.getdis().getnumedis(),  nota.getnota())
            result.append(sorted_stud_dto)
        return result

    def get_sortnota(self, id_dis):
        """
        Returneaza lista sortata cu studentii si notele la o disciplina data
        :return: lista ordonata descrescator  dupa nota
        :raises: ValueError daca nu exista disciplina cu id dat

        """
        dis = self.__dis_repo.findDis(id_dis)
        if dis is None:
            raise ValueError("Nu exista disciplina cu acest id")

        note_dis = self.get_all_pt_dis(id_dis)  # lista cu elementele de obiect nota care au nota la disciplina data
        #sorted_not = sorted(note_dis, key=lambda x: x.getnota(), reverse=True)
        sorted_not = self.bubbleSort(note_dis, cmp=self.cmpnota,reverse=True)
        result = []
        for nota in sorted_not:
            sorted_not_dto = disnota(nota.getstudent().getnume(), nota.getdis().getnumedis(), nota.getnota())
            result.append(sorted_not_dto)
        return result

    def get_sort_medie(self):
      """
      Returneaza primii 20% de studenti dupa media notelor la toate disciplinele
      :return: lista
      """
      all_note=self.__nt_repo.get_all_note()
      stud_note={} # va fi {stud_id:dto}
      for no in all_note:
          if no.getstudent().getIdstudent() not in stud_note:
              dto=medie(no.getstudent().getnume(),no.getnota())
              stud_note[no.getstudent().getIdstudent()]=dto
          else:
              stud_note[no.getstudent().getIdstudent()].incr_note()
              stud_note[no.getstudent().getIdstudent()].addnote(no.getnota())

      for stud_id, avg_note in stud_note.items():
          avg_note.calcul()
      li_medii=list(stud_note.values())
      #sorted_not = sorted(li_medii, key=lambda x: x.getavgnote(), reverse=True)
      sorted_not=self.bubbleSort(li_medii,cmp=self.cmpavg,reverse=True)
      lg=int(len(sorted_not)*0.2)
      return sorted_not[:lg]

    def get_sort_medie_dis(self):
         """
         Returneaza lista cu primele 50% de discipline cu cea mai mare medie ordonata dupa medie,repectiv numele profesorului alfabetic
         :return:lista cu discipline de tip total_dis
         """
         all_note=self.__nt_repo.get_all_note()
         dis_note={} # va fi {dis_id:dto}
         for no in all_note:
           if no.getdis().getIdDisciplina() not in dis_note:
              dto=total_dis(no.getdis().getnumedis(),no.getdis().getprofesor(),no.getnota())
              dis_note[no.getdis().getIdDisciplina()]=dto
           else:
              dis_note[no.getdis().getIdDisciplina()].incr_note()
              dis_note[no.getdis().getIdDisciplina()].addnote(no.getnota())

         for dis_id, avg_note in dis_note.items():
                avg_note.calcul()
         li_medii=list(dis_note.values())
         #sorted_not = sorted(li_medii, key=lambda x: (x.getavg(), x.getprof()), reverse=True)
         sorted_not=self.bubbleSort(li_medii,cmp=self.cmpavg1,reverse=True)
         lg=int(len(sorted_not)*0.5)
         return sorted_not[:lg]

    def get__all(self):
            return self.__nt_repo


#TESTE

def test_adaugare():
    st1 = student('1', 'Truf Andreea')
    st2 = student('2', 'Boba Leo')
    st3 = student('3', 'Carnu Maria')
    st4 = student('4', 'Darda Leo')
    test_repo = stud_repository()
    test_repo.add_student(st1)
    test_repo.add_student(st2)
    test_repo.add_student(st3)
    test_repo.add_student(st4)

    dis1 = disciplina('101', 'Fundamentele programarii', 'Maria Andreea')
    dis2 = disciplina('102', 'Analiza', 'Boba Leo')
    dis3 = disciplina('103', 'Geografie', 'Carnu Maria')

    test_repo_dis = dis_repository()
    test_repo_dis.add_dis(dis1)
    test_repo_dis.add_dis(dis2)
    test_repo_dis.add_dis(dis3)

    note_repo=nota_repository()
    note_val=noteValidator()

    test_srv=nota_service(note_repo,note_val,test_repo,test_repo_dis)
    creat=test_srv.adaugare_nota('4','103',6)
    assert creat.getstudent()==test_repo.find('4')
    assert creat.getdis()==test_repo_dis.findDis('103')
    assert creat.getnota()==6

def test_stergere():
    st1 = student('1', 'Truf Andreea')
    st2 = student('2', 'Boba Leo')
    st3 = student('3', 'Carnu Maria')
    st4 = student('4', 'Darda Leo')
    test_repo = stud_repository()
    test_repo.add_student(st1)
    test_repo.add_student(st2)
    test_repo.add_student(st3)
    test_repo.add_student(st4)

    dis1 = disciplina('101', 'Fundamentele programarii', 'Maria Andreea')
    dis2 = disciplina('102', 'Analiza', 'Boba Leo')
    dis3 = disciplina('103', 'Geografie', 'Carnu Maria')

    test_repo_dis = dis_repository()
    test_repo_dis.add_dis(dis1)
    test_repo_dis.add_dis(dis2)
    test_repo_dis.add_dis(dis3)

    note_repo = nota_repository()
    note_val = noteValidator()

    test_srv = nota_service(note_repo, note_val, test_repo, test_repo_dis)
    creat = test_srv.adaugare_nota('4', '103',6)
    creat1=test_srv.adaugare_nota('4','101',8)
    creat2=test_srv.adaugare_nota('3','103',9)
    assert len(test_srv.get_all())==3
    test_srv.stergere_nota('4','103',6)
    assert len(test_srv.get_all())==2

def test_modificare():
    st1 = student('1', 'Truf Andreea')
    st2 = student('2', 'Boba Leo')
    st3 = student('3', 'Carnu Maria')
    st4 = student('4', 'Darda Leo')
    test_repo = stud_repository()
    test_repo.add_student(st1)
    test_repo.add_student(st2)
    test_repo.add_student(st3)
    test_repo.add_student(st4)

    dis1 = disciplina('101', 'Fundamentele programarii', 'Maria Andreea')
    dis2 = disciplina('102', 'Analiza', 'Boba Leo')
    dis3 = disciplina('103', 'Geografie', 'Carnu Maria')

    test_repo_dis = dis_repository()
    test_repo_dis.add_dis(dis1)
    test_repo_dis.add_dis(dis2)
    test_repo_dis.add_dis(dis3)

    note_repo = nota_repository()
    note_val = noteValidator()
    test_srv = nota_service(note_repo, note_val, test_repo, test_repo_dis)
    creat = test_srv.adaugare_nota('4', '103', 6)
    creat1 = test_srv.adaugare_nota('4', '101', 8)
    test_srv.modific_nota('4','101',8,10)
    assert creat1.getnota()==10
    test_srv.modific_nota('4','103',6,9)
    assert creat.getnota()==9

def test_s1():
    st1 = student('1', 'Truf Andreea')
    st2 = student('2', 'Boba Leo')
    st3 = student('3', 'Carnu Maria')
    st4 = student('4', 'Darda Leo')
    test_repo = stud_repository()
    test_repo.add_student(st1)
    test_repo.add_student(st2)
    test_repo.add_student(st3)
    test_repo.add_student(st4)

    dis1 = disciplina('101', 'Fundamentele programarii', 'Maria Andreea')
    dis2 = disciplina('102', 'Analiza', 'Boba Leo')
    dis3 = disciplina('103', 'Geografie', 'Carnu Maria')

    test_repo_dis = dis_repository()
    test_repo_dis.add_dis(dis1)
    test_repo_dis.add_dis(dis2)
    test_repo_dis.add_dis(dis3)

    note_repo = nota_repository()
    note_val = noteValidator()
    test_srv = nota_service(note_repo, note_val, test_repo, test_repo_dis)
    creat = test_srv.adaugare_nota('4', '103', 6)
    creat1 = test_srv.adaugare_nota('4', '101', 8)
    create2=test_srv.adaugare_nota('3', '101', 7)
    create3=test_srv.adaugare_nota('2', '101', 5)
    create4=test_srv.adaugare_nota('1', '101', 4)
    tes=test_srv.get_sortnume('101')
    #assert tes[0].getstudnume()=='Boba Leo'
    #assert tes[1].getnota()==7

def test_s2():
    st1 = student('1', 'Truf Andreea')
    st2 = student('2', 'Boba Leo')
    st3 = student('3', 'Carnu Maria')
    st4 = student('4', 'Darda Leo')
    test_repo = stud_repository()
    test_repo.add_student(st1)
    test_repo.add_student(st2)
    test_repo.add_student(st3)
    test_repo.add_student(st4)

    dis1 = disciplina('101', 'Fundamentele programarii', 'Maria Andreea')
    dis2 = disciplina('102', 'Analiza', 'Boba Leo')
    dis3 = disciplina('103', 'Geografie', 'Carnu Maria')

    test_repo_dis = dis_repository()
    test_repo_dis.add_dis(dis1)
    test_repo_dis.add_dis(dis2)
    test_repo_dis.add_dis(dis3)

    note_repo = nota_repository()
    note_val = noteValidator()
    test_srv = nota_service(note_repo, note_val, test_repo, test_repo_dis)
    creat = test_srv.adaugare_nota('4', '103', 6)
    create2=test_srv.adaugare_nota('3', '101', 7)
    creat1 = test_srv.adaugare_nota('4', '101', 8)
    create3=test_srv.adaugare_nota('2', '101', 5)
    create4=test_srv.adaugare_nota('1', '101', 4)
    tes=test_srv.get_sortnota('101')
    assert tes[0].getstudnume()=='Darda Leo'
    assert tes[1].getnota()==7
    assert tes[2].getdisnume()=='Fundamentele programarii'

def test_s3():
    st1 = student('1', 'Truf Andreea')
    st2 = student('2', 'Boba Leo')
    st3 = student('3', 'Carnu Maria')
    st4 = student('4', 'Darda Leo')
    st5=student('5','andrei')
    st6 = student('6','maria')
    st7 = student('7','catalina')
    st8 = student('8','andra')
    st9 = student('9','andreea')
    st10 = student('10','valentin')

    test_repo = stud_repository()
    test_repo.add_student(st1)
    test_repo.add_student(st2)
    test_repo.add_student(st3)
    test_repo.add_student(st4)
    test_repo.add_student(st5)
    test_repo.add_student(st6)
    test_repo.add_student(st7)
    test_repo.add_student(st8)
    test_repo.add_student(st9)
    test_repo.add_student(st10)

    dis1 = disciplina('101', 'Fundamentele programarii', 'Maria Andreea')
    dis2 = disciplina('102', 'Analiza', 'Boba Leo')
    dis3 = disciplina('103', 'Geografie', 'Carnu Maria')

    test_repo_dis = dis_repository()
    test_repo_dis.add_dis(dis1)
    test_repo_dis.add_dis(dis2)
    test_repo_dis.add_dis(dis3)

    note_repo = nota_repository()
    note_val = noteValidator()
    test_srv = nota_service(note_repo, note_val, test_repo, test_repo_dis)
    creat = test_srv.adaugare_nota('4', '103', 6)
    test_srv.adaugare_nota('4', '101', 8)
    test_srv.adaugare_nota('4', '102', 3)
    test_srv.adaugare_nota('3', '101', 7)
    test_srv.adaugare_nota('3', '102', 4)
    test_srv.adaugare_nota('2', '101', 5)
    test_srv.adaugare_nota('1', '101', 4)
    test_srv.adaugare_nota('1', '102', 8)
    test_srv.adaugare_nota('1', '103', 6)
    test_srv.adaugare_nota('5', '102', 7)
    test_srv.adaugare_nota('6', '103', 8)
    test_srv.adaugare_nota('7', '101', 2)
    test_srv.adaugare_nota('8', '103', 10)
    test_srv.adaugare_nota('9', '103', 4)
    test_srv.adaugare_nota('9', '102', 2)
    test_srv.adaugare_nota('10', '103', 7)
    tes = test_srv.get_sort_medie()
    assert tes[0].getnume() == 'andra'
    assert tes[1].getnume() == 'maria'

def test_s4():
    st1 = student('1', 'Truf Andreea')
    st2 = student('2', 'Boba Leo')
    st3 = student('3', 'Carnu Maria')
    st4 = student('4', 'Darda Leo')
    st5 = student('5', 'andrei')
    st6 = student('6', 'maria')
    st7 = student('7', 'catalina')
    st8 = student('8', 'andra')
    st9 = student('9', 'andreea')
    st10 = student('10', 'valentin')

    test_repo = stud_repository()
    test_repo.add_student(st1)
    test_repo.add_student(st2)
    test_repo.add_student(st3)
    test_repo.add_student(st4)
    test_repo.add_student(st5)
    test_repo.add_student(st6)
    test_repo.add_student(st7)
    test_repo.add_student(st8)
    test_repo.add_student(st9)
    test_repo.add_student(st10)

    dis1 = disciplina('101', 'Fundamentele programarii', 'Maria Andreea')
    dis2 = disciplina('102', 'Analiza', 'Boba Leo')
    dis3 = disciplina('103', 'Geografie', 'Carnu Maria')
    dis4=disciplina('104','Logica','Andreea')

    test_repo_dis = dis_repository()
    test_repo_dis.add_dis(dis1)
    test_repo_dis.add_dis(dis2)
    test_repo_dis.add_dis(dis3)
    test_repo_dis.add_dis(dis4)

    note_repo = nota_repository()
    note_val = noteValidator()
    test_srv = nota_service(note_repo, note_val, test_repo, test_repo_dis)
    creat = test_srv.adaugare_nota('4', '103', 6)
    test_srv.adaugare_nota('4', '101', 8)
    test_srv.adaugare_nota('4', '102', 3)
    test_srv.adaugare_nota('3', '101', 7)
    test_srv.adaugare_nota('3', '102', 4)
    test_srv.adaugare_nota('2', '101', 5)
    test_srv.adaugare_nota('1', '101', 4)
    test_srv.adaugare_nota('1', '102', 8)
    test_srv.adaugare_nota('1', '103', 6)
    test_srv.adaugare_nota('5', '102', 7)
    test_srv.adaugare_nota('6', '103', 8)
    test_srv.adaugare_nota('7', '101', 2)
    test_srv.adaugare_nota('9', '103', 4)
    test_srv.adaugare_nota('10','104',10)
    tes=test_srv.get_sort_medie_dis()
    assert tes[0].getnume()=='Logica'
    assert tes[1].getnrnote()==4
    assert len(tes)==2







test_adaugare()
test_stergere()
test_modificare()
test_s1()
test_s2()
test_s3()
test_s4()



