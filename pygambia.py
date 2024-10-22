import pygame
import serial
import sys
#import json

# Configure a porta e a taxa de transmissão
porta = '/dev/ttyUSB0' # Altere para a porta correta
baud_rate = 9600

# Inicia a comunicação serial
ser = serial.Serial(porta, baud_rate)

# Inicializa o pygame
pygame.init()

# Configurações da tela
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Mover Retângulo')

# Configurações do retângulo
rect_width, rect_height = 60, 40
rect_x = width // 2 - rect_width // 2
rect_y = height // 2 - rect_height // 2
rect_color = (0, 128, 255)
rect_speed = 5

# Loop principal do jogo
running = True
while running:
    resposta=''
    # Lidar com eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Teclas pressionadas
    #keys = pygame.key.get_pressed()
    # Lê a resposta do Arduino
    if ser.in_waiting > 0:
        resposta = ser.readline().decode('utf-8').rstrip()
        #r = ser.read()
        print(resposta)
        #json.loads(resposta)
    if resposta=='A':
        rect_x += rect_speed
    if resposta=='B':
        rect_x -= rect_speed

    # Limitar o retângulo à tela
    if rect_x < 0:
        rect_x = 0
    elif rect_x > width - rect_width:
        rect_x = width - rect_width
    
    # Preencher a tela com cor de fundo
    screen.fill((0, 0, 0))
    
    # Desenhar o retângulo
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
    
    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de quadros
    pygame.time.Clock().tick(60)

# Sair do pygame
pygame.quit()
sys.exit()

vou fazer várias alterações bem legais!!! por que sim

renan um dia vai ter que trabalhar tbm!
ele está só na molezinha 
