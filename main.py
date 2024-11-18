import pygame

pygame.font.init()

background_colour = (255, 255, 255)
(width, height) = (1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hifi Chat')

bg = pygame.image.load("BG.png")

running = True
texty = "Enter Message: "
font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', 32)
text = font.render(texty, True, (255, 255, 255))
textRect = text.get_rect()
textRect.center = (text.get_width()/2+20, 50)
texting = []
bigger = 0
while running:

    screen.fill(background_colour)
    screen.blit(bg, (0, 0))
    screen.blit(text, textRect)
    for txt in texting:
        message = font.render(txt, True, (255, 255, 255))
        messageRect = message.get_rect()
        messageRect.center = (width//2, bigger+100)
        screen.blit(message, messageRect)
        bigger += 40
    bigger = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print("key: "+str(event.unicode)+", unicode: "+str(event.key))
            if event.key == 8:
                texty = texty[0:-1]
            elif event.key == 13:
                texting.append(str(texty[15:]))
                texty = texty[:15]
            else:
                texty += event.unicode
            text = font.render(texty, True, (255, 255, 255))

    pygame.display.flip()

