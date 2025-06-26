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
            print(f'\nVizinhos de {self.nomeCidade}:')
            for vizinho in self.vizinhanca:
                print(f'- {vizinho.nomeCidade}')
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

            for aresta in self.conexoes:
                if (aresta.cidade1 == self.cidades[nome_cidade1] and aresta.cidade2 == self.cidades[nome_cidade2]) or \
                (aresta.cidade1 == self.cidades[nome_cidade2] and aresta.cidade2 == self.cidades[nome_cidade1]):
                    print('\nEssa conexão já existe!\n')
                    return
                
            distancia = float(input('Distância em Km: '))

            vertice1 = self.cidades[nome_cidade1]
            vertice2 = self.cidades[nome_cidade2] 

            nova_aresta = Aresta(vertice1, vertice2, distancia)
            self.conexoes.append(nova_aresta)

            vertice1.vizinhanca.append(vertice2)
            vertice2.vizinhanca.append(vertice1)

            vertice1.conexoes.append(nova_aresta)
            vertice2.conexoes.append(nova_aresta)

            print(f'Conexão entre {vertice1.nomeCidade} e {vertice2.nomeCidade} de {distancia} km cadastrada com sucesso.\n')

        else:
            print('Uma das cidades não foi encontrada!')

    def info_cidades(self):
        if not self.cidades:
            print('\nNenhuma cidade encontrada.\n')
        else:
            print('\nCidades encontradas:')
            for nome in self.cidades:
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

    
def menu():
    grafo = Grafo()

    while True:
        print('1 - Cadastrar cidade')
        print('2 - Cadastrar conexão')
        print('3 - Listar cidades')
        print('4 - Listar conexões')
        print('5 - Consultar cidade')
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

                alter = input('O que deseja verificar? ')

                nome = input('\nDigite o nome da cidade: ').strip().title()
                if nome in grafo.cidades:
                    cidade = grafo.cidades[nome]

                if alter == '1':
                    cidade.info_vertice()
                elif alter == '2':
                    cidade.info_vizinhos()
                elif alter == '3':
                    cidade.info_conexoes()
                elif alter == '0':
                    break
                else:
                    print('Opção inválida!')
        elif opcao == '0':
            break
        else:
            print(f'Opção inválida!\n')
    
if __name__ == '__main__':
    menu()