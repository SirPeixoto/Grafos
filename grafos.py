import csv

class Vertice:
    def __init__(self, nomeCidade):
        self.nomeCidade = nomeCidade
        self.vizinhanca = [] #Vertice
        self.conexoes = [] #Aresta

    def info_vertice(self):
        print(f'\nCidade: {self.nomeCidade}')
        print(f'Quantidade de vizinhos: {len(self.vizinhanca)}')
        print(f'Quantidade de conexões: {len(self.conexoes)}\n')

    def info_vizinhos(self):
        if not self.vizinhanca:
            print(f'\n{self.nomeCidade} não possui vizinhos cadastrados.\n')
        else:
            vizinhos_dict = {}

            for vizinho in self.vizinhanca:
                for aresta in self.conexoes:
                    if (aresta.cidade1 == self and aresta.cidade2 == vizinho) or \
                        (aresta.cidade2 == self and aresta.cidade1 == vizinho):
                        vizinhos_dict[vizinho.nomeCidade] = aresta.distancia
                        break

            vizinhos_ordenados = sorted(vizinhos_dict.items(), key=lambda item: item[1])

            print(f'\nVizinhos de {self.nomeCidade}: ')
            for nome_vizinho, distancia in vizinhos_ordenados:
                print(f'- {nome_vizinho} ({distancia} km)')
            print()


    def info_conexoes(self):
        if not self.conexoes:
            print(f'\n{self.nomeCidade} não possui conexões cadastradas.\n')
        else:
            print(f'\nConexões de {self.nomeCidade}:')
            for aresta in self.conexoes:
                print(f'- {aresta.info_aresta()}')
            print()

class Aresta:
    def __init__(self, cidade1, cidade2, distancia):
        self.cidade1 = cidade1
        self.cidade2 = cidade2
        self.distancia = float(distancia)
        
    def info_aresta(self):
        return f'{self.cidade1.nomeCidade} <-> {self.cidade2.nomeCidade} = {self.distancia}km'
    
class Grafo:
    def __init__(self):
        self.cidades = {}
        self.conexoes = []
        
    def cadastro_cidade(self):
        nome = input('\nNome da cidade: ').strip().title()
        if nome in self.cidades:
            print('Cidade já cadastrada!')
        else:
            nova_cidade = Vertice(nome)
            self.cidades[nome] = nova_cidade
            print(f'\nCidade "{nome}" cadastrada com sucesso.\n')


    def cadastro_conexao(self):
        nome_cidade1 = input('\n1° Cidade: ').strip().title()
        nome_cidade2 = input('2ª Cidade: ').strip().title()
        if nome_cidade1 in self.cidades and nome_cidade2 in self.cidades:

            vertice1 = self.cidades[nome_cidade1]
            vertice2 = self.cidades[nome_cidade2] 

            conexao_existe = any(
                (aresta.cidade1 == vertice1 and aresta.cidade2 == vertice2) or
                (aresta.cidade1 == vertice2 and aresta.cidade2 == vertice1)
                for aresta in self.conexoes
            )

            if conexao_existe:
                print('\nEssa conexão já existe!\n')
                return
                
            distancia = float(input('Distância em Km: '))


            nova_aresta = Aresta(vertice1, vertice2, distancia)
            self.conexoes.append(nova_aresta)

            if vertice2 not in vertice1.vizinhanca:
                vertice1.vizinhanca.append(vertice2)
            if vertice1 not in vertice2.vizinhanca:
                vertice2.vizinhanca.append(vertice1)

            if nova_aresta not in vertice1.conexoes:
                vertice1.conexoes.append(nova_aresta)
            if nova_aresta not in vertice2.conexoes:
                vertice2.conexoes.append(nova_aresta)

            print(f'Conexão entre {vertice1.nomeCidade} e {vertice2.nomeCidade} de {distancia} km cadastrada com sucesso.\n')

            with open('conexoes.csv', 'a', encoding='UTF-8', newline='') as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow([vertice1.nomeCidade, vertice2.nomeCidade, f'{distancia}km'])

        else:
            print('Uma das cidades não foi encontrada!')

    def info_cidades(self):
        if not self.cidades:
            print('\nNenhuma cidade encontrada.\n')
        else:
            print('\nCidades encontradas:')
            for nome in sorted(self.cidades.keys()):
                print(f'- {nome}')
            print()

    def info_conexoes(self):
        if not self.conexoes:
            print('\nNenhuma conexão cadastrada.\n')
        else:
            print('\nConexões cadastradas:')
            for aresta in self.conexoes:
                print(f'- {aresta.info_aresta()}')
            print() 

    def importar_conexoes(self):
        with open('conexoes.csv', 'r', encoding='UTF-8') as arquivo:
            for linha in arquivo:
                linhas = linha.strip().split(',')
                if len(linhas) == 3:
                    cidade1 = linhas[0].strip().lower().title()
                    cidade2 = linhas[1].strip().lower().title()
                    distancia = float(linhas[2].replace('km','').strip())
                    if cidade1 not in self.cidades:
                        self.cidades[cidade1] = Vertice(cidade1)
                    if cidade2 not in self.cidades:
                        self.cidades[cidade2] = Vertice(cidade2)

                    vertice1 = self.cidades[cidade1]
                    vertice2 = self.cidades[cidade2]

                    conexao_existe = any(
                        (aresta.cidade1 == vertice1 and aresta.cidade2 == vertice2) or
                        (aresta.cidade1 == vertice2 and aresta.cidade2 == vertice1)
                        for aresta in self.conexoes
                    )

                    if not conexao_existe:
                        nova_aresta = Aresta(vertice1, vertice2, distancia)
                        self.conexoes.append(nova_aresta)

                        if vertice2 not in vertice1.vizinhanca:
                            vertice1.vizinhanca.append(vertice2)
                        if vertice1 not in vertice2.vizinhanca:
                            vertice2.vizinhanca.append(vertice1)

                        if nova_aresta not in vertice1.conexoes:
                            vertice1.conexoes.append(nova_aresta)
                        if nova_aresta not in vertice2.conexoes:
                            vertice2.conexoes.append(nova_aresta)
        print('\nImportação concluída com sucesso!')
    
def menu():
    grafo = Grafo()

    while True:
        print('\n1 - Cadastrar cidade')
        print('2 - Cadastrar conexão')
        print('3 - Listar cidades')
        print('4 - Listar conexões')
        print('5 - Consultar cidade')
        print('6 - Importar conexões do csv')
        print('0 - Sair')

        opcao = input('Selecione uma opção: ')
        
        if opcao == '1':
            grafo.cadastro_cidade()
        elif opcao == '2':
            grafo.cadastro_conexao()
        elif opcao == '3':
            grafo.info_cidades()
        elif opcao == '4':
            grafo.info_conexoes()
        elif opcao == '5':
            while True:
                print('\n1 - Informações do vértice')
                print('2 - Vizinhos')
                print('3 - Conexões')
                print('0 - Sair')

                alter = input('\nO que deseja verificar? ')

                if alter == '0':
                    break

                nome = input('\nDigite o nome da cidade: ').strip().title()
                if nome in grafo.cidades:
                    cidade = grafo.cidades[nome]

                    if alter == '1':
                        cidade.info_vertice()
                    elif alter == '2':
                        cidade.info_vizinhos()
                    elif alter == '3':
                        cidade.info_conexoes()
                    else:
                        print('Opção inválida!')
                else:
                    print('Cidade não encontrada!')
        elif opcao == '6':
            grafo.importar_conexoes()
        elif opcao == '0':
            break
        else:
            print(f'Opção inválida!\n')
    
if __name__ == '__main__':
    menu()