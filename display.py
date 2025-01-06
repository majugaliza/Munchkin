import pygame
import sys
import math

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (243, 231, 219)
BORDER_COLOR = (98, 61, 27)
BORDER_WIDTH = 20
BORDER_MARGIN = 20
BOTTOM_MARGIN = 50

font = pygame.font.SysFont("timesnewroman", 30)

CARDS_PER_ROW = 5
MARGIN = 10
SCROLL_BAR_MARGIN = 20
CARD_WIDTH = (screen_width - (CARDS_PER_ROW + 1) * MARGIN - SCROLL_BAR_MARGIN - 2 * BORDER_MARGIN) // CARDS_PER_ROW
CARD_HEIGHT = 220

spritesheet_portas = pygame.image.load("assets/door1.jpg")
spritesheet_tesouro = pygame.image.load("assets/treasure1.jpeg")

total_cards_door = 70
total_cards_treasure = 70
num_columns_in_spritesheet = 10
num_rows_in_spritesheet = 7

num_rows_for_display_door = math.ceil(total_cards_door / CARDS_PER_ROW)
num_rows_for_display_treasure = math.ceil(total_cards_treasure / CARDS_PER_ROW)

scroll_offset = 0

scroll_bar_width = 15
scroll_bar_height = screen_height - 2 * BORDER_MARGIN
scroll_bar_x = screen_width - scroll_bar_width - BORDER_MARGIN
scroll_bar_y = BORDER_MARGIN

total_cards_height = (num_rows_for_display_door + num_rows_for_display_treasure) * (CARD_HEIGHT + MARGIN) - MARGIN + BOTTOM_MARGIN
scroll_handle_height = max(50, (scroll_bar_height / total_cards_height) * scroll_bar_height)
scroll_handle_y = scroll_bar_y

scaled_cards_door = []
scaled_cards_treasure = []

def load_scaled_cards():
    # Load Door Deck
    for i in range(total_cards_door):
        card_col_in_spritesheet = i % num_columns_in_spritesheet
        card_row_in_spritesheet = i // num_columns_in_spritesheet
        card_rect = pygame.Rect(card_col_in_spritesheet * 378, card_row_in_spritesheet * 585, 378, 585)
        card_image = spritesheet_portas.subsurface(card_rect)
        
        scaled_card = pygame.transform.smoothscale(card_image, (CARD_WIDTH, CARD_HEIGHT))
        scaled_cards_door.append(scaled_card)

    # Load Treasure Deck
    for i in range(total_cards_treasure):
        card_col_in_spritesheet = i % num_columns_in_spritesheet
        card_row_in_spritesheet = i // num_columns_in_spritesheet
        card_rect = pygame.Rect(card_col_in_spritesheet * 244, card_row_in_spritesheet * 351, 244, 351)
        card_image = spritesheet_tesouro.subsurface(card_rect)
        
        scaled_card = pygame.transform.smoothscale(card_image, (CARD_WIDTH, CARD_HEIGHT))
        scaled_cards_treasure.append(scaled_card)

def display_card_details(screen, card_image, description):
    detail_width = 250
    detail_height = 400
    detail_surface = pygame.Surface((detail_width, detail_height))
    detail_surface.fill(WHITE)
    
    pygame.draw.rect(detail_surface, BORDER_COLOR, (0, 0, detail_width, 5))
    pygame.draw.rect(detail_surface, BORDER_COLOR, (0, detail_height - 5, detail_width, 5))
    pygame.draw.rect(detail_surface, BORDER_COLOR, (0, 0, 5, detail_height))
    pygame.draw.rect(detail_surface, BORDER_COLOR, (detail_width - 5, 0, 5, detail_height))
    
    card_image_aspect_ratio = card_image.get_width() / card_image.get_height()
    if card_image_aspect_ratio > (detail_width - 60) / (detail_height - 170):
        scaled_width = detail_width - 60
        scaled_height = int(scaled_width / card_image_aspect_ratio)
    else:
        scaled_height = detail_height - 170
        scaled_width = int(scaled_height * card_image_aspect_ratio)
    
    scaled_card = pygame.transform.smoothscale(card_image, (scaled_width, scaled_height))
    detail_surface.blit(scaled_card, ((detail_width - scaled_width) // 2, 20))
    
    description_text = font.render(description, True, (0, 0, 0))
    detail_surface.blit(description_text, (20, detail_height - 100))
    
    screen.blit(detail_surface, ((screen_width - detail_width) // 2, (screen_height - detail_height) // 2))
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

def display_cards():
    global scroll_offset, scroll_handle_y
    
    dragging = False
    
    while True:
        screen.fill(BACKGROUND_COLOR)

        # Borders
        if scroll_offset == 0:
            pygame.draw.rect(screen, BORDER_COLOR, (0, 0, screen_width, BORDER_WIDTH))
        if scroll_offset >= total_cards_height - screen_height + 300:
            pygame.draw.rect(screen, BORDER_COLOR, (0, screen_height - BORDER_WIDTH, screen_width, BORDER_WIDTH))
        pygame.draw.rect(screen, BORDER_COLOR, (0, 0, BORDER_WIDTH, screen_height))
        pygame.draw.rect(screen, BORDER_COLOR, (screen_width - BORDER_WIDTH, 0, BORDER_WIDTH, screen_height))
        # Render Door Title
        if scroll_offset == 0:
            title_text = font.render("BARALHO DA PORTA", True, (0, 0, 0))
            title_rect = title_text.get_rect(center=(screen_width // 2, BORDER_MARGIN + 30))
            screen.blit(title_text, title_rect)

        # Loop through all the cards from Door Deck
        for i in range(total_cards_door):
            col = i % CARDS_PER_ROW
            row = i // CARDS_PER_ROW
            
            x = BORDER_MARGIN + MARGIN + col * (CARD_WIDTH + MARGIN)
            y = BORDER_MARGIN + 100 + row * (CARD_HEIGHT + MARGIN) - scroll_offset
            
            screen.blit(scaled_cards_door[i], (x, y))

        # Render Treasure title
        tesouro_title_y = BORDER_MARGIN + 200 + num_rows_for_display_door * (CARD_HEIGHT + MARGIN) - scroll_offset
        if tesouro_title_y < screen_height:
            title_text = font.render("BARALHO DO TESOURO", True, (0, 0, 0))
            title_rect = title_text.get_rect(center=(screen_width // 2, tesouro_title_y + 30))
            screen.blit(title_text, title_rect)

        # Loop through all the cards from Treasure Deck
        for i in range(total_cards_treasure):
            col = i % CARDS_PER_ROW
            row = i // CARDS_PER_ROW
            
            x = BORDER_MARGIN + MARGIN + col * (CARD_WIDTH + MARGIN)
            y = BORDER_MARGIN + 300 + (num_rows_for_display_door * (CARD_HEIGHT + MARGIN)) + row * (CARD_HEIGHT + MARGIN) - scroll_offset
            
            screen.blit(scaled_cards_treasure[i], (x, y))
        
        pygame.draw.rect(screen, (200, 200, 200), (scroll_bar_x, scroll_bar_y, scroll_bar_width, scroll_bar_height))
        pygame.draw.rect(screen, (100, 100, 100), (scroll_bar_x, scroll_handle_y, scroll_bar_width, scroll_handle_height))
        
        # "Voltar" button
        button_width = 100
        button_height = 50
        button_x = (screen_width - button_width) // 2
        button_y = screen_height - button_height - 10
        pygame.draw.rect(screen, (181, 101, 29), (button_x, button_y, button_width, button_height))
        button_text = font.render("Voltar", True, (255, 255, 255))
        button_text_rect = button_text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
        screen.blit(button_text, button_text_rect)
        
        # Events
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if pygame.Rect(scroll_bar_x, scroll_handle_y, scroll_bar_width, scroll_handle_height).collidepoint(evento.pos):
                        dragging = True
                    elif pygame.Rect(button_x, button_y, button_width, button_height).collidepoint(evento.pos):
                        return
                    else:
                        for i in range(total_cards_door):
                            col = i % CARDS_PER_ROW
                            row = i // CARDS_PER_ROW
                            x = BORDER_MARGIN + MARGIN + col * (CARD_WIDTH + MARGIN)
                            y = BORDER_MARGIN + 100 + row * (CARD_HEIGHT + MARGIN) - scroll_offset
                            if pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT).collidepoint(evento.pos):
                                display_card_details(screen, scaled_cards_door[i], "Descrição")
                                break
                        for i in range(total_cards_treasure):
                            col = i % CARDS_PER_ROW
                            row = i // CARDS_PER_ROW
                            x = BORDER_MARGIN + MARGIN + col * (CARD_WIDTH + MARGIN)
                            y = BORDER_MARGIN + 300 + (num_rows_for_display_door * (CARD_HEIGHT + MARGIN)) + row * (CARD_HEIGHT + MARGIN) - scroll_offset
                            if pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT).collidepoint(evento.pos):
                                display_card_details(screen, scaled_cards_treasure[i], "Descrição")
                                break

            if evento.type == pygame.MOUSEBUTTONUP:
                if evento.button == 1:
                    dragging = False

            if evento.type == pygame.MOUSEMOTION:
                if dragging:
                    mouse_y = evento.pos[1]
                    scroll_handle_y = max(scroll_bar_y, min(mouse_y - scroll_handle_height // 2, scroll_bar_y + scroll_bar_height - scroll_handle_height))
                    scroll_offset = max(0, min((scroll_handle_y - scroll_bar_y) * total_cards_height // (scroll_bar_height - scroll_handle_height), total_cards_height - screen_height + 300))
        
        pygame.display.flip()
        pygame.time.Clock().tick(60)

load_scaled_cards()
