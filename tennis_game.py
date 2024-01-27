import random

class TennisGame:
    def __init__(self, player_name, ai_difficulty):
        self.player_name = player_name
        self.ai_opponents = ["Novak Djokovic", "Carlos Alcaraz", "Daniil Medvedev", 
                             "Alexander Zverev", "Jannik Sinner", "Stefanos Tsitsipas", 
                             "Andrey Rublev", "Karen Khachanov", "Taylor Fritz"]
        self.ai_name = random.choice(self.ai_opponents).title()
        self.ai_difficulty = ai_difficulty
        self.ball_position = (0, 0)
        self.shot_types = ['volley','forehand', 'backhand', 'spin', 'slice', 'lob']
        self.directions = ['left', 'right', 'straight']
        self.player_score = [0, 0, 0]  # Points, Games, Sets
        self.opponent_score = [0, 0, 0]
        self.current_server = 'player'
        self.tiebreak = False
        self.set_number = 1
        self.final_set = False # Indicates if the current set is the final set
        self.player_stamina = 100  # Stamina starts at 100 
    
    def serve(self):
        print(f"\n{self.current_server.title()} is serving...")
        # Assuming each unit is 10 feet, court is 27 feet wide and 78 feet long
        # Width from -3 to 3 (for one side of the court) and length from 0 to 7
        self.ball_position = (random.randint(-3, 3), random.randint(0, 7))
        print(f"Ball served to position {self.ball_position}")

    def get_player_input(self, prompt, choices):
        while True:
            print(prompt)
            for i, choice in enumerate(choices):
                print(f"{i}. {choice}")
            try:
                selection = int(input("Enter your choice: "))
                if 0 <= selection < len(choices):
                    return choices[selection]
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def ai_decision(self):
        difficulty_modifiers = {'easy': 0.2, 'medium': 0.1, 'hard': 0.05}
        error_chance = difficulty_modifiers[self.ai_difficulty]

        if random.random() < error_chance:
            return 'lob', 'out'
        else:
            return random.choice(self.shot_types), random.choice(self.directions)

    def play_shot(self, shot_type):
        self.reduce_stamina(shot_type)

        out_probability = self.calculate_out_probability(shot_type)
        if random.random() < out_probability:
            self.ball_position = (100, 100)  # Ball out of bounds
            print("The ball goes out of court.")
        else:
            self.ball_position = (random.randint(-3, 3), random.randint(1, 6))
            print(f"Ball moves to position {self.ball_position}")

    def reduce_stamina(self, shot_type):
        stamina_costs = {
            'volley': 5, 'forehand': 3, 'backhand': 3, 'spin': 4, 'slice': 4, 'lob': 4
        }
        self.player_stamina -= stamina_costs.get(shot_type, 2)
        self.player_stamina = max(self.player_stamina, 0)

    def calculate_out_probability(self, shot_type):
        shot_risks = {
            'volley': 0.2, 'forehand': 0.1, 'backhand': 0.1, 'spin': 0.15, 'slice': 0.12, 'lob': 0.18
        }
        base_out_probability = 0.1
        return base_out_probability + shot_risks.get(shot_type, 0)
    
    def check_in_out(self):
        # Check if the ball is in or out of court with updated court dimensions
        x, y = self.ball_position
        if -3 <= x <= 3 and 0 <= y <= 7:
            print("The ball is in.")
            return True
        else:
            print("The ball is out.")
            return False
        
    def update_score(self, point_winner):
        if point_winner == self.player_name:
            self.player_score[0] += 1
        else:
            self.opponent_score[0] += 1

        if self.player_score[0] >= 4 or self.opponent_score[0] >= 4:
            if abs(self.player_score[0] - self.opponent_score[0]) >= 2:
                self.award_game(point_winner)


    def award_game(self, winner):
        if winner == self.player_name:
            self.player_score[1] += 1
        else:
            self.opponent_score[1] += 1

        self.player_score[0] = self.opponent_score[0] = 0  # Reset points for new game

        # Check for set win
        if self.check_set_win(winner):
            if winner == 'player':
                self.player_score[2] += 1
            else:
                self.opponent_score[2] += 1
            self.player_score[1] = self.opponent_score[1] = 0  # Reset games
            if self.check_match_win(winner):
                print(f"\n{winner.title()} wins the match!")
                exit()

        # Check for tiebreak
        if self.player_score[1] == 6 and self.opponent_score[1] == 6:
            self.tiebreak = True

    def check_set_win(self, player):
        p_games = self.player_score[1]
        o_games = self.opponent_score[1]
        if self.set_number == 5:  # Final set logic
            self.final_set = True
        if p_games == 6 and o_games == 6:
            self.play_tiebreak()
        return (p_games == 6 and o_games <= 4) or (p_games == 7 and o_games == 5) or (p_games == 7 and o_games == 6)

    def check_tiebreak_win(self, player):
        # Check for tiebreak win conditions
        if player == 'player' and self.player_score[0] >= 7 and (self.player_score[0] - self.opponent_score[0]) >= 2:
            return True
        elif player == 'opponent' and self.opponent_score[0] >= 7 and (self.opponent_score[0] - self.player_score[0]) >= 2:
            return True
        return False

    def check_match_win(self, player):
        # Check for match win conditions (best of 3 sets)
        p_sets = self.player_score[2]
        o_sets = self.opponent_score[2]
        return p_sets == 2 or o_sets == 2
    
    def play_tiebreak(self):
        print("\nStarting a tiebreak!")
        tiebreak_end = 7 if not self.final_set else 10
        while self.player_score[0] < tiebreak_end and self.opponent_score[0] < tiebreak_end:
            if abs(self.player_score[0] - self.opponent_score[0]) >= 2 and \
               (self.player_score[0] >= tiebreak_end or self.opponent_score[0] >= tiebreak_end):
                break

            self.serve()
            if self.current_server == self.player_name:
                shot_type, direction = self.get_player_input("Choose your shot type:", self.shot_types)
            else:
                shot_type, direction = self.ai_decision()
            self.play_shot(shot_type, direction, self.current_server)

            if not self.check_in_out():
                point_winner = self.ai_name if self.current_server == self.player_name else self.player_name
                self.update_score(point_winner)
                
            self.display_score()
            self.switch_server()

        # Award the set to the tiebreak winner
        if self.player_score[0] > self.opponent_score[0]:
            self.award_set(self.player_name)
        else:
            self.award_set(self.ai_name)
        self.tiebreak = False
    
    def switch_server(self):
        # Switching the server
        self.current_server = self.ai_name if self.current_server == self.player_name else self.player_name
   
    def tennis_score_representation(self, player_points, opponent_points):
        # Convert numeric score to traditional tennis score
        if player_points >= 3 and opponent_points >= 3:
            if player_points == opponent_points:
                return 'Deuce'
            elif player_points == opponent_points + 1:
                return 'Advantage Player'
            elif opponent_points == player_points + 1:
                return 'Advantage Opponent'
        return ['0', '15', '30', '40'][player_points]

    def display_score(self):
        player_point_score = self.tennis_score_representation(self.player_score[0], self.opponent_score[0])
        opponent_point_score = self.tennis_score_representation(self.opponent_score[0], self.player_score[0])

        # Handling deuce and advantage
        if self.player_score[0] >= 3 and self.opponent_score[0] >= 3:
            if self.player_score[0] == self.opponent_score[0]:
                score_display = 'Deuce'
            elif self.player_score[0] > self.opponent_score[0]:
                score_display = f'Advantage Player'
            else:
                score_display = f'Advantage Opponent'
        else:
            score_display = f"{player_point_score}-{opponent_point_score}"

        print(f"\nCurrent Point Score: {score_display}")
        print(f"Games: Player - {self.player_score[1]}, Opponent - {self.opponent_score[1]}")
        print(f"Sets: Player - {self.player_score[2]}, Opponent - {self.opponent_score[2]}")


    def play(self):
        while True:
            self.serve()
            in_play = True

            while in_play:
                if self.current_server == self.player_name:
                    shot_type = self.get_player_input("Choose your shot type:", self.shot_types)
                    direction = self.get_player_input("Choose your direction:", self.directions)
                    print(f"{self.player_name} plays a {shot_type} shot towards {direction}.")  # Announce player's shot
                    self.play_shot(shot_type)
                else:
                    ai_shot_type, ai_direction = self.ai_decision()
                    print(f"{self.ai_name} plays a {ai_shot_type} shot towards {ai_direction}.")  # Announce AI's shot
                    self.play_shot(ai_shot_type)

                in_play = self.check_in_out()

                if not in_play:
                    point_winner = self.ai_name if self.current_server == self.player_name else self.player_name
                    print(f"Point for {point_winner}.")
                    self.update_score(point_winner)

                self.display_score()
                self.switch_server()

            input("\nPress Enter to continue...")


if __name__ == "__main__":
    first_name = input("Enter your first name: ").strip().title()
    last_name = input("Enter your last name: ").strip().title()
    difficulty = input("Choose AI difficulty (easy, medium, hard): ").strip().lower()
    player_name = f"{first_name} {last_name}"
    game = TennisGame(player_name, difficulty)
    print(f"Welcome to CLI Tennis Game, {player_name}! Your opponent is {game.ai_name}.")
    game.play()