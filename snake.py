from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Creates our 3-segment snake and puts it on screen next to each other it has,
    square shape, white color, puts pen up"""

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the original three squares on the starting positions next to each other"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """add a new segment to the snake"""
        self.add_segment(self.segments[-1].position())

    def reset(self):
        """sends the segments of the current snake in the list off-screen then clears the segment list
        of previous items, then creates a new snake in the middle of the screen and sets the first segment
        as the head of the snake"""
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        """moves the snake forward continuosly and make the rest of the body follow the head"""
        # we move the last segment to second to last make a loop for it. the range is
        # start = length of a segment list, stop is 0 and not included that is 1st seg in our seg list.
        # and the step is -1 we are moving backwards in range
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # new x nad y is the position of the second to last in range, and we
            # get its x and y coordinates
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # we want the last segment in the list to move to the position of the previous one.
            # so we find the position of the previous one first
            self.segments[seg_num].goto(x=new_x, y=new_y)
        # and we move the head of the snake seg 0 and all the other ones follow
        # to its previous position down the chaine
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """turns snake head (segment[0]) and turns it to 90 degree direct"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """turns snake head (segment[0]) and turns it to 270 degree direct"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """turns snake head (segment[0]) and turns it to 180 degree direct"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """turns snake head (segment[0]) and turns it to 0 degree direct"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)