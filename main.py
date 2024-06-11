from PySide6.QtWidgets import QApplication
from charts import ChartyApp
import sys

app = QApplication(sys.argv)

window = ChartyApp()

window.show()
app.exec()
