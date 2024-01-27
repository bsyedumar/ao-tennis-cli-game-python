# OATennis CLI Game

Welcome to the <b> OATennis CLI Game</b>, a Python-based command-line interface game that simulates a tennis match between you and an AI opponent, based on Men's single rules from the Australian Open. The game follows realistic tennis rules, including scoring, deuce, advantage, tiebreaks, and shot selection. Experience the thrill of tennis with intuitive gameplay, on your command line, playing against the likes of <b> Novak Djokovic, Carlos Alcaraz, Jannik Sinner, Daniil Medvedev</b>, and other top tennis star players.

## How to Play

* Start the Game: Enter your first and last name to create your player profile.
* Match Setup: The game randomly selects a top AI tennis player as your opponent.
* Gameplay: You will start by serving the ball.
* Choose your shot type (Forehand, Backhand, Lob, Volley, Slice, Spin) and direction (Left, Right, Straight).
* Watch as the AI opponent responds with its shot, strategically chosen based on the game situation. The ball's movement and whether it stays in court are determined according to the chosen shot. 
* Scoring: The game follows standard tennis scoring rules. Points lead to games, and games lead to sets.
* Winning: Win the match by being the first to win three out of five sets.


## Game Features
* Realistic Tennis Dynamics: Simulates real tennis match scenarios, including various shot types and strategic AI decision-making.
* Interactive Gameplay: Engages players with shot selection and tactical decisions.
* Intuitive Interface: Easy-to-follow prompts and clear game status updates.
* Tiebreaks and Final Sets: Implements tiebreak rules and adapts to final set scenarios.

## Code Overview
The game's logic is encapsulated in the TennisGame class within the tennis_game.py file. Key components of the code include:

* TennisGame Class: The core class managing game state, rules, and interactions.
* serve Method: Handles the serving logic, initiating each point.
* get_player_input Method: Retrieves player's shot choices.
* ai_decision Method: Determines AI's shot based on the set difficulty and game context.
* play_shot Method: Executes the shot, updates ball position, and checks for out-of-bounds.
* check_in_out Method: Validates if the ball is within court boundaries.
* update_score Method: Updates the score after each point.
* award_game Method: Awards a game to the player or AI upon winning a point.
* check_set_win and check_match_win Methods: Determine the winner of a set and the overall match.
* play_tiebreak Method: Executes the tiebreak gameplay when required.
* Stamina Mechanics: Incorporates player stamina, influencing shot success rate.
## How to Run
* Ensure Python is installed on your system.
* Clone or download the tennis_game.py file.
* Run the file in a Python environment: python tennis_game.py.
* Follow the on-screen prompts to play the game.

Enjoy this Australian Open-inspired Tennis CLI game; game, set, match! 