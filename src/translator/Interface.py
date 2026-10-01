import sys  # noqa: N999

from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QWidget

app = QApplication(sys.argv)
janela = QWidget()
janela.resize(500, 400)
janela.setWindowTitle("Tranlator")

btn = QPushButton("Origin", janela)
btn.setGeometry(100, 100, 80, 150)
btn.setStyleSheet("color:red")

btn = QPushButton("Origin", janela)
btn.setGeometry(120, 100, 100, 100)
btn.setStyleSheet("background-color:blue;color:white")

label = QLabel("Tranlator", janela)
label.move(400,100)

janela.show()
app.exec()
