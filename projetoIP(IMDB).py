from imdb import Cinemagoer
import requests

API_URL = "https://api-inference.huggingface.co/models/lvwerra/distilbert-imdb"
headers = {"Authorization": "Bearer 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"}

ia = Cinemagoer()
def pesquisar(txt):
    x_id = txt.movieID
    fx_id = ia.get_movie(x_id)
    print(f'{fx_id["title"]:^80}', end=' ')
    print(f'Ano: {fx_id["year"]}')
    print(f'Tempo: {fx_id["runtimes"][0]} min')
    print(f'Nota: {fx_id["rating"]}')
    print(f'{fx_id["plot"][0]:}')
    output = query({
        "inputs": input("")})
    print(output)

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def reiniciar():
    usuario_sabe_filme = str(input('Você sabe qual filme quer assistir [s/n]? ')).upper()[0].strip()
    while usuario_sabe_filme not in 'SN':
        usuario_sabe_filme = str(input('Deseja pesquisar um filme [s/n]: ')).upper()[0].strip()

    if usuario_sabe_filme == 'S':
        filme_2 = ia.search_movie(input('Escreva o título do filme: '))

        for i in range(0, 10):
            print(f'[{i + 1}] - {filme_2[i]}')
        opc = int(input('Escolha uma opção: '))
        while opc not in range(1, 11):
            opc = int(input('Escolha uma opção: '))
        filme_2 = filme_2[opc - 1]

        # encontrando id do  filme:
        filmeid_2 = filme_2.movieID

        # encontrando o filme com banco de dados maior:
        filme2 = ia.get_movie(filmeid_2)

        # imprimindo o filme escolhido:
        print(filme2['title'])

        # confirmando se é o filme certo com tratamento de erro
        filme_certo = str(input('Esse é o filme que você estava procurando [s/n]? ')).upper()[0].strip()
        while filme_certo not in 'SN':
            filme_certo = str(input('Esse é o filme que você estava procurando [s/n]? ')).upper()[0].strip()
        if filme_certo == 'S':
            pesquisar(filme_2)
        elif filme_certo == 'N':
            reiniciar()
            exit()
    elif usuario_sabe_filme == 'N':
        genero()

def genero():

    lista_filtros_portugues = ['Gênero', 'Pessoa']
    lista_de_filtros = ['genre', 'person']
    print('Escolha um filtro:')
    for i in range(0, len(lista_filtros_portugues)):
        print(f'[{i + 1}] - {lista_filtros_portugues[i]}')
    filtro = int(input('Escolha um filtro: '))
    while filtro not in range(1, len(lista_filtros_portugues) + 1):
        filtro = int(input('Escolha um filtro: '))
    filtro = lista_de_filtros[filtro - 1]
    if filtro == 'genre':
        # definindo a lista de gêneros:
        lista_generos_portugues = ['Ação', 'Aventura', 'Animação', 'Biografia', 'Comédia',
                                   'Crime', 'Documentário', 'Drama', 'Família', 'Fantasia',
                                   'Film-Noir', 'História', 'Horror', 'Música', 'Musical',
                                   'Mistério', 'Romance', 'Ficção Científica', 'Esporte', 'Suspense',
                                   'Guerra', 'Faroeste']

        lista_generos = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy',
                         'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy',
                         'Film-Noir', 'History', 'Horror', 'Music', 'Musical',
                         'Mystery', 'Romance', 'Sci-Fi', 'Sport', 'Thriller',
                         'War', 'Western']

        # usuário escolhe o gênero:
        print('Escolha um gênero:')
        for i in range(0, len(lista_generos)):
            print(f'[{i + 1}] - {lista_generos_portugues[i]}')
        genero = int(input('Escolha um gênero: '))
        while genero not in range(1, len(lista_generos_portugues) + 1):
            genero = int(input('Escolha um gênero: '))
        genero = lista_generos[genero - 1]

        # imprimindo os 10 primeiros filmes do gênero escolhido:
        top = ia.get_top50_movies_by_genres(genero)
        for i in range(0, 10):
            print(f'[{i + 1}] - {top[i]}')
        opc_genero = int(input('Escolha um filme: '))
        while opc_genero not in range(1, 11):
            opc_genero = int(input('Escolha um filme: '))
        filme_escolhido = top[opc_genero - 1]
        pesquisar(filme_escolhido)

    elif filtro == 'person':
        # usuário pesquisa a pessoa:
        pessoa = ia.search_person(input('Escreva o nome da pessoa: '))

        # usuário escolhe uma das opções de pessoa:
        print('Escolha uma das opções:')
        for i in range(0, 5):
            print(f'[{i + 1}] - {pessoa[i]}')
        opc_pessoa = int(input('Escolha uma opção: '))
        while opc_pessoa not in range(1, 6):
            opc_pessoa = int(input('Escolha uma opção: '))
        pessoa = pessoa[opc_pessoa - 1]
        print(pessoa)
        # confirmando se é a pessoa certa com tratamento de erro:
        ator_certo = str(input('O ator acima é o que você estava procurando [s/n]? ')).upper()[0].strip()
        while ator_certo not in 'SN':
            ator_certo = str(input('O ator acima é o que você estava procurando [s/n]? ')).upper()[0].strip()

        # encontrando id da pessoa:
        person_id = pessoa.personID

        # encontrando a pessoa com banco de dados maior:
        pessoa_id = ia.get_person(person_id)

        if ator_certo == 'S':
            filmes = ia.get_person(person_id)['filmography']
            # imprimindo os 10 pricipais filmes que a pessoa participou:
            for i in range(0, 10):
                print(f'[{i + 1}] - {filmes["actor"][i]}')
            opc_filme = int(input('Escolha um filme: '))
            while opc_filme not in range(1, 11):
                opc_filme = int(input('Escolha um filme: '))
            filme_escolhido = filmes["actor"][opc_filme - 1]
            pesquisar(filme_escolhido)
        elif ator_certo == 'N':
            while ator_certo == 'N':
                reiniciar()
                exit()


p = str(input('Você deseja pesquisar um filme [s/n]? ')).upper()[0].strip()

while p not in 'SN':
    p = str(input('Você deseja pesquisar um filme [s/n]? ')).upper()[0].strip()

if p == 'S':
    filme_entrada = ia.search_movie(input('Escreva o título do filme: '))

    for i in range(0, 10):
        print(f'[{i + 1}] - {filme_entrada[i]}')
    opc = int(input('Escolha uma opção: '))

    while opc not in range(1, 11):
        opc = int(input('Escolha uma opção: '))

    filme_entrada = filme_entrada[opc - 1]
    movie_id = filme_entrada.movieID
    filme_id = ia.get_movie(movie_id)

    print(filme_id['title'])
    filme_certo = str(input('Esse é o filme que você estava procurando [s/n]? ')).upper()[0].strip()

    if filme_certo == 'S':
        pesquisar(filme_entrada)

    elif filme_certo == 'N':
        while filme_certo == 'N':
            reiniciar()
            exit()

elif p == 'N':
    genero()
