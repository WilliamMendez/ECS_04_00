#!/usr/bin/python3
"""Función Main"""

import asyncio
from src.engine.game_engine import GameEngine

# pyinstaller --onefile --noconsole --icon=icon.ico main.py
# pygbag main.py

if __name__ == "__main__":
    engine = GameEngine()
    asyncio.run(engine.run())
