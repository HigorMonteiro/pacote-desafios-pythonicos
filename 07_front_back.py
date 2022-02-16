"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""

"""
    First try 
"""
# def front_back(a, b):
#     # +++ SUA SOLUÇÃO +++
#     result = None
#     mod = len(a) % 2
#     if mod == 0 and len(a)/2:
#         r = int(len(a)/2)
#         if len(b) % 2 != 0:
#             mod_b = len(b) % 2
#             result = f"{a[:r]}{b[:2+mod_b]}{a[r:]}{b[-2:]}"
#         else:
#             result = f"{a[:r]}{b[0]}{a[r:]}{b[1]}"
#     else:
#         result = f"{a[:2+mod]}{b[:2]}{a[-2:]}{b[-1:]}"
#     return result
import math

def front_back(a, b):

    return ''.join([a[:(math.ceil(len(a) / 2))], b[:(math.ceil(len(b) / 2))],
                    a[(math.ceil(len(a) / 2)):], b[(math.ceil(len(b) / 2)):]])

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')


def string_slice(s):

    String = s

    # Using slice constructor
    s1 = slice(3)
    s2 = slice(1, 5, 2) 
    s3 = slice(-1, -12, -2)
    
    print("String slicing") 
    print(String[s1]) 
    print(String[s2]) 
    print(String[s3])

