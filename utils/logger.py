from datetime import datetime

import allure


class Logger:

    def __init__(self):
        self.log = ''
        self.warning_count = 0
        self.error_count = 0

    def add_log(self, level, new_log):
        hour = datetime.now().strftime("%H:%M:%S")
        return f'<p style="font-family:helvetica;font-size: 14px;"><strong>{hour} - {level}</strong> - {new_log}</p>'

    def info(self, new_log):
        self.log += self.add_log('<span style="color:#03a9f4;">INFO</span>', new_log)

    def warning(self, new_log):
        self.log += self.add_log('<span style="color:#ff9800;">WARNING</span>', new_log)
        self.warning_count += 1

    def error(self, new_log):
        self.log += self.add_log('<span style="color:#ef5350;">ERROR</span>', new_log)
        self.error_count += 1

    def clear_log(self):
        self.log = ''
        self.warning_count = 0
        self.error_count = 0

    def attach_log(self):
        allure.attach(self.log, name="log", attachment_type=allure.attachment_type.HTML)
        self.clear_log()

    def new_line(self):
        return '''<br>
               &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
               &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
               &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
               '''

    def get_warning_count(self):
        return self.warning_count

    def get_error_count(self):
        return self.error_count
