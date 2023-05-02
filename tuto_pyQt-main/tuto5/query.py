import sys

from PyQt6.QtSql import QSqlDatabase, QSqlQuery

# Creation de la connexion
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("contacts.sqlite")

# Ouverture de la connexion
if not con.open():
    print("Database Error: %s" % con.lastError().databaseText())
    sys.exit(1)

# Créez une requête et exécutez-la immédiatement en utilisant .exec()
createTableQuery = QSqlQuery()
createTableQuery.exec(
    """
    CREATE TABLE contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name VARCHAR(40) NOT NULL,
        job VARCHAR(50),
        email VARCHAR(40) NOT NULL
    )
    """
)

# Création d'une requête pour une exécution ultérieure à l'aide de .prepare()
insertDataQuery = QSqlQuery()
insertDataQuery.prepare(

    """
    INSERT INTO contacts (
        name,
        job,
        email
    )
    VALUES (?, ?, ?)
    """
)

# Data
data = [
    ("Joe", "Senior Web Developer", "joe@example.com"),
    ("Lara", "Project Manager", "lara@example.com"),
    ("David", "Data Analyst", "david@example.com"),
    ("Jane", "Senior Python Developer", "jane@example.com"),
]

# Utilisez .addBindValue() pour insérer des données
for name, job, email in data:
    insertDataQuery.addBindValue(name)
    insertDataQuery.addBindValue(job)
    insertDataQuery.addBindValue(email)
    insertDataQuery.exec()

print(con.tables())
