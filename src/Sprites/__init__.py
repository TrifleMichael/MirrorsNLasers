from abc import ABC, abstractmethod


class Sprite(ABC):
    """Abstract class for all sprites. Forces child classes to implement draw."""
    @abstractmethod
    def draw(self, *args, **kwargs):
        pass
