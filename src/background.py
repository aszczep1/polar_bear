import pygame

class Tree(pygame.sprite.Sprite):
     
     def __init__(self, x=0, y=0, width = 100, height = 100,  img_file = "./../assets/tree.png"):
        '''
        Initializes tree object 
        '''
        super().__init__()
        self.image = pygame.image.load(img_file) 
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = x, y
      
     def update(self): 
         '''
         '''
         self.rect.y += 1

