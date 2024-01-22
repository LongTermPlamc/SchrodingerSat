import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
width, height = 500, 500
center = (width // 2, height // 2)

##Kinetical initial conditions
#radius
r0 = 10
rvel0 = 0
racc0 = 0
#angle
theta0 = 0
thetavel0 = 0.01
thetaacc0 = 0

# Colors
black = (0, 0, 0)
red = (255, 0, 0)

# Create Pygame window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Circular Motion Simulation")

# Main loop
clock = pygame.time.Clock()
prev_x, prev_y = center

racc_act = racc0
rvel_act = rvel0
rpos_act = r0
print("time, rpos, rvel, racc: ",0 ,", ", rpos_act,", ",rvel_act,", ",racc_act)

alpha_act = thetaacc0
omega_act = thetavel0
theta_act = theta0
print("time, theta, omega, alpha: ",0 ,", ", theta_act,", ",omega_act,", ",alpha_act)

velx_act = 0
vely_act = 0
posx_act = r0
posy_act = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    time = pygame.time.get_ticks()
    ## Integrating angular position
    timestep=clock.tick(120)

    racc_prev = racc_act
    rvel_prev = rvel_act
    rpos_prev = rpos_act

    racc_act = racc_prev
    rvel_act = rvel_prev + timestep * racc_act
    rpos_act = rpos_prev + timestep * rvel_act

    #print("time, rpos, rvel, racc: ",time ,", ", rpos_act,", ",rvel_act,", ",racc_act)

    alpha_prev = alpha_act
    omega_prev = omega_act
    theta_prev = theta_act

    alpha_act = alpha_prev
    omega_act = omega_prev + timestep * alpha_act
    theta_act = theta_prev + timestep * omega_act

    #print("time, theta, omega, alpha: ",time ,", ", theta_act,", ",omega_act,", ",alpha_act)

    accx = ( racc_act * math.cos(theta_act) 
             + 2 * rvel_act * omega_act * -1 * math.sin(theta_act)
             + rpos_act * (omega_act**2) * -1 * math.cos(theta_act)
             + rpos_act * alpha_act * -1 * math.sin(theta_act) )
    accy = ( racc_act * math.sin(theta_act) 
             + 2 * rvel_act * omega_act * -1 * math.cos(theta_act)
             + rpos_act * (omega_act**2) * -1 * math.sin(theta_act)
             + rpos_act * alpha_act * -1 * math.cos(theta_act) )

    print("theta, accx, accy: ", theta_act,", ",accx,", ", accy)

    velx_prev = velx_act
    vely_prev = vely_act

    velx_act = velx_prev + timestep * accx
    vely_act = vely_prev + timestep * accy

    posx_prev = posx_act
    posy_prev = posy_act
    
    posx_act = posx_prev + timestep * velx_act
    posy_act = posy_prev + timestep * vely_act

    #print("time, radius: ", time,", ", velx_act**2, vely_act**2)

    # Draw the background
    #screen.fill(black)

    # Draw the circle
    #pygame.draw.circle(screen, red, (x, y), 20)

    # Draw the velocity vector
    #pygame.draw.line(screen, (0, 255, 0), (x, y), (x + velocity_x, y + velocity_y), 2)

    # Update the display
    #pygame.display.flip()

    # Set the frame rate
    #clock.tick(1)