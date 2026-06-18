"""Textual terminal UI for Pico."""

__all__ = ["PicoTuiApp"]


def __getattr__(name):
    if name == "PicoTuiApp":
        from .app import PicoTuiApp

        return PicoTuiApp
    raise AttributeError(name)
