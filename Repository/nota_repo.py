from domain.entities import student, disciplina, notare
from Repository.stud_repo import stud_repository,RepoStudFile
from Repository.dis_repo import dis_repository,RepoDisFile

class nota_repository:
    def __init__(self):
        self.__note = []

    def find(self, n):
        """
        Cauta nota in lista de evaluari
        :param n: nota cautata
        :return: nota cautata daca exista in lista, None altfel
        """
        for no in self.__note:
            if n == no:
                return no
        return None

    def add_nota(self, nota):
        """
        Adauga o evaluare in lista
        :return: -; se adauga nota la lista de evaluari
        """
        n = self.find(nota)
        if n is not None:
            raise ValueError("Exista deja aceasta nota la disciplina studentului")
        self.__note.append(nota)

    def add_nota_RECURSIV(self,i,nota):
        if i>=len(self.__note):
            self.__note.append(nota)
            return
        elif self.__note[i]==nota:
            raise ValueError("Exista deja aceasta nota la disciplina studentului")
        else:
            self.add_nota_RECURSIV(i+1,nota)

    def dell_nota(self,nota):
        """
        Sterge o evaluare a unui student la o disciplina
        """
        n=self.find(nota)
        if n is None:
            raise ValueError("Nu exista nota")
        else:
            self.__note = [el for el in self.__note if (el.getnota() != nota.getnota() or el.getstudent()!=nota.getstudent() or el.getdis()!=nota.getdis())]

    def modif_nota(self,cr,nota):
        """
        Modifica o nota a unui student la o disciplina
        """
        cr1 = self.find(cr)
        if cr1 is None:
            raise ValueError("Nu exista nota")
        else:
            for el in self.__note:
                if el.getnota() == cr.getnota() and el.getstudent()==cr.getstudent() and el.getdis()==cr.getdis():
                    el.setnota(nota)

    def add_ran(self,nota):
        self.__note.append(nota)

    def get_all_note(self):
        """
        Returneaza o lista cu toate notele disponibile
        :return: lista cu note disponibile
        :rtype: list of notare objects
        """
        return self.__note

    def dell_all(self):
        self.__note=[]

class RepoNotFile(nota_repository):
    def __init__(self, filename,stud_repo,dis_repo):
        nota_repository.__init__(self)
        self.__filename = filename
        self.__stud_repo=stud_repo
        self.__dis_repo=dis_repo
        self.__load_from_file()

    def __load_from_file(self):
        try:
            with open(self.__filename, 'r') as f1:
                val = False
                while not val:
                    line = f1.readline().strip()
                    if line == "":
                        val = True
                    else:
                        stud_id = line
                        dis_id = f1.readline().strip()
                        nota = f1.readline().strip()
                        st = self.__stud_repo.find(stud_id)
                        dis = self.__dis_repo.findDis(dis_id)
                        a = notare(st, dis, nota)
                        nota_repository.add_nota(self, a)
        except ValueError:
            raise print("fisier invalid")

    def __save_to_file(self):
        not_list = nota_repository.get_all_note(self)
        with open(self.__filename, 'w') as f:
            for no in not_list:
                dis_string = f"{str(no.getstudent().getIdstudent())}\n{str(no.getdis().getIdDisciplina())}\n+{str(no.getnota())}\n"
                f.write(dis_string)
    """
    def __load_from_file(self):
        try:
            f = open(self.__filename, 'r')
        except ValueError:
            raise print('Fisier invalid')
        lines = f.readlines()
        for line in lines:
            stud_id, dis_id, nota = [token.strip() for token in line.split(';')]
            st=self.__stud_repo.find(stud_id)
            dis=self.__dis_repo.findDis(dis_id)
            a = notare(st, dis,nota)
            nota_repository.add_nota(self, a)
        f.close()

    def __save_to_file(self):
        not_list = nota_repository.get_all_note(self)
        with open(self.__filename, 'w') as f:
            for no in not_list:
                no_string = str(no.getstudent().getIdstudent()) + ';' + str(no.getdis().getIdDisciplina()) + ';' + str(no.getnota())+'\n'
                f.write(no_string)
    """

    def add_nota(self, nota):
        nota_repository.add_nota(self, nota)
        self.__save_to_file()

    def add_ran(self,nota):
        nota_repository.add_ran(self,nota)
        self.__save_to_file()

    def modif_nota(self, cr,nota):
        updated_not = nota_repository.modif_nota(self,cr,nota)
        self.__save_to_file()
        return updated_not

    def dell_nota(self, nota):
        deleted_not = nota_repository.dell_nota(self, nota)
        self.__save_to_file()
        return deleted_not

    def get_all_note(self):
        return nota_repository.get_all_note(self)

    def find(self, no):
        return nota_repository.find(self, no)

    def dell_all(self):
        nota_repository.dell_all(self)
        self.__save_to_file()
    def add_nota_RECURSIV(self,i,nota):
        nota_repository.add_nota_RECURSIV(self,i,nota)
        self.__save_to_file()
