
from pyexpat.errors import codes
import re

# variaveis
codes = ["288355555123888", "335333555584333", "223343555124001", "002111555874555", "111188555654777", "111333555123333", "432055555123888", "079333555584333", "155333555124001", "333188555584333",
         "555288555123001", "111388555123555", "288000555367333", "066311555874001", "110333555123555", "333488555584333", "455448555123001", "022388555123555", "432044555845333", "034311555874001", "102401555999888", "102401555999001", "102401555999111"]


# Separar codigos
def separarNumero(code):
    grupoSeparado = re.findall('...', code)
    return list(map(lambda value: int(value), grupoSeparado))

# classe para calcular região


class TotalRegiao:
    def __init__(self, type):
        self.type = type
        self.sudoeste = 0
        self.sul = 0
        self.centroOeste = 0
        self.norte = 0
        self.nordeste = 0
        self.regiaoNaoEncontrada = 0

    def set(self, regiao):
        if(regiao == "Sudoeste"):
            self.sudoeste += 1
        elif(regiao == "Centro Oeste"):
            self.centroOeste += 1
        elif(regiao == "Nordeste"):
            self.nordeste += 1
        elif(regiao == "Norte"):
            self.norte += 1
        elif(regiao == "Sul"):
            self.sul += 1
        else:
            self.regiaoNaoEncontrada += 1

    def output(self):
        print("Total " + self.type)
        print("")
        print("Total Sudoeste: ", self.sudoeste)
        print("Total Sul: ", self.sul)
        print("Total Centro Oeste: ", self.centroOeste)
        print("Total Norte: ", self.norte)
        print("Total Nordeste: ", self.nordeste)
        print("Total Região não encontrada: ", self.regiaoNaoEncontrada)
        print("")


# variais com classe
totalOrigem = TotalRegiao("Origem")
totalDestino = TotalRegiao("Destino")

# Encontrando a região


def regiao(code, type):
    name = ""
    code = int(code)
    if (code >= 201 and code <= 299):

        name = "Centro Oeste"
    elif(code >= 300 and code <= 399):

        name = "Nordeste"

    elif(code >= 400 and code <= 499):

        name = "Norte"

    elif(code >= 1 and code <= 99):

        name = "Sudoeste"

    elif(code >= 100 and code <= 199):

        name = "Sul"

    else:
        name = "Região não encontrada"

    # Setando contadores
    if (type == "origem"):
        totalOrigem.set(name)
    else:
        totalDestino.set(name)

    return name

# lista de codigos validos


def validacao(produto, origem, vendedor):
    if (produto == "Produto não identificado"):
        return False
    elif(produto == "Joias" and origem == "Centro Oeste"):
        return False
    elif(vendedor == 367):
        return False
    else:
        return True


# Verificar se o produto é da Loggi
def codloggi(code):
    code = int(code)
    if(code != 555):
        return "Loggi"
    else:
        return "Produto não pertence a Loggi"

# Tipo de produto


def tipoProduto(code):
    code = int(code)
    if (code == 1):
        return"Joias"
    elif(code == 111):
        return"Livros"
    elif(code == 333):
        return"Eletrônicos"
    elif(code == 555):
        return"Bebidas"
    elif(code == 888):
        return"Brinquedos"
    else:
        return "Produto não identificado"

# classe para manter dados das entregas


class Entrega:
    def __init__(self, code):

        numSeparado = separarNumero(code)
        self.numSeparado = numSeparado
        self.code = code
        self.origem = regiao(numSeparado[0], "origem").upper()
        self.destino = regiao(numSeparado[1], "destino").upper()
        self.loggi = codloggi(numSeparado[2])
        self.vendedor = (numSeparado[3])
        self.produto = tipoProduto(numSeparado[4])
        self.valido = validacao(self.produto, self.origem, self.vendedor)

# validos invalidos print
    def validosEInvalidos(self):
        print("Numero de rastreamento: ", self.code)
        if (self.valido == True):
            print("Entrega Válida")
        else:
            print("Entrega Inválida")
        print("")

# impressão padrão todas as informaçoes
    def output(self):
        print("Trincas: ", self.numSeparado)
        print("Numero de rastreamento: ", self.code)
        print("Origem: ", self.origem)
        print("Destino: ", self.destino)
        print("Vendedor: ", self.vendedor)
        print("Tipo de produto: ", self.produto)
        if (self.valido == True):
            print("Entrega Válida")
        else:
            print("Entrega Inválida")
        print("")

# impressão destino e tipo de produto
    def destinoETipo(self):
        print("Numero de rastreamento: ", self.code)
        print("Tipo de produto: ", self.produto)
        print("Destino: ", self.destino)

# impressão destino norte
    def destinoNorte(self):
        print("Numero de rastreamento: ", self.code)
        print("Tipo de produto: ", self.produto)
        print("Destino: ", self.destino)
        print("Origem: ", self.origem)

# classe para calculo


class Entregas:
    # variaveis
    def __init__(self):
        self.lista = []
        self.gerador()
        self.vendedor123 = 0
        self.vendedor584 = 0
        self.vendedor124 = 0
        self.vendedor874 = 0
        self.vendedor654 = 0
        self.vendedor845 = 0
        self.notfound = 0
        self.bancoDeDadosVendedores()
        self.centroOeste = []
        self.nordeste = []
        self.norte = []
        self.sudeste = []
        self.sul = []
        self.totalRegiaoValido()
        self.desSul = []
        self.desNorte = []
        self.desNordeste = []
        self.desSudeste = []
        self.desCentro = []

    def append(self, entrega):
        self.lista.append(entrega)

    # Gerador
    def gerador(self):
        for code in codes:
            entrega = Entrega(code)
            self.append(entrega)

    # Validaçoes
    def validacoes(self, type):
        if(type == "validas"):
            print("Entregas válidas")
        elif(type == "invalidas"):
            print("Entregas inválidas")
        else:
            print("Entregas válidas e inválidas")

        for entrega in self.lista:
            if (type == "validas" and entrega.valido == True):
                entrega.validosEInvalidos()
            if(type == "invalidas" and entrega.valido == False):
                entrega.validosEInvalidos()
            if(type == "todas"):
                entrega.validosEInvalidos()
        print("")

    # Entrega valida
    def validos(self):
        self.validacoes("validas")

    # Entrega invalida
    def invalidos(self):
        self.validacoes("invalidas")

    # entrega todas
    def todas(self):
        self.validacoes("todas")

    # entregas Sul /brinquedos
    def entregasSul(self):
        print("Entregas que possuem brinquedos com origem no Sul")
        for entrega in self.lista:
            if(entrega.produto == "Brinquedos" and entrega.origem == "Sul"):
                entrega.output()
        print("")

    # Calculos vendedores
    def bancoDeDadosVendedores(self):

        for entrega in self.lista:
            if (entrega.vendedor == 123 and entrega.valido == True):
                self.vendedor123 += 1
            elif (entrega.vendedor == 584 and entrega.valido == True):
                self.vendedor584 += 1
            elif (entrega.vendedor == 124 and entrega.valido == True):
                self.vendedor124 += 1
            elif (entrega.vendedor == 874 and entrega.valido == True):
                self.vendedor874 += 1
            elif (entrega.vendedor == 654 and entrega.valido == True):
                self.vendedor654 += 1
            elif (entrega.vendedor == 845 and entrega.valido == True):
                self.vendedor845 += 1
            else:
                self.notfound += 1
    # impressão vendedores

    def vendedoresOutput(self):
        print("Numero de pacotes enviados por vendedor")
        print("")
        print("N° 123: ", self.vendedor123)
        print("N° 584: ", self.vendedor584)
        print("N° 124: ", self.vendedor124)
        print("N° 874: ", self.vendedor874)
        print("N° 654: ", self.vendedor654)
        print("N° 845: ", self.vendedor845)

    # impressão
    def output(self):
        for entrega in self.lista:

            entrega.output()

    # total validos por região
    def totalRegiaoValido(self):

        for entrega in self.lista:
            if (entrega.destino == "CENTRO OESTE" and entrega.valido == True):
                self.centroOeste.append(entrega)
            if (entrega.destino == "NORDESTE" and entrega.valido == True):
                self.nordeste.append(entrega)
            if (entrega.destino == "NORTE" and entrega.valido == True):
                self.norte.append(entrega)
            if (entrega.destino == "SUL" and entrega.valido == True):
                self.sul.append(entrega)
            if (entrega.destino == "SUDESTE" and entrega.valido == True):
                self.sudeste.append(entrega)

    # impressão validos
    def totalRegiaoValidooutput(self):
        print("")
        if (len(self.centroOeste) == 0):
            print("Não possui entregas com destino Centro Oeste")
        else:
            print("Entregas no Centro Oeste")
            for entrega in self.centroOeste:
                entrega.output()
                print("")
        if (len(self.sul) == 0):
            print("Não possui entregas com destino Sul")
        else:
            print("Entregas no Sul")
            for entrega in self.sul:
                entrega.output()
                print("")
        if (len(self.norte) == 0):
            print("Não possui entregas com destino Norte")
        else:
            print("Entregas no Norte")
        for entrega in self.norte:
            entrega.output()
        if (len(self.nordeste) == 0):
            print("Não possui entregas com destino Nordeste")
        else:
            print("Entregas no Nordeste")
        for entrega in self.nordeste:
            entrega.output()
        if (len(self.sudeste) == 0):
            print("Não possui entregas com destino Sudeste")
        else:
            print("Entregas no Sudeste")
        for entrega in self.sudeste:
            entrega.output()

    # destino e tipo de produto
    def destinoETipo(self):
        print("")
        if (len(self.centroOeste) == 0):
            print("Não possui entregas com destino Centro Oeste")
        else:
            print("Entregas no Centro Oeste")
            for entrega in self.centroOeste:
                entrega.destinoETipo()
            print("")
        if (len(self.sul) == 0):
            print("Não possui entregas com destino Sul")
        else:
            print("Entregas no Sul")
        for entrega in self.sul:
            entrega.destinoETipo()
            print("")
        if (len(self.norte) == 0):
            print("Não possui entregas com destino Norte")
        else:
            print("Entregas no Norte")
        for entrega in self.norte:
            entrega.destinoETipo()
            print("")
        if (len(self.nordeste) == 0):
            print("Não possui entregas com destino Nordeste")
        else:
            print("Entregas no Nordeste")
        for entrega in self.nordeste:
            entrega.destinoETipo()
            print("")
        if (len(self.sudeste) == 0):
            print("Não possui entregas com destino Sudeste")
        else:
            print("Entregas no Sudeste")
        for entrega in self.sudeste:
            entrega.destinoETipo()
            print("")

    # separar destinos
    def separarDestinos(self):
        for entrega in self.lista:
            if (entrega.produto == "Joias" and entrega.destino == "NORTE" and (entrega.origem == "SUL" or entrega.origem == "CENTRO OESTE" or entrega.origem == "SUDESTE")):
                self.desNorte.append(entrega)

        for entrega in self.lista:
            if (entrega.produto != "Joias" and entrega.destino == "NORTE" and (entrega.origem == "SUL" or entrega.origem == "CENTRO OESTE" or entrega.origem == "SUDESTE")):
                self.desNorte.append(entrega)

        if (len(self.desNorte) == 0):
            print(
                "Não possui entregas com destino NORTE que passam pelo Centro Oeste")
            print("")
        else:
            print("Pacotes com destino NORTE que passam pelo Centro Oeste")
            print("")

    # impressão destino
    def destinoNorteoutput(self):
        if (len(self.desNorte) == 0):
            print(
                "Não possui entregas com destino NORTE que passam pelo Centro Oeste")
            print("")
        else:
            print("Pacotes com destino NORTE que passam pelo Centro Oeste")
            print("")
            for entrega in self.desNorte:
                entrega.destinoNorte()
                print("")


    # Principal(Sempre deixar funcional)
entregas = Entregas()

# 1# total por região (tire do comentario para executar)
# totalDestino.output()

# 2# lista de entregas validas e invalidas (tire do comentario para executar)
# entregas.todas()

# 3# lista de entregas que tem origem no sul e são brinquedos (tire do comentario para executar)
# entregas.entregasSul()

# 4# total por região validas (tire do comentario para executar)
# entregas.totalRegiaoValidooutput()

# 5# quantidade de envios por vendedor (tire do comentario para executar)
# entregas.vendedoresOutput()

# 6# lista de entregas e tipos de produtos (tire do comentario para executar)
# entregas.destinoETipo()

# 7-8-9 #entregas con distino ao Norte que passam pelo centro oeste
# entregas.destinoNorteoutput()

# 10# lista de entregas invalidas (tire do comentario para executar)
# entregas.invalidos()

##EXTRA##
# Extra# informaçoes completas por codigo (tire do comentario para executar)
# entregas.output()

# EXTRA# lista de entregas validas (tire do comentario para executar)
# entregas.validos()


# EXTRA# total por região origem (tire do comentario para executar)
# totalOrigem.output()
