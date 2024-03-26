class SquareGenerator:
    def generate_squares(self, start, end):
        if start > end:
            raise ValueError('End value must be greater than or equal to start value')
        return [x ** 2 for x in range(start, end)]


class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):
        if start > end:
            raise ValueError('End value must be greater than or equal to start value')
        return [x ** 3 for x in range(start)]
