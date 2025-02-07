import tkinter as tk
from tkinter import filedialog
import csv
from datetime import datetime, timedelta

def select_files():
    """Open a file dialog to select multiple .ics files."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_paths = filedialog.askopenfilenames(title="Select ICS files", filetypes=[("ICS Files", "*.ics")])
    return file_paths

def extract_deadlines(file_paths):
    """Extracts deadline dates from multiple .ics files."""
    deadlines = set()
    for file_path in file_paths:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if line.startswith("DTEND;VALUE=DATE:"):
                    date_str = line.strip().split(":")[1]
                    date = datetime.strptime(date_str, "%Y%m%d").date() - timedelta(days=1)
                    deadlines.add(date)
    return sorted(deadlines)

def generate_calendar(dates, output_path, summary):
    """Generates an .ics calendar from given dates."""
    ics_content = "BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\n"
    for date in dates:
        date_str = date.strftime("%Y%m%d")
        event = f"""BEGIN:VEVENT\nSUMMARY:{summary}\nDTSTART;VALUE=DATE:{date_str}\nDTEND;VALUE=DATE:{date_str}\nEND:VEVENT\n"""
        ics_content += event
    ics_content += "END:VCALENDAR"
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(ics_content)
    print(f"Calendar saved to {output_path}")

def get_year_range(deadlines):
    """Determine the year range from the deadlines"""
    if not deadlines:
        return datetime.now().year
    return max(date.year for date in deadlines)

if __name__ == "__main__":
    print("Select calendar files to process...")
    file_paths = select_files()
    if not file_paths:
        print("No files selected. Exiting.")
        exit()
    
    deadlines = extract_deadlines(file_paths)
    year = get_year_range(deadlines)
    
    # Calculate if it's a leap year
    is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    days_in_year = 366 if is_leap_year else 365
    
    # Create set of all days for the detected year
    all_days = set(datetime(year, 1, 1).date() + timedelta(days=i) for i in range(days_in_year))
    free_days = sorted(all_days - set(deadlines))
    
    # Use absolute paths for output files
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    generate_calendar(deadlines, os.path.join(current_dir, "Dias_Ocupados.ics"), "Día de Entrega")
    generate_calendar(free_days, os.path.join(current_dir, "Dias_Libres.ics"), "Día Libre")
