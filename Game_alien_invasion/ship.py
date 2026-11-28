import pygame

class Ship:
    """우주선을 관리하는 클래스"""
    def __init__(self, ai_game):
        """우주선을 초기화하고 시작 위치를 설정"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #우주선 이미지를 불러오고 사각형을 가져온다.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #우주선 초기 위치는 화면 하단 중앙입니다.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """우주선을 현재 위치에 그림"""
        self.screen.blit(self.image, self.rect)