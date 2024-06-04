# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (ACADEMICAMENTE o retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (Overload) - Python não possui
# Sobreposição de métodos (Overload) - Python possui

from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, msg) -> None:
        self.msg = msg

    @abstractmethod
    def enviar_notif(self) -> bool:         # Type annotations - TIPAGEM DO MÈTODO
        ...


# notif = Notificacao('Teste')


class Notif_email(Notificacao):
    def enviar_notif(self, email):
        print(f'Email: {email} Enviando: {self.msg}')
        return True
    
class Notif_sms(Notificacao):
    def enviar_notif(self, numero):
        print(f'Numero: {numero} Enviando: {self.msg}')
        return True



def notificar(notificacao: Notificacao):                # 1. Notificacao => Tipo | DO TIPO QUE SERÁ INTRODUZIDO AO CHAMAR FUNÇÃO
    notificacao_enviada = notificacao.enviar_notif('gg@gmail.com')    # 2. metodo enviar_notivo => Retorna Bool
                                                                        # POLIMORFISMO = HERDA E MODIFICA O OBJETO SEM DEIXAR DE FUNCIONAR 
    if notificacao_enviada:
        print('Notificação enviada com sucesso')
    else :
        print('Erro Notificação não enviada')




# notif = Notif_email('Teste')
# notif2 = Notif_sms('Teste',)

# notif.enviar_notif('gggg@gmail.com')
# notif2.enviar_notif('00000000000')


notificar(Notif_email('Teste da função.'))                  # CHAMADO FUNÇÃO COM O MÉTODO DO TIPO NOTIFICACAO



'''
MEU RESUMO

1. É criado uma classe abstrata com o nome "Notificacao" e com o método abstrado "enviar_notif" que retorna um booleano (-> bool)
2. É criado logo em seguida duas classes que herdam a super classe Notificacao (Notif_Email e Notif_sms), ambas com o método enviar_notif,
já que é obrigatório (@abstractmethod)
3. É criado uma função chamada notificar, com um parâmetro notificacao, este parâmetro aceita apenas o tipo "Notificacao" (Tipo de classe criada no passo 1)
4. Nesta função, uma variável chamada notificacao_enviada recebe o parametro notificacao.enviar_notif() => que é o método que retorna boleano
5. Com isso, a função será chamada com uma classe do tipo Notificacao (Notif_email ou Notif_sms), e logo depois será chamado o método-
enviar_notif e retornará True caso realizada com sucesso ou False para o contrário
6. A função retornará se a operção foi feita ou não com base nestes dados.


'''