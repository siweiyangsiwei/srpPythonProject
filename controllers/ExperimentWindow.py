import os.path

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QPushButton
from view.experiment import Ui_ExperimentWindow

from tools import SqlTools


class ExperimentWindow(QMainWindow, Ui_ExperimentWindow):
    # 记录当前正在学习的章节
    nowChapter = 1

    # 记录是否已经开始当前章节的学习
    startLearnOrNot = False

    # 记录当前显示的实验原理的图片
    nowPrincipleImg = 1

    # 记录当前显示的实验步骤的图片
    nowStepImg = 1

    # 记录当前正在回答的题目
    nowTestQuestion = 1

    # 保存当前章节的所有test题目
    questionList = []

    # 记录是否结束了测试
    answerList = []

    chapterNameList = ["第一章", "第二章", "第三章", "第四章", "第五章", "第六章", "第七章", "第八章", "第九章"]
    chapterBtnNameList = ["chapter_one", "chapter_two", "chapter_three", "chapter_four", "chapter_five", "chapter_six",
                          "chapter_seven", "chapter_eight", "chapter_nine"]

    def __init__(self):
        super(ExperimentWindow, self).__init__()
        self.setupUi(self)

        # 将所有test模块中的label设置为自动换行
        self.question.setWordWrap(True)
        self.section_A.setWordWrap(True)
        self.section_B.setWordWrap(True)
        self.section_C.setWordWrap(True)
        self.section_D.setWordWrap(True)

        # 点击实验原理下一页按钮触发next_principle_page_click事件
        self.next_principle_page.clicked.connect(self.next_principle_page_click)

        # 点击实验原理上一页按钮触发pre_principle_page_click事件
        self.pre_principle_page.clicked.connect(self.pre_principle_page_click)

        # 点击实验步骤下一页按钮触发next_steps_page_click事件
        self.next_steps_page.clicked.connect(self.next_steps_page_click)

        # 点击实验步骤上一页按钮触发pre_steps_page_click事件
        self.pre_steps_page.clicked.connect(self.pre_steps_page_click)

        # 点击test部分下一题触发next_test_question_click事件
        self.next_test_question.clicked.connect(self.next_test_question_click)

        # 点击test部分上一题触发pre_test_question_click事件
        self.pre_test_question.clicked.connect(self.pre_test_question_click)

        self.shutdown.clicked.connect(lambda: self.close())
        self.mini.clicked.connect(lambda: self.showMinimized())
        self.back.clicked.connect(self.back_main)

    # 章节改变的事件
    def chapter_click(self, num):

        self.nowChapter = num

        # 设置窗口的Title为当前章节名
        self.setWindowTitle(self.chapterNameList[num - 1])

        # 章节改变将当前实验原理和实验步骤图片恢复为1
        self.nowPrincipleImg = 1
        self.nowStepImg = 1

        # 显示当前章节的实验原理(默认只显示当前章节的第一张)
        self.set_principle_img(1)
        # 显示当前章节的实验步骤(默认只显示当前章节的第一张)
        self.set_steps_img(1)
        # 显示当前章节的test部分的题目(默认值显示当前章节的第一题)
        self.nowTestQuestion = 1
        self.get_test_question()
        self.set_test_question()
        # 清空test输入框的内容
        self.answer.setText("")
        # 清空回答
        self.answerList = []

    # 开始学习按钮的点击触发事件
    def start_learn(self):
        # 清空test部分的答题框
        self.answer.setText("")
        # 开放test部分的答题框
        self.answer.setEnabled(True)
        # 默认获取焦点
        self.answer.setFocus()
        self.nowTestQuestion = 1
        # 恢复下一题按钮的文字
        self.next_test_question.setText("下一题")

    # 结束学习按钮的点击触发事件
    def finish_learn(self):
        # TODO 这里需要设置一个确定是否结束学习的弹窗
        finish = True

    # 设置实验原理图片的函数
    def set_principle_img(self, index):
        self.principle_img.setText("")
        img = os.path.abspath(
            ('resources/Image/principle/chapter' + str(self.nowChapter) + '/principle' + str(index) + '.png'))
        image = QtGui.QPixmap(img).scaled(11182, 1182)
        self.principle_img.setScaledContents(True)
        self.principle_img.setPixmap(image)

    # 设置实验步骤的函数
    def set_steps_img(self, index):
        self.steps_img.setText("")
        img = os.path.abspath(
            ('resources/Image/steps/chapter' + str(self.nowChapter) + '/step' + str(index) + '.png'))
        image = QtGui.QPixmap(img).scaled(11182, 1182)
        self.steps_img.setScaledContents(True)
        self.steps_img.setPixmap(image)

    # 点击实验原理的下一页触发的事件
    def next_principle_page_click(self):
        # 当前页+1
        self.nowPrincipleImg += 1
        # 上一页按钮可用
        self.pre_principle_page.setEnabled(True)
        # 改变实验原理图片内容
        self.set_principle_img(self.nowPrincipleImg)
        # 判断是否为最后一页
        principle_img_num = os.listdir('resources/Image/principle/chapter' + str(self.nowChapter))
        if self.nowPrincipleImg >= len(principle_img_num):
            self.next_principle_page.setEnabled(False)

    # 点击实验原理的上一页触发的事件
    def pre_principle_page_click(self):
        # 当前页-1
        self.nowPrincipleImg -= 1
        # 下一页按钮可用
        self.next_principle_page.setEnabled(True)
        # 改变实验原理图片内容
        self.set_principle_img(self.nowPrincipleImg)
        # 判断是否为第一页
        if self.nowPrincipleImg <= 1:
            self.pre_principle_page.setEnabled(False)

    # 点击实验步骤的下一页触发的事件(实现同实验原理)
    def next_steps_page_click(self):
        self.nowStepImg += 1
        self.pre_steps_page.setEnabled(True)
        self.set_steps_img(self.nowStepImg)
        steps_img_num = os.listdir('resources/Image/steps/chapter' + str(self.nowChapter))
        if self.nowStepImg >= len(steps_img_num):
            self.next_steps_page.setEnabled(False)

    # 点击实验的步骤上一页触发的事件(实现同实验原理)
    def pre_steps_page_click(self):
        self.nowStepImg -= 1
        self.next_steps_page.setEnabled(True)
        self.set_steps_img(self.nowStepImg)
        if self.nowStepImg <= 1:
            self.pre_steps_page.setEnabled(False)

    # 点击test部分下一题触发的事件
    def next_test_question_click(self):
        # 判断是否已经填入答案
        if self.answer.text() == "":
            print("请先填写答案再进入下一题")
            return
        # 判断是否为结束测试按钮
        if self.nowTestQuestion >= len(self.questionList):
            # 将答案保存到answerList中
            self.answerList.append(self.answer.text().upper())
            # 调用答题结束的函数
            self.finish_test()
            # 禁用上一题和下一题按钮
            self.next_test_question.setEnabled(False)
            self.pre_test_question.setEnabled(False)
        else:
            # 保存答案(先判断该题是否填过,填过则更新答案,没填过则加入)
            if self.nowTestQuestion > len(self.answerList):
                self.answerList.append(self.answer.text().upper())
            else:
                self.answerList[self.nowTestQuestion - 1] = self.answer.text().upper()
            self.nowTestQuestion += 1
            # 判断是否已经填过答案
            if self.nowTestQuestion <= len(self.answerList):
                self.answer.setText(self.answerList[self.nowTestQuestion - 1])
            else:
                # 清空输入框
                self.answer.setText("")
            # 输入框自动获取焦点
            self.answer.setFocus()
            self.pre_test_question.setEnabled(True)
            self.set_test_question()
            # 判断是否为最后一题
            if self.nowTestQuestion >= len(self.questionList):
                self.next_test_question.setText("结束测试")

    # 点击test部分上一题触发的事件
    def pre_test_question_click(self):
        self.nowTestQuestion -= 1
        self.next_test_question.setEnabled(True)
        self.set_test_question()
        # 点击了上一题那么上一题一定填入了答案,需要取出对应答案并填入输入框中
        self.answer.setText(self.answerList[self.nowTestQuestion - 1])
        # 判断是否为第一题
        if self.nowTestQuestion <= 1:
            self.pre_test_question.setEnabled(False)
            self.next_test_question.setText("下一题")

    # 获取test部分的题目
    def get_test_question(self):
        self.questionList = SqlTools.get_question_by_chapter(self.chapterBtnNameList[self.nowChapter - 1])

    # 设置test部分的题目
    def set_test_question(self):
        question = self.questionList[self.nowTestQuestion - 1]
        section_a = ""
        section_b = ""
        section_c = ""
        section_d = ""
        if question[3] != "":
            section_a = "A." + question[3]
            section_b = "B." + question[4]
            section_c = "C." + question[5]
            section_d = "D." + question[6]
        self.question.setText(question[1])
        self.section_A.setText(section_a)
        self.section_B.setText(section_b)
        self.section_C.setText(section_c)
        self.section_D.setText(section_d)

    # 答题结束的函数
    def finish_test(self):
        print("你的答案是: " + str(self.answerList))
        print("正确答案是: " + str(
            SqlTools.get_correct_answer_by_chapter(self.chapterBtnNameList[self.nowChapter - 1])))
        print("答题结束")

    # 接收主窗口，下面用于返回主窗口
    def receive_main(self, mainWindow):
        self.mainWindow = mainWindow

    # 返回主界面
    def back_main(self):
        self.mainWindow.show()
        self.close()