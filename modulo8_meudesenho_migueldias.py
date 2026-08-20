'''
hora de aventura - finn
gumball - gumball
ben 10 - benjmim tennyson
'''

class meninoheroirelogio: 

    def __init__(self,nome,dono,frase_de_efeito):
        self.nome = nome
        self.dono = dono
        self.frase_de_efeito = frase_de_efeito

ben10 = meninoheroirelogio(

    nome = "Benjamim Tennyson",
    dono = "Vô Max",
    frase_de_efeito = "hora de virar heroi"
)

gwentennyson = meninoheroirelogio(
    nome = "Gwen tennyson",
    dono = "Vô Max",
    frase_de_efeito = "Pronto pra desistir?"
)

VôMax = meninoheroirelogio(
    nome = "Max Tennyson", 
    dono = "???",
    frase_de_efeito = "Eu sou apenas um encanador"

)

KevinLevin = meninoheroirelogio(
    nome = "Kevin Levin",
    dono = "Gwen",
    frase_de_efeito = "Você nunca vai me vencer, porque você é o mocinho. E mocinhos nunca têm coragem de acabar com as pessoas feito eu!"

)


print(f'Nome: {ben10.nome} | {ben10.dono} | {ben10.frase_de_efeito}')
print(f'Nome: {VôMax.nome} | {VôMax.dono} | {VôMax.frase_de_efeito}')