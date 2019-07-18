def metade(m):
    met = m / 2
    return formata(met)

def dobro(m):
    dob = m * 2
    return formata(dob)


def aumentar(m):
    aum = m + (m*0.10)
    return formata(aum)


def diminuir(m):
    dim = m - (m*0.13)
    return formata(dim)

def formata(n):
    convert = '%.2f' % n
    return convert.replace('.' , ',')



