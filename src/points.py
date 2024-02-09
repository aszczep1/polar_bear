import pygame
from bear import Bear


class Points(pygame.sprite.Sprite): 
    def __init__(self, x = 0 , y = 0, width = 175, height = 175,  img_file = "./../assets/coke.png"):
         '''
         Initalizes the bear object
         args: 
         '''
         super().__init__()
         self.img = img_file
         self.image = pygame.image.load(img_file) 
         self.image = pygame.transform.scale(self.image, (width, height))
         self.rect = self.image.get_rect()

         self.rect.x, self.rect.y = x, y
    
    def update(self):
         '''
         '''
         self.rect.y += 5
        
        