# Project Summary

## College Attendance Analyzer

**Language:** Python 3
**Libraries:** Pandas, Matplotlib
**Input:** `attendance.csv` (Name, Subject, Classes_Held, Classes_Attended)

---

## What the project does

This is a command-line program that reads student attendance from a CSV file, calculates each student's attendance percentage, finds the students who are below the 75% requirement, and shows the results as charts.

## Main points

1. **Percentage:** Shows the overall attendance of every student (all subjects combined) with a bar chart. A red dashed line marks 75%.
2. **Shortage list:** Lists students below 75% and shows a pie chart (green = 75% or above, red = below 75%). A student with exactly 75% is treated as eligible.
3. **Subject-wise average:** Shows the average attendance of each subject with a bar chart.
4. **Exit:** Closes the program.
5. **Data checking:** Wrong rows are skipped with a clear message, and the program does not crash if the file is missing.
6. **Formula used:** Overall % = (total classes attended ÷ total classes held) × 100.

## Result on the sample data

| Student | Overall % | Status |
|---|---|---|
| Aman | 90.00% | Eligible |
| Riya | 70.00% | Shortage |
| Karan | 75.00% | Eligible (exactly 75%) |

Subject-wise average: Python 78.33%, Maths 90.00%.

---

## Difficulties faced and how they were solved

**1. The CSV might or might not have a header row.**
Some files start with the column names and some do not. If the header is read as data, the program breaks because "Classes_Held" is text, not a number. The fix was to read the file without assuming a header and then remove any row where the Name is literally "Name".

**2. Wrong or bad data in the rows.**
Real attendance files are not always clean. A row can have 0 classes held (division by zero), a negative number, text like `abc`, or attended greater than held (for example 45 out of 40). The program checks every row, prints which row is wrong and why, and skips it instead of stopping.

**3. Confusion about row numbers in error messages.**
The message says "Row 7 invalid" but the user may count the header too. In this program the row number counts data rows only (the header is not counted). This is written in the README so there is no confusion while testing.

**4. What if every row is invalid?**
In one test the only row was invalid, so nothing was left to calculate. Without a check, the program would crash later. Now it prints "Koi valid data nahi mila" and exits properly.

**5. Student with exactly 75%.**
It was not clear whether 75% counts as a shortage. The rule followed is that 75% is eligible and only below 75% is shortage. The code uses `< 75`, so Karan is correctly not in the shortage list.

**6. Two ways to calculate the subject average.**
Subject average can be the average of each row's percentage, or total attended divided by total held. These give different answers when the number of classes differs. This project uses the simple average of row percentages, and it is mentioned in the README.

**7. Missing file.**
If `attendance.csv` is not in the same folder, the program would normally crash with a long error. A try/except block shows a short, clear message instead.

**8. Charts and the menu.**
The chart window stays open and the menu waits until it is closed. This is expected behaviour of `plt.show()`, so the README tells the user to close the chart to return to the menu.

---

## Testing done

| Test | What was checked | Result |
|---|---|---|
| test1 | Option 1, percentage and bar chart | Correct |
| test2 | Option 2, shortage list and pie chart | Only Riya shown |
| test3 | Only one row, and it is invalid | "No valid data" message |
| test4 | Option 3, subject-wise average | Python 78.33%, Maths 90.00% |
| test6 | Wrong menu option, then Exit | Asked again, then closed |
| test7 | Test file with invalid rows (7, 8, 9) | All three skipped |
| test8 | CSV file missing | Message shown, no crash |

## Conclusion

The program works correctly for valid data and handles wrong data and a missing file without crashing. In future it can be improved by exporting the shortage list to Excel, accepting any file name, and adding a per-student subject report.
