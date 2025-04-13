import openpyxl as xl
from openpyxl import Workbook
from faker import Faker
import random

fake = Faker()

def generateNames(num: int):
    names = list()

    for i in range(num):
        names.append(fake.name())

    return names

def generateAge(num: int):
    ages = list()
    for i in range(num):
        ages.append(random.randint(1,100))
    return ages

#Generate Name and Age
numRows = 10
nameCell = generateNames(numRows)
ageCell = generateAge(numRows)

# Create a new workbook and select the active worksheet
wb = Workbook()
ws = wb.active
ws.title = "Fake Data"

# Write headers
ws['A1'] = 'Name'
ws['B1'] = 'Age'

# Write data to cells
for i in range(numRows):
    ws.cell(row=i+2, column=1, value=nameCell[i])  # Column A - Name
    ws.cell(row=i+2, column=2, value=ageCell[i])   # Column B - Age

# Save the workbook
wb.save("fake_data.xlsx")