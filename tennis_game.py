import random

class TennisGame:
    def __init__(self):
        self.ball_position = (0, 0)  # (x, y) are the position of the ball on the court
        self.player_position = (0, 0)
        self.shot_types = ['forehand', 'backhand', 'lob', 'volley']
        self.directions = ['left', 'right', 'straight']
        self.serve_turn = 'player'

    def serve(self):
        print("\nServing the ball...")
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

    def play_shot(self, shot_type, direction):
        print(f"\nPlayer plays a {shot_type} shot towards {direction}.")
        # Simplified shot logic: randomize new ball position
        self.ball_position = (random.randint(-3, 3), random.randint(1, 6))
        print(f"Ball moves to position {self.ball_position}")

    def check_in_out(self):
        x, y = self.ball_position
        # Assuming court bounds to be -4 to 4 in x and 0 to 7 in y
        if -4 <= x <= 4 and 0 <= y <= 7:
            print("The ball is in.")
            return True
        else:
            print("The ball is out.")
            return False

    def play(self):
        while True:
            if self.serve_turn == 'player':
                self.serve()
                self.serve_turn = 'opponent'
            else:
                print("\nOpponent's turn to serve...")
                # Opponent serve logic (simplified)
                self.serve()
                self.serve_turn = 'player'

            shot_type, direction = self.get_player_input()
            self.play_shot(shot_type, direction)
            if not self.check_in_out():
                break
            # Switching turns after every shot
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    game = TennisGame()
    print("Welcome to CLI Tennis Game!")
    game.play()
