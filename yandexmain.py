import pygame


pygame.init()
size = 1000, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Чёрное в белое и наоборот')
clock = pygame.time.Clock()


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[1] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 3

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color('green'), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size, self.cell_size),
                                 self.board[y][x])
        for y in range(self.height):
            for x in range(self.width):
                if y >= 1:
                    if x >= 1:
                        if self.board[y][x] != self.board[y - 1][x]:
                            if self.board[y][x] != self.board[y][x - 1]:
                                if self.board[y][x] != self.board[y + 1][x]:
                                    if self.board[y][x] != self.board[y][x + 1]:
                                        self.board[y][x] = (self.board[y][x] + 1) % 2
                    else:
                        if self.board[y][x] != self.board[y - 1][x]:
                            if self.board[y][x] != self.board[y][x + 1]:
                                if self.board[y][x] != self.board[y + 1][x]:
                                    self.board[y][x] = (self.board[y][x] + 1) % 2
                else:
                    if x >= 1:
                        if self.board[y][x] != self.board[y + 1][x]:
                            if self.board[y][x] != self.board[y][x + 1]:
                                if self.board[y][x] != self.board[y][x - 1]:
                                    self.board[y][x] = (self.board[y][x] + 1) % 2
                    else:
                        if self.board[y][x] != self.board[y + 1][x]:
                            if self.board[y][x] != self.board[y][x + 1]:
                                self.board[y][x] = (self.board[y][x] + 1) % 2


    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def on_click_change_cell_color(self, cell_coords):
        self.board[cell_coords[0]][cell_coords[1]] = (self.board[cell_coords[0]][cell_coords[1]] + 1) % 2

    def get_cell(self, mouse_pos):
        if self.left <= mouse_pos[1] < self.left + self.height * self.cell_size and self.top <= mouse_pos[
            0] < self.top + self.width * self.cell_size:
            return (int((mouse_pos[1] - self.left) / self.cell_size), int((mouse_pos[0] - self.top) / self.cell_size))
        else:
            return None

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell != None:
            self.on_click_change_cell_color(cell)


board = Board(10, 8)
board.set_view(10, 10, 40)
fps = 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()