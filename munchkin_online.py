import random
import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Configurações básicas
tela_largura, tela_altura = 800, 600
fps = 60
fonte = pygame.font.Font(None, 36)
fonte_titulo = pygame.font.Font(None, 72)
clock = pygame.time.Clock()
tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption("Munchkin Online")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 200, 0)
VERMELHO = (200, 0, 0)
MARROM_CLARO = (181, 101, 29)
MARROM_ESCURO = (120, 72, 24)
AMARELO = (238, 173, 45)

# Dados do perfil do jogador
foto_perfil = pygame.Surface((100, 100))
foto_perfil.fill((150, 150, 150))  # Placeholder para foto de perfil
id_usuario = random.randint(1000, 9999)
nome_usuario = "Jogador"

# Botão genérico
def desenhar_botao(texto, x, y, largura, altura, cor_fundo, cor_texto):
    pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura), border_radius=10)
    texto_render = fonte.render(texto, True, cor_texto)
    texto_rect = texto_render.get_rect(center=(x + largura // 2, y + altura // 2))
    tela.blit(texto_render, texto_rect)
    return pygame.Rect(x, y, largura, altura)

# Tela inicial
def tela_inicial():
    while True:
        tela.fill(MARROM_ESCURO)

        # Desenhar título e logotipo
        pygame.draw.rect(tela, MARROM_CLARO, (200, 80, 400, 100), border_radius=10)
        titulo = fonte_titulo.render("Munchkin", True, BRANCO)
        titulo_rect = titulo.get_rect(center=(tela_largura // 2, 130))
        tela.blit(titulo, titulo_rect)

        # Botões
        botao_jogar = desenhar_botao("Jogar", 300, 240, 200, 50, MARROM_CLARO, BRANCO)
        botao_ver_cartas = desenhar_botao("Ver Cartas", 300, 310, 200, 50, MARROM_CLARO, BRANCO)
        botao_entrar_sala = desenhar_botao("Entrar em Sala", 300, 380, 200, 50, MARROM_CLARO, BRANCO)
        botao_criar_sala = desenhar_botao("Criar Sala", 300, 450, 200, 50, MARROM_CLARO, BRANCO)

        # Ícones
        icone_config = pygame.draw.circle(tela, BRANCO, (750, 550), 20)
        icone_perfil = pygame.draw.circle(tela, BRANCO, (50, 550), 20)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar.collidepoint(evento.pos):
                    tela_criar_partida()
                elif botao_ver_cartas.collidepoint(evento.pos):
                    tela_ver_cartas()
                elif botao_entrar_sala.collidepoint(evento.pos):
                    tela_multiplayer()
                elif botao_criar_sala.collidepoint(evento.pos):
                    tela_criar_partida()
                elif icone_perfil.collidepoint(evento.pos):
                    tela_perfil()

        pygame.display.flip()
        clock.tick(fps)

# Tela de perfil
def tela_perfil():
    global nome_usuario, foto_perfil
    entrada_ativa = False
    texto_digitado = nome_usuario

    while True:
        tela.fill(MARROM_CLARO)

        titulo = fonte.render("Perfil do Jogador", True, PRETO)
        tela.blit(titulo, (tela_largura // 2 - titulo.get_width() // 2, 50))

        # Exibir foto do perfil
        tela.blit(foto_perfil, (350, 120))
        botao_trocar_foto = desenhar_botao("Trocar Foto", 300, 250, 200, 50, MARROM_ESCURO, BRANCO)

        # Exibir nome do usuário
        texto_nome = fonte.render("Nome:", True, PRETO)
        tela.blit(texto_nome, (200, 350))
        entrada_nome = pygame.Rect(300, 340, 300, 40)
        pygame.draw.rect(tela, AMARELO if entrada_ativa else MARROM_ESCURO, entrada_nome, border_radius=5)
        texto_nome_render = fonte.render(texto_digitado, True, BRANCO)
        tela.blit(texto_nome_render, (entrada_nome.x + 10, entrada_nome.y + 5))

        # Exibir ID do usuário
        texto_id = fonte.render(f"ID: {id_usuario}", True, PRETO)
        tela.blit(texto_id, (200, 400))

        botao_voltar = desenhar_botao("Voltar", 300, 500, 200, 50, VERMELHO, BRANCO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_trocar_foto.collidepoint(evento.pos):
                    foto_perfil.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                elif entrada_nome.collidepoint(evento.pos):
                    entrada_ativa = True
                else:
                    entrada_ativa = False
                if botao_voltar.collidepoint(evento.pos):
                    return 
            if evento.type == pygame.KEYDOWN and entrada_ativa:
                if evento.key == pygame.K_BACKSPACE:
                    texto_digitado = texto_digitado[:-1]
                else:
                    texto_digitado += evento.unicode

        nome_usuario = texto_digitado

        pygame.display.flip()
        clock.tick(fps)

# Tela de ver cartas
def tela_ver_cartas():
    while True:
        tela.fill(BRANCO)

        titulo = fonte.render("Cartas", True, PRETO)
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
