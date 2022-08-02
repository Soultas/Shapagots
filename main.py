from random import randrange
import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()
size = width,height = 320,240
gray = 211,211,211
screen = pygame.display.set_mode(size)
screen.fill(gray)

def main():

    tama_start = True

    name_list = ("square","circle","rectangle","The Legendary Octagon")

    class Tama:
        hunger_start = 10
        happyness_start = 10

        def __init__(self):
            age = 1
            hunger_start = 10
            happyness_start = 10
            self.name = name_list[randrange(len(name_list))]
            self.age = age
            self.happyness = happyness_start
            self.hunger = hunger_start

        def play(self):
            if self.happyness >= 10:
                print("You have played with your tama!")
            else:
                print("You have played with your tama!")
                self.happyness += 1
        def feed(self):
            if self.hunger >=10:
                print("I am not hungry father")
            else:
                print('Thank you for feeding me father, I have gained hunger')
                self.hunger +=1

        def recall_name(self):
            my_name = self.name
            print("Hello, my name is ",my_name," and I am your tama")
        def recall_happy(self):
            my_happy = self.happyness
            print("My happyness level is", my_happy)

    other_tama = Tama()

    clock = pygame.time.Clock()
    time=0
    milli=clock.tick()

    seconds = milli/1000
    time += seconds
    print(time)

    while tama_start == True:
        print(time)
        other_tama.recall_name()
        will_play = input("Hello father, would you like to play, feed, or destroy?\n").lower()
        if will_play == "play":
            other_tama.play()
            other_tama.recall_happy()
        elif will_play == "feed":
            other_tama.feed()
        elif will_play == "destroy":
            # TODO add a list of different strings for it to choose from
            print("Goodbye father, it was nice knowing you")
            time.sleep(500)
            tama_start = False
        else:
            print("That's not any english I understand father")

main()