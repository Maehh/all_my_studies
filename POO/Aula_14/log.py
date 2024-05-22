# Abstrção
# Log

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'
class Log:
    def _log(self, msg):         # Assinatura do método
        raise NotImplementedError('Implemente um método log')           
    # Este erro define que o método não poderá ser utilizado diretamente
    # Portanto, necessário definir o método obrigatoriamente na classe que for herda-lo

    def logerror(self, msg):
        return self._log(f'Error: {msg}')
    
    def logsucess(self, msg):
        return self._log(f'Sucess: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} {self.__class__.__name__}'
        print(f'Salvando... : {msg_formatada}')
        with open(LOG_FILE, 'a') as arquivo: 
            arquivo.write(msg_formatada)
            arquivo.write('\n')
        

class LogPrintMixin(Log):
    ...
    def _log(self, msg):                                              # <- Caso Não seja Herdado: raise NotImplementedError('Implemente um método log')
        print(f'{msg} {self.__class__.__name__}')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.logerror('qualquer coisa')
    lp.logsucess('Sucesso')
    lf = LogFileMixin()
    lf.logerror('Teste Erro')
    lf.logsucess('Teste Sucesso')

    # print(LOG_FILE)