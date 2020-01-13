from datetime import date
an = int(input('Em que nao você nasceu ??'))
aa = date.today().year
id = aa - an
if id <=9:
    print('O atleta tem {} anos \n CLASSIFICAÇÃO: MIRIM'.format(id))
elif id > 9 and id <=14:
    print('O atleta tem {} anos \n CLASSIFICAÇÃO: INFANTIL'.format(id))
elif id > 14 and id <=19:
    print('O atleta tem {} anos \n CLASSIFICAÇÃO: JUNIOR'.format(id))
elif id == 20:
    print('O atleta tem {} anos \n CLASSIFICAÇÃO: SÊNIOR'.format(id))
elif id > 20:
    print('O atleta tem {} anos \n CLASSIFICAÇÃO: MASTER'.format(id))

