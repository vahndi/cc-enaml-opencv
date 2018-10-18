from atom.atom import Atom
from atom.scalars import Str


class MainModel(Atom):

    message = Str()

    def __init__(self, message: str):

        self.message = message
