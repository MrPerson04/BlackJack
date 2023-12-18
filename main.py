import pygame
import time

from Deck import Deck
from Hand import Hand
from Player import Player

pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BlackJack")

BG = pygame.transform.scale(pygame.image.load("images/background.jpg"), (WIDTH, HEIGHT))

FONT = pygame.font.SysFont("timesnewroman", 30)
RESULTSFONT = pygame.font.SysFont("timesnewroman", 150)
TITLEFONT = pygame.font.SysFont("timesnewroman", 80)


def draw_game(elapsed_time, deck_rect, flipped_deck, player_hand, dealer_hand, stand_button, stand, player, current_bet,
              add_bet_button, subtract_bet_button):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    deck_image = pygame.image.load('images/deck.png').convert()
    deck_image = pygame.transform.scale(deck_image, (150, 250))

    WIN.blit(deck_image, deck_rect)

    chips_text = FONT.render("Chips: " + str(player.get_chips()), 1, "white")
    WIN.blit(chips_text, (WIDTH / 2 - chips_text.get_width() / 2, 150))

    current_bet_text = FONT.render("Current Bet: " + str(current_bet), 1, "white")
    WIN.blit(current_bet_text, (WIDTH / 2 - current_bet_text.get_width() / 2, 200))

    if flipped_deck:
        if not stand:
            dealer_text = FONT.render(str(dealer_hand.get_first_card()) + ", ?", 1, "white")
            dealer_value_text = FONT.render("Value: " + str(dealer_hand.get_first_card().get_value()), 1, "white")
        else:
            dealer_text = FONT.render(str(dealer_hand), 1, "white")
            dealer_value_text = FONT.render("Value: " + str(dealer_hand.get_value()), 1, "white")

        player_text = FONT.render(str(player_hand), 1, "white")
        player_value_text = FONT.render("Value: " + str(player_hand.get_value()), 1, "white")
        WIN.blit(dealer_text, (100, 50))
        WIN.blit(dealer_value_text, (100, 100))
        WIN.blit(player_text, (100, 600))
        WIN.blit(player_value_text, (100, 650))
        stay_text = FONT.render('Stay', True, 'white')
        pygame.draw.rect(WIN, (180, 180, 180), stand_button)
        WIN.blit(stay_text, (stand_button.x + 23, stand_button.y + 10))
    else:
        add_bet_text = FONT.render('Add to Bet', True, 'white')
        pygame.draw.rect(WIN, (180, 180, 180), add_bet_button)
        WIN.blit(add_bet_text, (add_bet_button.x + 23, add_bet_button.y + 10))

        subtract_bet_text = FONT.render('Subtract Bet', True, 'white')
        pygame.draw.rect(WIN, (180, 180, 180), subtract_bet_button)
        WIN.blit(subtract_bet_text, (subtract_bet_button.x + 23, subtract_bet_button.y + 10))

    pygame.display.update()


def draw_menu(play_button, quit_button, player):
    WIN.blit(BG, (0, 0))

    title_text = TITLEFONT.render("BlackJack", 1, "white")
    WIN.blit(title_text, (WIDTH / 2 - title_text.get_width() / 2, 10))

    chips_text = FONT.render("Chips: " + str(player.get_chips()), 1, "white")
    WIN.blit(chips_text, (WIDTH / 2 - chips_text.get_width() / 2, 100))

    play_text = FONT.render('Play', True, 'white')
    pygame.draw.rect(WIN, (180, 180, 180), play_button)
    WIN.blit(play_text, (play_button.x + 23, play_button.y + 10))

    quit_text = FONT.render('Quit', True, 'white')
    pygame.draw.rect(WIN, (180, 180, 180), quit_button)
    WIN.blit(quit_text, (quit_button.x + 23, quit_button.y + 10))

    pygame.display.update()


def main():
    end_text = "Quitting"
    run = True

    clock = pygame.time.Clock()
    start_time = time.time()

    stand_button = pygame.Rect(700, 400, 100, 60)
    play_button = pygame.Rect(WIDTH / 2 - 50, HEIGHT / 2 - 100, 100, 60)
    quit_button = pygame.Rect(WIDTH / 2 - 50, HEIGHT / 2, 100, 60)
    add_bet_button = pygame.Rect(WIDTH / 2 + 150, 150, 170, 60)
    subtract_bet_button = pygame.Rect(WIDTH / 2 + 150, 250, 190, 60)

    deck_image = pygame.image.load('images/deck.png').convert()
    deck_image = pygame.transform.scale(deck_image, (150, 250))
    # Create a rect with the size of the image.
    deck_rect = deck_image.get_rect()
    deck_rect.center = (WIDTH / 2, HEIGHT / 2)

    player_one = Player()

    while run:
        in_game = True
        menu = True

        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    in_game = False
                    menu = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y positions of the mouse click
                    x, y = event.pos
                    if play_button.collidepoint(x, y):
                        in_game = True
                        menu = False
                        break
                    if quit_button.collidepoint(x, y):
                        run = False
                        in_game = False
                        menu = False
                        break

            draw_menu(play_button, quit_button, player_one)

        deck = Deck()
        deck.shuffle()

        player_hand = Hand(deck)
        dealer_hand = Hand(deck)

        current_bet = 10

        while in_game:
            clock.tick(60)
            elapsed_time = time.time() - start_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    in_game = False
                    if deck.is_flipped():
                        player_one.lose_chips(current_bet)
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Set the x, y positions of the mouse click
                    x, y = event.pos
                    if deck_rect.collidepoint(x, y) and deck.is_clickable():
                        if not deck.is_flipped():
                            deck.set_flipped(True)
                            # check for an immediate win
                            if player_hand.get_value() == 21:
                                # auto win game
                                end_text = "Win"
                                player_one.gain_chips(current_bet)
                                in_game = False
                                draw_game(elapsed_time, deck_rect, deck.is_flipped(), player_hand, dealer_hand,
                                          stand_button, False, player_one, current_bet, add_bet_button,
                                          subtract_bet_button)
                                break
                        else:
                            player_hand.hit(deck)
                            draw_game(elapsed_time, deck_rect, deck.is_flipped(), player_hand, dealer_hand,
                                      stand_button, False, player_one, current_bet, add_bet_button, subtract_bet_button)
                            if player_hand.get_value() == 21:
                                # auto win game
                                end_text = "Win"
                                player_one.gain_chips(current_bet)
                                in_game = False
                                break
                            elif player_hand.get_value() > 21:
                                # auto lose game
                                end_text = "Lose"
                                player_one.lose_chips(current_bet)
                                in_game = False
                                break
                    elif (add_bet_button.collidepoint(x, y) and not deck.is_flipped() and current_bet + 10 <=
                          player_one.get_chips()):
                        current_bet += 10
                    elif subtract_bet_button.collidepoint(x, y) and not deck.is_flipped() and current_bet - 10 >= 10:
                        current_bet -= 10
                    elif stand_button.collidepoint(x, y) and deck.is_flipped():
                        deck.set_clickable(False)
                        draw_game(elapsed_time, deck_rect, deck.is_flipped(), player_hand, dealer_hand, stand_button,
                                  True, player_one, current_bet, add_bet_button, subtract_bet_button)
                        pygame.time.wait(1000)
                        while dealer_hand.get_value() < 17:
                            dealer_hand.hit(deck)
                            draw_game(elapsed_time, deck_rect, deck.is_flipped(), player_hand, dealer_hand,
                                      stand_button, True, player_one, current_bet, add_bet_button, subtract_bet_button)
                            pygame.time.wait(1000)
                        if player_hand.get_value() <= dealer_hand.get_value() <= 21:
                            end_text = "Lose"
                            player_one.lose_chips(current_bet)
                            in_game = False
                            break
                        else:
                            end_text = "Win"
                            player_one.gain_chips(current_bet)
                            in_game = False
                            break
            if not in_game:
                draw_game(elapsed_time, deck_rect, deck.is_flipped(), player_hand, dealer_hand, stand_button, True,
                          player_one, current_bet, add_bet_button, subtract_bet_button)
                end_text = RESULTSFONT.render(end_text, True, 'green')
                results_rect = pygame.Rect(WIDTH / 2 - (end_text.get_width() + 50) / 2,
                                           HEIGHT / 2 - end_text.get_height() / 2,
                                           end_text.get_width() + 50, end_text.get_height())
                pygame.draw.rect(WIN, (180, 180, 180), results_rect)
                WIN.blit(end_text, (WIDTH / 2 - end_text.get_width() / 2, HEIGHT / 2 - end_text.get_height() / 2))
                pygame.display.update()
                pygame.time.wait(3000)
                pygame.event.clear(pygame.MOUSEBUTTONDOWN)
            else:
                draw_game(elapsed_time, deck_rect, deck.is_flipped(), player_hand, dealer_hand, stand_button, False,
                          player_one, current_bet, add_bet_button, subtract_bet_button)

    pygame.quit()


if __name__ == "__main__":
    main()
