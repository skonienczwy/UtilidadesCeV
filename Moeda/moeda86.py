def metade(m,form=True):
    if form == True:
        met = m / 2
        return formata(met)
    else:
        return m/2

def dobro(m,form=True):
    if form == True:
        dob = m * 2
        return formata(dob)
    else:
        return m *2


def aumentar(m,form=True):
    if form == True:
        aum = m + (m*0.10)
        return formata(aum)
    else:
        return m + (m*0.10)

def diminuir(m,form=True):
    if form == True:
        dim = m - (m*0.13)
        return formata(dim)
    else:
        return m - (m*0.13)

def formata(n):
    convert = '%.2f' % n
    return convert.replace('.' , ',')


def resumo(v,a,r):
    v1 =a
    v2=r
    a = v + (v * (a/100))
    r = v - (v * (r/100))
    print('----------------------------------------------')
    print(f'RESUMO DO VALOR')
    print('----------------')
    print(f'Preço analisado:    R${formata(v)}')
    print(f'Dobro do preço:     R${dobro(v)}')
    print(f'Metade do preço:    R${metade(v)}')
    print(f'{int(v1)}% de aumento:     R${formata(a)}')
    print(f'{int(v2)}% de redução:    R${formata(r)}')
    print('----------------------------------------------')





