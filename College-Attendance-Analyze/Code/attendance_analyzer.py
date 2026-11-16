"""
College Attendance Analyzer
Language : Python 3
Libraries: Pandas, Matplotlib
Input    : attendance.csv (Name, Subject, Classes_Held, Classes_Attended)
"""

import pandas as pd
import matplotlib.pyplot as plt

MIN = 75
cols = ["Name", "Subject", "Classes_Held", "Classes_Attended"]

# 1. File load karo (header ho ya na ho, dono chalega)
try:
    df = pd.read_csv("attendance.csv", header=None, names=cols)
except FileNotFoundError:
    print("attendance.csv nahi mili, file check kar lijiye.")
    exit()

df = df[df["Name"] != "Name"].reset_index(drop=True)  # header row hata do

# 2. Galat rows skip karo
good = []
for i, r in df.iterrows():
    held = pd.to_numeric(r["Classes_Held"], errors="coerce")
    att = pd.to_numeric(r["Classes_Attended"], errors="coerce")

    if pd.isna(held) or pd.isna(att) or held <= 0 or att < 0:
        print(f"Row {i + 1} invalid: wrong values. Row skipped.")
    elif att > held:
        print(f"Row {i + 1} invalid: attended ({int(att)}) cannot exceed held ({int(held)}). Row skipped.")
    else:
        good.append([r["Name"], r["Subject"], held, att])

data = pd.DataFrame(good, columns=cols)
if data.empty:
    print("Koi valid data nahi mila.")
    exit()

# 3. Har student ka overall percentage
total = data.groupby("Name", sort=False)[["Classes_Held", "Classes_Attended"]].sum()
pct = total["Classes_Attended"] / total["Classes_Held"] * 100

# 4. Menu
while True:
    print("\n1. Percentage\n2. Shortage list\n3. Subject-wise average\n4. Exit")
    ch = input("Option chuniye: ").strip()

    if ch == "1":
        print(" | ".join(f"{n}: {p:.2f}%" for n, p in pct.items()))
        plt.bar(pct.index, pct.values, color="skyblue")
        plt.axhline(MIN, color="red", linestyle="--")
        plt.title("Student-wise Attendance %")
        plt.ylabel("Attendance (%)")
        plt.show()

    elif ch == "2":
        low = pct[pct < MIN]  # boolean filtering
        if low.empty:
            print("No student below 75%.")
            for n, p in pct[pct == MIN].items():
                print(f"{n} ({p:.2f}%) is eligible.")
        else:
            for n, p in low.items():
                print(f"{n}: {p:.2f}% (below 75%)")
        plt.pie([len(pct) - len(low), len(low)], labels=["75% or above", "Below 75%"],
                colors=["green", "red"], autopct="%1.0f%%")
        plt.title("Attendance Status")
        plt.show()

    elif ch == "3":
        data["Pct"] = data["Classes_Attended"] / data["Classes_Held"] * 100
        avg = data.groupby("Subject", sort=False)["Pct"].mean()
        print(" | ".join(f"{s}: {p:.2f}%" for s, p in avg.items()))
        plt.bar(avg.index, avg.values, color="orange")
        plt.title("Subject-wise Average Attendance")
        plt.ylabel("Average (%)")
        plt.show()

    elif ch == "4":
        print("Dhanyavaad!")
        break

    else:
        print("Galat option, 1 se 4 chuniye.")