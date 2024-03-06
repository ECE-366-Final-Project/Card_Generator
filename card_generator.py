from PIL import Image

suits: list[tuple[str, str]] = [('spade', 'black'), ('club', 'black'), ('diamond', 'red'), ('heart', 'red')]
ranks: list[str] = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']

class Card:
    def __init__(self, suit: tuple[str, str], rank: str) -> None:
        self.rank_image = f"{rank}_{suit[1]}.png"
        self.suit_image = f"{suit[0]}.png"
        # NOTE 1 -> 10
        self.image_out_name = f"{rank[0].upper()}{suit[0][0].upper()}.png"
    def __str__(self) -> str:
        return f"{self.image_out_name}, {self.suit_image}, {self.rank_image}"
    def generate_card_image() -> Image:
        base = Image.open("Base/card_base.png")
        return





def main() -> None:
    cards = [Card(suit, rank) for suit in suits for rank in ranks]
    for card in cards:
        print(card)
    










if __name__ == '__main__':
    main()