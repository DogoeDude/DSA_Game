import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
GRID_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Snake class
class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = RIGHT

    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0] * GRID_SIZE, head[1] + self.direction[1] * GRID_SIZE)
        self.body.insert(0, new_head)

    def change_direction(self, new_direction):
        if (new_direction[0] != -self.direction[0]) and (new_direction[1] != -self.direction[1]):
            self.direction = new_direction

    def check_collision(self):
        head = self.body[0]
        if (
            head[0] < 0 or head[0] >= screen.get_width() or
            head[1] < 0 or head[1] >= screen.get_height() or
            head in self.body[1:]
        ):
            return True
        return False

    def eat_food(self, food_position):
        if self.body[0] == food_position:
            return True
        return False

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.spawn_food()

    def spawn_food(self):
        x = random.randrange(0, screen.get_width(), GRID_SIZE)
        y = random.randrange(0, screen.get_height(), GRID_SIZE)
        self.position = (x, y)

# Function to display menu screen
# Function to display menu screen
def show_menu(player_names, scores):
    screen.fill(BLACK)
    font = pygame.font.Font(None, 36)

    title_text = font.render("Snake Game", True, WHITE)
    screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 50))

    player_text = font.render(f"Player: {player_names[0]}", True, WHITE)
    screen.blit(player_text, (screen.get_width() // 2 - player_text.get_width() // 2, 100))

    leaderboard_text = font.render("Leaderboard", True, WHITE)
    screen.blit(leaderboard_text, (screen.get_width() // 2 - leaderboard_text.get_width() // 2, 150))

    player_scores = list(zip(player_names, scores))
    player_scores.sort(key=lambda x: x[1], reverse=True)

    # Display player rankings
    for i, (player_name, score) in enumerate(player_scores):
        if player_name == player_names[0]:
            player_ranking_text = font.render(f"{i + 1}. Player 1: {score}", True, WHITE)
        else:
            player_ranking_text = font.render(f"{i + 1}. {player_name}: {score}", True, WHITE)

        screen.blit(player_ranking_text, (screen.get_width() // 2 - player_ranking_text.get_width() // 2, 200 + i * 30))

    start_text = font.render("Press SPACE to start", True, WHITE)
    screen.blit(start_text, (screen.get_width() // 2 - start_text.get_width() // 2, screen.get_height() - 100))

    pygame.display.flip()


# Selection sort algorithm
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

#Speed Increase
def SpeedIncrement(scores):
    for i in range(5, 60, 5):
        if scores[current_player] > i:
            return True
    return False

# Initialize game
screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

players = 3
player_names = ["Player 1", "Player 2", "Player 3"]
current_player = 0
scores = [0] * players

# Main game loop
while True:
    show_menu(player_names, scores)
    if SpeedIncrement(scores):
        FPS= +10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Start the game
                snake = Snake()
                food = Food()
                score = 0
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                snake.change_direction(UP)
                            elif event.key == pygame.K_DOWN:
                                snake.change_direction(DOWN)
                            elif event.key == pygame.K_LEFT:
                                snake.change_direction(LEFT)
                            elif event.key == pygame.K_RIGHT:
                                snake.change_direction(RIGHT)
                    snake.move()
                    if snake.check_collision():
                        scores[current_player] += score
                        current_player = (current_player + 1) % players
                        break
                    if snake.eat_food(food.position):
                        food.spawn_food()
                        score += 1
                    else:
                        snake.body.pop()
                    # Draw everything
                    screen.fill(BLACK)
                    pygame.draw.rect(screen, GREEN, (*food.position, GRID_SIZE, GRID_SIZE))
                    for segment in snake.body:
                        pygame.draw.rect(screen, WHITE, (*segment, GRID_SIZE, GRID_SIZE))
                    pygame.display.flip()
                    clock.tick(FPS)
    clock.tick(FPS)
