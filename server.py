from network import Rede
from board import Board
import dama
class Server:
    def __init__(self, host, porta):
        dama.pygame.display.set_caption('Jogo de Damas')
        dama.pygame.font.init()
        # Configurações do servidor
        self.host = host
        self.port = porta
        self.jogo = Board()
        self.rede = Rede(self.host, self.port)
        # Se for o servidor, cria e aguarda uma conexão
        self.rede.criar_servidor()
        self.rede.aceitar_conexao()
        self.iniciar_jogo()
    
    def iniciar_jogo(self):
        
        while not self.jogo.verificar_fim_de_jogo():
            for evento in dama.pygame.event.get():
                #se for a vez do servidor
                if self.jogo.turno() == 1:
                    if evento.type == dama.pygame.QUIT:
                        self.sair = True
                        dama.pygame.quit()
                        quit()
                    if evento.type == dama.pygame.MOUSEBUTTONDOWN :
                        self.jogo.jogo.avalia_clique(dama.pygame.mouse.get_pos())
                    self.rede.enviar_mensagem(self.jogo.obter_estado_do_jogo())
                else: 
                # Recebe o estado atual do jogo para os clientes
                    self.jogo.alterar_estado_do_jogo(self.rede.receber_mensagens())

            vencedor = self.jogo.jogo.verifica_vencedor()

            if vencedor is not None:
                self.jogo.sair = True
                self.jogo.tela_vencedor(vencedor) 
                   
            self.jogo.jogo.display.fill(dama.PRETO)
            self.jogo.jogo.desenha()
            dama.pygame.display.update()
            self.jogo.jogo.clock.tick(50)
            
        
        mensagem_fim_jogo = "Fim de jogo! Vencedor: " + self.jogo.vencedor()
        self.rede.enviar_mensagem(mensagem_fim_jogo)
        # Fecha a conexão ao final do programa
        self.rede.fechar_conexao()
             
if __name__ == "__main__":
    servidor = Server('127.0.0.1', 8000)