# Author: Rehjii Martin
# GitHub username: Rehjii-Martin
# Date: 03/06/2024
# Description: a program that calculates line segments

class Point:
    """

    Represents point in 2D space on x / y coordinate.

    """
    def __init__(self, x_coord, y_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord
    def get_x_coord(self):
        return self._x_coord
    def get_y_coord(self):
        return self._y_coord
    def distance_to(self, other):
        # Calculate Euclidean distance to other point using the distance formula
        return ((other.get_x_coord() - self._x_coord) ** 2 +
                (other.get_y_coord() - self._y_coord) ** 2) ** 0.5
class LineSegment:

    """

    Represents line segment in 2D space defined by two endpoints.

    """
    def __init__(self, endpoint_1, endpoint_2):
        self._endpoint_1 = endpoint_1 # Initializes endpoint1
        self._endpoint_2 = endpoint_2 # Initializes endpoint2
    def get_endpoint_1(self):
        return self._endpoint_1
    def get_endpoint_2(self):
        return self._endpoint_2

    def length(self):
        # Use class Point's distance_to getter method to calculate length of line segment
        return self._endpoint_1.distance_to(self._endpoint_2)

    def slope(self):
        # Check if the line segment has identical endpoints
        if (self._endpoint_1.get_x_coord() == self._endpoint_2.get_x_coord()
                and self._endpoint_1.get_y_coord() == self._endpoint_2.get_y_coord()):

            return None  # Identical endpoints mean no slope

        # Check for a vertical line segment
        if self._endpoint_1.get_x_coord() == self._endpoint_2.get_x_coord():
            return None  # Vertical line segment has no slope

        # Calculate slope for non-vertical, non-identical endpoints
        x1, y1 = self._endpoint_1.get_x_coord(), self._endpoint_1.get_y_coord()
        x2, y2 = self._endpoint_2.get_x_coord(), self._endpoint_2.get_y_coord()
        return (y2 - y1) / (x2 - x1)

    def is_parallel_to(self, other):
        # Check for zero-length segments
        if self.length() == 0 or other.length() == 0:
            return False # Zero length segments aren't parallel to anything

        # Check parallelism for non-zero length segments
        slope_self = self.slope()
        slope_other = other.slope()

        # Check for parallelism in vertical line segments
        if slope_self is None and slope_other is None:
            return True  # Both segments are vertical and hence parallel

        # Check for parallelism with non-vertical line segments
        return slope_self is not None and slope_other is not None and abs(slope_self - slope_other) < 0.000001


# Test with zero-length segments and parallelism check
# point_1 = Point(1, 1)
# point_2 = Point(1, 1)
# line_seg_1 = LineSegment(point_1, point_2)

# point_3 = Point(1, 1)
# point_4 = Point(1, 1)
# line_seg_2 = LineSegment(point_3, point_4)

# Test if two zero-length line segments are considered parallel
# line_seg_1.is_parallel_to(line_seg_2)

# Print the result of checking if two zero-length line segments are considered parallel
# print("Are line_seg_1 and line_seg_2 parallel:", line_seg_1.is_parallel_to(line_seg_2))