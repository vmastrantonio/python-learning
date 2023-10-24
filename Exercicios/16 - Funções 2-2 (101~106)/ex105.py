# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings da função.

def notas(* num, sit=False):
    """-> Permite adicionar quantos parametros numéricos quiser para calcular as notas de um aluno
    :param n: float (obrigatório), uma ou mais notas do aluno
    :param sit: boolean (opcional), indica se deve ou não mostrar a situação do aluno
    :return: Retorna um dicionário contendo a soma das notas, maior nota, menor nota e média.
    """

    media = sum(num) / len(num)
    dicionario = {'total': len(num), 'maior': max(num), 'menor': min(num), 'media': media}

    if sit:
        if media >= 7:
            dicionario['situacao'] = 'APROVADO'
        else:
            dicionario['situacao'] = 'REPROVADO'
    
    return dicionario

resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)