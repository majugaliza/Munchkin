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