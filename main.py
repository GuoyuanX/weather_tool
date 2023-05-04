import sys

from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox

from mainwindow import Ui_MainWindow
from input_key import Ui_Form

import weath
import config

def ico_rul(name):
    ic_url = "image: url(:/pics/3d_180/" + str(name) + ".png);"
    return ic_url


class MyForm(QWidget, Ui_Form):
    def __init__(self):
        super(MyForm, self).__init__()
        # global  u1
        self.setupUi(self)
        # 读取key
        self.key_lineEdit.setText(config.read_json_config_private_key())

    def setkey(self):
        config.set_json_config_private_key(self.key_lineEdit.text())
        print("ok")


class MyWindow(QMainWindow, Ui_MainWindow):
    ms = 0

    def __init__(self):
        # QMainWindow.__init__(self)
        super(MyWindow, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("-天气获取工具 v3 maker: 拾贰-")
        #self.get_weath_action.triggered.connect(self.get_slot)
        self.set_key_action.triggered.connect(self.set_key_slot)
        self.about_action.triggered.connect(self.about_slot)
        self.exit_action.triggered.connect(self.exit_app)

        self.lineEdit_area.setPlaceholderText("~在此输入城市~")

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.showTime)

        config.read_json()
        # 设置json里的城市
        self.lineEdit_area.setText(config.read_json_config_city())
        self.get_slot()

    def get_slot(self):
        area = self.lineEdit_area.text()

        weathdata_code = weath.get_weather(area)
        if weathdata_code == 0:
            QMessageBox.information(self, "失败" , "设置失败，可能输入的城市不在该列表中😥")
            return
        #QMessageBox.information(self, "提示", "设置成功😁")

        # 写入json
        config.set_json_config_city(area)

        dic = weath.get_all_weath_dic()

        ins = ""
        ins = dic["last_update"]
        ina = ins.index('+')

        print(ins[:ina])
        self.city_lable.setText(dic["location"] + "·" + "发布于:" + ins[:ina])


        self.ico_label_0.setStyleSheet(ico_rul(dic['code_day_0']))
        self.ico_label_1.setStyleSheet(ico_rul(dic['code_day_1']))
        self.ico_label_2.setStyleSheet(ico_rul(dic['code_day_2']))

        self.day_label_0.setText(dic['text_day_0'])
        self.day_label_1.setText(dic['text_day_1'])
        self.day_label_2.setText(dic['text_day_2'])

        temp_0 = dic['high_0'] + "℃" + "/" + dic['low_0'] + "℃"
        temp_1 = dic['high_1'] + "℃" + "/" + dic['low_1'] + "℃"
        temp_2 = dic['high_2'] + "℃" + "/" + dic['low_2'] + "℃"

        self.day_label_0.setText(temp_0)
        self.day_label_1.setText(temp_1)
        self.day_label_2.setText(temp_2)


    def showTime(self):
        time = QDateTime.currentDateTime().toString('hh:mm:ss')
        self.datatime_label.setText(time)

    def about_slot(self):
        QMessageBox.information(self, "提示",
                                "~💃网络获取天气工具 内测版 v2~\n输入正确城市后，点击刷新即可获取到哦😊~\n制作：拾贰 ~")

    def set_key_slot(self):
        self.ms.show()
        #QMessageBox.information(self, "提示", "待开发中...感谢支持呀😀")

    def exit_app(self):
        sys.exit()




def main():
    app = QApplication(sys.argv)

    my = MyWindow()
    my.show()
    my.ms = MyForm()




    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
