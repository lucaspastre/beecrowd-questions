n1, n2, n3, n4 = map(float, input().split())
m = (n1*2+n2*3+n3*4+n4)/10

if m >= 7.0:
    print('Media: %.1f\nAluno aprovado.' % m)

elif m < 5:
    print('Media: %.1f\nAluno reprovado.' % m)

else:
    print('Media: %.1f\nAluno em exame.' % m)
    rec = float(input())
    print('Nota do exame: %.1f' % rec)

    e = (rec+m)/2

    if e >= 5:
        print('Aluno aprovado.\nMedia final: %.1f' % e)

    else:
        print('Aluno reprovado.\nMedia final: %.1f' % e)
