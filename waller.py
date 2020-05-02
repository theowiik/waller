import ctypes
import platform
import os
import random

# Windows constant for changing wallpapers
WINDOWS_SPI_SET_WALLPAPER = 20

# The name of the wallpaper folder
WALLPAPER_FOLDER = 'wallpapers'


def change_bg(path: str) -> None:
    ctypes.windll.user32.SystemParametersInfoW(WINDOWS_SPI_SET_WALLPAPER, 0, path, 3)


def get_random_local_image() -> str:
    """
    :returns the path to a random image locally.
    """
    images = os.listdir(WALLPAPER_FOLDER)
    image = random.choice(images)

    return os.path.abspath(WALLPAPER_FOLDER + '/' + image)


system = platform.system()

if system == 'Windows':
    print('Windows')
elif system == 'Darwin':
    print('MacOS')
elif system == 'Linux':
    print('Linux')
else:
    print('OS not supported')

change_bg(get_random_local_image())
