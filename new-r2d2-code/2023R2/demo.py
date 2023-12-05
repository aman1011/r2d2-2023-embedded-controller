import pygame
import sys

pygame.init()

# Set up the display (optional)
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bluetooth Joystick Demo")


#List of selected sounds
hums = ["Jedi/hum/HUM1.mp3", "Jedi/hum/HUM7.mp3", "Jedi/hum/HUM13.mp3", "Jedi/hum/HUM17.mp3","Jedi/hum/HUM23.mp3"]
screams = ["Jedi/scream/SCREAM1.mp3", "Jedi/scream/SCREAM2.mp3", "Jedi/scream/SCREAM3.mp3", "Jedi/scream/SCREAM4.mp3"]
sents = ["Jedi/sent/SENT2.mp3", "Jedi/sent/SENT4.mp3", "Jedi/sent/SENT5.mp3", "Jedi/sent/SENT17.mp3", "Jedi/sent/SENT20.mp3"]
procs = ["Jedi/proc/PROC2.mp3", "Jedi/proc/PROC3.mp3", "Jedi/proc/PROC5.mp3", "Jedi/proc/PROC13.mp3", "Jedi/proc/PROC15.mp3"]

# Set up the joystick
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
    print("No joystick found. Exiting...")
    pygame.quit()
    sys.exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Joystick Name: {joystick.get_name()}")

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.JOYAXISMOTION:
                print(f"Axis {event.axis}: {joystick.get_axis(event.axis)}")

            if event.type == pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} pressed")

            if event.type == pygame.JOYBUTTONUP:
                print(f"Button {event.button} released")

            if event.type == pygame.JOYBUTTONDOWN:
                #Triangle on PS3
                if event.button == 2:
                    print("TRIANGLE | HUM")
                    clearLCDLine()
                    lcd.putstr("SOUND: HUM")
                    # For playing a sound, we initialize the pygame audio mixer
                    pygame.mixer.init()
                    # Choose a random sound
                    soundChoice = random.randint(0, 4)
                    # Load into memory and play.
                    # Same logic will apply every time we play a sound from now on.
                    pygame.mixer.music.load(hums[soundChoice])
                    pygame.mixer.music.play()
                
                # Square on PS3
                elif event.button == 3:
                    print("SQUARE | PROC")
                    clearLCDLine()
                    lcd.putstr("SOUND: PROC")
                    pygame.mixer.init()
                    soundChoice = random.randint(0, 4)
                    pygame.mixer.music.load(procs[soundChoice])
                    pygame.mixer.music.play()
                
                # Cross on PS3
                elif event.button == 0:
                    print("CROSS | SENT")
                    clearLCDLine()
                    lcd.putstr("SOUND: SENT")
                    pygame.mixer.init()
                    soundChoice = random.randint(0, 4)
                    pygame.mixer.music.load(sents[soundChoice])
                    pygame.mixer.music.play()
                
                # Circle on PS3
                elif event.button == 1:
                    print("CIRCLE | SCREAM")
                    clearLCDLine()
                    lcd.putstr("SOUND: SCREAM")
                    pygame.mixer.init()
                    soundChoice = random.randint(0, 3)
                    pygame.mixer.music.load(screams[soundChoice])
                    pygame.mixer.music.play()
                         
                elif event.button == 8:
                    print("SELECT | CANTINA")
                    clearLCDLine()
                    lcd.putstr("SOUND: CANTINA")
                    pygame.mixer.init()
                    pygame.mixer.music.load("Jedi/mix/CANTINA.mp3")
                    pygame.mixer.music.play()
                
                elif event.button == 10:
                    print("PS button | ANNOYED")
                    pygame.mixer.init()
                    pygame.mixer.music.load("Jedi/mix/ANNOYED.mp3")
                    pygame.mixer.music.play()
                    
                elif event.button == 9:
                    print("START | SHORT CIRCUIT")
                    clearLCDLine()
                    lcd.putstr("SOUND: SH.CIRC")
                    pygame.mixer.init()
                    pygame.mixer.music.load("Jedi/mix/SHORTCKT.mp3")
                    pygame.mixer.music.play()

except KeyboardInterrupt:
    pygame.quit()
    sys.exit()
