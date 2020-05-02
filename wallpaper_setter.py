import abc


class WallpaperSetter(abs.ABC):
    @abc.abstractmethod
    def set_wallpaper(self, path) -> None:
        pass
