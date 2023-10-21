# flake8: noqa

# Comandos para instalar e configurar o Python 3.10 e ambientes virtuais no Linux:

# 1. Instalação do Python 3.10:
# O primeiro passo é instalar o Python 3.10. Você pode fazer isso através do repositório da distribuição ou baixando do site oficial.
# No Ubuntu, você pode usar o seguinte comando:
"""
sudo apt-get install python3.10
"""

# 2. Verificar a versão do Python:
# Para garantir que o Python 3.10 foi instalado corretamente, você pode verificar a versão do Python com o seguinte comando:
"""
python3.10 --version
"""

# 3. Trocar de Versão do Python:
# Se você tem várias versões do Python instaladas, pode usar o comando 'update-alternatives' para trocar entre elas.
"""
sudo update-alternatives --config python3
"""

# 4. Verificar a versão do pip:
# O pip é o gerenciador de pacotes do Python. Para verificar a versão do pip, use o seguinte comando:
"""
pip3 --version
"""

# 5. Instalar ou Atualizar o pip:
# Se o pip não estiver instalado ou se você desejar atualizá-lo, pode usar o seguinte comando:
"""
sudo apt-get install python3-pip
"""

# 6. Instalar o venv:
# O venv é um módulo que vem com o Python 3.3+ e cria ambientes virtuais. Para instalar o venv, use o seguinte comando:
"""
sudo apt-get install python3.10-venv
"""

# 7. Criar e Ativar um Ambiente Virtual:
# Ambientes virtuais são úteis para isolar dependências para diferentes projetos.
"""
python3.10 -m venv meu_ambiente
source meu_ambiente/bin/activate  # Para ativar o ambiente virtual
"""

# 8. Instalar Dependências com requirements.txt:
# O arquivo requirements.txt lista todas as dependências necessárias para o seu projeto.
# Isso facilita a instalação de todas as dependências necessárias de uma vez.
"""
pip install -r requirements.txt
"""

# Nota:
# - O arquivo 'requirements.txt' deve estar no mesmo diretório em que você está executando o comando,
#   ou você deve fornecer o caminho completo para o arquivo.
# - O comando 'pip install -r requirements.txt' lerá o arquivo e instalará todas as dependências listadas nele.

# --------------------------------------------------------------------------------

# Operadores em Python:

# Aritméticos: +, -, *, /, //, %, **
soma = 5 + 3  # soma = 8
subtracao = 5 - 3  # subtracao = 2
multiplicacao = 5 * 3  # multiplicacao = 15
divisao = 5 / 3  # divisao = 1.666...
divisao_inteira = 5 // 3  # divisao_inteira = 1
resto = 5 % 3  # resto = 2
exponenciacao = 5**3  # exponenciacao = 125

# Comparação: ==, !=, >, <, >=, <=
igualdade = 5 == 3  # igualdade = False
desigualdade = 5 != 3  # desigualdade = True
maior = 5 > 3  # maior = True
menor = 5 < 3  # menor = False
maior_igual = 5 >= 3  # maior_igual = True
menor_igual = 5 <= 3  # menor_igual = False

# Lógicos: and, or, not ao invés de &&, ||, !
logico_and = True and False  # logico_and = False
logico_or = True or False  # logico_or = True
logico_not = not True  # logico_not = False

# Atribuição: =, +=, -=, *=, /=, //=, %=, **=
a = 5  # inicia a = 5
a += 3  # a = 8
a -= 3  # a = 5
a *= 3  # a = 15
a /= 3  # a = 5.0
a //= 3  # a = 1.0
a %= 3  # a = 1.0 (não houve mudança pois 1.0 % 3 = 1.0)
a **= 3  # a = 1.0 (não houve mudança pois 1.0 ** 3 = 1.0)

# Identidade: is, is not
identidade_is = 5 is 5  # identidade_is = True
identidade_is_not = 5 is not 5  # identidade_is_not = False

# Associação: in, not in
associacao_in = 5 in [1, 2, 3, 4, 5]  # associacao_in = True
associacao_not_in = 5 not in [1, 2, 3, 4, 5]

# Bhaskara do python: Bit a bit: &, |, ^, ~, <<, >>

# AND Bit a Bit (&):
# Este operador compara cada bit de dois números. Se ambos os bits forem 1, o bit resultante será 1. Se não, será 0.
result = (
    5 & 3
)  # 5 é 0101 em binário e 3 é 0011 em binário. Portanto, o resultado é 0001 em binário ou 1 em decimal.

# OR Bit a Bit (|):
# Este operador também compara cada bit de dois números. Se pelo menos um dos bits for 1, o bit resultante será 1. Se ambos forem 0, o bit resultante será 0.
result = (
    5 | 3
)  # 5 é 0101 em binário e 3 é 0011 em binário. Portanto, o resultado é 0111 em binário ou 7 em decimal.

# XOR Bit a Bit (^):
# Este operador compara cada bit de dois números. Se os bits forem diferentes, o bit resultante será 1. Se forem iguais, o bit resultante será 0.
result = (
    5 ^ 3
)  # 5 é 0101 em binário e 3 é 0011 em binário. Portanto, o resultado é 0110 em binário ou 6 em decimal.

# NOT Bit a Bit (~):
# Este operador inverte cada bit do número. Todos os bits 1 tornam-se 0 e vice-versa. Também é importante notar que o operador NOT bit a bit em Python é equivalente a adicionar 1 ao número e, em seguida, mudar o sinal do resultado.
result = (
    ~5
)  # 5 é 0101 em binário. Invertendo cada bit, obtemos 1010. Mas em Python, o resultado será -(5 + 1) = -6.

# Deslocamento à Esquerda (<<):
# Este operador desloca todos os bits do número à esquerda por um número especificado de posições. Os bits vazios à direita são preenchidos com zeros. O deslocamento à esquerda é equivalente a multiplicar o número por 2.
result = (
    5 << 1
)  # 5 é 0101 em binário. Deslocando 1 posição à esquerda, obtemos 1010 em binário ou 10 em decimal.

# Deslocamento à Direita (>>):
# Este operador desloca todos os bits do número à direita por um número especificado de posições. Os bits vazios à esquerda são preenchidos com o valor do bit mais à esquerda (significativo) antes do deslocamento. O deslocamento à direita é equivalente a dividir o número por 2.
result = (
    5 >> 1
)  # 5 é 0101 em binário. Deslocando 1 posição à direita, obtemos 0010 em binário ou 2 em decimal.

# --------------------------------------------------------------------------------

# Control Flow em Python:

# Instruções condicionais: if, elif, else
# If, elif, else
numero = 5
if numero > 0:
    print("O número é positivo.")  # Output: O número é positivo.
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# --------------------------------------------------------------------------------

# Instruções de repetição: for, while
# For loop
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

# While loop
i = 0
while i < 5:
    print(i)  # Output: 0 1 2 3 4
    i += 1

# --------------------------------------------------------------------------------

# Instruções de interrupção: break, continue, pass
# Break
for i in range(5):
    if i == 3:
        break  # Interrompe o loop quando i == 3
    print(i)  # Output: 0 1 2

# Continue
for i in range(5):
    if i == 3:
        continue  # Pula a iteração quando i == 3
    print(i)  # Output: 0 1 2 4

# Pass
for i in range(5):
    if i == 3:
        pass  # Não faz nada quando i == 3, útil como um preenchimento temporário
    print(i)  # Output: 0 1 2 3 4

# --------------------------------------------------------------------------------

# Instruções de exceção: try, except, finally, raise
# Try, except, finally
try:
    resultado = 10 / 0  # Tentativa de dividir por zero
except ZeroDivisionError:
    print("Erro: Divisão por zero.")  # Output: Erro: Divisão por zero.
finally:
    print("O programa foi encerrado.")  # Output: O programa foi encerrado.

# Raise
if numero < 0:
    raise Exception("O número não pode ser negativo.")  # Levanta uma exceção

# --------------------------------------------------------------------------------

# Instruções de importação: import, from, as
# Import, from, as
import math  # Importa o módulo math
from math import sqrt  # Importa a função sqrt do módulo math
import math as m  # Importa o módulo math com o alias m

# --------------------------------------------------------------------------------


# Instruções de definição: def, class, return, yield, lambda
# Def, return
def soma(a, b):
    return a + b  # Retorna a soma de a e b


# Class
class Pessoa:
    def __init__(self, nome):
        self.nome = nome  # Atribui o argumento 'nome' ao atributo 'nome' da instância.

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}.")


# Lambda
soma = lambda a, b: a + b  # Retorna a soma de a e b


# Yield
def gerar_numeros():
    for i in range(5):
        yield i  # Pausa a execução da função, retorna um valor e permite que a execução seja retomada na próxima vez que a função é chamada.


# --------------------------------------------------------------------------------

# Instruções de contexto: with, assert, del, global, nonlocal
# With
with open("arquivo.txt", "r") as f:
    print(f.read())  # Lê o conteúdo do arquivo

# Assert
numero = 5
assert (
    numero > 0
), "O número deve ser positivo."  # Levanta uma exceção se a condição for falsa

# Del
numero = 5
del numero  # Deleta a variável 'numero', útil para deletar elementos de listas e dicionários


# Global
def funcao():
    global numero  # Atribui o valor de 'numero' à variável global 'numero'
    numero = 5


# Nonlocal
def funcao():
    numero = 5  # Cria uma variável local 'numero'

    def funcao_interna():
        nonlocal numero  # Atribui o valor de 'numero' à variável não local 'numero'
        numero = 10

    funcao_interna()
    print(numero)  # Output: 10


# --------------------------------------------------------------------------------

"""
Big O notation é uma notação matemática que descreve o comportamento de tempo de execução ou espaço usado de um algoritmo à medida que o tamanho da entrada aumenta.
Não necessariamente o tempo de execução, mas o número de operações.
Não necessariamente a eficiência, mas a escalabilidade.
"""

# --------------------------------------------------------------------------------

"""
Constante (O(1)):
    O tempo de execução ou o espaço usado não dependem do tamanho da entrada.
    Exemplo: Acessar um elemento em um array pelo índice.
"""


def get_element(arr, index):
    return arr[index]  # O(1)


# Exemplo de uso:
arr = [1, 2, 3, 4, 5]
index = 2
result = get_element(arr, index)
print(result)  # Output: 3

# --------------------------------------------------------------------------------

"""
Logarítmica (O(log n)):
    O tempo de execução ou o espaço usado é proporcional ao logaritmo do tamanho da entrada. (Metade do tamanho da entrada)
    Exemplo: Busca binária em um array ordenado.
"""
# Busca Binária:
# A busca binária é um algoritmo eficiente para encontrar um item em um array ordenado.
# Ele começa comparando o item alvo com o valor no meio do array.
# Se eles são iguais, o índice do meio é retornado.
# Se o alvo é menor ou maior, a busca continua na metade inferior ou superior, respectivamente, repetindo o processo.
# Este algoritmo tem uma complexidade de tempo de O(log n) devido à divisão logarítmica do array em cada etapa.


def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Inicialize os ponteiros esquerdo e direito (O(1))

    while (
        left <= right
    ):  # Enquanto o ponteiro esquerdo for <= ponteiro direito (O(log n))
        mid = (left + right) // 2  # Calcule o índice médio (O(1))
        if (
            arr[mid] == target
        ):  # Se o valor no índice médio for igual ao alvo, retorne o índice médio (O(1))
            return mid
        elif (
            arr[mid] < target
        ):  # Se o valor no índice médio for menor que o alvo, mova o ponteiro esquerdo para a direita do meio (O(1))
            left = mid + 1
        else:  # Se o valor no índice médio for maior que o alvo, mova o ponteiro direito para a esquerda do meio (O(1))
            right = mid - 1
    return -1  # Se o alvo não for encontrado, retorne -1 (O(1))


# Exemplo de uso:
arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search(arr, target)
print(result)  # Output: 3

# --------------------------------------------------------------------------------

"""
Linear (O(n)):
    O tempo de execução ou o espaço usado é proporcional ao tamanho da entrada.
    Exemplo: Busca linear em um array não ordenado.
"""
# Busca Linear:
# A busca linear é o algoritmo mais simples para encontrar um item em um array, iterando sobre cada elemento até encontrar o alvo.
# Este algoritmo tem uma complexidade de tempo de O(n) pois, no pior caso, pode ter que iterar sobre todos os n elementos do array.


def linear_search(arr, target):
    for i in range(len(arr)):  # Para cada elemento no array (O(n))
        if arr[i] == target:  # Se o elemento for igual ao alvo, retorne o índice (O(1))
            return i
    return -1  # Se o alvo não for encontrado, retorne -1 (O(1))


# Exemplo de uso:
arr = [2, 3, 4, 10, 40]
target = 10
result = linear_search(arr, target)
print(result)  # Output: 3

# --------------------------------------------------------------------------------

"""
Linearítmica (O(n log n)):
    O tempo de execução ou o espaço usado é proporcional ao produto do tamanho da entrada e o logaritmo do tamanho da entrada.
    Exemplo: Algoritmo merge sort.
"""
# Merge Sort:
# O Merge Sort é um algoritmo de ordenação baseado no princípio de dividir para conquistar.
# Ele divide o array de entrada ao meio, ordena cada metade recursivamente e depois mescla as duas metades ordenadas.
# A função merge é usada para mesclar duas metades ordenadas em um array ordenado.
# Este algoritmo tem uma complexidade de tempo de O(n log n) devido à divisão logarítmica do array e a mesclagem linear das metades.


def merge_sort(arr):
    if len(arr) <= 1:
        return (
            arr  # Base da recursão: array com 0 ou 1 elemento já está ordenado (O(1))
        )

    mid = len(arr) // 2  # Calcule o ponto médio do array (O(1))
    left_half = arr[:mid]  # Divida o array em duas metades (O(n))
    right_half = arr[mid:]  # (O(n))

    sorted_left = merge_sort(left_half)  # Recursão na metade esquerda (O(n log n) / 2)
    sorted_right = merge_sort(right_half)  # Recursão na metade direita (O(n log n) / 2)

    return merge(sorted_left, sorted_right)  # Mescla as duas metades ordenadas (O(n))


def merge(left, right):
    result = []  # Array para armazenar o resultado da mesclagem (O(1))
    i = j = 0  # Índices para iterar pelas metades esquerda e direita (O(1))

    # Enquanto houver elementos nas duas metades, compare e insira o menor elemento no array resultante (O(n))
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Se uma das metades ainda tiver elementos, adicione todos ao final do array resultante (O(n))
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result  # Retorne o array mesclado e ordenado (O(1))


# Exemplo de uso:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [3, 9, 10, 27, 38, 43, 82]

# --------------------------------------------------------------------------------

"""
Quadrática (O(n^2)):
    O tempo de execução ou o espaço usado é proporcional ao quadrado do tamanho da entrada.
    Exemplo: Algoritmo bubble sort.
"""
#  Bubble Sort:
# A ordenação de bolha é um algoritmo simples que compara cada par de elementos adjacentes no array e os troca se estiverem na ordem errada.
# Este processo é repetido para cada elemento até que o array esteja ordenado.
# Este algoritmo tem uma complexidade de tempo de O(n^2) devido aos loops aninhados que iteram sobre os elementos do array.


def bubble_sort(arr):
    n = len(arr)  # Obtenha o número de elementos no array (O(1))
    for i in range(n):  # Itere sobre cada elemento do array (O(n))
        for j in range(
            0, n - i - 1
        ):  # Itere sobre o array, ignorando os últimos i elementos já ordenados (O(n))
            if (
                arr[j] > arr[j + 1]
            ):  # Se o elemento atual for maior que o próximo, troque-os (O(1))
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Exemplo de uso:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)  # Output: [11, 12, 22, 25, 34, 64, 90]


"""
Exponencial (O(2^n)):
    O tempo de execução ou o espaço usado é proporcional a uma potência da entrada.
    Exemplo: Algoritmo de força bruta. (Recursão em fibonacci)
"""


# A cada chamada recursiva, o problema é dividido em dois subproblemas.
# Fibonacci com Recursão
def fibonacci_recur(n):
    if n <= 1:  # O(1) - Verificação constante
        return n  # O(1) - Retorno constante
    # O(2^n) - Duas chamadas recursivas para cada n,
    # onde cada chamada resolve um subproblema do tamanho n-1 e n-2 respectivamente.
    return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)


# Exemplo de uso:
n = 10
result = fibonacci_recur(n)
print(result)  # Output: 55


# Fibonacci Sem Recursão
def fibonacci_iter(n):
    if n <= 1:  # O(1) - Verificação constante
        return n  # O(1) - Retorno constante

    a, b = 0, 1  # O(1) - Inicialização constante
    for i in range(2, n + 1):  # O(n) - Loop de 2 até n
        c = a + b  # O(1) - Soma constante
        a = b  # O(1) - Atribuição constante
        b = c  # O(1) - Atribuição constante

    return b  # O(1) - Retorno constante


# Exemplo de uso:
result = fibonacci_iter(n)
print(result)  # Output: 55


# --------------------------------------------------------------------------------

"""
Fatorial (O(n!)):
    O tempo de execução ou o espaço usado é proporcional ao fatorial da entrada.
    Exemplo: Algoritmo de força bruta. (Permutação de uma string)
"""
# Algoritmo de Permutação de String:
# Este algoritmo gera todas as permutações possíveis de uma string dada.
# A função permute é chamada recursivamente, trocando caracteres para gerar novas permutações.
# A complexidade de tempo deste algoritmo é O(n!) pois para cada caractere na string,
# ele faz n trocas recursivamente, resultando em n * (n-1) * (n-2) * ... * 1 = n! permutações possíveis.


def permute(data, i, length):
    if i == length:
        print("".join(data))  # Imprime a permutação atual (O(1))
    else:
        for j in range(i, length):  # Loop sobre os caracteres da string (O(n))
            # Troca o elemento atual pelo próximo (O(1))
            data[i], data[j] = data[j], data[i]
            permute(
                data, i + 1, length
            )  # Chama a função recursivamente para o próximo elemento (O(n!))
            data[i], data[j] = (
                data[j],
                data[i],
            )  # Backtrack para restaurar a ordem original (O(1))


string = "ABC"
permute(list(string), 0, len(string))

# --------------------------------------------------------------------------------

"""
Otimização e boas práticas:
    1- Evite Loops aninhados: Loops aninhados podem aumentar rapidamente o tempo de execução de O(n) para O(n^2) ou mais.
    2- Evite recursão: A recursão pode ser muito lenta.
    3- Evite cópias desnecessárias: Copiar uma lista pode ser muito lento.
    4- Use estruturas de dados apropriadas: Usar 'set' e 'dict' para operações de busca e inserção, pois são O(1), enquanto que em listas são O(n).
"""

# --------------------------------------------------------------------------------


# Sobre classes
class Pessoa:
    # Método construtor (__init__) para inicializar uma nova instância da classe Pessoa.
    def __init__(self, nome, idade):
        self.nome = nome  # Atribui o argumento 'nome' ao atributo 'nome' da instância.
        self.idade = (
            idade  # Atribui o argumento 'idade' ao atributo 'idade' da instância.
        )

    # Método para imprimir uma mensagem de apresentação.
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")


# Criando uma instância da classe Pessoa
p = Pessoa("João", 25)  # Cria uma nova instância de Pessoa com nome 'João' e idade 25.

# Chamando o método apresentar
p.apresentar()  # Chama o método 'apresentar' para imprimir a mensagem de apresentação.
# Output: Olá, meu nome é João e eu tenho 25 anos.

# --------------------------------------------------------------------------------


# Sobre métodos mágicos (dunder methods)
class Livro:
    # Método construtor (__init__) para inicializar uma nova instância da classe Livro.
    def __init__(self, titulo, autor):
        self.titulo = (
            titulo  # Atribui o argumento 'titulo' ao atributo 'titulo' da instância.
        )
        self.autor = (
            autor  # Atribui o argumento 'autor' ao atributo 'autor' da instância.
        )

    # Método __str__ para retornar uma representação de string da instância.
    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

    # Método __eq__ para comparar a igualdade de dois objetos Livro.
    def __eq__(self, outro):
        # Compara se o título e o autor são iguais entre as duas instâncias.
        return self.titulo == outro.titulo and self.autor == outro.autor


# Criando instâncias da classe Livro
livro1 = Livro("1984", "George Orwell")  # Cria uma nova instância de Livro.
livro2 = Livro("1984", "George Orwell")  # Cria outra nova instância de Livro.

# Usando o método __str__
print(livro1)  # Chama o método __str__ para obter a representação de string de livro1.
# Output: '1984' por George Orwell

# Usando o método __eq__
print(livro1 == livro2)  # Compara se livro1 é igual a livro2 usando o método __eq__.
# Output: True

# --------------------------------------------------------------------------------

"""
HashTable (Set e Dict):
A HashTable é uma estrutura de dados que permite o armazenamento e acesso eficiente a pares de chave-valor. Utiliza uma função hash para calcular um índice na tabela para cada chave, o que permite operações de inserção, busca e remoção rápidas. As colisões são tratadas através do encadeamento, onde cada entrada na tabela é uma lista de pares de chave-valor. A complexidade de tempo de uma HashTable é O(1) para operações de inserção, busca e remoção, no caso médio, e O(n) no pior caso.
"""


class HashTable:
    def __init__(self, size):
        self.size = size  # Define o tamanho da tabela hash (O(1))
        self.table = [
            [] for _ in range(size)
        ]  # Inicializa a tabela hash com listas vazias (O(n))

    def hash_function(self, key):
        return hash(key) % self.size  # Calcula o índice para a chave (O(1))

    def insert(self, key, value):
        index = self.hash_function(key)  # Calcula o índice para a chave (O(1))
        for pair in self.table[
            index
        ]:  # Verifica se a chave já existe (O(n), no pior caso)
            if pair[0] == key:
                pair[1] = value  # Atualiza o valor se a chave já existir (O(1))
                return
        self.table[index].append([key, value])  # Insere o novo par chave-valor (O(1))

    def get(self, key):
        index = self.hash_function(key)  # Calcula o índice para a chave (O(1))
        for pair in self.table[index]:  # Procura a chave na lista (O(n), no pior caso)
            if pair[0] == key:
                return pair[1]  # Retorna o valor se a chave for encontrada (O(1))
        return None  # Retorna None se a chave não for encontrada (O(1))

    def remove(self, key):
        index = self.hash_function(key)  # Calcula o índice para a chave (O(1))
        for i, pair in enumerate(
            self.table[index]
        ):  # Procura a chave na lista (O(n), no pior caso)
            if pair[0] == key:
                self.table[index].pop(
                    i
                )  # Remove o par chave-valor se a chave for encontrada (O(1))
                return

    def print_table(self):
        for i, bucket in enumerate(
            self.table
        ):  # Percorre cada bucket na tabela hash (O(n))
            print(f"Bucket {i}:", end=" ")
            for (
                pair
            ) in (
                bucket
            ):  # Percorre cada par chave-valor no bucket (O(m), onde m é o número de pares no bucket)
                print(f"({pair[0]}, {pair[1]})", end=" ")
            print()  # Imprime uma nova linha no final de cada bucket (O(1))


# Exemplo de uso:
ht = HashTable(5)
ht.insert("a", 1)
ht.insert("b", 2)
ht.insert("c", 3)

print(ht.get("a"))  # Output: 1
print(ht.get("b"))  # Output: 2
print(ht.get("c"))  # Output: 3

ht.remove("b")
print(ht.get("b"))  # Output: None
ht.print_table()  # Output: Bucket 0: ('a', 1) Bucket 1: Bucket 2: ('c', 3) Bucket 3: Bucket 4:

# --------------------------------------------------------------------------------

"""
Dynamic Array (List):
O DynamicArray é uma estrutura de dados que simula o funcionamento de uma lista em Python. Ele mantém um array interno que pode crescer dinamicamente à medida que elementos são adicionados. As operações de inserção e remoção podem exigir o deslocamento de elementos, o que pode ser custoso em termos de tempo, enquanto que o acesso aos elementos por índice é eficiente. A complexidade de tempo de um DynamicArray é O(1) para operações de acesso e inserção no final, O(n) para operações de inserção e remoção no início e O(n) para operações de inserção e remoção no meio.
"""


class DynamicArray:
    def __init__(self):
        self.array = []  # Inicializa um array vazio (O(1))
        self.length = 0  # Inicializa o comprimento do array como 0 (O(1))

    def insert(self, index, value):
        if index > self.length or index < 0:  # Verifica se o índice é válido (O(1))
            raise IndexError(
                "Index out of range"
            )  # Lança uma exceção se o índice não for válido (O(1))
        if (
            index == self.length
        ):  # Se o índice for igual ao comprimento do array, adicione o valor no final (O(1))
            self.array.append(None)  # Aumenta o tamanho do array (O(1))
        else:
            # Se o índice for menor que o comprimento do array, desloque todos os elementos à direita do índice um espaço à direita (O(n))
            self.array.append(None)
            for i in range(self.length, index, -1):
                self.array[i] = self.array[i - 1]
        self.array[index] = value  # Insere o valor no índice especificado (O(1))
        self.length += 1  # Atualiza o comprimento do array (O(1))

    def get(self, index):
        if 0 <= index < self.length:  # Verifica se o índice é válido (O(1))
            return self.array[index]  # Retorna o valor no índice especificado (O(1))
        return None  # Retorna None se o índice não for válido (O(1))

    def remove(self, index):
        if 0 <= index < self.length:  # Verifica se o índice é válido (O(1))
            for i in range(
                index, self.length - 1
            ):  # Desloca todos os elementos à direita do índice um espaço à esquerda (O(n))
                self.array[i] = self.array[i + 1]
            self.array.pop()  # Remove o último elemento do array (O(1))
            self.length -= 1  # Atualiza o comprimento do array (O(1))


# Exemplo de uso:
da = DynamicArray()
da.insert(0, 10)
da.insert(1, 20)
print(da.get(0))  # Output: 10
print(da.get(1))  # Output: 20
da.remove(0)
print(da.get(0))  # Output: 20

# --------------------------------------------------------------------------------
