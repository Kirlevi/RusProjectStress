import sys
import csv
from random import choice
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QTableWidgetItem, QInputDialog
from MainUI import Ui_MainWindow as Ui_MainWindow
from SessionUI import Ui_MainWindow as Ui_Session
from ChallengeSessionUI import Ui_MainWindow as Ui_ChallengeSession
from StatisticsUI import Ui_MainWindow as Ui_Statistics


with open('mistakes.csv', encoding='windows-1251') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    mistakes = [(i[0], i[1]) for i in list(reader)]
mistakes = set(mistakes)


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start_training_btn.clicked.connect(self.open_session)
        self.work_on_mistakes_btn.clicked.connect(self.open_work_on_mistakes)
        self.game_mode_btn.clicked.connect(self.open_challenge_session)
        self.record_table_btn.clicked.connect(self.record_table)

    def open_session(self):
        self.session_form = SessionForm()
        self.session_form.show()

    def open_work_on_mistakes(self):
        self.work_on_mistakes = WorkOnMistakes()
        self.work_on_mistakes.show()

    def open_challenge_session(self):
        self.challenge_session_form = ChallengeSessionForm()
        self.challenge_session_form.show()

    def record_table(self):
        self.statistics_form = StatisticsForm()
        self.statistics_form.show()


class SessionForm(QMainWindow, Ui_Session):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.answer_btn.clicked.connect(self.true_or_false_counter)
        self.finish_btn.clicked.connect(self.finish)
        self.true_ans = 0
        self.false_ans = 0

        with open('stress.csv', encoding='windows-1251') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            self.words = [(i[0], i[1]) for i in reader]
        self.random_word_to_check()

    def random_word_to_check(self):  # Функция случайного взятия слов из таблицы
        if len(self.words) != 0:
            self.word = choice(self.words)
            self.question_lbl.setText(self.word[1])
        else:
            self.question_lbl.setText('Слова закончились :)')

    def true_or_false_counter(self):  # Проверка правильности введенного ответа
        self.error_lbl.clear()
        if self.answer_field.text() == '':
            self.error_lbl.setText('Введите Ваш ответ в поле!!!')
        elif self.answer_field.text() == self.word[0]:
            self.true_ans += 1
            self.words.pop(self.words.index(self.word))
            self.random_word_to_check()
            self.answer_field.clear()
        else:
            self.false_ans += 1
            mistakes.add(self.word)
            self.error_lbl.setText(f'Правильный ответ: {self.word[0]}')
            self.random_word_to_check()

        self.true_counter.setText(f'ВЕРНО: {self.true_ans}')
        self.false_counter.setText(f'НЕВЕРНО: {self.false_ans}')

    def finish(self):  # Заканчивает сессию и записывает ошибки в отдельный файл
        with open('mistakes.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for i in mistakes:
                writer.writerow(i)
        self.close()
        self.destroy()


class WorkOnMistakes(SessionForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.answer_btn.clicked.connect(self.true_or_false_counter)
        self.finish_btn.clicked.connect(self.finish)
        self.true_ans = 0
        self.false_ans = 0
        self.to_discard_from_mistakes = set()

        with open('mistakes.csv', encoding='windows-1251') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            self.words = [(i[0], i[1]) for i in reader]
        self.random_word_to_check()

    def true_or_false_counter(self):  # Проверка правильности введенного ответа
        self.error_lbl.clear()
        if self.answer_field.text() == '':
            self.error_lbl.setText('Введите Ваш ответ в поле!!!')
        elif self.answer_field.text() == self.word[0]:
            self.true_ans += 1
            self.words.pop(self.words.index(self.word))
            self.random_word_to_check()
            self.answer_field.clear()
        else:
            self.false_ans += 1
            self.error_lbl.setText(f'Правильный ответ: {self.word[0]}')
            self.random_word_to_check()

        self.true_counter.setText(f'ВЕРНО: {self.true_ans}')
        self.false_counter.setText(f'НЕВЕРНО: {self.false_ans}')

    def finish(self):  # Заканчивает сессию и записывает ошибки в отдельный файл
        for i in self.words:
            self.to_discard_from_mistakes.add(i)
        with open('mistakes.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for i in self.to_discard_from_mistakes:
                writer.writerow(i)
        self.close()
        self.destroy()


class ChallengeSessionForm(QMainWindow, Ui_ChallengeSession):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.answer_btn.clicked.connect(self.true_or_false_counter)
        self.finish_btn.clicked.connect(self.finish)
        self.score = 0
        self.attemptions = 3
        with open('stress.csv', encoding='windows-1251') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            self.words = [(i[0], i[1]) for i in reader]
        self.random_word_to_check()

    def random_word_to_check(self):
        if len(self.words) != 0:
            self.word = choice(self.words)
            self.question_lbl.setText(self.word[1])
        else:
            self.question_lbl.setText('Слова закончились :)')


    def true_or_false_counter(self):
        if self.answer_field.text() == self.word[0]:
            if self.attemptions > 0:
                self.score += 10
                self.score_lbl.setText(f'Количество очков: {self.score}')
                self.random_word_to_check()
                self.answer_field.clear()
        else:
            self.attemptions -= 1
            if self.attemptions == 2:
                self.heart_1.setPixmap(QPixmap('empty_heart.png'))
            elif self.attemptions == 1:
                self.heart_2.setPixmap(QPixmap('empty_heart.png'))
            else:
                self.heart_3.setPixmap(QPixmap('empty_heart.png'))
            self.random_word_to_check()

    def finish(self):
        i, okBtnPressed = QInputDialog.getText(self, "Введите ник",
                                               "Введите ник (только латиница)")
        if okBtnPressed:
            player = [i, self.score]
            with open('records.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=';', quotechar='"')
                writer.writerow(player)
        self.close()
        self.destroy()


class StatisticsForm(QMainWindow, Ui_Statistics):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadTable('records.csv')

    def loadTable(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            title = next(reader)
            self.record_table.setColumnCount(len(title))
            self.record_table.setHorizontalHeaderLabels(title)
            self.record_table.setRowCount(0)
            for i, row in enumerate(reader):
                self.record_table.setRowCount(self.record_table.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.record_table.setItem(i, j, QTableWidgetItem(elem))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainForm()
    ex.show()
    sys.exit(app.exec())