import pygame

class Player():

    def __init__(self,position):
        self.width,self.height = 32,48
        self.pos = pygame.Vector2(position)
        self.rect = pygame.Rect(position[0],position[1],self.width,self.height)

        self.speed = 180

        self.velocity = pygame.Vector2(0,0)

        self.gravity = 1100

        self.grounded = False
        self.facing = 1
        self.max_fall_speed = 1100
        self.jump_strength = 670
        self.collision_rect = self.rect.copy()

    def jump(self):
        if self.grounded:
            self.velocity.y = -self.jump_strength
            self.grounded = False

    def move(self,keys,dt):
        self.velocity.x = 0
        if keys[pygame.K_a]:
            self.rect.x -= self.speed * dt

        if keys[pygame.K_d]:
            self.rect.x += self.speed * dt 

    def collision(self,platforms):
        for platform in platforms:
 
            if self.collision_rect.colliderect(platform):
                if self.velocity.y > 0:
                    self.rect.bottom = platform.top 
                    self.grounded = True
                elif self.velocity.y < 0:
                    self.rect.top = platform.bottom
                    self.collision_rect = self.rect.x + 1

                self.pos.y = self.rect.y
                self.velocity.y = 0

        for platform in platforms:
            if self.collision_rect.colliderect(platform):
                if self.velocity.x > 0:
                    self.rect.right = platform.left 
                elif self.velocity.x < 0:
                    self.rect.left = platform.right

                self.velocity.x = 0
                self.pos.x = self.rect.x

    def update(self, dt):

        # for platform in platforms:
        #     if self.rect.colliderect(platform):
        #         if self.velocity.x > 0:
        #             self.rect.right = platform.left
        #         elif self.velocity.x < 0:
        #             self.rect.left = platform.right

        #         self.pos.x = self.rect.x
        #         self.velocity.x = 0

        self.velocity.y += self.gravity * dt
        self.velocity.y = min(self.velocity.y, self.max_fall_speed)

        self.pos.y += self.velocity.y * dt
        self.rect.y = round(self.pos.y)

        self.grounded = False

        

    def draw(self,surface):
        pygame.draw.rect(surface,'red',self.rect)

