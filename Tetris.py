import pygame
import sys

pygame.init()

# ================= SETTINGS =================
WIDTH, HEIGHT = 900, 500
FPS = 144

GRAVITY = 0.7
JUMP_FORCE = -14
JUMP_CUT = 0.5          # variable jump
MOVE_ACC = 0.6
MAX_SPEED = 6
FRICTION = 0.80

MAX_JUMP = 2
COYOTE_TIME = 120       # ms

DASH_SPEED = 14
DASH_TIME = 120         # ms

WHITE = (240, 240, 240)
BLUE = (80, 140, 255)
BROWN = (160, 120, 60)
RED = (220, 60, 60)
GREEN = (60, 200, 120)
BG = (20, 20, 40)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Retro Platformer")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 22)

# ================= PLAYER =================
class Player(pygame.Rect):
    def __init__(self, x, y):
        super().__init__(x, y, 40, 50)
        self.vel_x = 0
        self.vel_y = 0
        self.jump_count = 0
        self.last_ground_time = 0

        self.dashing = False
        self.dash_timer = 0
        self.facing = 1

    def update(self, platforms, dt):
        # gravity
        if not self.dashing:
            self.vel_y += GRAVITY

        self.y += self.vel_y
        on_ground = False

        for p in platforms:
            if self.colliderect(p):
                if self.vel_y > 0:
                    self.bottom = p.top
                    self.vel_y = 0
                    self.jump_count = 0
                    on_ground = True
                elif self.vel_y < 0:
                    self.top = p.bottom
                    self.vel_y = 0

        if on_ground:
            self.last_ground_time = pygame.time.get_ticks()

        # horizontal
        self.x += self.vel_x
        for p in platforms:
            if self.colliderect(p):
                if self.vel_x > 0:
                    self.right = p.left
                elif self.vel_x < 0:
                    self.left = p.right
                self.vel_x = 0

        # dash timer
        if self.dashing:
            self.dash_timer -= dt
            if self.dash_timer <= 0:
                self.dashing = False

        # friction
        if not self.dashing:
            self.vel_x *= FRICTION
            if abs(self.vel_x) < 0.1:
                self.vel_x = 0

# ================= ENEMY =================
class Enemy(pygame.Rect):
    def __init__(self, x, y, l, r):
        super().__init__(x, y, 40, 40)
        self.speed = 2
        self.l = l
        self.r = r

    def update(self):
        self.x += self.speed
        if self.left <= self.l or self.right >= self.r:
            self.speed *= -1

# ================= LEVELS =================
LEVELS = [
    {
        "platforms": [
            pygame.Rect(0, 450, 3000, 50),
            pygame.Rect(400, 350, 120, 20),
            pygame.Rect(700, 280, 120, 20),
        ],
        "spikes": [
            pygame.Rect(550, 430, 40, 20),
            pygame.Rect(600, 430, 40, 20),
        ],
        "enemies": [
            Enemy(900, 410, 850, 1100)
        ]
    },
    {
        "platforms": [
            pygame.Rect(0, 450, 3000, 50),
            pygame.Rect(300, 360, 120, 20),
            pygame.Rect(600, 300, 120, 20),
            pygame.Rect(900, 240, 120, 20),
        ],
        "spikes": [
            pygame.Rect(500, 430, 40, 20),
            pygame.Rect(540, 430, 40, 20),
            pygame.Rect(580, 430, 40, 20),
        ],
        "enemies": [
            Enemy(1000, 410, 950, 1200),
            Enemy(1300, 410, 1250, 1500)
        ]
    }
]

while len(LEVELS) < 10:
    LEVELS.append(LEVELS[-1])

# ================= GAME STATE =================
level = 0
camera_x = 0
paused = False

def load_level(idx):
    return (
        Player(100, 300),
        LEVELS[idx]["platforms"],
        LEVELS[idx]["spikes"],
        LEVELS[idx]["enemies"]
    )

player, platforms, spikes, enemies = load_level(level)

# ================= MAIN LOOP =================
running = True
while running:
    dt = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                paused = not paused

            # jump (SPACE)
            if event.key == pygame.K_SPACE:
                now = pygame.time.get_ticks()
                if (
                    player.jump_count < MAX_JUMP or
                    now - player.last_ground_time <= COYOTE_TIME
                ):
                    player.vel_y = JUMP_FORCE
                    player.jump_count += 1

            # dash (SHIFT)
            if event.key == pygame.K_LSHIFT and not player.dashing:
                player.dashing = True
                player.dash_timer = DASH_TIME
                player.vel_x = DASH_SPEED * player.facing

        # variable jump height
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and player.vel_y < 0:
                player.vel_y *= JUMP_CUT

    keys = pygame.key.get_pressed()

    if not paused:
        if keys[pygame.K_a]:
            player.vel_x -= MOVE_ACC
            player.facing = -1
        if keys[pygame.K_d]:
            player.vel_x += MOVE_ACC
            player.facing = 1

        player.vel_x = max(-MAX_SPEED, min(MAX_SPEED, player.vel_x))
        player.update(platforms, dt)

        for e in enemies:
            e.update()
            if player.colliderect(e):
                player, platforms, spikes, enemies = load_level(level)

        for s in spikes:
            if player.colliderect(s):
                player, platforms, spikes, enemies = load_level(level)

        camera_x += (player.centerx - camera_x - WIDTH // 2) * 0.08

        if player.x > 2800:
            level = min(level + 1, 9)
            player, platforms, spikes, enemies = load_level(level)
            camera_x = 0

    # ================= DRAW =================
    screen.fill(BG)

    for p in platforms:
        pygame.draw.rect(screen, BROWN, (p.x - camera_x, p.y, p.width, p.height))

    for s in spikes:
        pygame.draw.rect(screen, RED, (s.x - camera_x, s.y, s.width, s.height))

    for e in enemies:
        pygame.draw.rect(screen, GREEN, (e.x - camera_x, e.y, e.width, e.height))

    pygame.draw.rect(screen, BLUE, (player.x - camera_x, player.y, player.width, player.height))

    ui = font.render(
        f"LEVEL {level+1} | SPACE Jump | SHIFT Dash | A/D Move | TAB Pause",
        True, WHITE
    )
    screen.blit(ui, (20, 20))

    if paused:
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        txt = font.render("PAUSED", True, WHITE)
        screen.blit(txt, (WIDTH//2 - txt.get_width()//2, HEIGHT//2))

    pygame.display.flip()