import platform
import os
import random

from linux_wallpaper_setter import LinuxWallpaperSetter
from mac_os_wallpaper_setter import MacOSWallpaperSetter
from wallpaper_setter import WallpaperSetter
from windows_wallpaper_setter import WindowsWallpaperSetter

# The name of the wallpaper folder
WALLPAPER_FOLDER = 'wallpapers'


def get_random_local_image() -> str:
    """
    :returns the path to a random image locally.
    """
    images = os.listdir(WALLPAPER_FOLDER)
    image = random.choice(images)

    return os.path.abspath(WALLPAPER_FOLDER + '/' + image)


def get_wallpaper_setter() -> WallpaperSetter:
    system = platform.system()

    if system == 'Windows':
        return WindowsWallpaperSetter()
    elif system == 'Linux':
        return LinuxWallpaperSetter()
    elif system == 'Darwin':
        return MacOSWallpaperSetter()
    else:
        raise Exception('OS is not supported')


wallpaper_setter = get_wallpaper_setter()
wallpaper_setter.set_wallpaper(get_random_local_image())
