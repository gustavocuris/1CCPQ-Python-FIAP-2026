from aluno import Aluno
from disciplina import Disciplina

# criar / instanciar 1 aluno
aluno1 = Aluno( "Russi", "123456", "Ciências da Computaria" )

# criar 2 disciplinas
cs = Disciplina("Computer Science", "Lucas")
model_mat = Disciplina('Modelagem Matemática', 'Christian')

# matricular aluno nas disciplinas
aluno1.matricular(cs)
aluno1.matricular(model_mat)

# adicionar notas do aluno referente a determinada disciplina
aluno1.adicionar_nota(cs, 10)
aluno1.adicionar_nota(cs, 8)
aluno1.adicionar_nota(cs, 5)
aluno1.adicionar_nota(cs, 4)

print(aluno1.calcuar_media_d(model_mat))