import dama 

class Board :
    def __init__(self):    
        
        self.sair = False
        self.vencedor = None
        self.jogo = dama.Jogo()   
    def verificar_fim_de_jogo(self):
        return self.sair
    def vencedor (self):
        return self.vencedor
    # FUNÇÃO PARA IMPRIMIR A TELA DO VENCEDOR
    def tela_vencedor(self,vencedor):
        sair = False

        while not sair:
            for evento in dama.pygame.event.get():
                if evento.type == dama.pygame.QUIT:
                    sair = True
                    dama.pygame.quit()
                    quit()
                if evento.type == dama.pygame.KEYDOWN or evento.type == dama.pygame.MOUSEBUTTONDOWN:
                    sair = True

            self.jogo.display.fill(dama.PRETO)

            fonte = dama.pygame.font.SysFont('comicsansms', 50)

            surface_texto, rect_texto = None, None

            if vencedor == "empate":
                surface_texto, rect_texto = self.jogo.text_objects("EMPATE!", fonte, dama.BRANCO)
            elif vencedor == "x":
                surface_texto, rect_texto = self.jogo.text_objects("VITORIA DO  VERMELHO", fonte, dama.VERMELHO)
            elif vencedor == "o":
                surface_texto, rect_texto = self.jogo.text_objects("VITORIA DO BRANCO", fonte, dama.BRANCO)

            rect_texto.center = ((dama.LARGURA / 2), dama.ALTURA / 3)
            self.jogo.display.blit(surface_texto, rect_texto)

            fonte = dama.pygame.font.Font(None, 30)
            voltar = fonte.render('Pressione qualquer tecla para voltar ao menu.', False, dama.VERDE_CLARO)

            self.jogo.display.blit(voltar, (25, 550))

            dama.pygame.display.update()
            self.jogo.clock.tick(60)
    # SAIR DO JOGO
    def sair(self):
        dama.pygame.quit()
        quit()
    def obter_estado_do_jogo(self):
        return self.jogo.get_estado()
    def alterar_estado_do_jogo(self, estado):
        self.jogo.set_estado(estado)
    def trocar_jogador(self):
        self.jogo.proximo_turno()
    def turno (self):
        return self.jogo.turno
    
            
        
