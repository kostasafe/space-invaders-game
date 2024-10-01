# Space Invaders Clone

A simple Space Invaders clone using Python and the Turtle graphics library. Players control a spaceship that shoots at enemies descending from the top of the screen. The goal is to defeat all enemies while avoiding being hit.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Mechanics](#game-mechanics)

## Features

- **Player Movement:** Move your spaceship left and right.
- **Shooting:** Fire bullets to destroy enemies.
- **Enemies:** Invaders move horizontally and drop down after hitting the screen edge.
- **Score System:** Score increases by 10 for each enemy destroyed.
- **Sound Effects:** Laser fire and explosions are accompanied by sounds.

## Installation

1. **Clone the repository:**
   
   Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/yourusername/space-invaders-clone.git

3. **Install Dependencies:**

   The game uses the turtle module (built-in with Python) and playsound for sound effects. To install playsound, run:

   ```bash
   pip install wheel   
   pip install playsound

4. **Download Assets:**

   Ensure that the required image and sound assets (```invader.gif```, ```player.gif```, ```space_invaders_background.gif```, ```laser.wav```, ```explosion.wav```) are located in the same directory as the script.

5. **Run the Game:** Run the ```space_invaders.py``` file using Python:
   ```
   python space_invaders.py
   ```
## How to Play

 - The goal of the game is to destroy as many enemies as possible while avoiding collision with them.
 - You control a spaceship that can move left and right at the bottom of the screen.
 - Use the spacebar to fire bullets to destroy incoming invaders.
 - Avoid enemies colliding with your spaceship, or the game is over!

## Game Mechanics

1. **Enemies:**
   - Enemies move horizontally and change direction after hitting the screen edges.
   - When an enemy hits the edge, all enemies drop down and move in the opposite direction.

2. **Collision Detection:**
   - If a bullet hits an enemy, the enemy disappears, and the score increases by 10 points.
   - If an enemy collides with the player, the game ends, and "Game Over" is displayed in the console.

3. **Scoring:**
   - The game plays a laser sound (```laser.wav```) when you fire a bullet.
   - An explosion sound (```explosion.wav```) is played when an enemy is hit or when the player collides with an enemy.

