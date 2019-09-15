import pygame

r1 = pygame.Rect((10,10),(20,20))
r2 = pygame.Rect((50,50),(20,20))
r3 = pygame.Rect((0,0),(0,0))
r4 = pygame.Rect((50,70),(20,20))

pygame.init()
screen = pygame.display.set_mode((300,300))
clock = pygame.time.Clock()
pygame.display.set_caption("Overlap test")

running = True

while(running):

    for e in pygame.event.get():
        if(e.type == pygame.QUIT):
            running = False
        if(e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            running = False

    c = pygame.key.get_pressed()
    if(c[pygame.K_LEFT]):
        r1 = r1.move((-1,0))
    if(c[pygame.K_RIGHT]):
        r1 = r1.move((1,0))
    if(c[pygame.K_UP]):
        r1 = r1.move((0,-1))
    if(c[pygame.K_DOWN]):
        r1 = r1.move((0,1))

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0),r1)
    pygame.draw.rect(screen, (0,255,0),r2)
    pygame.draw.rect(screen, (0,0,255),r4)
    
    if(r1.colliderect(r2)):
        print("R1 Collided with R2, coordinates:\n\
                R1: "+str(r1.x) + " " + str(r1.y) + " " + str(r1.right) + " " + str(r1.bottom) + "\n\
                R2: "+str(r2.x) + " " + str(r2.y) + " " + str(r2.right) + " " + str(r2.bottom) + "\n")
        
        pos = (max(r1.x, r2.x),max(r1.y, r2.y))
        size = ((r1.right-r1.left)+(r2.right-r2.left) - (max(r2.right-r1.left,r1.right-r2.left)),
                (r1.bottom-r1.top)+(r2.bottom-r2.top) - (max(r2.bottom-r1.top,r1.bottom-r2.top)))
        r3.left, r3.top = pos
        r3.size = size
        pygame.draw.rect(screen, (255,255,0),r3)
        
    if(r1.colliderect(r4)):
        print("R1 Collided with R2, coordinates:\n\
                R1: "+str(r1.x) + " " + str(r1.y) + " " + str(r1.right) + " " + str(r1.bottom) + "\n\
                R4: "+str(r4.x) + " " + str(r4.y) + " " + str(r4.right) + " " + str(r4.bottom) + "\n")
        
        pos = (max(r1.x, r4.x),max(r1.y, r4.y))
        size = ((r1.right-r1.left)+(r4.right-r4.left) - (max(r4.right-r1.left,r1.right-r4.left)),
                (r1.bottom-r1.top)+(r4.bottom-r4.top) - (max(r4.bottom-r1.top,r1.bottom-r4.top)))
        r3.left, r3.top = pos
        r3.size = size
        pygame.draw.rect(screen, (255,0,255),r3)
    pygame.display.flip()
    clock.tick(10)
