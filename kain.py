def standardize_names(character_name):

    name = character_name.strip()
    new_name = name.replace(" ", "-")

    return new_name

if __name__ == "__main__":

    hero_standardized = standardize_names(" Batman     ")
    print(hero_standardized)

    hero_standardized = standardize_names("      Super Man")
    print(hero_standardized)

def standardize_title(title):

    new_title = title.title()

    return new_title

if __name__ == "__main__":

    title = standardize_title("cinco quartos de laranja")
    print(title)


text = """a famosa atriz Constance Rattigan recebe uma encomenda desagradável: uma lista com números de
telefone de pessoas que morreram recentemente. é uma coisa assustadora, considerando que os nomes das
poucas pessoas vivas presentes na lista estão assinalados em vermelho com
uma cruz. O da própria Constance é um deles."""

def standardize_text(text):

    new_text = text.capitalize()

    return new_text


if __name__ == "__main__":

    normalized_text = standardize_text(text)
    print(normalized_text)

text = "pense num deserto"

def title_creator(text):

    new_text = text.title()
    center_text = new_text.center(57, "-")

    return center_text

if __name__ == "__main__":

    title = title_creator(text)
    print(title)


text_of_blog_a = """
na Londres do pós-guerra, a escritora     Juliet tenta encontrar uma   trama para seu novo livro. ela 
recebe ajuda por meio de uma     carta de um      desconhecido, um nativo da ilha de Guernsey, 
em cujas mãos havia chegado um livro    que há tempos tinha pertencido    a Juliet.
"""
text_of_blog_b = """
O romance "Cinco Quartos de Laranja" é como   um vinho intenso e delicado.    usando metáforas
culinárias, personagens peculiares   e acontecimentos sobrenaturais,      Harris cria uma história
complexa e      bela ao mesmo tempo.
"""

def text_merge(text_of_blog_a, text_of_blog_b):
    


if __name__ == "__main__":

    merged_text = text_merge(text_of_blog_a, text_of_blog_b)
    print(merged_text)