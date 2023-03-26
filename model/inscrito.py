from video import Video
from youtube import Youtube


class Inscrito:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.minha_inscricoes = []

    def fazer_inscricao(self, canal: Youtube) -> None:
        canal.adicionar_inscrito(self)
        self.minha_inscricoes.append(canal)

    def silenciar_notificacao(self, canal: Youtube) -> None:
        canal.remover_inscrito(self)
        self.minha_inscricoes.remove(canal)

    def receber_notificacao(self, video: Video) -> None:
        print(f"O usuário {self.nome} recebeu a notificação do vídeo '{video.titulo}'")
