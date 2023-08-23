import re
import openpyxl

# Define a function to process log entries
def process_log_entry(entry):
    file_name = None
    error_message = None
    peak_memory = None

    # Extract File Name
    file_name_match = re.search(r'File Name : (.+)', entry)
    if file_name_match:
        file_name = file_name_match.group(1)

    # Check for error message
    error_match = re.search(r'source file could :', entry)
    if error_match:
        error_message = "Error: source file could not be loaded"
    else:
        # Extract peak memory
        peak_memory_match = re.search(r'peak memory is (\d+)', entry)
        if peak_memory_match:
            peak_memory = int(peak_memory_match.group(1))

    return file_name, error_message, peak_memory

# Define the main loop to read the log file and process each entry
log_file_path = 'D:\PYTHON-PROJECTS\preprationforinterview\doc300rtm.txt'
file = "D:\PYTHON-PROJECTS\preprationforinterview\data.xlsx"
workbook = openpyxl.load_workbook(file)
sheet = workbook["Sheet"]

with open(log_file_path, 'r') as log_file:
    entry = ''
    for line in log_file:
        if '====== RUNNING IN LAUNCH & KILL MODE ======' in line:
            file_name, error_message, peak_memory = process_log_entry(entry)
            if file_name:
                if error_message:
                    #sheet = wb.create_sheet(title=file_name)
                    sheet1 = workbook["Sheet1"]
                    sheet1['A1'] = 'File Name'
                    sheet1['B1'] = 'Error'
                    sheet1['A2'] = file_name
                    sheet1['B2'] = error_message
                elif peak_memory is not None:
                    sheet['A1'] = 'File Name'
                    sheet['B1'] = 'Peak Memory'
                    row = [file_name, peak_memory]
                    sheet.append(row)
            entry = ''
        entry += line

# Save the Excel file
workbook.save('data.xlsx')
