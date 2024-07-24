def visible_area(mountains: list[dict[str, int]]) -> float:
    """
    Calculate the total visible area of a set of mountains.

    Each mountain is represented as a dictionary with keys 'left', 'right', and 'height',
    indicating the horizontal position and height of the mountain.

    Args:
        mountains (list[dict[str, int]]): A list of mountains, each represented as a dictionary.

    Returns:
        float: The total visible area of the mountains.

    Note:
        - Overlapping mountains will have their visible area calculated accordingly.
    """

    RIGHT = 'right'
    LEFT = 'left'
    HEIGHT = 'height'

    def is_mountain_not_fully_overlapped(mountain_to_compare: dict[str, int], current_mountain: dict[str, int]) -> bool:
        """
        Determine if a mountain should be considered for visible area calculation when compared to another mountain.

        Args:
            mountain_to_compare (dict[str, int]): The next mountain to compare with.
            current_mountain (dict[str, int]): The current mountain under consideration. 

        Returns:
            bool: True if mountain_2 overlaps significantly with mountain_1 and should be considered in the area calculation; False otherwise.

        Explanation:
            The function checks if the distance between the mountains is less than twice the height of the second mountain. 
            If the peak of the second mountain is at or below the edge of the first mountain, then the area of the second mountain overlaps with or is encompassed by the area of the first mountain.
        """
        if mountain_to_compare[RIGHT] - current_mountain[LEFT] >= 2 * current_mountain[HEIGHT]:
            return False
        else:
            return True

    def calculate_area(mountain: dict[str, int]) -> float:
        """
        Calculate the area of a mountain based on its height.

        Args:
            mountain (dict[str, int]): A mountain represented as a dictionary.

        Returns:
            float: The calculated area of the mountain.
        """
        return mountain[HEIGHT] * mountain[HEIGHT]

    def calculate_intersection_area(left_mountain: dict[str, int], right_mountain: dict[str, int]) -> float:
        """
        Calculate the intersection area between two mountains.

        Args:
            left_mountain (dict[str, int]): Mountain on the left.
            right_mountain (dict[str, int]): Mountain on the right.

        Returns:
            float: The area of overlap between the two mountains.

        Note:
            This function assumes that the mountains are overlapping.
        """
        mountain_base_width = left_mountain[RIGHT] - right_mountain[LEFT]
        return mountain_base_width * mountain_base_width / 4

    def get_unique_mountains(sorted_mountains: list[dict[str, int]]) -> list[dict[str, int]]:
        """
        Preprocess the mountains list to ensure only the highest mountain at each x position 
        of their bottom-left corner is retained.

        Args:
            sorted_mountains (list[dict[str, int]]): A mountain list sorted in ascending order 
            of the x position of their bottom-left corner and descending order of height values.

        Returns:
            list[dict[str, int]]: A processed list of mountains, with only the highest mountain 
            retained for each unique x position of their bottom-left corner.

        Explanation:
            The function ensures that for each x position of the bottom-left corner, only the highest mountain is considered for the visible area calculation. 
            This is because the area of any smaller mountain at the same x position is overshadowed by or included within the area of the higher mountain.
        """

        unique_mountains = {}

        for mountain in sorted_mountains:
            left_value = mountain[LEFT]
            if left_value not in unique_mountains or mountain[HEIGHT] > unique_mountains[left_value][HEIGHT]:
                unique_mountains[left_value] = mountain

        return list(unique_mountains.values())

    def calculate_visible_area(unique_mountains: list[dict[str, int]]) -> float:
        """
        Calculate visible area of mountains in a given landscape.

        Args:
            unique_mountains (list[dict[str, int]]): A list of mountains, each represented as a dictionary,
        with only the highest mountain retained for each unique x position of their bottom-left corner.  

        Returns:
            float: The total visible area of the mountains in the list.

        Explanation:
            The function iterates through the list of unique mountains, starting from the mountain with the lowest x-axis value.
            For each mountain, it checks if there is an overlap with the previously considered mountain ('mountain_to_compare').
            If there is no overlap, the entire area of 'mountain_to_compare' is added to the visible area. 
            If there is an overlap, the function calculates and adds the visible portion of 'mountain_to_compare' to the total area.
            After each comparison, 'mountain_to_compare' is updated to the current mountain for subsequent comparisons.
        """
        visible_area = 0
        mountain_to_compare = {LEFT: 0, RIGHT: 0, HEIGHT: 0}

        for current_mountain in unique_mountains:
            if current_mountain[LEFT] >= mountain_to_compare[RIGHT]:
                visible_area += calculate_area(mountain_to_compare)
                mountain_to_compare = current_mountain
            elif is_mountain_not_fully_overlapped(mountain_to_compare, current_mountain):
                visible_area += calculate_area(mountain_to_compare) - calculate_intersection_area(
                    mountain_to_compare, current_mountain)
                mountain_to_compare = current_mountain

        visible_area += calculate_area(mountain_to_compare)
        return visible_area

    sorted_mountains = sorted(mountains, key=lambda x: (x[LEFT], -x[HEIGHT]))

    unique_mountains = get_unique_mountains(sorted_mountains)

    return calculate_visible_area(unique_mountains)
