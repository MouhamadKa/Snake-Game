import random

class Food:
    def __init__(self, block_size, width, height , snake_body):
        self.block_size = block_size
        self.width = width
        self.height = height 
        self.position = self.create(snake_body)
        
    def create(self, snake_body):
        while True:
            x = random.randint(0, (self.width - self.block_size) // self.block_size) * self.block_size
            y = random.randint(0, (self.height - self.block_size) // self.block_size) * self.block_size
            if (x, y) not in snake_body:
                return (x, y)