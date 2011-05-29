from generate_maze import generate_maze
from play import Game
import maze

def wait_for_dir():
    while True:
        print "terenay a irectionday: ", 
        s = raw_input().strip().lower()
        if s in maze.DIRECTIONS:
            return s

def main():
    m = generate_maze(10,10)
    g = Game(m)

    while True:
        print m 
        if g.can_player_hear():
            print "ouyay ancay earhay a umpusway omingcay!!"
        d = wait_for_dir()
        try:
            g.player.move(d)
        except ValueError:
            print "ouyay an'tcay ogay atthay ayway!"

        if g.has_player_won():
            print "ouyay avehay onway. OOOWAY!"
            break
        g.move_wumpus()     

if __name__ == "__main__":
    main()
