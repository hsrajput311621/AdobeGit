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
    error_match = re.search(r'Fontconfig error:', entry)
    if error_match:
        error_message = "Error: source file could not be loaded"
    else:
        # Extract peak memory
        peak_memory_match = re.search(r'peak memory is (\d+)', entry)
        if peak_memory_match:
            peak_memory = int(peak_memory_match.group(1))

    return file_name, error_message, peak_memory

# Define the main loop to process multiple log entries
log_file_path = 'D:\PYTHON-PROJECTS\preprationforinterview\doc300rtm.txt'
wb = openpyxl.load_workbook("D:\selenium\parsed_logss.xlsx")

with open(log_file_path, 'r') as log_file:
    entry = ''
    for line in log_file:
        if '====== RUNNING IN LAUNCH & KILL MODE ======' in line:
            file_name, error_message, peak_memory = process_log_entry(entry)
            if file_name:
                #sheet = wb.create_sheet(title=file_name)
                sheet = wb["Sheet1"]
                sheet['A1'] = 'File Name'
                if error_message:
                    sheet['B1'] = 'Error'
                    sheet['A2'] = file_name
                    sheet['B2'] = error_message
                elif peak_memory is not None:
                    sheet['B1'] = 'Peak Memory'
                    sheet['A2'] = file_name
                    sheet['B2'] = peak_memory
            entry = ''
        entry += line

# Save the Excel file
wb.save('parsed_logss.xlsx')
