class Consola:
    def __init__(self,srv_stud,srv_dis,srv_not):
        """
        Initializeaza consola
        """
        self.__srv_stud=srv_stud
        self.__srv_dis=srv_dis
        self.__srv_not=srv_not

    def __print(self,op):
        "Afiseaza ambele liste de studenti sau cea de discipline"
        if op=='1':
            student_list=self.__srv_stud.get_all_students()
            if len(student_list)==0:
                print("Nu exista studenti in lista.")
            else:
                print('Lista de studenti este:')
                for st in student_list:
                    print('ID: ',st.getIdstudent(),'Nume: ', st.getnume())

        elif op=='2':
            dis_list=self.__srv_dis.get_all_discipline()
            if len(dis_list)==0:
                print("Nu exista discipline in lista.")
            else:
                print('Lista de discipline este:')
                for dis in dis_list:
                    print('ID: ', dis.getIdDisciplina(), 'Nume disciplina: ', dis.getnumedis(),'Nume profesor: ',dis.getprofesor())
        else:
            not_list=self.__srv_not.get_all()
            if len(not_list)==0:
                print("Nu exista notari. ")
            else:
                print("Lista de notari este: ")
                for el in not_list:
                    print(" STUDENTUL: ", el.getstudent().getnume(),"DISCIPLINA: ",el.getdis().getnumedis(),'NOTA:',el.getnota())

    def __adaugare(self, op):
        """
        Adauga un student sau o disciplina cu datele citite de la tastatura
        """
        if op == '1':
            ID = input("ID student: ")
            nume = input("Nume student: ")
            try:
                self.__srv_stud.adaugare_student(ID, nume)
                print("STudentul a fost adaugat cu succes")
            except ValueError as e:
                print(e)
        elif op == '2':
            id = input("ID disciplina:")
            nume_dis = input("Numele disciplinei este: ")
            numeprof = input("Numele profesorului este ")
            try:
                self.__srv_dis.adaugare_dis(id, nume_dis, numeprof)
                print("Disciplina a fost adaugata cu succes")
            except ValueError as e:
                print(e)
        else:
            id_stud = input("Introduceti id-ul studentului la care vreti sa adaugati nota ")
            id_dis = input("Introduceti id-ul disciplinei la care vreti sa adaugati nota ")
            nota = input("Nota acordata este: ")
            try:
                self.__srv_not.adaugare_nota(id_stud, id_dis, nota)
                print("Nota a fost adaugata cu succes")
            except ValueError as e:
                print(e)


    def __modificare(self,op):
        """
        Modifica un student sau o disciplina in functie de optiunea aleasa de utilizator
        """
        if(op=='1'):
            ID=input("Introduceti id-ul studentului la care vreti sa modificati datele ")
            print("Ce doriti sa schimbati la acest student? ")
            print("0.Id  1.Nume")
            poz=input("Optiunea dumneavoastra este: ")
            value=input(" Noua valoare pe care doriti sa o aiba data este: ")

            try:
                self.__srv_stud.update_stud(ID,value,poz)
                print("Studentul a fost modifcat cu succes")
            except ValueError as e:
                print(e)

        elif(op=='2'):
            ID=input("Introduceti id-ul disciplinei la care vreti sa modificati datele ")
            print("Ce doriti sa schimbati la aceasta disciplina? ")
            print("0.Id  1.Nume disciplina   2.Nume profesor ")
            poz=input("Optiunea dumneavoastra este: ")
            value = input(" Noua valoare pe care doriti sa o aiba data este: ")

            try:
                self.__srv_dis.update_dis(ID,value,poz)
                print("Disciplina a fost modificata cu succes")
            except ValueError as e:
                print(e)

        else:
            id_stud = input("Introduceti id-ul studentului la care vreti sa modificati nota ")
            id_dis=input("Introduceti id-ul disciplinei la care vreti sa modificati nota ")
            nota= input("Nota curenta este: ")
            value = input(" Noua valoare pe care doriti sa o aiba nota este: ")
            try:
                self.__srv_not.modific_nota(id_stud,id_dis,nota,value)
                print("Nota a fost modificata cu succes")
            except ValueError:
                print("data invalida")

    def __delete(self,op):
        """
        Sterge un student sau o diciplina dupa criteriul ales de utilizator
        """
        if op=='1':
            print("Dupa ce criteriu doriti sa stergeti un student? ")
            print("0.Id  1.Nume")
            poz=input("Optiunea dumneavoastra este: ")
            value=input("Dati detaliile datei alese")

            try:
                self.__srv_stud.stergere_student(value,poz)
                print("Studentul a fost sters cu succes")
            except ValueError as e:
                print(e)

        elif op=='2':
            print("Dupa ce criteriu doriti sa stergeti o disciplina? ")
            print("0.Id  1.Nume disciplina 2.Nume profesor")
            poz = input("Optiunea dumneavoastra este: ")
            value = input("Dati detaliile datei alese")

            try:
                self.__srv_dis.stergere_dis(value,poz)
                print("Disciplina a fost stearsa cu succes")
            except ValueError as e:
                print(e)

        else:
            id_stud = input("Introduceti id-ul studentului la care vreti sa stergeti nota ")
            id_dis = input("Introduceti id-ul disciplinei la care vreti sa stergeti nota ")
            nota = input("Nota curenta este: ")
            try:
                self.__srv_not.stergere_nota(id_stud, id_dis, nota)
                print("Nota a fost stearsa cu succes")
            except ValueError:
                print("data invalida")


    def __cautare(self,op):
        """
        Cauta un student sau o disciplina
        """
        if op=='1':
            poz=input("Introduceti dupa ce vreti sa cautati studentul ('0'-id,'1'-nume): ")
            val=input("Introduceti valoarea acestei date ")
            try:
                st=self.__srv_stud.cautare_stud(val,poz)
                print('ID: ',st.getIdstudent(), 'Nume: ',st.getnume())
            except ValueError as e:
                print(e)
        print()
        if op=='2':
                poz = input("Introduceti dupa ce vreti sa cautati disciplina( 0-id  1-nume disciplina  2-profesor): ")
                val = input("Introduceti valoarea acestei date ")
                try:
                    dis = self.__srv_dis.cautare_dis(val, poz)
                    print('ID: ',dis.getIdDisciplina(),'Nume disciplina: ',dis.getnumedis(),'Nume profesor: ',dis.getprofesor())
                except ValueError as e:
                    print(e)

    def __filtrarepref(self):
        """
        Afiseaza lista de studenti la care au prefixul numelui coincide cu prefixul dat de la utilizator
        """
        prefix=input("Introduceti prefixul dorit: ")
        try:
            lista=self.__srv_stud.filter_by_prefix(prefix)
            if lista==[]:
                print("Nu exista studenti cu acest prefix")
            else:
                for el in lista:
                    print(el.getnume())
        except ValueError:
            print("data invalida")

    def __adaugareran(self, op, val):
        """
        Adauga un student sau o disciplina cu datele citite de la tastatura
        """
        if op == '1':
            while val != 0:
                st=self.__srv_stud.adauga_random()
                print('ID: ', st.getIdstudent(), 'Nume: ', st.getnume())
                val = val - 1


        elif op == '2':
            while val != 0:
                dis=self.__srv_dis.adauga_random()
                print('ID: ', dis.getIdDisciplina(), 'Nume disciplina: ', dis.getnumedis(), 'Nume profesor: ',
                      dis.getprofesor())
                val = val - 1

        else:
            try:
                no=self.__srv_not.adauga_ran(val)
                for nota in no:
                    print('ID: ', nota.getstudent().getIdstudent(), 'Nume: ', nota.getstudent().getnume(),'ID: ', nota.getdis().getIdDisciplina(), 'Nume disciplina: ', nota.getdis().getnumedis(), 'Nume profesor: ',
                      nota.getdis().getprofesor(), 'Nota: ',nota.getnota())
            except ValueError as e:
                    print(e)

    def __sort(self,op,dis):
        """
        Se afiseaza lista de studenti si nototele lor intr-anumita ordine la o disciplina data
        """
        if op=='1':
            try:
                li=self.__srv_not.get_sortnume(dis)
                if li==[]:
                    print("Nu exista notari")
                else:
                    for st in li:
                        print('Nume: ', st.getstudnume(),'Nota: ',st.getnota())
            except ValueError as e:
                    print(e)
        elif op=='2':
            try:
                li = self.__srv_not.get_sortnota(dis)
                if li == []:
                    print("Nu exista notari")
                else:
                    for st in li:
                        print('Nume student: ',  st.getstudnume(), 'Nota: ', st.getnota())
            except ValueError as e:
                print(e)

    def __raport(self):
        """
        Se afiseaza  primii 20% de studenti in functie de media de la toate disciplinele
        """
        try:
            li = self.__srv_not.get_sort_medie()
            if li==[]:
                print("Nu exista notari")
            else:
                for st in li:
                    print('Nume student: ', st.getnume(), 'Nota: ', st.getavgnote())
        except ValueError as e:
            print(e)

    def __proc(self):
        """
        Se afiseaza primele 50% de discipline in functie de medie,respectiv ordonata alfabetic dupa profesor
        """
        try:
            li = self.__srv_not.get_sort_medie_dis()
            if li==[]:
                print("Nu exista notari")
            else:
                for st in li:
                    print('Nume disciplina: ', st.getnume(),'Medie: ',st.getavg())
        except ValueError as e:
            print(e)



    def catalog(self):
        while True:
            print("Comenzi disponibile:add, dell, update, cautare, show_all, filter_st, random, sort,raport,proc,exit")
            cmd=input("Comanda este: ")
            print()
            cmd=cmd.lower().strip()
            if cmd=='add':
                print('Adaugati un student,o disciplina sau o notare?')
                print('1-student   2-disciplina  3-notare')
                op=input("Optiunea dumneavoastra este ")
                try:
                    if(op!='1' and op!='2' and op!='3'):
                        print("optiune invalida")
                        continue
                    else:
                        self.__adaugare(op)
                except ValueError:
                    print("data invalida")

            elif cmd=='dell':
                print('Stergeti un student, o disciplina sau o notare?')
                print('1-student   2-disciplina  3-notare')
                op = input("Optiunea dumneavoastra este ")
                try:
                    if (op != '1' and op != '2' and op!='3'):
                        print("optiune invalida")
                        continue
                    else:
                        self.__delete(op)
                except ValueError:
                    print("data invalida")

            elif cmd=='update':
                print('Modificati un student, o disciplina sau o notare?')
                print('1-student   2-disciplina   3-notare')
                op = input("Optiunea dumneavoastra este ")
                try:
                    if (op != '1' and op != '2' and op!='3'):
                        print("optiune invalida")
                        continue
                    else:
                        self.__modificare(op)
                except ValueError:
                    print("data invalida")

            elif cmd=='cautare':
                print('Cautati un student sau o disciplina?')
                print('1-student   2-disciplina')
                op = input("Optiunea dumneavoastra este ")
                try:
                    if (op != '1' and op != '2'):
                        print("optiune invalida")
                        continue
                    else:
                        self.__cautare(op)
                except ValueError:
                    print("optiune invalida")
            elif cmd=='show_all':
                print('Afisati lista de studenti, de discipline sau de note?')
                print('1-studenti   2-discipline   3-note')
                op = input("Optiunea dumneavosatra este ")
                try:
                    if (op != '1' and op != '2' and op!='3'):
                        print("optiune invalida")
                        continue
                    else:
                        self.__print(op)
                except ValueError:
                    print("optiune invalida")
            elif cmd=='filter_st':
                try:
                    self.__filtrarepref()
                except ValueError:
                    print("data invalida")
            elif cmd=='random':
                print('Generati lista de studenti, de discipline sau de note?')
                print('1-studenti   2-discipline   3-note')
                op=input("optiunea dorita este ")
                var=input('Cate entitati doriti sa generati?' )
                self.__adaugareran(op,int(var))
            elif cmd=='sort':
                print('Doriti sa sortati studentii alfabetic sau dupa nota? ')
                print('1-alfabetic    2-dupa nota')
                op=input("optiunea dorita este: ")
                dis=input('Introduceti id-ul disciplinei la care doriti sortarea' )
                try:
                    if (op != '1' and op != '2'):
                        print("optiune invalida")
                        continue
                    else:
                        self.__sort(op,dis)
                except ValueError:
                    print("optiune invalida")
            elif cmd=='raport':
                    self.__raport()
            elif cmd=='proc':
                    self.__proc()
            elif cmd == 'exit':
                return
            else:
                print('Comanda invalida.')






































