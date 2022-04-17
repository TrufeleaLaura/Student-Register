from consola import Consola
from Repository.stud_repo import RepoStudFile
from Repository.dis_repo import RepoDisFile
from Repository.nota_repo import RepoNotFile
from Validators.validators import studValidator,discValidator,noteValidator
from Service.stud_service import student_service
from Service.dis_service import disciplina_service
from Service.nota_service import nota_service

#repo_stud=stud_repository()
repo_file_stud=RepoStudFile('files_doc\\students_repo.txt')
val_stud=studValidator()
#repo_dis=dis_repository()
repo_file_dis=RepoDisFile('files_doc\\discipline_repo.txt')
val_dis=discValidator()
#repo_not=nota_repository()
repo_file_not=RepoNotFile('files_doc\\note_repo.txt',repo_file_stud,repo_file_dis)
val_not=noteValidator()
srv_stud=student_service(repo_file_stud,val_stud)
srv_dis=disciplina_service(repo_file_dis,val_dis)
srv_not=nota_service(repo_file_not,val_not,repo_file_stud,repo_file_dis)
ui=Consola(srv_stud,srv_dis,srv_not)
ui.catalog()


