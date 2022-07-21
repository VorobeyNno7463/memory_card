from  PyQt5.QtCore import Qt
from  PyQt5.QtWidgets import (QApplication, QWidget, QBoxLayout, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1 
        self.wrong2 = wrong2 
        self.wrong3 = wrong3


question_list = []
question_list.append(Question('Какого цвета нету на фалге России?', 'Зеленый', "Белый", 'Красный','Синий'))
question_list.append(Question('Какой государственый язык Бразилии?',"Португальский","Бразильский",'Английский', 'Итальянский'))
#написат 10 вопрос

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory card')

btn_ok = QPushButton('Ответить')
question = QLabel('Вопрос?')
rtbn_1  = QRadioButton('1')
rtbn_2  = QRadioButton('2')
rtbn_3  = QRadioButton('3')
rtbn_4  = QRadioButton('4')

layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()

RadioGroup = QButtonGroup()
RadioGroup.addButton(rtbn_1)
RadioGroup.addButton(rtbn_2)
RadioGroup.addButton(rtbn_3)
RadioGroup.addButton(rtbn_4)




layout2.addWidget(rtbn_1)
layout2.addWidget(rtbn_2)
layout3.addWidget(rtbn_3)
layout3.addWidget(rtbn_4)

layout1.addLayout(layout2)
layout1.addLayout(layout3)
RadioGroupBox = QGroupBox('Варианты ответов')
RadioGroupBox.setLayout(layout1)


AnsGroupBox = QGroupBox('Результат теста')
result = QLabel("правильно/не правильно")
correct = QLabel('Ответ тут')

layout_res = QVBoxLayout()
layout_res.addWidget(result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(correct, alignment = Qt.AlignCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)






layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()




layout_line1.addWidget(question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch = 2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.addSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rtbn_1.setChecked(False)
    rtbn_2.setChecked(False)
    rtbn_3.setChecked(False)
    rtbn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rtbn_1, rtbn_2, rtbn_3, rtbn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    correct.setText(q.right_answer)
    show_question()


def show_correct(res):
    result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score  += 1
        print('Статистика\n-Всего вопросов:', window.total, '\n-Правильных ответов:', window.score)
        print('Рейтинг:', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг:', (window.score/window.total*100), '%')

def next_question():
    window.total  += 1
    print('Статистика\n-Всего вопросов:', window.total, '\n-Правильных ответов:', window.score)
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)


def click_ok():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.setLayout(layout_card)
btn_ok.clicked.connect(click_ok)
window.score = 0
window.total = 0
next_question()
window.show()
app.exec_()

