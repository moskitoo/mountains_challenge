# mountains = [
#     {'left': 9, 'right': 15, 'height': 3},
#     {'left': 8, 'right': 14, 'height': 3},
#     {'left': 5, 'right':  9, 'height': 2},
#     {'left': 0, 'right':  6, 'height': 3},
#     {'left': 2, 'right': 12, 'height': 5},
#     {'left': 5, 'right': 13, 'height': 4},
# ]

mountains = [
    {'left': 9, 'right': 15, 'height': 3},
    {'left': 8, 'right': 14, 'height': 3},
    {'left': 0, 'right':  6, 'height': 3},
]


def area(mountain: dict) -> float:
        return mountain["height"] * mountain["height"]

def intersection_area(mnt_1: dict, mnt_2: dict) -> float:
        a = mnt_1["right"] - mnt_2["left"]
        return a * a / 4


def ret_area(m_1, m_2):
    mnt_1 = mountains[m_1 - 1]
    mnt_2 = mountains[m_2 - 1]
    area_1 = area(mnt_1)
    print(area_1)

    intersection = intersection_area(mnt_1, mnt_2)
    print(intersection)


    print(area_1 - intersection)

ret_area(2, 1)