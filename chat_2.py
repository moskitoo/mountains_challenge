mountains = [
    {'left': 9, 'right': 15, 'height': 3},
    {'left': 8, 'right': 14, 'height': 3},
    {'left': 0, 'right':  6, 'height': 3},
]

def visible_area(mountains: list) -> float:
    def calculate_area(mountain):
        return (mountain['right'] - mountain['left']) * mountain['height'] / 2

    # Sort mountains by left position and then height descending
    mountains.sort(key=lambda x: (x['left'], -x['height']))

    def update_active_mountains(mountain, active_mountains):
        updated_mountains = []
        for active in active_mountains:
            if active['right'] <= mountain['left']:
                # If the active mountain is completely to the left of the new mountain, keep it
                updated_mountains.append(active)
            elif active['left'] < mountain['left']:
                # If the active mountain overlaps with the new mountain, adjust its right
                active['right'] = mountain['left']
                updated_mountains.append(active)
        updated_mountains.append(mountain)
        return updated_mountains

    active_mountains = []
    total_visible_area = 0

    for mountain in mountains:
        total_visible_area += calculate_area(mountain)
        active_mountains = update_active_mountains(mountain, active_mountains)

        # Subtract the area of the parts that are not visible
        for i in range(len(active_mountains) - 1):
            overlap = min(active_mountains[i]['right'], active_mountains[-1]['right']) - active_mountains[-1]['left']
            if overlap > 0:
                total_visible_area -= overlap * active_mountains[-1]['height'] / 2

    return total_visible_area



print(visible_area(mountains))