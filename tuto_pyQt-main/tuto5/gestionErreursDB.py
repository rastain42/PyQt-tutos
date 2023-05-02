import sys

from PyQt6.QtSql import QSqlDatabase
from PyQt6.QtWidgets import QApplication, QMessageBox, QLabel

# Création de la connexion
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("/home/contacts.sqlite")

# Création de l'application
app = QApplication(sys.argv)

# Gestion des erreurs
if not con.open():
    QMessageBox.critical(
        None,
        "App Name - Error!",
        "Database Error: %s" % con.lastError().databaseText(),
    )
    sys.exit(1)

# Create the application's window
win = QLabel("Connection Successfully Opened!")
win.setWindowTitle("App Name")
win.resize(200, 100)
win.show()

sys.exit(app.exec_())
