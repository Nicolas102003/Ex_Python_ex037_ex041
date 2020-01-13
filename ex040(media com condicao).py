n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
n3 = float(input('Digite a terceira nota'))
n4 = float(input('Digite a quarta nota:'))
m = (n1+n2+n3+n4)/4

if m <= 5.0:
    print('Com a média de {} o aluno está REPROVADO')
elif m > 5.0 and m < 6.9:
    print('Com a média de {} o aluno está em RECUPERAÇÃO'.format(m))
elif m >= 7.0:
    print('Com a média de {} o aluno está APROVADO'.format(m))
