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
        with open(LOG_FILE, 'w') as arquivo: 
            arquivo.write(msg_formatada)
            arquivo.write('\n')
        print(msg)

class LogPrintMixin(Log):
    ...
    def _log(self, msg):                                              # <- Caso Não seja Herdado: raise NotImplementedError('Implemente um método log')
        print(f'{msg} {self.__class__.__name__}')

if __name__ == '__main__':
    l = LogPrintMixin()
    l.logerror('qualquer coisa')
    l.logsucess('Sucesso')
    lf = LogFileMixin()
    l._log('Teste')
    # print(LOG_FILE)