from video import Video
from inscrito import Inscrito

class Youtube:
    def __init__(self) -> None:
        self.videos = []
        self.inscritos = []

    def adicionar_video(self, video: Video) -> None:
        self.videos.append(video)
        self.notificar_inscritos(video)

    def adicionar_inscrito(self, inscrito: Inscrito) -> None:
        self.inscritos.append(inscrito)

    def remover_inscrito(self, inscrito: Inscrito) -> None:
        self.inscritos.remove(inscrito)

    def notificar_inscritos(self, video: Video) -> None:
        for inscrito in self.inscritos:
            inscrito.receber_notificacao(video)
