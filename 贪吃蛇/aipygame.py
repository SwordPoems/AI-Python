import pygame
import random
import sys

# 设置游戏界面大小、蛇身大小和蛇的初始位置
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 480
BLOCK_SIZE = 20
INIT_POS = [100, 100]

# 随机生成食物的位置
def get_food_pos():
    return [random.randrange(1, SCREEN_WIDTH//BLOCK_SIZE)*BLOCK_SIZE,
            random.randrange(1, SCREEN_HEIGHT//BLOCK_SIZE)*BLOCK_SIZE]

# 主程序
def main():
    # 初始化 pygame 库
    pygame.init()

    # 创建游戏界面和游戏时钟
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('贪吃蛇 - Python小游戏')
    clock = pygame.time.Clock()

    # 加载字体
    font = pygame.font.SysFont('Arial', 30)

    # 初始化蛇的初始长度和位置
    snake_length = 1
    snake_pos = [INIT_POS]
    snake_direction = [BLOCK_SIZE, 0]

    # 初始化食物
    food_pos = get_food_pos()

    # 游戏主循环
    while True:
        # 处理游戏退出事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 处理键盘按键
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            snake_direction = [-BLOCK_SIZE, 0]
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            snake_direction = [BLOCK_SIZE, 0]
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            snake_direction = [0, -BLOCK_SIZE]
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            snake_direction = [0, BLOCK_SIZE]
            

        # 移动蛇
        snake_pos.insert(0, [snake_pos[0][0]+snake_direction[0],
                            snake_pos[0][1]+snake_direction[1]])
        snake_pos = snake_pos[:snake_length]

        # 判断是否吃到食物，更新食物和蛇的位置
        if snake_pos[0] == food_pos:
            food_pos = get_food_pos()
            snake_length += 1

        # 判断游戏是否结束
        if snake_pos[0][0] < 0 or snake_pos[0][0] >= SCREEN_WIDTH or \
           snake_pos[0][1] < 0 or snake_pos[0][1] >= SCREEN_HEIGHT or \
           snake_pos[0] in snake_pos[1:]:
            text = font.render('Game Over', True, (255, 0, 0))
            screen.blit(text, (SCREEN_WIDTH//2-80, SCREEN_HEIGHT//2))
            pygame.display.update()
            pygame.time.delay(2000)
            return

        # 绘制游戏界面
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (255, 0, 0), [food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE])
        for i, pos in enumerate(snake_pos):
            pygame.draw.rect(screen, (0, 0, 255), [pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE])
        pygame.display.update()

        # 控制游戏帧率
        clock.tick(10)

# 启动游戏
if __name__ == '__main__':
    main()
