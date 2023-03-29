class Imobiliaria:
    def __init__(self, qtd_quartos: int, vaga_estacionar: int, qtd_banheiro: int, tamanho: float) -> None:
        self.qtd_quartos = qtd_quartos
        self.vaga_estacionar = vaga_estacionar
        self.qtd_banheiro = qtd_banheiro
        self.tamanho = tamanho
        self.imovel = []

class Escritorio(Imobiliaria):
    def __init__(self, qtd_quartos: int, vaga_estacionar: int, qtd_banheiro: int, tamanho: float) -> None:
        super().__init__(qtd_quartos, vaga_estacionar, qtd_banheiro, tamanho)

class Casa(Imobiliaria):
    def __init__(self, qtd_quartos: int, vaga_estacionar: int, qtd_banheiro: int, tamanho: float) -> None:
        super().__init__(qtd_quartos, vaga_estacionar, qtd_banheiro, tamanho)

class Quarto(Imobiliaria):
    def __init__(self, qtd_quartos: int, vaga_estacionar: int, qtd_banheiro: int, tamanho: float) -> None:
        super().__init__(qtd_quartos, vaga_estacionar, qtd_banheiro, tamanho)