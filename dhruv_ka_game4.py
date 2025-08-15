def reset_game(self):
    self.state = 'toss'
    self.player_score = 0
    self.comp_score = 0
    self.player_wickets = 0
    self.comp_wickets = 0
    self.balls = 0
    self.target = None
    self.batting_side = None
    self.toss_result = None
    self.first_batting = None

def create_widgets(self):
    self.info = tk.Label(self.root, text="Welcome to Simple Cricket Game!", font=("Arial", 14))
    self.info.pack(pady=10)

    self.toss_frame = tk.Frame(self.root)
    self.toss_label = tk.Label(self.toss_frame, text="Choose Heads or Tails:")
    self.toss_label.pack(side=tk.LEFT)
    self.heads_btn = tk.Button(self.toss_frame, text="Heads", command=lambda: self.do_toss('H'))
    self.heads_btn.pack(side=tk.LEFT, padx=5)
    self.tails_btn = tk.Button(self.toss_frame, text="Tails", command=lambda: self.do_toss('T'))
    self.tails_btn.pack(side=tk.LEFT, padx=5)
    self.toss_frame.pack(pady=10)

    self.choice_frame = tk.Frame(self.root)
    self.bat_btn = tk.Button(self.choice_frame, text="Bat", command=lambda: self.choose_bat_bowl('bat'))
    self.bowl_btn = tk.Button(self.choice_frame, text="Bowl", command=lambda: self.choose_bat_bowl('bowl'))
    self.bat_btn.pack(side=tk.LEFT, padx=5)
    self.bowl_btn.pack(side=tk.LEFT, padx=5)

    self.play_frame = tk.Frame(self.root)
    self.run_buttons = []
    for i in range(1, 7):
        btn = tk.Button(self.play_frame, text=str(i), width=3, command=lambda x=i: self.play_ball(x))
        btn.pack(side=tk.LEFT, padx=2)
        self.run_buttons.append(btn)

    self.score_label = tk.Label(self.root, text="", font=("Arial", 12))
    self.score_label.pack(pady=10)

    self.restart_btn = tk.Button(self.root, text="Restart", command=self.restart)
    self.restart_btn.pack(pady=5)
    self.restart_btn.pack_forget()

def do_toss(self, call):
    self.toss_result = random.choice(['H', 'T'])
    result_str = "Heads" if self.toss_result == 'H' else "Tails"
    if call == self.toss_result:
        self.info.config(text=f"Toss result: {result_str}. You won the toss! Bat or Bowl?")
        self.toss_frame.pack_forget()
        self.choice_frame.pack(pady=10)
    else:
        comp_choice = random.choice(['bat', 'bowl'])
        self.info.config(text=f"Toss result: {result_str}. Computer won and chose to {comp_choice} first.")
        self.toss_frame.pack_forget()
        self.first_batting = 'computer' if comp_choice == 'bat' else 'player'
        self.root.after(1500, self.start_innings)

def choose_bat_bowl(self, choice):
    self.choice_frame.pack_forget()
    self.first_batting = 'player' if choice == 'bat' else 'computer'
    self.start_innings()

def start_innings(self):
    self.balls = 0
    self.player_score = 0
    self.comp_score = 0
    self.player_wickets = 0
    self.comp_wickets = 0
    self.target = None
    self.batting_side = self.first_batting
    self.score_label.config(text="")
    self.info.config(text=f"{self.batting_side.capitalize()} is batting! (2 wickets, 2 overs)")
    self.play_frame.pack(pady=10)
    self.update_score()

def play_ball(self, player_run):
    if self.batting_side == 'player':
        comp_run = random.randint(1, 6)
        msg = f"You played: {player_run}, Computer bowled: {comp_run}\n"
        if player_run == comp_run:
            self.player_wickets += 1
            msg += f"Wicket! Total wickets: {self.player_wickets}"
        else:
            self.player_score += player_run
            msg += f"Score: {self.player_score}/{self.player_wickets}"
        self.balls += 1
        self.score_label.config(text=msg)
        if self.player_wickets == 2 or self.balls == 12:
            self.info.config(text=f"Player finished with {self.player_score} runs.")
            self.batting_side = 'computer'
            self.target = self.player_score + 1
            self.balls = 0
            self.root.after(1500, self.start_computer_innings)
    else:
        comp_run = random.randint(1, 6)
        msg = f"Computer played: {comp_run}, You bowled: {player_run}\n"
        if player_run == comp_run:
            self.comp_wickets += 1
            msg += f"Wicket! Total wickets: {self.comp_wickets}"
        else:
            self.comp_score += comp_run
            msg += f"Score: {self.comp_score}/{self.comp_wickets}"
        self.balls += 1
        self.score_label.config(text=msg)
        if self.comp_wickets == 2 or self.balls == 12 or (self.target and self.comp_score >= self.target):
            self.info.config(text=f"Computer finished with {self.comp_score} runs.")
            self.play_frame.pack_forget()
            self.root.after(1500, self.show_result)
    self.update_score()

def start_computer_innings(self):
    self.info.config(text=f"Computer is batting! Target: {self.target}")
    self.score_label.config(text="")
    self.balls = 0
    self.comp_score = 0
    self.comp_wickets = 0
    self.play_frame.pack(pady=10)

def update_score(self):
    if self.batting_side == 'player':
        self.score_label.config(text=f"Score: {self.player_score}/{self.player_wickets} Balls: {self.balls}/12")
    else:
        self.score_label.config(text=f"Score: {self.comp_score}/{self.comp_wickets} Balls: {self.balls}/12")

def show_result(self):
    self.play_frame.pack_forget()
    if self.player_score > self.comp_score:
        result = "Congratulations! You win!"
    elif self.player_score < self.comp_score:
        result = "Computer wins! Better luck next time."
    else:
        result = "It's a tie!"
    self.info.config(text=result)
    self.restart_btn.pack(pady=5)

def restart(self):
    self.restart_btn.pack_forget()
    self.reset_game()
    self.info.config(text="Welcome to Simple Cricket Game!")
    self.score_label.config(text="")
    self.toss_frame.pack(pady=10)