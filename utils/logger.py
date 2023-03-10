import allure
from datetime import datetime

class Logger:

    def __init__(self):
        self.log = ''

    def add_log(self, level, new_log):
        hour = datetime.now().strftime("%H:%M:%S")
        return f'<p style="font-family:helvetica;font-size: 14px;"><strong>{hour} - {level}</strong> - {new_log}</p>'

    def info(self, new_log):
        self.log += self.add_log('<span style="color:#03a9f4;">INFO</span>', new_log)

    def warning(self, new_log):
        self.log += self.add_log('<span style="color:#ff9800;">WARNING</span>', new_log)

    def error(self, new_log):
        self.log += self.add_log('<span style="color:#ef5350;">ERROR</span>', new_log)

    def clear_log(self):
        self.log = ''

    def attach_log(self):
        allure.attach(self.log, name="log", attachment_type=allure.attachment_type.HTML)
        self.clear_log()
