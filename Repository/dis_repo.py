from domain.entities import disciplina
class dis_repository:
    """
        Clasa creata cu responsabilitatea de a gestiona  multimea de discipline
    """
    def __init__(self):
        """
        Este o lista care contine toate disciplinele introduse,lista fiind la inceput goala
        """
        self.__discipline=[]

    def sizedis(self):
        """
        Returneaza numarul de discipline din multime
        :return: numar discipline existente
        """
        return len(self.__discipline)

    def findDis(self, id):  #COMPLEXITATE
        """
        Cauta disciplina cu id dat
        :param id: id dat
        :return: diisciplina cu id dat, None daca nu exista
        """
        """
        Complexitatea functiei este O(n)
        Caz favorabil: primul element este cel cautat,se executa un singur pas,T(n)=1 ce apartine de O(1)
        Caz defavorabil: nu exista disciplina cautata in lista,se executa n pasi, T(n)=n ce apartine de O(n)
        caz neutru: for poate fi executat de 1,2,3,..,n ori,deci T(n)=(n+1)/2, ce apartine O(n)
        """
        for dis in self.__discipline:
            if dis.getIdDisciplina() ==id:
                return dis
        return None
    def find1Dis(self,numedis):
        """
         Cauta disciplina cu nume dat
         :param id: nume dat
         :return: diisciplina cu nume dat, None daca nu exista
               """
        for dis in self.__discipline:
            if dis.getnumedis() == numedis:
                return dis
        return None
    def find2Dis(self,prof):
        """
        Cauta disciplina cu profesor dat
        :param id: profesor dat
        :return: diisciplina cu profesor dat, None daca nu exista
               """
        for dis in self.__discipline:
            if dis.getprofesor() == prof:
                return dis
        return None


    def add_dis(self,dis):
       """
        Adauga o disciplina in lista
        param: disciplina care se adauga de tip disciplina"""

       if self.findDis(dis.getIdDisciplina()) is not None:
           raise ValueError('Exista deja disciplina cu acest id.')

       self.__discipline.append(dis)

    def dell_dis(self,value,poz):
        """
        Sterge o disciplina dupa criteriul ales de utilizator
        :param : value:valoarea criteriului ales,poz-pozitia in entitata disciplina(0-id,1-nume disciplina,2-nume profesor)
        """
        if poz=='0':
                st = self.findDis(value)
                if st is None:
                    raise ValueError('Nu exista disciplina cu acest id.')
                else:
                    self.__discipline=[el for el in self.__discipline if el.getIdDisciplina()!=value]
        if poz=='1':
                 st = self.find1Dis(value)
                 if st is None:
                    raise ValueError('Nu exista disciplina cu acest nume.')
                 else:
                    self.__discipline=[el for el in self.__discipline if el.getnumedis()!=value]
        if poz=='2':
                 st = self.find2Dis(value)
                 if st is None:
                    raise ValueError('Nu exista disciplina cu acest profesor.')
                 else:
                    self.__discipline = [el for el in self.__discipline if el.getprofesor() != value]

    def update_dis(self, id, value,poz):
        """
        Modifica valoarea parametrului poz(0, 1 sau 2) din disciplina
        :param id: idul disciplinei pe care vrem sa il modificam
        :param value: data pe care vrem sa o modificam in interiorul disciplinei
        poz:pozitia in obiectul disciplina(0-id, 1-nume dis,2-nume profesor)
        """
        st = self.findDis(id)
        if st is None:
            raise ValueError('Nu exista disciplina cu acest id.')
        else:
            for elem in self.__discipline:
                if elem.getIdDisciplina()==id:
                    if poz=='0':
                        elem.setIdDisciplina(value)
                    if poz=='1':
                        elem.setnumedis(value)
                    if poz=='2' :
                        elem.setprofesor(value)

    def add_ran(self, dis):
        self.__discipline.append(dis)


    """
    def get_students_by_criteria(self, filter_function):
       
        Selecteaza elementele din multime care indeplinesc un criteriu
        :param filter_function: functia dupa care se filtreaza
        :return: lista de discipline  care indeplinesc criteriul
        
        return [dis for dis in self.__discipline if filter_function(dis)]
    """
    def get_discipline(self):
        """
        Returneaza o lista cu toate disciplinele existente
        """
        return self.__discipline
    def dell_all(self):
        self.__discipline=[]

class RepoDisFile(dis_repository):
    def __init__(self,filename):
        dis_repository.__init__(self)
        self.__filename=filename
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
                            dis_id = line
                            dis_name = f1.readline().strip()
                            dis_prof = f1.readline().strip()
                            a = disciplina(dis_id, dis_name, dis_prof)
                            dis_repository.add_dis(self, a)

            except ValueError:
                raise print("fisier invalid")

    def __save_to_file(self):
            dis_list = dis_repository.get_discipline(self)
            with open(self.__filename, 'w') as f:
                for dis in dis_list:
                    dis_string = f"{str(dis.getIdDisciplina())}\n{str(dis.getnumedis())}\n+{str(dis.getprofesor())}\n"
                    f.write(dis_string)
    """
    def __load_from_file(self):
        try:
            f = open(self.__filename, 'r')
        except ValueError:
            raise print('Fisier invalid')
        lines = f.readlines()
        for line in lines:
            dis_id, dis_name, dis_prof=[token.strip() for token in line.split(';')]
            a = disciplina(dis_id, dis_name,dis_prof)
            dis_repository.add_dis(self, a)
        f.close()

    def __save_to_file(self):
        dis_list=dis_repository.get_discipline(self)
        with open(self.__filename,'w') as f:
            for dis in dis_list:
                dis_string=str(dis.getIdDisciplina())+ ';' +str(dis.getnumedis())+';'+str(dis.getprofesor())+'\n'
                f.write(dis_string)
                """

    def add_dis(self,dis):
        dis_repository.add_dis(self,dis)
        self.__save_to_file()

    def dell_dis(self,value,poz):
        dis=dis_repository.dell_dis(self,value,poz)
        self.__save_to_file()
        return dis

    def findDis(self, id):
        return dis_repository.findDis(self,id)


    def find1Dis(self,numedis):
        return dis_repository.find1Dis(self,numedis)

    def find2Dis(self,prof):
        return dis_repository.find2Dis(self,prof)

    def update_dis(self, id, value,poz):
        dis=dis_repository.update_dis(self,id,value,poz)
        self.__save_to_file()
        return dis

    def get_discipline(self):
        return dis_repository.get_discipline(self)

    def sizedis(self):
        return dis_repository.sizedis(self)

    def dell_all(self):
        dis_repository.dell_all(self)
        self.__save_to_file()


