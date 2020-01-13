from datetime import date
adn = int(input('em que ano você nasceu ??'))
ano = date.today().year
alist = ano - adn
if alist == 18:
    print('Já está na hora de se alistar para o exercito vc ja tem {}'.format(alist))
elif alist < 18:
    ar = 18 - alist
    print('Ainda falta {} ano(s) para você se alsitar'.format(ar))
elif alist > 18:
    ap = alist - 18
    print('Já passou {} ano(s) que você deveria ter se alistado'.format(ap))


