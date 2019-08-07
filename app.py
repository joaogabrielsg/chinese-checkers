import pygame


def main():
  pygame.init()
  screen = pygame.display.set_mode((800, 800))
  done = False

  while not done:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True



if __name__ == "__main__":
	main()