# College Attendance Analyzer



A simple command-line Python project that reads student attendance from a CSV file, checks which students are below the 75% requirement, and shows the results as charts.



## Features



1. **Percentage**: overall attendance % of each student (all subjects combined), with a bar chart and a red 75% line.

2. **Shortage list**: students below 75%, with a pie chart (green = 75% or above, red = below 75%). A student with exactly 75% is treated as eligible.

3. **Subject-wise average**: average attendance % of each subject, with a bar chart.

4. **Exit**: closes the program.



The program also checks the data:



- Skips rows where Classes_Held is 0, a value is negative, or a value is not a number (for example `abc`).

- Skips rows where Classes_Attended is greater than Classes_Held.

- Shows a message if the CSV file is missing, or if no valid rows are found.

- Shows a message for a wrong menu option and asks again.



## Requirements



- Python 3

- pandas

- matplotlib



Install them with:



```

pip install -r requirements.txt

```



## Input format



The input file must be named `attendance.csv` and be in the same folder as `attendance_analyzer.py`.



```

Name,Subject,Classes_Held,Classes_Attended

Aman,Python,40,36

Riya,Python,40,28

Karan,Python,40,30

Aman,Maths,50,45

```



The header row is optional. A student can have more than one subject (more than one row).



## How to run



1. Open a terminal in the project folder.

2. Run:



```

python attendance_analyzer.py

```



3. Choose an option from the menu (1 to 4). Close the chart window to return to the menu.



## Sample output



For the sample `attendance.csv` above:



```

1. Percentage       ->  Aman: 90.00% | Riya: 70.00% | Karan: 75.00%

2. Shortage list    ->  Riya: 70.00% (below 75%)

3. Subject-wise     ->  Python: 78.33% | Maths: 90.00%

```



## Notes



- In "Row N invalid" messages, N counts data rows only (the header row is not counted).

- Subject-wise average is the simple average of each row's percentage, not total attended divided by total held.

- Rows with a blank Name are not counted in student-wise totals.



## Files



| File | Purpose |

|---|---|

| `attendance_analyzer.py` | Main program |

| `attendance.csv` | Input data |

| `attendance_test.csv` | Test data with invalid rows (Row 7, 8, 9 are invalid) |

| `requirements.txt` | Libraries needed |

