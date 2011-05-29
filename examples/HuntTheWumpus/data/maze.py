from collections import namedtuple
Direction = namedtuple('Direction', ('rel', 'name', 'inv'))

DIRECTIONS = {
    'n': Direction((0, -1), 'North', 's'),
    's': Direction((0, 1), 'South', 'n'),
    'e': Direction((1, 0), 'East', 'w'),
    'w': Direction((-1, 0), 'West', 'e')
}


class Room(object):
    def __init__(self, maze, coord):
        self.maze = maze
        self.coord = coord
        for k in DIRECTIONS:
            setattr(self, k, None)
        self.contents = set()

    def rel(self, vec):
        dx, dy = vec
        x, y = self.coord
        c = (x + dx, y + dy)
        return self.maze[c]

    def cut(self, dir):
        """Cut a hole in the wall in this direction"""
        d = DIRECTIONS[dir]
        r = self.rel(d.rel)
        if isinstance(r, Wall):
            raise ValueError("Can't tunnel into a wall")
        setattr(self, dir, r)
        setattr(r, d.inv, self)

    def __str__(self):
        #FIXME: return representation of contents
        if len(self.contents) == 0:
            return ' '
        elif len(self.contents) > 1:
            return '@'
        else:
            c = list(self.contents).pop()
            return str(c)

    def enter(self, actor):
        self.contents.add(actor)

    def exit(self, actor):
        self.contents.remove(actor)


class Wall(Room):
    def __str__(self):
        return '#'


class Maze(object):
    def __init__(self, w=10, h=5):
        self.w = w
        self.h = h
        self.cells = []
        
        for j in range(h):
            for i in range(w):
                self.cells.append(Room(self, (i, j)))

    def __getitem__(self, pos):
    	x, y = pos
        if 0 <= x < self.w and 0 <= y < self.h:
            return self.cells[x + y * self.w]
        return Room(self, pos) # rooms start off disconnected

    def enumerate(self):
        for j in range(self.h):
            for i in range(self.w):
                c = (i, j)
                room = self[c]
                yield c, room

    def __str__(self):
        s = []
        FILLED = '#'
        BLANK = ' '
        for j in range(self.h):
            for i in range(self.w):
                c = (i, j)
                room = self[c]

            	s.append(FILLED)
            	s.append(BLANK if room.n else FILLED)
        
            s += [FILLED, '\n']

            for i in range(self.w):
                c = (i, j)
                room = self[c]

                s.append(BLANK if room.w else FILLED)
                s.append(str(room))

            s += [FILLED, '\n']

        s += [FILLED] * (self.w * 2 + 1)

        return ''.join(s)


if __name__ == '__main__':
    m = Maze()
    print m
