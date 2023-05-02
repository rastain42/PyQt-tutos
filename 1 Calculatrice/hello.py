import sys

# 1. Import de la QApplication et de tous les widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# 2. Création d'une instance
app = QApplication([])

# 3. Creation de l'application GUI
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60, 15)

# 4. Affichage de l'application
window.show()

# 5. Lancer l'application
sys.exit(app.exec())
