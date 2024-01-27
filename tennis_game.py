import random

class TennisGame:
    def __init__(self):
        # (x, y) position of the ball on the court
        self.ball_position = (0, 0) 
        self.shot_types = ['forehand', 'backhand', 'lob', 'volley']
        self.directions = ['left', 'right', 'straight']
        self.player_score = [0, 0]  # [Games, Sets]
        self.opponent_score = [0, 0]  # [Games, Sets]
        self.current_server = 'player'  # Player or Opponent
        self.point_winner = None  # Player, Opponent, or None

    def serve(self):
        if self.current_server == 'player':
            print("\nYou are serving...")
        else:
            print("\nOpponent is serving...")
        # Serve logic: randomize ball position
        self.ball_position = (random.randint(-3, 3), random.randint(1, 6))
        print(f"Ball served to position {self.ball_position}")

    def get_player_input(self):
        print("\nChoose your shot type:")
        for i, shot in enumerate(self.shot_types):
            print(f"{i}. {shot}")
        shot_choice = int(input("Enter your choice: "))

        print("\nChoose your direction:")
        for i, direction in enumerate(self.directions):
            print(f"{i}. {direction}")
        direction_choice = int(input("Enter your choice: "))

        return self.shot_types[shot_choice], self.directions[direction_choice]

    def ai_decision(self):
        # Simple AI logic: random shot type and direction
        shot_type = random.choice(self.shot_types)
        direction = random.choice(self.directions)
        return shot_type, direction

    def play_shot(self, shot_type, direction, player):
        if player == 'player':
            print(f"\nPlayer plays a {shot_type} shot towards {direction}.")
        else:
            print(f"\nOpponent plays a {shot_type} shot towards {direction}.")
        # Simple shot logic: randomize new ball position
        self.ball_position = (random.randint(-3, 3), random.randint(1, 6))
        print(f"Ball moves to position {self.ball_position}")

    def check_in_out(self):
        x, y = self.ball_position
        if -4 <= x <= 4 and 0 <= y <= 7:
            print("The ball is in.")
            return True
        else:
            print("The ball is out.")
            return False

    def update_score(self, point_winner):
        scores = ['0', '15', '30', '40', 'Game']
        if point_winner == 'player':
            if self.player_score[0] < 3:
                self.player_score[0] += 1
            elif self.player_score[0] == 3 and self.opponent_score[0] < 3:
                self.player_score[0] = 'Game'
        elif point_winner == 'opponent':
            if self.opponent_score[0] < 3:
                self.opponent_score[0] += 1
            elif self.opponent_score[0] == 3 and self.opponent_score[0] < 3:
                self.opponent_score[0] = 'Game'

    def display_score(self):
        print(f"\nCurrent Score: Player - {self.player_score[0]}, Opponent - {self.opponent_score[0]}")

    def play(self):
        while True:
            self.serve()
            if self.current_server == 'player':
                shot_type, direction = self.get_player_input()
            else:
                shot_type, direction = self.ai_decision()
            self.play_shot(shot_type, direction, self.current_server)
            if not self.check_in_out():
                self.point_winner = 'opponent' if self.current_server == 'player' else 'player'
                self.update_score(self.point_winner)
                self.display_score()
                break

            # Switching turn after each serve
            self.current_server = 'opponent' if self.current_server == 'player' else 'player'
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    game = TennisGame()
    print("Welcome to CLI AO Tennis Game!")
    game.play()
