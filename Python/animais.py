class Reptil():

    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade

    def tomar_sol(self):
        return '{} tomando sol'.format(self.nome)

    def botar_ovo(self):
        if self.idade > 2:
            return '{} botou um ovo'.format(self.nome)
        else:
            return'{} ainda não atingiu maturidade sexual'.format(self.nome)

class Mamifero():

    def __init__(self, nome, cor_pelo, idade, tipo_pata):
        self.nome = nome
        self.cor_pelo = cor_pelo
        self.idade = idade
        self.tipo_pata = tipo_pata

    def correr(self):
        return '{} correndo'.format(self.nome)

    def mamar(self):
        if self.idade <= 1 :
            return '{} mamando'.format(self.nome)
        else:
            return '{} já desmamou'.format(self.nome)

class Camaleao(Reptil):

    def __init__(self, nome, cor, idade, inseto_favorito):
        super().__init__(nome, cor, idade)
        self.inseto_favorito = inseto_favorito

    def mudar_de_cor(self):
        return '{} mudando de cor'.format(self.nome)

    def comer_inseto(self):
        return '{} comendo inseto'.format(self.nome)

class Cavalo(Mamifero):

    def __init__(self, nome, cor_pelo, idade, tipo_pata, cor_crina):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.cor_crina = cor_crina
    
    def galopar(self):       
        return '{} galopando'.format(self.nome)
    
    def relinchar(self):
        return '{} relinchando'.format(self.nome)

class Cobra(Reptil):

    def __init__(self, nome, cor, idade, veneno):
        super().__init__(nome, cor, idade)
        self.veneno = veneno

    def rastejar(self):
        return '{} rastejando'.format(self.nome)

    def trocar_de_pele(self):
        return '{} trocando de pele'.format(self.nome)

class Cachorro(Mamifero):

    def __init__(self, nome, cor_pelo, idade, tipo_pata, raca):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.raca = raca

    def latir(self):
        return '{} latindo'.format(self.nome)

    def rosnar(self):
        return '{} rosnando'.format(self.nome)

class Jacare(Reptil):

    def __init__(self, nome, cor, idade, num_dentes):
        super().__init__(nome, cor, idade)
        self.num_dentes = num_dentes

    def atacar(self):
        return '{} atacando'.format(self.nome)

    def dormir(self):
        return '{} dormindo'.format(self.nome)

class Gato(Mamifero):

    def __init__(self, nome, cor_pelo, idade, tipo_pata):
        super().__init__(nome, cor_pelo, idade, tipo_pata)
        self.vidas = 7

    def miar(self):
        return '{} miando'.format(self.nome)

    def morrer(self):
        self.vidas -= 1
        if self.vidas <= 0:
            return '{} morreu'.format(self.nome)
        else:
            return '{} tem {} vidas sobrando'.format(self.nome, self.vidas)   

def main():
    Camufla = Camaleao("Disfarce", "green", 6, "Grilo")
    print(Camufla.nome)
    print(Camufla.cor)
    print(Camufla.idade)
    print(Camufla.inseto_favorito)
    print(Camufla.tomar_sol())
    print(Camufla.mudar_de_cor())
    print(Camufla.comer_inseto())
    print("==========================================")

    Wildfire = Cavalo("Cavalo de Fogo", "Roxa",10, "Quadrúpede", "Vermelho")
    print(Wildfire.nome)
    print(Wildfire.cor_pelo)
    print(Wildfire.idade)
    print(Wildfire.tipo_pata)
    print(Wildfire.cor_crina)
    print(Wildfire.correr())
    print(Wildfire.mamar())
    print(Wildfire.galopar())
    print(Wildfire.relinchar())
    print("==========================================")

    Cascavel = Cobra("Orochimaru", "Vinho", 10, "Mortal")
    print(Cascavel.nome)
    print(Cascavel.cor)
    print(Cascavel.idade)
    print(Cascavel.veneno)
    print(Cascavel.tomar_sol())
    print(Cascavel.botar_ovo())
    print(Cascavel.rastejar())
    print(Cascavel.trocar_de_pele())
    print("==========================================")

    Pastor = Cachorro("Alemão", "Marrom", 8, "Quadrúpede", "Pastor Alemão")
    print(Pastor.nome)
    print(Pastor.cor_pelo)
    print(Pastor.idade)
    print(Pastor.tipo_pata)
    print(Pastor.raca)
    print(Pastor.correr())
    print(Pastor.mamar())
    print(Pastor.latir())
    print(Pastor.rosnar()) 
    print("==========================================")

    Alligator = Jacare("Cuca", "Verde", 15, 40)
    print(Alligator.nome)
    print(Alligator.cor)
    print(Alligator.idade)
    print(Alligator.num_dentes)
    print(Alligator.tomar_sol())
    print(Alligator.botar_ovo())
    print(Alligator.atacar()) 
    print(Alligator.dormir())
    print("==========================================")

    Siames = Gato("Garfield", "Amarelo", 5, "Quadrúpede")
    print(Siames.nome)
    print(Siames.cor_pelo)
    print(Siames.idade)
    print(Siames.tipo_pata)
    print(Siames.correr())
    print(Siames.mamar())
    print(Siames.miar())
    print(Siames.morrer())
    print(Siames.morrer())
    print(Siames.morrer())
    print(Siames.morrer())
    print(Siames.morrer())
    print(Siames.morrer())
    print(Siames.morrer())

if __name__ == "__main__":
    main()