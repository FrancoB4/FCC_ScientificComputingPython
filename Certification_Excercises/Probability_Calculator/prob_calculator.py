import copy
import random


# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.params = kwargs
        self.contents = []
        for key, quantity in kwargs.items():
            for _ in range(quantity):
                self.contents.append(key)

    def draw(self, n_balls):
        if n_balls > len(self.contents):
            return self.contents

        draw_balls = []
        for i in range(n_balls):
            ball = random.choice(self.contents)
            draw_balls.append(ball)
            self.contents.pop(self.contents.index(ball))

        return draw_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for i in range(num_experiments):
        experimental_hat = copy.deepcopy(hat)
        expected = True
        balls_count = {}
        balls = experimental_hat.draw(num_balls_drawn)

        for ball in balls:
            if ball in balls_count.keys():
                balls_count[ball] += 1
            else:
                balls_count[ball] = 1

        for expected_ball, expected_amount in expected_balls.items():
            if expected_ball not in balls_count.keys():
                expected = False
                break
            else:
                if expected_amount > balls_count[expected_ball]:
                    expected = False
                    break

        if expected:
            m += 1

    return m / num_experiments
