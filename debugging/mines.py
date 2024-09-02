def reveal(self, x, y):
    if (y * self.width + x) in self.mines:
        return False
    self.revealed[y][x] = True
    if self.count_mines_nearby(x, y) == 0:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                    self.reveal(nx, ny)
    
    if self.check_win():
        return 'win'
    
    return True

def check_win(self):
    for y in range(self.height):
        for x in range(self.width):
            if not self.revealed[y][x] and (y * self.width + x) not in self.mines:
                return False
    return True

def play(self):
    while True:
        self.print_board()
        try:
            x = int(input("Enter x coordinate: "))
            y = int(input("Enter y coordinate: "))
            result = self.reveal(x, y)
            if result == False:
                self.print_board(reveal=True)
                print("Game Over! You hit a mine.")
                break
            elif result == 'win':
                self.print_board(reveal=True)
                print("Congratulations! You've won the game.")
                break
        except ValueError:
            print("Invalid input. Please enter numbers only.")
