dias = int(input())
ano = dias // 365
mes = (dias % 365)//30
dias = (dias % 365) % 30
print('%d ano(s)\n%d mes(es)\n%d dia(s)' % (ano, mes, dias))
