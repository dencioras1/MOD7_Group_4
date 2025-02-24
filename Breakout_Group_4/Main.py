import pygame
from Paddle import Paddle
from Ball import Ball
from Board import Board
from Window import Window

def make_balls(window_width, window_height, ball_speed, colour):
    BALLS = [Ball(window_width / 3, window_height / 2, 10, ball_speed, colour),
             Ball(window_width / 2, window_height / 2, 10, ball_speed, colour),
             Ball(window_width / 3 * 2, window_height / 2, 10, ball_speed, colour)]
    return BALLS

def main():

    BALL_SPEED = 1

    score = 0

    FRAMERATE = 120
    BACKGROUND = (0, 0, 0)
    WINDOW_WIDTH = 1080
    WINDOW_HEIGHT = 720
    SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
    RED = (247, 74, 74)
    BLUE = (74, 129, 247)
    WHITE = (255, 255, 255)

    PADDLES = [Paddle(150, 600, 5, [pygame.K_LEFT, pygame.K_RIGHT], RED),
               Paddle(850, 600, 5, [pygame.K_a, pygame.K_d], BLUE)]
    BALLS = make_balls(WINDOW_WIDTH, WINDOW_HEIGHT, BALL_SPEED, WHITE)

    # Code for game window settings
    pygame.init()
    SCREEN = pygame.display.set_mode(SIZE)
    CLOCK = pygame.time.Clock()

    # Set name for game window
    pygame.display.set_caption('BREAKOUT - G4')
    WINDOW = Window(1080, 720, 120, (0, 0, 0))

    WINDOW.initialize_window()

    BOARD = Board(WINDOW.get_surface())


    # Initialize font for displaying the score / speed
    pygame.font.init()
    FONT = pygame.font.SysFont("consolas", 24)


    # Main loop for the Breakout game
    while(True):
        # Check if the game window is closed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the screen is closed, quit the program
                pygame.quit()

        # Fill screen with background color
        SCREEN.fill(BACKGROUND)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            for ball in BALLS:
                ball.initialize_balls()

        i = 0
        for b in BALLS:
            if b.get_state() == 2:
                i += 1
        if i == 3:
            BALLS = make_balls(WINDOW_WIDTH, WINDOW_HEIGHT, BALL_SPEED, WHITE)





        WINDOW.check_exit_window()

        # Game logic goes here

        WINDOW.fill_background()

        BOARD.render_frame()
        BOARD.render_bricks()

        for paddle in PADDLES:
            paddle.update_paddle(keys)
            paddle.draw_paddle(SCREEN)

        BALLS[0].collision_paddle(PADDLES)
        BALLS[1].collision_paddle(PADDLES)
        BALLS[2].collision_paddle(PADDLES)

        hit_brick_1 = BALLS[0].collision_bricks(BOARD.get_bricks())
        hit_brick_2 = BALLS[1].collision_bricks(BOARD.get_bricks())
        hit_brick_3 = BALLS[2].collision_bricks(BOARD.get_bricks())

        if hit_brick_1 is not None:
            BOARD.remove_brick(hit_brick_1)
            score += 1
        if hit_brick_2 is not None:
            BOARD.remove_brick(hit_brick_2)
            score += 1
        if hit_brick_3 is not None:
            BOARD.remove_brick(hit_brick_3)
            score += 1

        BALLS[0].update_ball(WINDOW_WIDTH, WINDOW_HEIGHT)
        BALLS[1].update_ball(WINDOW_WIDTH, WINDOW_HEIGHT)
        BALLS[2].update_ball(WINDOW_WIDTH, WINDOW_HEIGHT)

        BALLS[0].draw_ball(SCREEN)
        BALLS[1].draw_ball(SCREEN)
        BALLS[2].draw_ball(SCREEN)
        
        score_surface = FONT.render("Bricks broken: " + str(score), True, (255, 255, 255))
        speed_surface = FONT.render("Current ball speed: " + str(BALLS[0].get_speed()), True, (255, 255, 255))
        enter_message = FONT.render("Press SPACE to start the game :)", True, WHITE)

        SCREEN.blit(score_surface, (30, 30))
        SCREEN.blit(speed_surface, (30, 50))
        SCREEN.blit(enter_message, (WINDOW_WIDTH/2-200, 690))

        WINDOW.update_canvas()

if __name__ == "__main__":
    main()



