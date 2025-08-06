# test_game.py

import unittest
from SnakeGame  import Snake  # This will now work

class TestSnakeGame(unittest.TestCase):

    def setUp(self):
        self.snake = Snake()

    def test_initial_length(self):
        self.assertEqual(len(self.snake.body), 3)

    def test_move_forward(self):
        initial_head = self.snake.body[0]
        self.snake.move()
        new_head = self.snake.body[0]
        self.assertNotEqual(initial_head, new_head)

    def test_direction_change(self):
        self.snake.change_direction("DOWN")
        self.assertEqual(self.snake.direction, "DOWN")

if __name__ == '__main__':
    unittest.main()
