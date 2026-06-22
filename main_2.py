# main.py - Entry Point

from game import Game


def main():
    try:
        game = Game()
        game.play()
    except KeyboardInterrupt:
        print("\n\n  Game interrupted. Goodbye! ❌⭕\n")


if __name__ == "__main__":
    main()
