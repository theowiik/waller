import ctypes
import platform

PATH = 'D:\\GitHub\\wallpapers\\wallpapers\\wallpaper.jpg'
SPI_SETDESKWALLPAPER = 20


def change_bg(path):
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, PATH, 3)


os = platform.system()

if os == 'Windows':
    print('Windows')
elif os == 'Darwin':
    print('MacOS')
elif os == 'Linux':
    print('Linux')
else:
    print('OS not supported')

change_bg(PATH)
