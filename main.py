import pygame

# pygame setup
pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 1, 1)
clock = pygame.time.Clock()

GROUND_LEVEL = 400
# ground
ground_rect = pygame.Rect(0, GROUND_LEVEL, WINDOW_WIDTH, WINDOW_HEIGHT-GROUND_LEVEL)

# ALL THE P1 STUFF - facing right
p1_character = "stick_stabber" #input("p1:")
p1_direction = "right"
# body
p1_body = pygame.image.load(f"characters/{p1_character}/body/{p1_direction}.png")
p1_body_rect = p1_body.get_rect()
p1_body_tr_x = 100
p1_body_tr_y = GROUND_LEVEL - 128
p1_body_tr = (p1_body_tr_x, p1_body_tr_y)
p1_body_rect.topright = p1_body_tr
# stabber
p1_stabber = pygame.image.load(f"characters/{p1_character}/stabber/{p1_direction}.png")
p1_stabber_rect = p1_stabber.get_rect()
p1_stabber_tr = (p1_body_rect.topright[0]-2, p1_body_rect.topright[1]+87)
p1_stabber_rect.topright = p1_stabber_tr
p1_stabbing = False
p1_stab_ct = 0
p1_stab_frame_ct = 0
p1_arm_width = 1
p1_arm_rect = pygame.Rect(p1_body_rect.topright[0]-24, p1_body_rect.topright[1]+87, p1_arm_width, 5)
# shield
p1_shield = pygame.image.load(f"characters/{p1_character}/shield/{p1_direction}.png")
p1_shield_rect = p1_shield.get_rect()
p1_shield_rect.topleft = p1_body_tr
p1_shield_activated = False
p1_shield_frame_ct = 0

p1_jumping = False

# ALL THE P2 STUFF - facing left
p2_character = "stick_stabber" #input("p1:")
p2_direction = "left"
# body
p2_body = pygame.image.load(f"characters/{p2_character}/body/{p2_direction}.png")
p2_body_rect = p2_body.get_rect()
p2_body_tr_x = 800
p2_body_tr_y = GROUND_LEVEL - 128
p2_body_tr = (p2_body_tr_x, p2_body_tr_y)
p2_body_rect.topright = p2_body_tr
# stabber
p2_stabber = pygame.image.load(f"characters/{p1_character}/stabber/{p1_direction}.png")
p2_stabber_rect = p1_stabber.get_rect()
p2_stabber_tr = (p2_body_rect.topright[0]-2, p2_body_rect.topright[1]+87)
p2_stabber_rect.topright = p2_stabber_tr
p2_stabbing = False
p2_stab_ct = 0
p2_stab_frame_ct = 0
p2_arm_width = 1
p2_arm_rect = pygame.Rect(p2_body_rect.topright[0]-24, p2_body_rect.topright[1]+87, p2_arm_width, 5)
# shield
p2_shield = pygame.image.load(f"characters/{p2_character}/shield/{p2_direction}.png")
p2_shield_rect = p2_shield.get_rect()
p2_shield_rect.topleft = p2_body_tr
p2_shield_activated = False
p2_shield_frame_ct = 0

p2_jumping = False





running = True

in_battle = False

while running:
    if not in_battle:
        display_surface.fill((50,100,10))
    if in_battle:
        display_surface.fill((255,255,255))
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
        if not in_battle and keys[pygame.K_RETURN]:
            in_battle = True
        # controls p1
        if in_battle and keys[pygame.K_a]:
            p1_direction = "left"
            p1_body_tr_x -= 5
        if in_battle and keys[pygame.K_d]:
            p1_direction = "right"
            p1_body_tr_x += 5
        if in_battle and keys[pygame.K_x]:
            p1_stabbing = True
            p1_stab_ct = 0
            p1_stab_frame_ct = 0
            # stop shield
            p1_shield_activated = False
            p1_shield_frame_ct = 0
        if in_battle and keys[pygame.K_c]:
            p1_shield_activated = True
            p1_shield_frame_ct = 0
        if in_battle and keys[pygame.K_w] and not p1_jumping:
            p1_jumping = True
            p1_jump_ct = 0
        # controls p2
        if in_battle and keys[pygame.K_LEFT]:
            p2_direction = "left"
            p2_body_tr_x -= 5
        if in_battle and keys[pygame.K_RIGHT]:
            p2_direction = "right"
            p2_body_tr_x += 5
        if in_battle and keys[pygame.K_SLASH]:
            p2_stabbing = True
            p2_stab_ct = 0
            p2_stab_frame_ct = 0
            # stop shield
            p2_shield_activated = False
            p2_shield_frame_ct = 0
        if in_battle and keys[pygame.K_PERIOD]:
            p2_shield_activated = True
            p2_shield_frame_ct = 0
        if in_battle and keys[pygame.K_UP] and not p2_jumping:
            p2_jumping = True
            p2_jump_ct = 0

    if in_battle:
        # ground
        pygame.draw.rect(display_surface, (180,180,130), ground_rect)
        # update p1
        p1_body = pygame.image.load(f"characters/{p1_character}/body/{p1_direction}.png")
        p1_stabber = pygame.image.load(f"characters/{p1_character}/stabber/{p1_direction}.png")
        p1_shield = pygame.image.load(f"characters/{p1_character}/shield/{p1_direction}.png")
        # jump logik
        if p1_jumping:
            p1_jump_ct += 1
            if p1_jump_ct <= 30:
                p1_body_tr_y -= 2
            if p1_jump_ct > 30:
                p1_body_tr_y += 2
            if p1_jump_ct >= 60:
                p1_jumping = False
                p1_jump_ct = 0
        p1_body_tr = (p1_body_tr_x, p1_body_tr_y)
        p1_body_rect.topright = p1_body_tr
        if p1_direction	== "right":
            p1_stabber_tr = (p1_body_rect.topright[0]-2 +p1_stab_ct//3, p1_body_rect.topright[1]+87)
            p1_stabber_rect.topright = p1_stabber_tr
            if p1_stabbing:
                p1_stab_frame_ct +=1
                if p1_stab_frame_ct < 20:
                    p1_stab_ct +=3
                else:
                    p1_stab_ct -=3
                if p1_stab_frame_ct >= 40:
                    p1_stabbing = False
                    p1_stab_ct = 0
                    p1_stab_frame_ct = 0
        if p1_direction == "left":
            p1_stabber_tr = (p1_body_rect.topleft[0]+2 +p1_stab_ct//3, p1_body_rect.topright[1]+87)
            p1_stabber_rect.topleft = p1_stabber_tr
            if p1_stabbing:
                p1_stab_frame_ct +=1
                if p1_stab_frame_ct < 20:
                    p1_stab_ct -=3
                else:
                    p1_stab_ct +=3
                if p1_stab_frame_ct >= 40:
                    p1_stabbing = False
                    p1_stab_ct = 0
                    p1_stab_frame_ct = 0
        p1_arm_width = p1_stab_ct//3
        display_surface.blit(p1_body, p1_body_rect)
        display_surface.blit(p1_stabber, p1_stabber_rect)
        if p1_direction == "right":
            p1_arm_rect = pygame.Rect(p1_body_rect.topright[0]-24, p1_body_rect.topright[1]+87, p1_arm_width, 5)
            p1_shield_rect.topleft = p1_body_tr
        if p1_direction == "left":
            p1_arm_rect = pygame.Rect(p1_body_rect.topleft[0]+24+p1_arm_width, p1_body_rect.topright[1]+87, -1*(p1_arm_width), 5)
            p1_shield_rect.topright = p1_body_rect.topleft
        pygame.draw.rect(display_surface, (0,0,0), p1_arm_rect)
        if p1_shield_activated:
            display_surface.blit(p1_shield, p1_shield_rect)
            p1_shield_frame_ct += 1
            if p1_shield_frame_ct >= 70:
                p1_shield_activated = False
                p1_shield_frame_ct = 0

        # update p2
        p2_body = pygame.image.load(f"characters/{p2_character}/body/{p2_direction}.png")
        p2_stabber = pygame.image.load(f"characters/{p2_character}/stabber/{p2_direction}.png")
        p2_shield = pygame.image.load(f"characters/{p2_character}/shield/{p2_direction}.png")
        # jump logik
        if p2_jumping:
            p2_jump_ct += 1
            if p2_jump_ct <= 30:
                p2_body_tr_y -= 2
            if p2_jump_ct > 30:
                p2_body_tr_y += 2
            if p2_jump_ct >= 60:
                p2_jumping = False
                p2_jump_ct = 0
        p2_body_tr = (p2_body_tr_x, p2_body_tr_y)
        p2_body_rect.topright = p2_body_tr
        if p2_direction	== "right":
            p2_stabber_tr = (p2_body_rect.topright[0]-2 +p2_stab_ct//3, p2_body_rect.topright[1]+87)
            p2_stabber_rect.topright = p2_stabber_tr
            if p2_stabbing:
                p2_stab_frame_ct +=1
                if p2_stab_frame_ct < 20:
                    p2_stab_ct +=3
                else:
                    p2_stab_ct -=3
                if p2_stab_frame_ct >= 40:
                    p2_stabbing = False
                    p2_stab_ct = 0
                    p2_stab_frame_ct = 0
        if p2_direction == "left":
            p2_stabber_tr = (p2_body_rect.topleft[0]+2 +p2_stab_ct//3, p2_body_rect.topright[1]+87)
            p2_stabber_rect.topleft = p2_stabber_tr
            if p2_stabbing:
                p2_stab_frame_ct +=1
                if p2_stab_frame_ct < 20:
                    p2_stab_ct -=3
                else:
                    p2_stab_ct +=3
                if p2_stab_frame_ct >= 40:
                    p2_stabbing = False
                    p2_stab_ct = 0
                    p2_stab_frame_ct = 0
        p2_arm_width = p2_stab_ct//3
        display_surface.blit(p2_body, p2_body_rect)
        display_surface.blit(p2_stabber, p2_stabber_rect)
        if p2_direction == "right":
            p2_arm_rect = pygame.Rect(p2_body_rect.topright[0]-24, p2_body_rect.topright[1]+87, p2_arm_width, 5)
            p2_shield_rect.topleft = p2_body_tr
        if p2_direction == "left":
            p2_arm_rect = pygame.Rect(p2_body_rect.topleft[0]+24+p2_arm_width, p2_body_rect.topright[1]+87, -1*(p2_arm_width), 5)
            p2_shield_rect.topright = p2_body_rect.topleft
        pygame.draw.rect(display_surface, (0,0,0), p2_arm_rect)
        if p2_shield_activated:
            display_surface.blit(p2_shield, p2_shield_rect)
            p2_shield_frame_ct += 1
            if p2_shield_frame_ct >= 70:
                p2_shield_activated = False
                p2_shield_frame_ct = 0


    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60