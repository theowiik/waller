import ctypes

from wallpaper_setter import WallpaperSetter


class WindowsWallpaperSetter(WallpaperSetter):
    # Windows constant for changing wallpapers
    WINDOWS_SPI_SET_WALLPAPER = 20

    def set_wallpaper(self, path) -> None:
        win64 = True
        if win64:
            ctypes.windll.user32.SystemParametersInfoW(self.WINDOWS_SPI_SET_WALLPAPER, 0, path, 3)
        else:
            ctypes.windll.user32.SystemParametersInfoA(self.WINDOWS_SPI_SET_WALLPAPER, 0, path, 3)
