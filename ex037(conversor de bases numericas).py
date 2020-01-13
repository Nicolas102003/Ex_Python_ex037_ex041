num = int(input('Digite um número:'))
op = int(input('Escolha uma das opções de conversão:\n'
      '[1] - Converter para Binário \n'
      '[2] - Conversão para Octal\n'
      '[3] - Conversão para Hexadecima\n'))
if op == 1:
    print('A conversão de {} para Binário é {}'.format(num,bin(num)[2:]))
elif op == 2:
    print('A conversão de {} para Octal é {}'.format(num,oct(num)[2:]))
elif op == 3:
    print('A conversão de {} para Hexadecimal é {}'.format(num,hex(num)[2:]))