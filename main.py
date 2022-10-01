# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


import os
from PIL import Image

from dataclasses import dataclass

ROOT_PATH = './data/jpg/'


@dataclass
class Flower:
    """Flower metadate"""
    name: str
    width: int
    height: int

    def get_full_path(self) -> str:
        return os.path.join(ROOT_PATH, self.name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    filenames = os.listdir(ROOT_PATH)
    print(filenames[:5])

    flowers = []
    for file in filenames[:5]:
        path = os.path.join(ROOT_PATH, file)
        with Image.open(path) as img:
            width, height = img.width, img.height
            meta = Flower(file, width, height)
            flowers.append(meta)

    print(len(flowers))
    print(flowers[0])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
