from utils.decocators import calculate_time


@calculate_time
def locate_card_liner_search(cards, query):
    position = 0
    while True:
        print(f"position: {position}")
        if not cards:
            return -1
        if cards[position] == query:
            return position
        position += 1
        if position == len(cards):
            return -1
