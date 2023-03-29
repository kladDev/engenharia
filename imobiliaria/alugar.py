from promocao import Promocao


class Alugar:
    def __init__(self, aluguel: float, valor_energia: float, valor_agua: float, outras_despesas: float) -> None:
        self.aluguel = aluguel
        self.valor_energia = valor_energia
        self.valor_agua = valor_agua
        self.outras_despesas = outras_despesas

    def simular_financiamento():
        pass

    def desconto_aluguel(self, desconto: Promocao):
        self.valor_agua = desconto.gratuitidade_da_agua()
