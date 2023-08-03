import pygame

pygame.init()

font20 = pygame.font.Font('freesansbold.ttf', 20)

Black = (0, 0, 0)
White = (255, 255, 255)
Blue = (0, 0, 255)

Width, Height = 900, 600
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
FPS = 30


class Striker:
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.geekRect = pygame.Rect(posx, posy, width, height)
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

    def display(self):
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

    def update(self, yFac):
        self.posy = self.posy + self.speed * yFac

        if self.posy <= 0:
            self.posy = 0
        elif self.posy + self.height >= Height:
            self.posy = Height - self.height

        self.geekRect = (self.posx, self.posy, self.width, self.height)

    def displayScore(self, text, score, x, y, color):
        text = font20.render(text + str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)

        screen.blit(text, textRect)

    def getRect(self):
        return self.geekRect




class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac = 1
        self.yFac = -1
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = 1

    def display(self):
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy), self.radius)

    def update(self):
        self.posx += self.speed * self.xFac
        self.posy += self.speed * self.yFac

        if self.posy <= 0 or self.posy >= Height:
            self.yFac *= -1

        if self.posx <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posx >= Width and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0

    def reset(self):
        self.posx = Width // 2
        self.posy = Height // 2
        self.xFac *= -1
        self.firstTime = 1
        self.speed = 7

    def hit(self):
        self.xFac *= -1
        self.speed += 1


    def getRect(self):
        return self.ball




def main():
    running = True
    HighScore = 0
    Player = Striker(870, 0, 10, 100, 20, Blue)
    ball = Ball(Width // 2, Height // 2, 7, 10, White)

    PlayerScore = 0
    PlayerYFac = 0

    while running:
        screen.fill(Black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    PlayerYFac = -1
                if event.key == pygame.K_s:
                    PlayerYFac = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    PlayerYFac = 0

        if pygame.Rect.colliderect(ball.getRect(), Player.getRect()):
            ball.hit()
            PlayerScore += 1

        if ball.xFac == 1:
            Player.posx = 870
        else:
            Player.posx = 20

        Player.update(PlayerYFac)
        point = ball.update()

        if point:
            ball.reset()
            if PlayerScore >= HighScore:
                HighScore = PlayerScore
            PlayerScore = 0

        Player.display()
        ball.display()
        Player.displayScore("Score : ",PlayerScore, 100, 20, White)
        Player.displayScore("HighScore: ", HighScore, 300, 20, White)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()