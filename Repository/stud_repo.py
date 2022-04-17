from domain.entities import student
class stud_repository:
    """
        Clasa creata cu responsabilitatea de a gestiona  multimea de studenti
    """
    def __init__(self):
        """
        Este o lista care contine toti studentii introdusi,lista fiind la inceput goala
        """
        self.__students=[]

    def size(self):
        """
        Returneaza numarul de studenti din multime
        :return: numar studenti existenti
        """
        return len(self.__students)

    def find(self, id):
        """
        Cauta studentul cu id dat
        :param id: id dat
        :return: studentul cu id dat, None daca nu exista
        """
        for st in self.__students:
            if st.getIdstudent() ==id:
                return st
        return None
    def find_RECURSIV(self,i,id):
        if i>=len(self.__students):
            return None
        elif self.__students[i].getIdstudent()==id:
            return self.__students[i]
        else:
            return self.find_RECURSIV(i+1,id)


    def find1(self, nume):
        """
        Cauta student cu nume dat
        :param nume: nume dat
        :return: student cu nume dat, None daca nu exista
               """
        for st in self.__students:
            if st.getnume() == nume:
                return st
        return None

    def add_student(self,student):
       """
        Adauga un student in lista
        param: studentul care se adauga de tip student
        return:lista care se modifica prin adaugarea studentului"""
       if self.find(student.getIdstudent()) is not None:
           raise ValueError('Exista deja student cu acest id.')

       self.__students.append(student)

    def add_ran(self,student):
        self.__students.append(student)

    def dell(self,value,poz):
        """
        Sterge un student dupa criteriul ales de utilizator
        :param id: value:valoarea criteriului ales,poz-pozitia in entitata student(0-id,1-nume)
        :return: syudentul sters
        """

        if poz=='0':
            st=self.find(value)
            if st is None:
                raise ValueError('Nu exista student cu acest id.')
            else:
                self.__students=[el for el in self.__students if el.getIdstudent()!=value]
        if poz=='1':
            st = self.find1(value)
            if st is None:
                raise ValueError('Nu exista student cu acest nume.')
            else:
                self.__students=[el for el in self.__students if el.getnume()!=value]

    def update(self, id, value,poz):
        """
        Modifica valoarea parametrului poz(0 sau 1) din student
        :param id: idul studentului pe care vrem sa il modificam
        :param value: data pe care vrem sa o modificam in interiorul studentului
        poz:pozitia in obiectul student(0-id, 1-nume)
        """
        st = self.find(id)
        if st is None:
            raise ValueError('Nu exista student cu acest id.')
        else:
            for elem in self.__students:
                if elem.getIdstudent()==id:
                    if poz=='0':
                            elem.setIdstudent(value)
                    if poz=='1':
                        elem.setnume(value)

    def get_all_students(self):
        """
        Functia returneaza o lista cu toti studentii existenti
        return: lista cu studentii existenti sau [] daca nu exista inca studenti
        rtype: lista de obiecte de tip student

        """
        return self.__students

    def dell_all(self):
        self.__students=[]


class RepoStudFile(stud_repository):
    def __init__(self, filename):
        stud_repository.__init__(self)
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        try:
            with open(self.__filename, 'r') as f1:
                val=False
                while not val:
                    line=f1.readline().strip()
                    if line=="":
                        val=True
                    else:
                        stud_id=line
                        stud_name=f1.readline().strip()
                        a = student(stud_id, stud_name)
                        stud_repository.add_student(self, a)
        except ValueError:
            raise print("fisier invalid")

    def __save_to_file(self):
        stud_list = stud_repository.get_all_students(self)
        with open(self.__filename, 'w') as f:
            for st in stud_list:
                st_string = f"{str(st.getIdstudent())}\n{str(st.getnume())}\n"
                f.write(st_string)
    """
    def __load_from_file(self):
        try:
            f = open(self.__filename, 'r')
        except ValueError:
            raise print('Fisier invalid')
        lines = f.readlines()
        for line in lines:
            stud_id, stud_name = [token.strip() for token in line.split(';')]
            a = student(stud_id, stud_name)
            stud_repository.add_student(self, a)
        f.close()

    def __save_to_file(self):
        stud_list = stud_repository.get_all_students(self)
        with open(self.__filename, 'w') as f:
            for st in stud_list:
                st_string = str(st.getIdstudent()) + ';' + str(st.getnume()) + ';' + '\n'
                f.write(st_string)
    """
    def add_student(self, student):
        stud_repository.add_student(self, student)
        self.__save_to_file()

    def add_ran(self,student):
        stud_repository.add_ran(self,student)
        self.__save_to_file()

    def update(self, id, value,poz):
        updated_st = stud_repository.update(self, id, value,poz)
        self.__save_to_file()
        return updated_st

    def dell(self, value,poz):
        deleted_stud = stud_repository.dell(self, value,poz)
        self.__save_to_file()
        return deleted_stud

    def get_all_students(self):
        return stud_repository.get_all_students(self)

    def size(self):
        return stud_repository.size(self)


    def find(self, id):
        return stud_repository.find(self, id)
    def find1(self,nume):
        return stud_repository.find(self, nume)
    def dell_all(self):
        stud_repository.dell_all(self)
        self.__save_to_file()


