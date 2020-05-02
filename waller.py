import platform
import os
import random

# The name of the wallpaper folder
WALLPAPER_FOLDER = 'wallpapers'


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
