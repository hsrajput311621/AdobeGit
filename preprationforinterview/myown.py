import re
import xlsxwriter

# Define regular expressions to match the relevant lines in the log file
# error_pattern = re.compile(r'Error: source file could not be loaded')
# file_name_pattern = re.compile(r'File Name : (.+)')
# memory_pattern = re.compile(r'peak memory is (\d+)')

# Initialize data lists to store extracted information
error_data = []
memory_data = []

# Read the log file
with open('D:\PYTHON-PROJECTS\preprationforinterview/doc300rtm.log', 'r') as file:
    lines = file.readlines()
    #print(lines,"\n")

# Process each line in the log file
i = 0
while i < len(lines):
    line = lines[i].strip()

    # Check for File Name and Error
    #file_name_match = file_name_pattern.search(line)
    file_name_match = re.search(r'File Name : (.+)', line)
    if file_name_match:
        file_name = file_name_match.group(1)
        #print(file_name,"\n")
        #if error_pattern.search(lines[i+1]):
        if re.search(r'Error: source file could not be loaded', lines[i+1]):
            error_data.append((file_name, "Error: source file could not be loaded"))
        i += 2
        continue

    # Check for peak memory
    #memory_match = memory_pattern.search(line)
    memory_match = re.search(r'peak memory is (\d+)', line)
    if memory_match:
        memory_data.append((file_name, int(memory_match.group(1))))

    i += 1

# Create an Excel workbook and sheets
workbook = xlsxwriter.Workbook('outputnew.xlsx')
error_sheet = workbook.add_worksheet('Error Data')
memory_sheet = workbook.add_worksheet('Memory Data')

# Write data to Excel sheets
# for row, (file_name, error) in enumerate(error_data):
#     error_sheet.write(row, 0, file_name)
#     error_sheet.write(row, 1, error)

for row in range(len(error_data)):
    file_name, error = error_data[row]

    error_sheet.write(row, 0, file_name)
    error_sheet.write(row, 1, error)

for row, (file_name, memory) in enumerate(memory_data):
    memory_sheet.write(row, 0, file_name)
    memory_sheet.write(row, 1, memory)

# Close the workbook
workbook.close()
