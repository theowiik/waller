import abc


class WallpaperSetter:
    @abc.abstractmethod
    def set_wallpaper(self, path) -> None:
        pass
