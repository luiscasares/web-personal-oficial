import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Explorador de Cuerpos de Agua")

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 120, 255)
LIGHT_BLUE = (173, 216, 230)
BROWN = (139, 69, 19)
BLACK = (0, 0, 0)

# Fuentes
font = pygame.font.Font(None, 28)
title_font = pygame.font.Font(None, 40)

# Definición de cuerpos de agua
water_bodies = {
    "salada": [
        {"nombre": "Océano", "descripcion": "Cuerpo extenso de agua salada que cubre el 71% de la Tierra", "color": BLUE, "pos": (100, 150)},
        {"nombre": "Mar", "descripcion": "Cuerpo de agua salada más pequeño que un océano", "color": LIGHT_BLUE, "pos": (300, 200)},
        {"nombre": "Arrecife de Coral", "descripcion": "Estructura submarina formada por colonias de corales", "color": (255, 105, 180), "pos": (500, 250)}
    ],
    "dulce": [
        {"nombre": "Lago", "descripcion": "Cuerpo de agua dulce rodeado de tierra", "color": (0, 191, 255), "pos": (200, 400)},
        {"nombre": "Río", "descripcion": "Corriente natural de agua que fluye continuamente", "color": (65, 105, 225), "pos": (400, 350)},
        {"nombre": "Glaciar", "descripcion": "Masa de hielo que se desplaza lentamente", "color": (240, 248, 255), "pos": (600, 450)}
    ]
}

current_info = None

def draw_button(text, position, size):
    rect = pygame.Rect(position, size)
    pygame.draw.rect(screen, BROWN, rect)
    text_surf = font.render(text, True, WHITE)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)
    return rect

def draw_info(info):
    screen.fill(WHITE)
    # Dibujar cuadro de información
    info_rect = pygame.Rect(50, 50, 700, 500)
    pygame.draw.rect(screen, LIGHT_BLUE, info_rect)
    
    # Título
    title = title_font.render(info["nombre"], True, BLACK)
    screen.blit(title, (100, 80))
    
    # Descripción con wrap de texto
    description = info["descripcion"]
    words = description.split(' ')
    lines = []
    current_line = []
    max_width = 600
    
    for word in words:
        test_line = ' '.join(current_line + [word])
        width, _ = font.size(test_line)
        if width > max_width:
            lines.append(' '.join(current_line))
            current_line = [word]
        else:
            current_line.append(word)
    lines.append(' '.join(current_line))
    
    y = 150
    for line in lines:
        text_surf = font.render(line, True, BLACK)
        screen.blit(text_surf, (100, y))
        y += 30
    
    # Botón de regreso
    back_btn = draw_button("Volver al mapa", (600, 500), (150, 50))
    return back_btn

def main():
    global current_info
    running = True
    
    while running:
        screen.fill(WHITE)
        
        if current_info is None:
            # Dibujar título
            title = title_font.render("Explora los cuerpos de agua de la Tierra", True, BLACK)
            screen.blit(title, (100, 50))
            
            # Dibujar categorías
            pygame.draw.rect(screen, BROWN, (50, 100, 300, 40))
            screen.blit(font.render("Agua Salada", True, WHITE), (160, 110))
            
            pygame.draw.rect(screen, BROWN, (450, 100, 300, 40))
            screen.blit(font.render("Agua Dulce", True, WHITE), (560, 110))
            
            # Dibujar cuerpos de agua
            for category in water_bodies.values():
                for body in category:
                    pygame.draw.circle(screen, body["color"], body["pos"], 30)
                    text = font.render(body["nombre"], True, BLACK)
                    text_rect = text.get_rect(center=(body["pos"][0], body["pos"][1] + 40))
                    screen.blit(text, text_rect)
        else:
            back_btn = draw_info(current_info)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                
                if current_info is not None:
                    if back_btn.collidepoint(x, y):
                        current_info = None
                else:
                    # Verificar clic en cuerpos de agua
                    for category in water_bodies.values():
                        for body in category:
                            distance = ((x - body["pos"][0])**2 + (y - body["pos"][1])**2)**0.5
                            if distance < 30:
                                current_info = body

if __name__ == "__main__":
    main()