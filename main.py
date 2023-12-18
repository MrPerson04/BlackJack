import pygame
import time

from Deck import Deck
from Hand import Hand

pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BlackJack")

BG = pygame.transform.scale(pygame.image.load("background.jpg"), (WIDTH, HEIGHT))

FONT = pygame.font.SysFont("timesnewroman", 30)


def draw(elapsed_time, deck_rect, flipped_deck, player_hand, dealer_hand, stay_button):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    deck_image = pygame.image.load('deck.png').convert()
    deck_image = pygame.transform.scale(deck_image, (150, 250))

    WIN.blit(deck_image, deck_rect)

    if flipped_deck:
        dealer_text = FONT.render(str(dealer_hand), 1, "white")
        dealer_value_text = FONT.render("Value: " + str(dealer_hand.get_value()), 1, "white")
        player_text = FONT.render(str(player_hand), 1, "white")
        player_value_text = FONT.render("Value: " + str(player_hand.get_value()), 1, "white")
        WIN.blit(dealer_text, (100, 50))
        WIN.blit(dealer_value_text, (100, 100))
        WIN.blit(player_text, (100, 600))
        WIN.blit(player_value_text, (100, 650))
        stay_text = FONT.render('Stay', True, 'white')
        pygame.draw.rect(WIN, (180, 180, 180), stay_button)
        WIN.blit(stay_text, (stay_button.x + 23, stay_button.y+10))

    pygame.display.update()


def main():
    run = True

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    stay_button = pygame.Rect(650, 400, 100, 60)

    deck_image = pygame.image.load('deck.png').convert()
    deck_image = pygame.transform.scale(deck_image, (150, 250))
    # Create a rect with the size of the image.
    deck_rect = deck_image.get_rect()
    deck_rect.center = (WIDTH / 2, HEIGHT / 2)

    deck = Deck()
    deck.shuffle()

    player_hand = Hand(deck)
    dealer_hand = Hand(deck)

    while run:
        clock.tick(60)
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Set the x, y positions of the mouse click
                x, y = event.pos
                if deck_rect.collidepoint(x, y) and deck.is_clickable():
                    if not deck.is_flipped():
                        deck.set_flipped(True)
                    else:
                        player_hand.hit(deck)
                        if player_hand.get_value() == 21:
                            # auto win game
                            print("win")
                            run = False
                            pygame.time.wait(1000)
                            break
                        elif player_hand.get_value() > 21:
                            # auto lose game
                            print("lose")
                            run = False
                            pygame.time.wait(1000)
                            break
                elif stay_button.collidepoint(x, y) and deck.is_flipped():
                        deck.set_clickable(False)
                        while(dealer_hand.get_value() < 17):
                            dealer_hand.hit(deck)
                            draw(elapsed_time, deck_rect, deck.is_flipped(), player_hand, dealer_hand, stay_button)
                            pygame.time.wait(1000)
                        if(dealer_hand.get_value() >= player_hand.get_value() and dealer_hand.get_value() <= 21):
                            print("lose")
                            run = False
                            pygame.time.wait(1000)
                            break
                        else:
                            print("win")
                            run = False
                            pygame.time.wait(1000)
                            break

        draw(elapsed_time, deck_rect, deck.is_flipped(), player_hand, dealer_hand, stay_button)

    pygame.quit()


if __name__ == "__main__":
    main()
