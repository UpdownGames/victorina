from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QButtonGroup)
app = QApplication([])
win = QWidget()
l = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox('варианты ответов')
b1 = QRadioButton('Энцы')
b2 = QRadioButton('Смурфы')
b3 = QRadioButton('Чулымцы')
b4 = QRadioButton('Алеуты')
but = QPushButton('ответить')
RadioGroup = QButtonGroup()
RadioGroup.addButton(b1)
RadioGroup.addButton(b2)
RadioGroup.addButton(b3)
RadioGroup.addButton(b4)

layH1 = QHBoxLayout()
layH2 = QHBoxLayout()
layH3 = QHBoxLayout()
laymann = QVBoxLayout()
layV1 = QVBoxLayout()
layV2 = QVBoxLayout()
layV1.addWidget(b1)
layV1.addWidget(b2)
layV2.addWidget(b3)
layV2.addWidget(b4)
layH1.addWidget(l)
layH2.addLayout(layV1)
layH2.addLayout(layV2)
layH3.addWidget(but)
RadioGroupBox.setLayout(layH2)
AnsGroupBox = QGroupBox('Результаты теста')
lb_res = QLabel('прав или нет?')
lb_cor = QLabel('ответ будет тут!')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_res, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_cor, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


layH2_2 = QHBoxLayout()
layH2_2.addWidget(RadioGroupBox)
layH2_2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
RadioGroupBox.show()
laymann.addLayout(layH1)
laymann.addLayout(layH2_2)
laymann.addLayout(layH3)
win.setLayout(laymann)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    but.setText('след. вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    but.setText('ответить')
    RadioGroup.setExclusive(False)
    b1.setChecked(False)
    b2.setChecked(False)
    b3.setChecked(False)
    b4.setChecked(False)
    RadioGroup.setExclusive(True)

def test():
    if 'ответить' == but.text():
        show_result()
    else:
        show_question()


ans = [b1, b2, b3, b4]
def ask(question, right_ans, wrong1, wrong2, wrong3):
    shuffle(ans)
    ans[0].setText(right_ans)
    ans[1].setText(wrong1)
    ans[2].setText(wrong2)
    ans[3].setText(wrong3)
    lb_Question.setText(question)
    lb_Correct.setText(right_ans)
    show_question()
def show_correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if ans[0].isChecked():
        show_correct("Правильно!")
    else:
        if ans[1].isChecked() and ans[2].isChecked() and ans[3].isChecked():
            show_correct('Не правильно!')

but.clicked.connect(check_answer)

win.show()
app.exec_()
