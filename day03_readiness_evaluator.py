# ====================================================================
# File: day03_readiness_evaluator.py
# Purpose: Conditional logic, relational operators, and multi-way branching
# Author: BOORI KOTESWARA RAO
# Target: Python 30-Day Engineering Challenge - Day 3
# ====================================================================

print("==================================================")
print("     AI/ML DEVELOPER SPRINT READINESS ENGINE      ")
print("==================================================")

# 1. Capture Dynamic Metrics
dev_name: str = input("Candidate Name: ")
daily_hours: float = float(input("Average daily study hours (e.g. 3.0): "))
has_git_repo: str = input("Have you initialized Git & GitHub? (yes/no): ").strip().lower()
target_contributions: int = int(input("Target total contributions (e.g. 2000): "))

# 2. Decision Logic Engine
has_git: bool = (has_git_repo == "yes" or has_git_repo == "y")

# Evaluate Commitment Bandwidth
if daily_hours >= 4.0:
    bandwidth_status = "High-Intensity Velocity"
    sprint_duration_months = 6
elif daily_hours >= 3.0:
    bandwidth_status = "Target Baseline Cadence"
    sprint_duration_months = 10
elif daily_hours >= 1.5:
    bandwidth_status = "Moderate Progression"
    sprint_duration_months = 16
else:
    bandwidth_status = "At-Risk Cadence (Below threshold)"
    sprint_duration_months = 24

# Evaluate Readiness Tier
if has_git and target_contributions >= 2000 and daily_hours >= 3.0:
    tier = "Tier 1: Job-Ready Engineering Track"
    recommendation = "Maintain daily commits and deploy full-stack AI applications."
elif has_git and daily_hours >= 1.5:
    tier = "Tier 2: Developing Contributor"
    recommendation = "Increase study block to 3 hours daily to hit 10-month target."
else:
    tier = "Tier 3: Foundations Required"
    recommendation = "Set up Git tracking immediately and commit to a minimum daily schedule."

# 3. Formatted Performance Report
print("\n" + "=" * 50)
print("            CANDIDATE READINESS REPORT            ")
print("=" * 50)
print(f"Developer Name       : {dev_name}")
print(f"Daily Commitment     : {daily_hours} hrs/day")
print(f"Bandwidth Status     : {bandwidth_status}")
print(f"Estimated Runway     : {sprint_duration_months} Months")
print(f"Version Control Live : {'Enabled (GitHub)' if has_git else 'Disabled'}")
print("-" * 50)
print(f"Evaluation Tier      : {tier}")
print(f"Recommendation       : {recommendation}")
print("=" * 50)