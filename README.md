# HOSPITAL_MANAGEMENT
Hospital Management System created using python,pyqt5 and sqlite
hospital.py and hospitalui.py files contain the code for the the program.
Sqlite db is used to store the data.
When it is run first time click on refresh btn to load existing data and extract btn will extract the data in excel file.

Tools Used:
pyqt5 designer was used for layout which when saved will result in .ui file.
--Command to turn .ui to .py
    pyuic5 –x "filename".ui –o "filename".py
    
Summary:

UI contains of three tabs:
1. First Tab contains functionality for displaying details and extracting report.
2. Second Tab contains functionality to Add new patient details
3. Third Tab contains functionality to search specify patients and retrieve information from database.
