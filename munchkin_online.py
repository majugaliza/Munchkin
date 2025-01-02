import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Configurações básicas
tela_largura, tela_altura = 800, 600
fps = 60
fonte = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Munchkin Online")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 200, 0)
VERMELHO = (200, 0, 0)
AZUL = (0, 0, 200)

# Botão genérico
def desenhar_botao(texto, x, y, largura, altura, cor_fundo, cor_texto):
    pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura))
    texto_render = fonte.render(texto, True, cor_texto)
    texto_rect = texto_render.get_rect(center=(x + largura // 2, y + altura // 2))
    tela.blit(texto_render, texto_rect)
    return pygame.Rect(x, y, largura, altura)

# Tela inicial
def tela_inicial():
    while True:
        tela.fill(BRANCO)

        # Desenhar botões
        titulo = fonte.render("Munchkin Online", True, PRETO)
        tela.blit(titulo, (tela_largura // 2 - titulo.get_width() // 2, 100))
        
        botao_criar_partida = desenhar_botao("Criar Partida", 300, 250, 200, 50, VERDE, BRANCO)
        botao_ver_cartas = desenhar_botao("Ver Cartas", 300, 320, 200, 50, AZUL, BRANCO)
        botao_multiplayer = desenhar_botao("Multiplayer", 300, 390, 200, 50, VERMELHO, BRANCO)
        botao_sair = desenhar_botao("Sair", 300, 460, 200, 50, VERMELHO, BRANCO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_criar_partida.collidepoint(evento.pos):
                    tela_criar_partida()
                elif botao_ver_cartas.collidepoint(evento.pos):
                    tela_ver_cartas()
                elif botao_multiplayer.collidepoint(evento.pos):
                    tela_multiplayer()
                elif botao_sair.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(fps)

# Tela de criar partida
def tela_criar_partida():
    while True:
        tela.fill(BRANCO)

        titulo = fonte.render("Criar Partida", True, PRETO)
        tela.blit(titulo, (tela_largura // 2 - titulo.get_width() // 2, 100))

        botao_iniciar = desenhar_botao("Iniciar Partida", 300, 250, 200, 50, VERDE, BRANCO)
        botao_voltar = desenhar_botao("Voltar", 300, 320, 200, 50, VERMELHO, BRANCO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_iniciar.collidepoint(evento.pos):
                    tela_jogo()
                elif botao_voltar.collidepoint(evento.pos):
                    return

        pygame.display.flip()
        clock.tick(fps)

# Tela de ver cartas
def tela_ver_cartas():
    while True:
        tela.fill(BRANCO)

        titulo = fonte.render("Suas Cartas", True, PRETO)
        tela.blit(titulo, (tela_largura // 2 - titulo.get_width() // 2, 100))

        cartas = ["Carta 1", "Carta 2", "Carta 3", "Carta 4"]  # Exemplo de cartas
        for i, carta in enumerate(cartas):
            carta_texto = fonte.render(carta, True, PRETO)
            tela.blit(carta_texto, (50, 150 + i * 40))

        botao_voltar = desenhar_botao("Voltar", 300, 500, 200, 50, VERMELHO, BRANCO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_voltar.collidepoint(evento.pos):
                    return

        pygame.display.flip()
        clock.tick(fps)

# Tela de multiplayer (lobby)
def tela_multiplayer():
    while True:
        tela.fill(BRANCO)

        titulo = fonte.render("Lobby Multiplayer", True, PRETO)
        tela.blit(titulo, (tela_largura // 2 - titulo.get_width() // 2, 100))

        info = fonte.render("Convide outros jogadores para jogar.", True, PRETO)
        tela.blit(info, (50, 150))

        botao_voltar = desenhar_botao("Voltar", 300, 500, 200, 50, VERMELHO, BRANCO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_voltar.collidepoint(evento.pos):
                    return

        pygame.display.flip()
        clock.tick(fps)

# Tela do jogo principal
def tela_jogo():
    nivel_jogador = 1

    while True:
        tela.fill(BRANCO)

        # Mostrar informações do jogador
        nivel_texto = fonte.render(f"Nível: {nivel_jogador}", True, PRETO)
        tela.blit(nivel_texto, (50, 50))

        # Botões de ação
        botao_abrir_porta = desenhar_botao("Abrir Porta", 300, 250, 200, 50, VERDE, BRANCO)
        botao_voltar = desenhar_botao("Voltar", 300, 320, 200, 50, VERMELHO, BRANCO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_abrir_porta.collidepoint(evento.pos):
                    nivel_jogador += 1  # Simular ganhar nível ao abrir uma porta
                elif botao_voltar.collidepoint(evento.pos):
                    return

        pygame.display.flip()
        clock.tick(fps)

# Iniciar o jogo
tela_inicial()
