from rpsapi import rps as game
import os
import sys

def main():
    print("Machine Learning Rock-Paper-Scissors Game v1.0")
    print("Copyright (c) 2025 Miles Muehlbach")
    rps = game.RPSGame()
    rps.play()

main()