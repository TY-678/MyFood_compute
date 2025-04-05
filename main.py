from PyQt5 import QtWidgets
from MyFood import MyApplication


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    my_app = MyApplication()
    my_app.show()
    sys.exit(app.exec_())
