import os
import xlsxwriter
from constant import *

#JUST GIVE PATH OF RTM LOGS
test_directory = "D:\PYTHON-PROJECTS\preprationforinterview/doc300rtm.log"       #PATH OF LOGS

test_directory+=r'\rtm'

os.chdir(test_directory)

for filename in os.listdir(test_directory):
    row = 0
    col = 0
    # print(test_directory)
    # print("TEST: ",test_directory.split("\\")[-2])

    workbook = xlsxwriter.Workbook(filename[:-4]+'.xlsx')  # NAME OF EXCEL
    worksheet = workbook.add_worksheet()
    worksheet_error = workbook.add_worksheet()

    worksheet.write(row, col, "File Name")
    worksheet.write(row, col + 1, "Memory Manager " + test_directory.split("\\")[-2])
    # worksheet.write(row, col + 2, "Time")
    # worksheet.write(row, col + 3, "Time(in seconds)")

    row_e = 0
    col_e = 0

    worksheet_error.write(row_e, col_e, "File Name")
    worksheet_error.write(row_e, col_e + 1, "Error Message")

    row += 1
    row_e += 1

    if filename.endswith('.log'):
        f = open(filename, 'r')  # LOG NAME
        text = f.read()

        x = 'SVInit : peak_memory: '
        y = 'Exit status:'

        print("Filename: ", filename)
        if filename == "int300rtm.log" or filename == "int600rtm.log":
            board_path = 'File Name : /mnt/rw/nikhil/intergration_all/'  # PATH OF FILE IN BOARD
        else:
            board_path = 'File Name : /mnt/rw/nikhil/HP_allfiles/'  # PATH OF FILE IN BOARD

        # board_path='File Name : /media/sda1/nikhil/allfiles/'  #PATH OF FILE IN BOARD
        # board_path='File Name : /mnt/rw/nikhil/HP_allfiles/'  #PATH OF FILE IN BOARD
        # board_path = 'File Name : /media/sda1/nikhil/intergration_all/'  # PATH OF FILE IN BOARD
        # board_path='File Name : /nikhil_nfs/NativeOfficeIntegrationSuccessCriteriaSuite/intergration_all/'  #PATH OF FILE IN BOARD

        print(board_path)
        I = [index for index in range(len(text)) if text.startswith('Fontconfig error: Cannot load default config file: No such file: (null)', index)]
        J = [index for index in range(len(text)) if text.startswith('Exit status:', index)]

        for i in range(int(len(I))):
            file = text[I[i]:J[i] + 14]
            data = file.splitlines()

            x = -1
            y = -1

            signal_11 = [line for line in file.splitlines() if 'Command terminated by signal' in line]
            source_file = [line for line in file.splitlines() if 'Error: source file could not be loaded' in line]
            x = len(signal_11)
            y = len(source_file)
            if x > 0 or y > 0:
                file_name = [line for line in file.splitlines() if board_path in line]
                if len(file_name) >= 0:
                    length = len(board_path)
                    # print("FileName: ",file_name)

                    filename = file_name[0][length:]
                    if (x > 0):
                        sig_len = len('Command terminated by signal')
                        signal = signal_11[0][sig_len:]
                        # print('Command terminated by signal  ',filename)
                        worksheet_error.write(row_e, col_e, filename)
                        worksheet_error.write(row_e, col_e + 1, 'Command terminated by signal ' + signal)
                        row_e += 1
                    else:
                        # print('Error: source file could not be loaded  ', filename)
                        worksheet_error.write(row_e, col_e, filename)
                        worksheet_error.write(row_e, col_e + 1, 'Error: source file could not be loaded')
                        row_e += 1

            if x == 0 and y == 0:

                file_name = [line for line in file.splitlines() if board_path in line]
                if len(file_name) >= 0:
                    length = len(board_path)
                    filename = file_name[0][length:]
                    # print(filename)
                    worksheet.write(row, col, filename)

                MemoryManager = [line for line in file.splitlines() if 'from OEM_MEMORY_TRACKING mem tracker, peak memory is ' in line]
                if len(MemoryManager) > 0:
                    length = len('from OEM_MEMORY_TRACKING mem tracker, peak memory is ')
                    # m = MemoryManager[0].find('Bytes allocated:')
                    MemoryManagerValue = MemoryManager[0][length:]
                    MemoryManagerValue = float(MemoryManagerValue) / 1024 / 1024
                    worksheet.write(row, col + 1, MemoryManagerValue)

                MemoryManagerHook = [line for line in file.splitlines() if 'SVProcess : peak_memory hook: ' in line]
                if len(MemoryManagerHook) > 0:
                    length = len('SVProcess : peak_memory hook: ')
                    m = MemoryManagerHook[0].find('Bytes allocated:')
                    MemoryManagerHookValue = MemoryManagerHook[0][length:m]
                    # print(MemoryManagerHookValue)
                    # MemoryManager = float(file[a+length:a+length+10]) / 1024 / 1024
                    # print(MemoryManager)
                    # worksheet.write(row, col+2 , MemoryManagerHookValue)

                # Time = [line for line in file.splitlines() if 'Elapsed (wall clock) time (h:mm:ss or m:ss): ' in line]
                # if len(Time) > 0:
                #     length = len('Elapsed (wall clock) time (h:mm:ss or m:ss): ')
                #     time = Time[0][length:]
                #     length = len(time)
                #     #
                #     i = time.find('h')
                #     j = time.find('m')
                #     k = time.find('s')
                #
                #     hrs = 0
                #     min = 0
                #     sec = 0
                #
                #     if i > 0:
                #         hrs = int(time[0:i])
                #     if j > 0:
                #         if i == -1:
                #             min = int(time[0:j])
                #         else:
                #             min = int(time[i + 1:j])
                #     if k > 0:
                #         sec = float(time[j + 2:k])
                #
                #     t = (hrs * 60 * 60) + min * 60 + sec
                #     worksheet.write(row, col + 2, time)
                #     worksheet.write(row, col + 3, t)
                #     row += 1
                print(filename, " : ", MemoryManagerValue)
                row+=1

        test_directory = test_directory
        os.chdir(test_directory)
        workbook.close()