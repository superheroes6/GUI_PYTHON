from modelo import AppContador
import sys
from PyQt6.QtWidgets import QApplication



if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = AppContador()
    w.show()

    sys.exit(app.exec())