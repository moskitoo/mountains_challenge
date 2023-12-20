
import random

mountains = [
    {'left': 9, 'right': 15, 'height': 3},
    {'left': 8, 'right': 14, 'height': 3},
    {'left': 5, 'right':  9, 'height': 2},
    {'left': 0, 'right':  6, 'height': 3},
    {'left': 2, 'right': 12, 'height': 5},
    {'left': 5, 'right': 13, 'height': 4},
]

mountains = [
    {'left': 9, 'right': 15, 'height': 3},
    {'left': 8, 'right': 14, 'height': 3},
    {'left': 0, 'right':  6, 'height': 3},
]


def visible_area(mountains: list) -> float:

    def mnt_out(mnt_1: dict, mnt_2: dict):
        if mnt_1["right"] - mnt_2["left"] >= 2 * mnt_2["height"]:
            return False
        else:
            return True

    def area(mountain: dict) -> float:
        return mountain["height"] * mountain["height"]

    def intersection_area(mnt_1: dict, mnt_2: dict) -> float:
        a = mnt_1["right"] - mnt_2["left"]
        return a * a / 4

    sorted_mountains = sorted(
        mountains, key=lambda x: (x['left'], -x['height']))

    unique_mountains = {}
    for mnt_2 in sorted_mountains:
        left = mnt_2['left']
        if left not in unique_mountains or mnt_2['height'] > unique_mountains[left]['height']:
            unique_mountains[left] = mnt_2

    mnt_1 = {'left': 0, 'right': 0, 'height': 0}
    visible_area = 0
    mountains_preprocess = list(unique_mountains.values())

    for mnt_2 in mountains_preprocess:
        if mnt_2["left"] >= mnt_1["right"]:
            visible_area += area(mnt_1)
            mnt_1 = mnt_2
        elif mnt_out(mnt_1, mnt_2):
            visible_area += area(mnt_1) - intersection_area(mnt_1, mnt_2)
            mnt_1 = mnt_2
        else:
            pass

    last_area = area(mountains_preprocess[-1])
    visible_area += last_area
    return visible_area



def generate_mountains(n):
    """
    Generates a list of n mountains with random properties, 
    ensuring that right - left = 2 * height (45° slope).
    """
    mountains = []

    for _ in range(n):
        # Randomly select a height
        height = random.randint(1, 50000)

        # Ensure right - left = 2 * height
        left = random.randint(0, 100000 - 2 * height)
        right = left + 2 * height

        mountains.append({'left': left, 'right': right, 'height': height})

    return mountains

test_1 = generate_mountains(1000)

# result = visible_area(mountains)
# print(result)

test_result = visible_area(test_1)

print(test_result)
