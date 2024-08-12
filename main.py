import pygame

pygame.init()

# Constants
WIDTH, HEIGHT = 700, 700
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)

TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE

FPS = 60

# Setting up the pygame window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

CLOCK = pygame.time.Clock()

# Creating a white cell surfaces
CELL_SURFACE = pygame.Surface((TILE_SIZE, TILE_SIZE))
CELL_SURFACE.fill(WHITE)
pygame.draw.rect(CELL_SURFACE, GREY, pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE), 2)    # Adding a border


def draw_grid(cells):
    for row in range(GRID_HEIGHT):
        pygame.draw.line(WIN, GREY, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE), 2)
    
    for col in range(GRID_WIDTH):
        pygame.draw.line(WIN, GREY, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT), 2)

    for cell in cells:
        WIN.blit(CELL_SURFACE, tuple((pos * TILE_SIZE)+1 for pos in cell))

def get_neighbours(cell):
    neighbours = set()
    neighbours.add((cell[0]-1, cell[1]-1))
    neighbours.add((cell[0], cell[1]-1))
    neighbours.add((cell[0]+1, cell[1]-1))
    neighbours.add((cell[0]-1, cell[1]))
    neighbours.add((cell[0]+1, cell[1]))
    neighbours.add((cell[0]-1, cell[1]+1))
    neighbours.add((cell[0], cell[1]+1))
    neighbours.add((cell[0]+1, cell[1]+1))

    return neighbours

def update_grid(cells):

    killed_cells = list()
    created_cells = list()

    for cell in cells:

        cell_neighbours = get_neighbours(cell)
        active_neighbours = cell_neighbours & cells     # Intersection of the sets
        if len(active_neighbours) not in [2, 3]:
            killed_cells.append(cell)

        inactive_neighbours = cell_neighbours - cells
        for cell in inactive_neighbours:
            cell_neighbours = get_neighbours(cell)
            active_neighbours = cell_neighbours & cells     # Intersection of the sets
            if len(active_neighbours) == 3:
                created_cells.append(cell)

    for cell in killed_cells:
        cells.discard(cell)

    for cell in created_cells:
        cells.add(cell)

# Event Loop
def main():
    running = True
    playing = False

    active_cells = set()

    while running:
        CLOCK.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:        # Pausing on mouse click
                if playing:
                    playing = False
            
            if not playing:
                if pygame.mouse.get_pressed()[0]:           # Creating a cell on left click
                    pos_x, pos_y = pygame.mouse.get_pos()
                    col = pos_x // TILE_SIZE
                    row = pos_y // TILE_SIZE
                    active_cells.add((col, row))
                if pygame.mouse.get_pressed()[2]:           # Deleting a cell on right click
                    pos_x, pos_y = pygame.mouse.get_pos()
                    col = pos_x // TILE_SIZE
                    row = pos_y // TILE_SIZE
                    active_cells.discard((col, row))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:         # Playing/Pausing on pressing space
                    playing = not playing
                if event.key == pygame.K_c:             # Clearing all the cells on pressing C
                    active_cells.clear()

        if playing:
            update_grid(active_cells)
            pygame.time.delay(500)                      # Delay 500ms

        WIN.fill(BLACK)                                 # Black background
        draw_grid(active_cells)

        pygame.display.update()
    
    pygame.quit()
    
if __name__ == "__main__":
    main()