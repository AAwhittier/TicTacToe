from dataclasses import dataclass


@dataclass
class Player:
    token = ""

    def __init__(self, token):
        self.token = token
