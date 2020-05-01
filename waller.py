import ctypes

PATH = 'D:\\GitHub\\wallpapers\\wallpapers\\wallpaper.jpg'
SPI_SETDESKWALLPAPER = 20


def change_bg(path):
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, PATH, 3)


change_bg(PATH)
