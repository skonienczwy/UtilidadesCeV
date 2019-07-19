import re
def leiaDinheiro(num):


    while True:
        t = input(num)
        if re.search(r'[a-zA-z]', t):

                from colorama import Fore, Back, Style
                print(Fore.RED + 'ERRO! Digite um valor válido:')
                print(Style.RESET_ALL)

        else:
            t = t.replace(',', '.')
            t = float(t)
            return t


def formata(n):
    convert = '%.2f' % n
    return convert.replace('.' , ',')

