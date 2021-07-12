"""
    Caculate Bowling Game
"""


class BowlingGame(object):

    def __init__(self, game_rolls):
        self.game_rolls = game_rolls

    def validate_data(self):  # Checking Input Data
        if len(self.game_rolls) == 10:  # Must Have Rolls Of 10 Frames
            for index, frame_rolls in enumerate(self.game_rolls):
                if type(frame_rolls) is tuple and len(frame_rolls) != 0:
                    if index != 9:  # (a, b), (a,)
                        if len(frame_rolls) <= 2:
                            if self.is_strike(frame_rolls) and len(frame_rolls) == 2:  # (10, )
                                raise Exception(f"This {frame_rolls} Is Strike, Frame Roll Only One Pins!")
                            elif not self.is_strike(frame_rolls) and len(frame_rolls) == 1:  # (3, 5) (Wrong: (3, ))
                                raise Exception(f"This {frame_rolls} Missing Roll!")
                            elif sum(frame_rolls) > 10:
                                raise Exception(f"This {frame_rolls} Total Pins Over Than 10!")
                        else:
                            raise Exception(f"This {frame_rolls} Over Than 2 Rolls")
                    else:
                        if 1 < len(frame_rolls) <= 3:
                            if self.is_strike(frame_rolls) or self.is_spare(frame_rolls):
                                if len(frame_rolls) < 3:
                                    raise Exception(f"This {frame_rolls} Missing Roll!")
                                else:
                                    for roll in frame_rolls:
                                        if roll > 10:
                                            raise Exception(f"This {roll} In {frame_rolls} Total Pins Over Than 10!")
                        else:
                            raise Exception(f"Please Checking This {frame_rolls} Again!")
                else:
                    raise Exception(f"This {frame_rolls} is Missing Data!")
        else:
            raise Exception(f"Missing Frame Or Over Frame! Please Checking Your Input!")

        return True

    def total_score(self):
        total_score = 0
        if self.validate_data():
            for index, frame_rolls in enumerate(self.game_rolls):
                if index != 9:
                    if self.is_strike(frame_rolls):
                        if self.is_strike(self.game_rolls[index + 1]):
                            if index != 8:
                                total_score += frame_rolls[0] + self.game_rolls[index + 1][0] + \
                                               self.game_rolls[index + 2][0]
                            else:
                                total_score += frame_rolls[0] + self.game_rolls[index + 1][0] + \
                                               self.game_rolls[index + 1][1]
                        else:
                            total_score += frame_rolls[0] + self.game_rolls[index + 1][0] + self.game_rolls[index + 1][1]
                    elif self.is_spare(frame_rolls):
                        total_score += sum(frame_rolls) + self.game_rolls[index + 1][0]
                    else:
                        total_score += sum(frame_rolls)
                else:
                    total_score += sum(frame_rolls)
        print(f"Total Score: {total_score}")
        return total_score

    # Checking Frame Is Spare.
    def is_spare(self, roll_pins):
        return roll_pins[0] + roll_pins[1] == 10

    # Checking Frame Is Strike.
    def is_strike(self, roll_pins):
        return roll_pins[0] == 10


if __name__ == '__main__':
    test_cases = [
        [(10,), (3, 7), (4, 4), (5, 4), (5, 4), (6, 4), (4, 4), (5, 5), (0, 10), (10, 10, 10)],
        [(4, 4), (4, 4), (4, 4), (4, 4), (4, 4), (4, 4), (4, 4), (4, 4), (4, 4), (4, 4)],
        [(10,), (10,), (10,), (10,), (10,), (10,), (10,), (10,), (10,), (10, 10, 10)],
        [(10,), (10,), (10,), (10,), (10,), (10,), (10,), (10,), (10,), (10, 4, 6)],
        [(10,), (10,), (10,), (10,), (10,), (10,), (10,), (10,), (10,), (6, 4, 5)],
        [(10,), (10,), (10,), (10,), (10,), (10,), (10,), (10,), (10,), (4, 4)],
        [(5, 3), (4, 4), (2, 1), (3, 2), (4, 3), (1, 1), (0, 0), (0, 0), (1, 1), (0, 4)],
        [(5, 3), (4, 4), (2, 1), (3, 2), (4, 3), (1, 1), (0, 0), (0, 0), (1, 1), (0, 4)],
        [(5, 5), (4, 6), (2, 8), (3, 7), (7, 3), (1, 9), (0, 10), (8, 2), (1, 9), (9, 1, 10)],
        [(10, ), (4, 6), (2, 3), (3, 7), (10, ), (1, 9), (3, 5), (8, 2), (1, 9), (9, 1, 10)],
        [(1, 4), (4, 5), (6, 4), (5, 5), (10,), (0, 1), (7, 3), (6, 4), (10, ), (2, 8, 6)],
    ]
    for index, data in enumerate(test_cases):
        print(f"Test Case {index + 1}")
        game = BowlingGame(data)
        game.total_score()
