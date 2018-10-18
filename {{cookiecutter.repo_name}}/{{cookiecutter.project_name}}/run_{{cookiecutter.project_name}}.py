import enaml
from enaml.qt.qt_application import QtApplication


if __name__ == '__main__' and __package__ is None:

    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


if __name__ == '__main__':

    with enaml.imports():
        from main_view import MainView

    app = QtApplication()
    view = MainView()
    view.show()
    app.start()
