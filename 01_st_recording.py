import sys
import os

import subprocess
import shlex
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon

form_class = uic.loadUiType("creator2.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('nc.png'))
        self.btn_m_config.clicked.connect(self.get_configCheck)
        self.btn_r_clientPath.clicked.connect(self.get_gameClientPath)
        self.btn_r_pcapname.clicked.connect(self.get_pcapName)
        self.btn_r_recording_start.clicked.connect(self.start_recording)
        self.btn_r_recording_stop.clicked.connect(self.stop_recording)

    def get_configCheck(self):
        global s_path
        global rec_num
        global full_filename
        try:
            for (path, dir, files) in os.walk("c:\Program Files"):
                for filename in files:
                    if filename == 'Wireshark.exe':
                        full_filename = os.path.join(path, filename)
                        s_path = os.path.dirname(full_filename)
                        self.label.setText(full_filename)
                        break
                    else:
                        continue
            cmd = s_path + "\\tshark.exe -D"
            ps = subprocess.Popen(cmd, stdout=subprocess.PIPE, encoding='UTF8')
            output = ps.communicate()[0]

            splited = output.split('\n')
            for adapter in splited:
                search = "이더넷"
                if search in adapter:
                    #print (adapter)
                    self.label_15.setText(adapter)
                    rec_num = adapter[:1]
                    print(rec_num)
        except PermissionError:
            pass



    def get_gameClientPath(self):
        fname_c = QFileDialog.getOpenFileName(self, 'Open file', "", "All Files(*);; Exe Files(*.exe)", 'c:/')

        if fname_c[0]:
            self.client_path.setText(fname_c[0])
        else:
            QMessageBox.about(self, "Info", "파일을 선택하지 않았습니다.")

    def get_pcapName(self):
        fname_p = QFileDialog.getSaveFileName(self, 'Save file', "", "pcap Files(*.pcap);; pcap Files(*.pcap)", 'c:/')

        if fname_p[0]:
            self.pcap_path.setText(fname_p[0])
        else:
            QMessageBox.about(self, "Info", "파일을 선택하지 않았습니다.")

    def start_recording(self):
        cmd = s_path + "\\tshark.exe -i " + rec_num + " -c 5000 -w " + self.pcap_path.text()
        print(cmd)
        # cmd2 = "%{ \"$_\" }"
        ps = subprocess.Popen(cmd)
        #ps2 = subprocess.Popen(cmd2,stdin=ps.stdout)
        ps.communicate()

    def stop_recording(self):
        cmd = "taskkill /F /IM dumpcap.exe"
        print(cmd)
        # cmd2 = "%{ \"$_\" }"
        ps = subprocess.Popen(cmd,stdout=subprocess.PIPE)
        #ps2 = subprocess.Popen(cmd2,stdin=ps.stdout)
        ps.communicate()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
