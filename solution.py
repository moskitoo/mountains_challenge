def visible_area(mountains: list[dict[str, int]]) -> float:
    RIGHT = 'right'
    LEFT = 'left'
    HEIGHT = 'height'

    unique_mountains = {}
    mnt_1 = {LEFT: 0, RIGHT: 0, HEIGHT: 0}
    visible_area = 0
    """

    """
    # POZAMIENIAC NAZWY ZMIENNYCH NA BARDZIEJ ZROZUMIALE
    # nazwa funkcji czynnosc lub czasownik
    def mnt_out(mountain_1: dict[str, int], mnt_2: dict[str, int]) -> bool:
        """
        """
        if mountain_1[RIGHT] - mnt_2[LEFT] >= 2 * mnt_2[HEIGHT]:
            # mountain(zrozumiale nazwy)
            return False
        else:
            return True

    def area(mountain: dict[str, int]) -> float:
        """
        """
        return mountain[HEIGHT] * mountain[HEIGHT]

    def intersection_area(mnt_1: dict[str, int], mnt_2: dict[str, int]) -> float:
        """
        """
        a = mnt_1[RIGHT] - mnt_2[LEFT]
        return a * a / 4

    sorted_mountains = sorted(
        mountains, key=lambda x: (x[LEFT], -x[HEIGHT]))

    # sortowanie do funkcji
    for mnt_2 in sorted_mountains:
        left = mnt_2[LEFT]
        if left not in unique_mountains or mnt_2[HEIGHT] > unique_mountains[left][HEIGHT]:
            unique_mountains[left] = mnt_2

    mountains_preprocessed = list(unique_mountains.values())

    # tez do funkcji
    for mnt_2 in mountains_preprocessed:
        if mnt_2["left"] >= mnt_1[RIGHT]:
            visible_area += area(mnt_1)
            mnt_1 = mnt_2
        elif mnt_out(mnt_1, mnt_2):
            visible_area += area(mnt_1) - intersection_area(mnt_1, mnt_2)
            mnt_1 = mnt_2

# tez do osobnej funkcji
    if len(mountains_preprocessed) != 0:
        visible_area += area(mountains_preprocessed[-1])

    return visible_area
