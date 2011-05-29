import random
import maze

class Actor(object):
    def __init__(self, symbol, initial_room):
        self.symbol = symbol
        self.room = initial_room
        self.room.enter(self)

    def __str__(self):
        return self.symbol

    def move(self, dir):
        dest = getattr(self.room, dir)
        if dest:
            self.room.exit(self)     
            dest.enter(self)     
            self.room = dest
        else:
            raise ValueError("Cannot move in that direction")


class Game(object):
    def __init__(self, maze):
        self.maze = maze
        self.player = self.spawn('P')
        self.wumpus = self.spawn('W')
        self.lastwumpusdir = None

    def spawn(self, symbol):
        """Create an actor in a random room."""
        c, room = random.choice(list(self.maze.enumerate()))
        return Actor(symbol, room) 

    def move_wumpus(self):
        dirs = [(d, dir) for d, dir in maze.DIRECTIONS.items() if d != self.lastwumpusdir]
        random.shuffle(dirs)
        for d, dir in dirs:
            try:
                self.wumpus.move(d)
            except ValueError:
                continue
            else:
                self.lastwumpusdir = dir.inv
                return
        self.wumpus.move(self.lastwumpusdir)
        self.lastwumpusdir = maze.DIRECTIONS[self.lastwumpusdir].inv

    def can_player_hear(self):
        r = self.player.room
        for d in maze.DIRECTIONS:
            adj = getattr(r, d)
            if adj is not None and self.wumpus in adj.contents:
                return True
        return False

    def has_player_won(self):
        return self.wumpus in self.player.room.contents
    
