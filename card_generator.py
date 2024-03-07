from PIL import Image, ImageDraw

class Card:
    background_dir: str = 'Background/'
    suit_dir: str = 'Suit/'
    rank_dir: str = 'Rank/'
    save_dir: str = 'Cards/'
    # bg_style -> '_accent' or '_accented_bg'
    def __init__(self, suit: tuple[str, str], rank: str, bg_style: str = '') -> None:
        self.rank_image: str = f"{self.rank_dir}{rank}_{suit[1]}.png"
        self.suit_image: str = f"{self.suit_dir}{suit[0]}.png"
        self.background_image: str = f"{self.background_dir}background_{suit[1]}{bg_style}.png"
        # NOTE 1 -> 10
        self.image_out_name: str = f"{self.save_dir}{rank[0].upper()}{suit[0][0].upper()}.png"
    def __str__(self) -> str:
        return f"{self.image_out_name}, {self.suit_image}, {self.rank_image}"
    def generate_card_image(self) -> None:
        offset_x: int = 4
        offset_y: int = 8
        # --------------------------
        card_img: Image = Image.open(self.background_image)
        suit_img_side: Image = Image.open(self.suit_image).convert("RGBA").resize((33, 33))
        suit_img_center: Image = Image.open(self.suit_image).convert("RGBA").resize((65*3, 65*3))
        rank_img: Image = Image.open(self.rank_image).convert("RGBA").resize((65, 65))
        # --------------------------
        card_w: int = card_img.size[0]
        card_h: int = card_img.size[1]
        rank_w: int = rank_img.size[0]
        rank_h: int = rank_img.size[1]
        suit_side_w: int = suit_img_side.size[0]
        suit_center_w: int = suit_img_center.size[0]
        suit_center_h: int = suit_img_center.size[1]
        # --------------------------
        card_img = card_img.rotate(180)
        card_img.paste(rank_img, (offset_x, offset_y), rank_img)
        card_img.paste(suit_img_side, (offset_x+(rank_w-suit_side_w)//2, offset_y+rank_h), suit_img_side)
        card_img = card_img.rotate(180)
        card_img.paste(rank_img, (offset_x, offset_y), rank_img)
        card_img.paste(suit_img_side, (offset_x+(rank_w-suit_side_w)//2, offset_y+rank_h), suit_img_side)
        card_img.paste(suit_img_center, (((card_w - suit_center_w) // 2, (card_h - suit_center_h) // 2)), suit_img_center)
        # --------------------------
        card_img.save(self.image_out_name)
        return
    
def generate_background(save_dir: str, save_name: str, border_color: str = 'black', fill_color: str = 'white', 
                        bg_w: int = 325, bg_h: int = 455, rad: int = 33, border_width: int = 4) -> None:
    bg = Image.new("RGBA", (bg_w, bg_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(bg)
    draw.rounded_rectangle((0, 0, bg_w, bg_h), fill=fill_color, outline=border_color, width=border_width, radius=rad)
    bg.save(f"{save_dir}{save_name}")

def main() -> None:
    print("Generating Backgrounds...")
    generate_background('Background/', 'background_red.png', border_color='#be2633')
    generate_background('Background/', 'background_black.png', border_color='#000000')
    generate_background('Background/', 'background_red_accent.png', border_color='#c89899')
    generate_background('Background/', 'background_black_accent.png', border_color='#9d9d9d')
    generate_background('Background/', 'background_red_accented_bg.png', border_color='#be2633', fill_color='#c89899')
    generate_background('Background/', 'background_black_accented_bg.png', border_color='#000000', fill_color='#9d9d9d')
    print("Background Generation Completed.")
    print("Generating Cards...")
    suits: list[tuple[str, str]] = [('spade', 'black'), ('club', 'black'), ('diamond', 'red'), ('heart', 'red')]
    ranks: list[str] = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
    cards: list[Card] = [Card(suit, rank)for rank in ranks for suit in suits ]
    for card in cards:
        card.generate_card_image()
        print(card.image_out_name, "Generated.")
    print("Card Generation Completed.")

if __name__ == '__main__':
    main()