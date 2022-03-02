"""
This module is for reading and writing json.

Written by: AlphaBeta906
Use: Utils

3/2/2022
"""

import json
import os

class JSONLoader:
    def __init__(self, file) -> None:
        self.file = f"{os.getcwd()}/{file}"

    def read(self) -> dict:
        try:
            with open(self.file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            with open(self.file, 'x') as f:
                json.dump({}, f, indent=4)
            return {}

    def write(self, data: dict) -> None:
        try:
            with open(self.file, 'w') as f:
                json.dump(data, f, indent=4)
        except FileNotFoundError:
            with open(self.file, 'x') as f:
                json.dump(data, f, indent=4)