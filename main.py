class ComidaRestaurante:
    def __init__(self, descrição,tipo = "Acompanhamento", nome = "Cheesebúger", preço = 30):
        self.nome = nome
        self.preço = preço
        self.descrição = descrição
        self.tipo = tipo

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_preço(self):
        return self.preço

    def set_preço(self, novo_preço):
        if isinstance(novo_preço, (int or float)):
            self.preço = novo_preço
        else:
            print("Digite apenas números (inteiros ou decimais)")

    def get_descrição(self):
        return self.descrição

    def set_descrição(self, novo_descrição):
        self.descrição = novo_descrição

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, novo_tipo):
        self.tipo = novo_tipo

    def mostra_dados(self):
        print(f" Nome: {self.nome}\n Preço: R${self.preço}\n Descrição: {self.descrição}\n Tipo: {self.tipo}\n")

    def __str__(self):
        return f"{self.nome}, {self.preço}, {self.descrição}, {self.tipo}"

    def calcula_quantidade(self, quantidade):
        return self.preço * quantidade

    def aplica_desconto(self, desconto_percentual):
        self.preço -= self.preço * (desconto_percentual / 100)

    def aumenta_preço(self, aumento):
        self.preço = self.preço + aumento

    def atualiza_valor(self, novo_preço):
        self.preço = novo_preço + novo_preço/10

if __name__ == '__main__':
    comida1 = ComidaRestaurante(preço = 25, descrição = "100g carne bovina, uma fatia de cheddar, pão sem gergelim. Serve 1 pessoa", tipo = "Prato principal")
    comida2 = ComidaRestaurante(nome = "Fritas com Carne", descrição = "Bata frita ondulada, carne suína desfiada, molho barbacue e queijo muçarela. Serve até 3 pessoas")
    comida3 = ComidaRestaurante(nome = "Milkshake ", preço = 18, descrição = "Sorvete de baunilha, leite em pó e calda de caramelo.", tipo = "Bebida e Sobremesa")

    print(f"-Comida 1 :\n Nome: {comida1.get_nome()}\n Preço: R${comida1.get_preço()}\n Descrição: {comida1.get_descrição()}\n Tipo: {comida1.get_tipo()}\n")
    print(f"-Comida 2 :\n Nome: {comida2.get_nome()}\n Preço: R${comida2.get_preço()}\n Descrição: {comida2.get_descrição()}\n Tipo: {comida2.get_tipo()}\n")
    print(f"-Comida 3 :")
    comida3.mostra_dados()

    comida1.set_descrição("100g carne bovina, uma fatia de cheddar, pão sem gergelim.")
    comida2.set_preço(32)
    comida3.set_nome("Milkshake de Ninho")
    comida3.set_tipo("Sobremesa")

    comida1.aplica_desconto(10)
    print("\nComida 1 com 10% de desconto:", comida1.get_preço())
    comida2.aumenta_preço(5)
    print("Preço da Comida 2 aumentado :", comida2.get_preço())
    print("Preço de duas unidade da Comida 3:", comida3.calcula_quantidade(2))

    novo_preço = 40
    comida1.atualiza_valor(novo_preço)
    print("Comida 1 com a gorjeta: ", comida1.get_preço())