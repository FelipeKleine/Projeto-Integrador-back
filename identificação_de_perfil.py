import uuid
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Perfil:
    def __init__(self, login, pwd, respostas):
        self.id = self.gerar_id()
        self.login = login
        self.pwd = pwd
        self.respostas = self.resposta()
       


    def gerar_id(self):
        global id_perfil
        return str(uuid.uuid4())
        
        
    def exibir_perfil(self):
        print(f"ID: {self.id}")
        print(f"login: {self.login}")
        print(f"pwd: {self.pwd}")
        print(f"Respostas: {self.respostas}")
        

    def resposta(self):
        respostas = {'R1': [], 'R2': [], 'R3': [], 'R4': [], 'R5': [], 'R6': [], 'R7': [], 'R8': [], 'R9': [], 'R10': [], 'R11': []}
            
        print(f'1] Por quanto tempo pretende deixar o dinheiro investido?\n')
        print(f'a) Menos de 6 meses\nb) Entre 6 meses e 1 ano\nc) Entre 1 ano e 3 anos\nd) Acima de 3 anos\n')
        r1 = int(input('a)1\nb)2\nc)3\nd)4\nResposta: \n'))
        respostas['R1'] = r1 
        
        
        
        print(f'2] Qual o objetivo desse investimento?\n')
        print(f'a) Preservação do capital para não perder valor ao longo do tempo,assumindo baixos riscos de perdas\nb) Aumento gradual do capital ao longo do tempo, assumindo riscosmoderados\nc) Aumento do capital acima da taxa de retorno média do mercado, mesmoque isso implique assumir riscos de perdas elevadas\nd) Obter no curto prazo retornos elevados e significativamente acima da taxade retorno média do mercado, assumindo riscos elevados\n')
        r2 = int(input('a)1\nb)2\nc)3\nd)4\nResposta: \n'))
        respostas['R2'] = r2 
        
        
        print(f'3] Qual das alternativas melhor classifica sua formação e experiencia com o mercado financeiro?\n')
        print(f'a) Não possuo formação acadêmica ou conhecimento do mercado financeiro\nb Possuo formação acadêmica na área financeira, mas não tenho experiênciacom o mercado financeiro\nc) Possuo formação acadêmica em outra área, mas possuo conhecimento domercado financeiro\nd) Possuo formação acadêmica na área financeira ou pleno conhecimento domercado financeiro\n')
        r3 = int(input('a)1\nb)2\nc)3\nd)4\nResposta: \n'))
        respostas['R3'] = r3 
        
        print(f'4] Considerando seus rendimentos regulares, qual é a porcentagem voce pretende reservar para aplicaçẽs financeiras?\n')
        print(f'a) No máximo 25%\nb) Entre 25,01 e 50%\nc) Acima de 50%\n')
        r4 = int(input('a)1\nb)2\nc)3\nResposta: \n'))
        respostas['R4'] = r4
        
        print(f'5] Caso as suas aplicações sofressem uma queda superior a 30%, oque voce faria?\n')
        print(f'a) Resgataria toda a aplicação e aplicaria na poupança\nb) Manteria aplicação aguardando uma melhora do mercado\nc) Aumentaria a aplicação para aproveitar as oportunidades do mercado\n')
        r5 = int(input('a)1\nb)2\nc)3\nResposta: \n'))
        respostas['R5'] = r5 
        
        print(f'6] Como esta distribuido seu patrimonio?\n')
        print(f'a) Meu patrimônio não está aplicado ou está todo aplicado em renda fixa e/ouimóveis\nb) Menos de 25% em renda variável e o restante em renda fixa e/ou imóveis\nc) Entre 25,01 e 50% aplicado em renda variável e o restante em renda fixae/ou imóveis\nd) Acima de 50% em renda variável\n')
        r6 = int(input('a)1\nb)2\nc)3\nd)4\nResposta: \n'))
        respostas['R6'] = r6
        
        print(f'7] Em relação as aplicações erendimentos, em qual dessas situações voce se enquadrada?\n')
        print(f'a) Conto com o rendimento dessas aplicações para complementar minharenda mensal\nb) Eventualmente posso resgatar parte das aplicações para fazer frente aosmeus gastos. Contudo, não tenho intenção de resgatar no curto prazo epretendo fazer aplicações regulares\nc) Não tenho intenção de resgatar no curto prazo e ainda pretendo fazeraplicações regulares\nd) Não tenho intenção de resgatar no curto prazo, mas não pretendo realizarnovas aplicações\n')
        r7 = int(input('a)1\nb)2\nc)3\nd)4\nResposta: \n'))
        respostas['R7'] = r7
        
        print(f'8] Qual sua faixa de renda mensal?\n')
        print(f'a) Até R$ 1.000\nb) De R$ 1.001 até R$ 5.000\nc) De R$ 5.001 até R$ 10.000\nd) Acima de R$ 10.000\n')
        r8 = int(input('a)1\nb)2\nc)3\nd)4\nResposta: \n'))
        respostas['R8'] = r8 
        
        print(f'9] Qual o valor aproximado do seu patrimonio?\n')
        print(f'a) Até R$ 10.000\nb) De R$ 10.001 até R$ 100.000\nc) De R$ 100.001 até R$ 500.000\nd)De R$ 500.001 até R$ 1.000.000\ne) Acima de R$ 1.000.001\n')
        r9 = int(input('a)1\nb)2\nc)3\nd)4\ne)5\nResposta: \n'))
        respostas['R9'] = r9
        
        Dez = [
        {'Tipos de Aplicações': 'Fundo de Renda Fixa / TítulosPúblicos / CDB / LCI / LCA / CRI /CRA / Debêntures / LC', 'Nunca investi': 0, '1 a 2 Vezes': 1, '3 Vezes ou mais': 1},
        {'Tipos de Aplicações': 'Mercado à vista em Bolsa deValores / Posições doadoras emempréstimo de ações (BTC) /Fundos Multimercado semAlavancagem / Clube deInvestimento / Fundo de Ações /Fundo Cambial / FIDC / FIP /Fundos de InvestimentoImobiliários (FII) / Ouro à vista / BDR','Nunca investi': 0, '1 a 2 Vezes': 2, '3 Vezes ou mais': 3},
        {'Tipos de Aplicações': 'Derivativos / Posições tomadoras em empréstimos de ações (BTC) /Fundo Multimercado com Alavancagem', 'Nunca investi': 0, '1 a 2 Vezes': 5, '3 Vezes ou mais': 6}
        ]
        print(f'10] Indique em quais aplicações listadas abaixo você já investiu e qual afrequência nos últimos dois anos. Pode assinalar mais do que uma alternativa.\n')
        tabela = pd.DataFrame(Dez)
        pd.set_option('display.max_colwidth', 200)
        display(tabela)
        print(f'Obs: Efetue a somatória dos pontos referente a questão acima e escolha a alternativa equivalente:')
        print(f'a)Entre 0 e 1 ponto\nb) Entre 2 e 4 pontos\nc) Acima de 5 pontos\n')
        r10 = int(input('a)1\nb)2\nc)3\nResposta: \n'))
        respostas['R10'] = r10
        
        
        onze = [
        {'Tipos de Aplicações': 'Fundo de Renda Fixa / TítulosPúblicos / CDB / LCI / LCA / CRI /CRA / Debêntures / LC', 'Nuca investi': 0, 'Menos de 10K': 1, 'Entre 10 e 50K':1 , 'Entre 51 e 100K': 1, 'Acima de 100K': 1},
        {'Tipos de Aplicações': 'Mercado à vista em Bolsa deValores / Posições doadoras emempréstimo de ações (BTC) /Fundos Multimercado semAlavancagem / Clube deInvestimento / Fundo de Ações /Fundo Cambial / FIDC / FIP /Fundos de InvestimentoImobiliários (FII) / Ouro à vista / BDR','Nuca investi': 0,'Menos de 10K': 2, 'Entre 10 e 50K':3 , 'Entre 51 e 100K': 4, 'Acima de 100K': 5},
        {'Tipos de Aplicações': 'Derivativos / Posições tomadoras em empréstimos de ações (BTC) /Fundo Multimercado com Alavancagem', 'Nuca investi': 0,'Menos de 10K': 7, 'Entre 10 e 50K': 8 , 'Entre 51 e 100K': 9, 'Acima de 100K': 10}
        ]
        
        print(f'11] Tomando por base as respostas da questão anterior, informar o volume aproximado que foi destinado a cada operação no período.')
        tabela2 = pd.DataFrame(onze)
        pd.set_option('display.max_colwidth', 200)
        display(tabela2)
        print(f'Obs: Efetue a somatória dos pontos referente a questão acima e escolha a alternativa equivalente:')
        print(f'a)Entre 0 e 1 ponto\nb) Entre 2 e 4 pontos\nc) Acima de 5 pontos\n')
        r11 = int(input('a)1\nb)2\nc)3\nResposta: \n'))
        respostas['R11'] = r11
        
        soma = sum(respostas.values())
        print(f'Voce somou {soma} pontos em suas respostas')
        
        igualdade = ''
        
        if soma <= 14:
            igualdade = 'Conservador'
        elif soma >15 or soma <= 35:
            igualdade = 'Moderado'
        else:
            igualdade = 'Arrojado'
        
        
        pontos = list(respostas.values())
        #variavel pontos é o acumulado para calculo de grafico
        classificacoes = [respostas.values()]
        pontuacao_cumulativa = np.cumsum(pontos)
        plt.plot(pontuacao_cumulativa, marker='o')
        
        plt.xlabel("Número de Respostas")
        plt.ylabel("Pontuação Cumulativa")
        plt.title("Progressão do Perfil de Risco")
        
        plt.axhline(14, color='red', linestyle='--', label='Conservador')
        plt.axhline(35, color='orange', linestyle='--', label='Moderado')
        plt.legend()
        
        pontuacao_final = pontuacao_cumulativa[-1]
        
        if pontuacao_final <= 14:
            perfil = "Conservador"
        elif pontuacao_final <= 35:
            perfil = "Moderado"
        else:
            perfil = "Arrojado"
        
        plt.text(len(respostas) - 1, pontuacao_final, f"Perfil: {perfil}", ha='right')
        
        plt.show()
        return perfil
    

def criar_perfil():
    login = input(f"Digite seu Login: ")
    pwd = input(f"Digite seu password: ")   
    perfil = Perfil(login, pwd, resposta)
    return perfil


perfis = []
while True:
    perfil = criar_perfil()
    perfis.append(perfil)

    continuar = str(input(f'Deseja continuar?(s/n)'))
    if continuar.lower() != 's':
        break

print('Perfil criado')
for perfil in perfis:
    perfil.exibir_perfil()
