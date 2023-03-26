from model.inscrito import Inscrito
from model.video import Video
from model.youtube import Youtube


v1 = Video('Fortnite', '12/01/2001')
v2 = Video('MCPE', '21/04/2001')
v3 = Video('Terraria', '01/04/2003')
v4 = Video('Free Fire', '04/01/2010')
v5 = Video('Honor of Kings', '12/01/2023')
v6 = Video('Clash of Clans', '01/12/2024')

juci = Youtube()
juci.adicionar_video(v4)
juci.adicionar_video(v3)

reis = Youtube()
reis.adicionar_video(v2)
reis.adicionar_video(v6)

claudio = Youtube()
claudio.adicionar_video(v1)
claudio.adicionar_video(v5)

fabricio = Inscrito('Fabricio')
fabricio.fazer_inscricao(juci)

igor = Inscrito('Igor')
igor.fazer_inscricao(reis)

kaio = Inscrito('Kaio')
kaio.fazer_inscricao(claudio)

claudio.notificar_inscritos()

v1 = Video('Fortnite', '12/01/2001')
v2 = Video('MCPE', '21/04/2001')
v3 = Video('Terraria', '01/04/2003')
v4 = Video('Free Fire', '04/01/2010')
v5 = Video('Honor of Kings', '12/01/2023')
v6 = Video('Clash of Clans', '01/12/2024')

juci = Youtube()
juci.adicionar_video(v4)
juci.adicionar_video(v3)

reis = Youtube()
reis.adicionar_video(v2)
reis.adicionar_video(v6)

claudio = Youtube()
claudio.adicionar_video(v1)
claudio.adicionar_video(v5)

fabricio = Inscrito('Fabricio')
fabricio.fazer_inscricao(juci)

igor = Inscrito('Igor')
igor.fazer_inscricao(reis)

kaio = Inscrito('Kaio')
kaio.fazer_inscricao(claudio)

claudio.notificar_inscritos()