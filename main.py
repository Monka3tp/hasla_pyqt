import sys

from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox

from layout import Ui_Dialog
import random

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.generujButton.clicked.connect(self.generuj_haslo)
        self.ui.zatwierdzButton.clicked.connect(self.zatwierdz)
        self.haslo = ""
        self.show()

    def generuj_haslo(self):
        try:
            dlugosc = int(self.ui.znakEdit.text())
            if dlugosc < 4:
                blad = QMessageBox()
                blad.setText("Hasło musi mieć przynajmniej 4 znaki")
                blad.exec()
                return
        except ValueError:
            blad = QMessageBox()
            blad.setText("Wprowadź poprawną liczbę znaków")
            blad.exec()
            return

        duze_litery = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O","P", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        male_litery = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t","u", "v", "w", "x", "y", "z"]
        cyfry = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        znaki_specjalne = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "="]
        znaki = male_litery
        haslo = []

        for i in range(dlugosc):
            if i == 0 and self.ui.literyBox.isChecked():
                haslo.append(random.choice(duze_litery))
                continue
            elif i == 1 and self.ui.cyfryBox.isChecked():
                haslo.append(random.choice(cyfry))
                continue
            elif i == 2 and self.ui.znakiSpecjalneBox.isChecked():
                haslo.append(random.choice(znaki_specjalne))
                continue
            else:
                haslo.append(random.choice(male_litery))


        self.haslo = "".join(haslo)
        informacja = QMessageBox()
        informacja.setText(f"{self.haslo}")
        informacja.exec()

    def zatwierdz(self):
        imie_pracownika = self.ui.imieEdit.text()
        nazwisko_pracownika = self.ui.nazwiskoEdit.text()
        stanowisko_pracownika = self.ui.stanowiskoBox.currentText()
        if not imie_pracownika:
            blad = QMessageBox()
            blad.setText("Wprowadź imię pracownika")
            blad.exec()
            return
        if not nazwisko_pracownika:
            blad = QMessageBox()
            blad.setText("Wprowadź nazwisko pracownika")
            blad.exec()
            return
        if not stanowisko_pracownika:
            blad = QMessageBox()
            blad.setText("Wprowadź stanowisko pracownika")
            blad.exec()
            return
        if not self.haslo:
            blad = QMessageBox()
            blad.setText("Wprowadź hasło")
            blad.exec()
            return
        else:
            informacja = QMessageBox()
            informacja.setText(f"Dane pracownika: {imie_pracownika} {nazwisko_pracownika} {stanowisko_pracownika} Hasło: {self.haslo}")
            informacja.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())