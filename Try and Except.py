from numeros_escrito import numeros_escrito


def converta_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            try:
                for x in numeros_escrito:
                    for key, valores in x.items():
                        if valor.lower() in key:
                            return valores
            except Exception as error:
                print(error)


while True:
    numero = converta_numero(input('Digite um número: ').strip().lower())
    if numero is None:
        print('Erro: digite apenas números!')
    else:
        print(numero)
        break
