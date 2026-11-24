import pygame

class Player():

    def __init__(self,position):
        self.width,self.height = 32,48
        x,y = 100, 480
        self.pos = pygame.Vector2(position)
        self.rect = pygame.Rect(position[0],position[1],self.width,self.height)

        self.speed = 180
        self.run_speed = 260

        self.acceleration = 1400
        self.friction = 1800

        self.velocity = pygame.Vector2(0, 0)

        self.gravity = 1100
        self.jump_force = 620
        self.max_fall_speed = 650

        self.grounded = False
        self.facing = 1

    def jump(self):
        if self.grounded:
            self.velocity.y = -self.jump_force
            self.grounded = False

    def move_towards(self, current, target, amount):
        if current < target:
            return min(current + amount, target)
        if current > target:
            return max(current - amount, target)
        return target

    def update(self, dt, keys, platforms):

        direction = (
            int(keys[pygame.K_d])-int(keys[pygame.K_a])
        )

        max_speed = (
            self.run_speed if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] else self.speed            
        )

        target_speed = direction * max_speed

        acceleration = self.acceleration 
        if not self.grounded:
            acceleration *= 0.7

        if direction:
            self.velocity.x = self.move_towards(
                self.velocity.x, 
                target_speed,
                acceleration * dt
            )
            self.facing = direction

        else:
            self.velocity.x = self.move_towards(
                self.velocity.x,
                0,
                self.friction * dt
            )

        self.pos.x += self.velocity.x * dt
        self.rect.x = round(self.pos.x)

        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.velocity.x > 0:
                    self.rect.right = platform.left
                elif self.velocity.x < 0:
                    self.rect.left = platform.right

                self.pos.x = self.rect.x
                self.velocity.x = 0

        self.velocity.y += self.gravity * dt
        self.velocity.y = min(self.velocity.y, self.max_fall_speed)

        self.pos.y += self.velocity.y * dt
        self.rect.y = round(self.pos.y)

        self.grounded = False

        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.velocity.y > 0:
                    self.rect.bottom = platform.top 
                    self.grounded = True
                elif self.velocity.y < 0:
                    self.rect.top = platform.bottom

                self.pos.y = self.rect.y
                self.velocity.y = 0

    def draw(self,surface):
        pygame.draw.rect(surface,'red',self.rect)

