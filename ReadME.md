## **Table of Contents**
- [Extra - Strings](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1a_ee_01_strings.html&ref=master#mcetoc_1esj4slvm0) 
  - [Objetivo](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1a_ee_01_strings.html&ref=master#mcetoc_1f33pqfa47)
  - [Preparativos](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1a_ee_01_strings.html&ref=master#mcetoc_1f33pqfa48)
- [Exercícios](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1a_ee_01_strings.html&ref=master#mcetoc_1egvsckqv3)
- [Entregáveis](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1a_ee_01_strings.html&ref=master#mcetoc_1egvoav555j) 
  - [Repositório](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1a_ee_01_strings.html&ref=master#mcetoc_1egvrpv6k1l4)
- [Critérios de aceitação](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1a_ee_01_strings.html&ref=master#mcetoc_1eh146n6m3)
# **Extra - Strings**
Nessa entrega você exercitará seus conhecimentos sobre métodos de string desenvolvendo operações de fatiamento e processamento de strings no estilo **kata**.


## **Objetivo**
Trabalhar seus conhecimentos sobre strings e a utilização dos seus métodos. 


## **Preparativos**
Você deverá criar um arquivo chamado **kain.py** para a implementação das funções.
# **Exercícios**
Defina as seguintes funções, observando os exemplos de retorno de cada uma:  

- **standardize\_names(character\_name)** 
  - **Parâmetros:** Nome do personagem a ser normalizado.
  - **Procedimento:** A função deve: 
    - Remover os **espaços a esquerda e a direita** do texto passado em **character\_name**;
    - Separar **nomes compostos** por **hífen**.
  - **Retorno:** Nome do personagem normalizado.

\# EXEMPLO 1:

hero\_standardized = standardize\_names(" Batman     ")

print(hero\_standardized)

\> Batman

\# EXEMPLO 2

hero\_standardized = standardize\_names("      Super Man")

print(hero\_standardized)

\> Super-Man



- **standardize\_title(title)** 
  - **Parâmetros:** Título de um livro, filme ou série a ser normalizado.
  - **Procedimento:** A função deve: 
    - Colocar a primeira letra de cada palavra em **maiúsculo**.
  - **Retorno:** O título normalizado.

\# EXEMPLO 1

title = standardize\_title("cinco quartos de laranja")

print(title)

\> Cinco Quartos De Laranja



- **standardize\_text(text)** 
  - **Parâmetros:** texto de um lívro não normalizado.
  - **Procedimento:** A função deve: 
    - Fazer com que a primeira letra do texto seja **maiúscula**;
    - A letra após a primeira ocorrência de um ponto deve ser **maiúscula**.
  - **Retorno:** O texto normalizado. 

\# EXEMPLO 1

text = """a famosa atriz Constance Rattigan recebe uma encomenda desagradável: uma lista com números de

telefone de pessoas que morreram recentemente. é uma coisa assustadora, considerando que os nomes das

poucas pessoas vivas presentes na lista estão assinalados em vermelho com

uma cruz. O da própria Constance é um deles."""

normalized\_text = standardize\_text(text)

print(normalized\_text)

\> A famosa atriz Constance Rattigan recebe uma encomenda desagradável: uma 

lista com números de telefone de pessoas que morreram recentemente. É uma 

coisa assustadora, considerando que os nomes das poucas pessoas vivas presentes

na lista estão assinalados em vermelho com uma cruz. O da própria Constance é um deles.



- **title\_creator(text)** 
  - **Parâmetros:** Um texto com o qual o título será criado.
  - **Procedimento:** A função deve: 
    - Setar a primeira letra de cada palavra para **maiúsculo**;
    - **Centralizar o título**, inserindo **20** **hífens a esquerda** e **20 hífens a direita** do título.
  - **Retorno:** O título criado. 

\# Exemplo 1

text = "pense num deserto"

title = title\_creator(text)

print(title)

\> --------------------Pense Num Deserto--------------------



- **text\_merge(text\_of\_blog\_a, text\_of\_blog\_b)** 
  - **Parâmetros:** Um texto com o qual o título será criado.
  - **Procedimento:** A função deve: 
    - Remover mais de um espaço entre as palavras de ambos os textos;
    - A letra após um ponto deve ser **maiúscula em ambos os textos**;
    - Setar a primeira letra do texto **text\_of\_blog\_a** para **maiúsculo**;
    - Setar a primeira letra do texto **text\_of\_blog\_b** para **minúsculo**;
    - Remover o ponto final do texto **text\_of\_blog\_a**;
    - Juntar o texto **text\_of\_blog\_a** com o texto **text\_of\_blog\_b**.
  - **Retorno:** O texto resultado da união entre o texto **text\_of\_blog\_a** e **text\_of\_blog\_b**. 

text\_of\_blog\_a = """

na Londres do pós-guerra, a escritora     Juliet tenta encontrar uma   trama para seu novo livro. ela 

recebe ajuda por meio de uma     carta de um      desconhecido, um nativo da ilha de Guernsey, 

em cujas mãos havia chegado um livro    que há tempos tinha pertencido    a Juliet.

"""

text\_of\_blog\_b = """

O romance "Cinco Quartos de Laranja" é como   um vinho intenso e delicado.    usando metáforas

culinárias, personagens peculiares   e acontecimentos sobrenaturais,      Harris cria uma história

complexa e      bela ao mesmo tempo.

"""

merged\_text = text\_merge(text\_of\_blog\_a, text\_of\_blog\_b)

print(merged\_text)

\> Na Londres do pós-guerra, a escritora Juliet tenta encontrar uma trama para seu novo livro. Ela 

recebe ajuda por meio de uma carta de um desconhecido, um nativo da ilha de Guernsey, em cujas

mãos havia chegado um livro que há tempos tinha pertencido a Juliet o romance 

"Cinco Quartos de Laranja" é como um vinho intenso e delicado. Usando metáforas culinárias, 

personagens peculiares e acontecimentos sobrenaturais, Harris cria uma história complexa e bela

ao mesmo tempo.

-----
# **Entregáveis**
## **Repositório**
- Link do **repositório** do **GitLab**
- **Código fonte:** 
  - arquivo **kain.py**.
- **Privacidade** 
  - Incluir **ka-br-out-2020-correcoes** como REPORTER.
-----
# **Critérios de aceitação**

|**pts**|**Dado**|**Quando**|**É esperado**|
| :-: | :-: | :-: | :-: |
|1.0|Função **standardize\_names**|Executada a bateria de testes semelhante ao que foi especificado nas **Entradas e Saídas**.|O retorno seja de acordo com o especificado.|
|1.0|Função **standardize\_title(title)**|Executada a bateria de testes semelhante ao que foi especificado nas **Entradas e Saídas**.|O retorno seja de acordo com o especificado.|
|1.0|Função **standardize\_text(text)**|Executada a bateria de testes semelhante ao que foi especificado nas **Entradas e Saídas**.|O retorno seja de acordo com o especificado.|
|1.0|Função **title\_creator(text)**|Executada a bateria de testes semelhante ao que foi especificado nas **Entradas e Saídas**.|O retorno seja de acordo com o especificado.|
|1.0|Função **text\_merge(text\_of\_blog\_a, text\_of\_blog\_b)**|Executada a bateria de testes semelhante ao que foi especificado nas **Entradas e Saídas**.|O retorno seja de acordo com o especificado.|


**Boa diversão, devs! 🤠**






