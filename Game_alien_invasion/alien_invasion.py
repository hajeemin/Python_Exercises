import sys

import pygame

from settings import Settings

class AlienInvasion:
    """게임 자원과 동작을 전체적으로 관리하는 클래스"""

    def __init__(self):
        """게임 자원을 초기화하고 게임 자원을 만듦"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """게임의 메인 루프 시작"""
        while True:
            #키보드와 마우스에 응답
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #루프 반복때마다 화면을 다시 그림
            self.screen.fill(self.settings.bg_color)

            #가장 최근 그린 화면을 표시
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

