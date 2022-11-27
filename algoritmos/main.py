

"""
Testes exercícios
Para os testes abaixo, pode-se criar uma aplicação simples.
1. Escreve um método que faça a soma de 1 até um número dado. O número deve ser maior que
zero e um dos números deve ser 100000 (cem mil).
Exemplos:
Soma(2) -> 3 (1 +2)
Soma(8) -> 36 (1+2+3+4+5+6+7+8)

2. Dado um array de strings, remova as letras duplicadas em sequência de cada palavra,
exemplos:
duplicados(["abracadabra","allottee","assessee"])=["abracadabra","alote","asese"]
duplicados(["kelless","keenness","Alfalggo"])=["keles","kenes","Alfalgo"]
"""

def Soma(number: int) -> int:
    if isinstance(number, int):
        if number == 1:
            return 1
        elif number < 0:
            raise ValueError('Only positive values ​​are accepted')
        result = sum([item for item in range(1, number+1)])
        return result
    raise ValueError('This function accepts integers only')
    
    
    
def duplicados(list_words: list[str]) -> list[str]:
    list_new_words = []
    if isinstance(list_words, list) and len(list_words) != 0:
        for words in list_words:
            if isinstance(words, str) == False:
                raise ValueError("List must only contain words with type string")
            ant = None
            new_str = ""
            for letter in words:
                if ant == letter:
                    continue
                new_str = "".join([new_str, letter])
                ant = letter
            list_new_words.append(new_str)
        return list_new_words
    raise ValueError("This function only takes a string list")
    

    
if __name__ == '__main__':
    print(f"Resultado: {Soma(2)}")
    print(f"Resultado: {Soma(8)}", end="\n")

    print(f'Resultado: {duplicados(["kelless","keenness","Alfalggo"])} | Esperado: ["keles","kenes","Alfalgo"]')
    print(f'Resultado: {duplicados(["abracadabra","allottee","assessee"])} | Esperado: ["abracadabra","alote","asese"]')
