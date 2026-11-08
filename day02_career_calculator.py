# ====================================================================
# File: day02_career_calculator.py
# Purpose: Dynamic user input, type casting, arithmetic, and formatters
# Author: BOORI KOTESWARA RAO
# Target: Python 30-Day Engineering Challenge - Day 2
# ====================================================================

print("==================================================")
print("     DEVELOPER CAREER & COMMITMENT CALCULATOR     ")
print("==================================================")

# 1. Dynamic User Input (strings by default)
developer_name: str = input("Enter your full name: ")
target_role: str = input("Enter your target role (e.g. AI-ML Developer): ")

# 2. Numeric Input with Type Casting
daily_hours_str: str = input("Enter planned daily study hours (e.g. 3): ")
daily_hours: int = int(daily_hours_str)

target_lpa_str: str = input("Enter target annual CTC in LPA (e.g. 12.5): ")
target_lpa: float = float(target_lpa_str)

# 3. Arithmetic Computations
weekly_study_hours: int = daily_hours * 7
monthly_study_hours: int = weekly_study_hours * 4

annual_salary_inr: float = target_lpa * 100000.0
monthly_gross_salary: float = annual_salary_inr / 12.0
estimated_hourly_value: float = annual_salary_inr / (52.0 * 40.0)

# 4. Formatted Metrics Output
print("\n" + "=" * 50)
print("              CAREER PROJECTION REPORT            ")
print("=" * 50)
print(f"Candidate Name       : {developer_name}")
print(f"Target Career Track  : {target_role}")
print(f"Weekly Commitment    : {weekly_study_hours} Hours")
print(f"Monthly Commitment   : {monthly_study_hours} Hours")
print("-" * 50)
print(f"Target CTC (Annual)  : ₹{target_lpa:.2f} LPA")
print(f"Gross Monthly Salary : ₹{monthly_gross_salary:,.2f}")
print(f"Implied Hourly Value : ₹{estimated_hourly_value:,.2f} / hr")
print("=" * 50)
print("Commitment verification complete. Code ready to ship.")
print("=" * 50)