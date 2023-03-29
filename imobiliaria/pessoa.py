class Pessoa:
    def __init__(self, nome: str, email: str, contato: str) -> None:
        self.nome = nome
        self.email = email
        self.contato = contato

    def enviar_mensagem(self):
        pass

class PessoaFisica(Pessoa):
    def __init__(self, nome: str, email: str, contato: str, cpf: str) -> None:
        super().__init__(nome, email, contato)
        self.cpf = cpf

class PessoaJuridica(Pessoa): 
    def __init__(self, nome: str, email: str, contato: str, cnpj: str) -> None:
        super().__init__(nome, email, contato)
        self.cnpj = cnpj