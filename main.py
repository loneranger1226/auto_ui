import os

from config import log_run
from read_data.excel_read import run

if __name__ == '__main__':
    log = log_run.get_log("config/log.ini")
    for file_path, file_folder, file_name_list in os.walk("test_data"):
        for file_name in file_name_list:
            if file_name.split(".")[-1] == "xlsx":
                file = file_path + "/" + file_name
                log.info("正在运行{}".format(file))
                run(file, log)