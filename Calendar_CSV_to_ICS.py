import tkinter as tk
from tkinter import filedialog
import csv
import os
from datetime import datetime, timedelta

def select_files():
    """Open a file dialog to select multiple CSV files."""
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(title="Select CSV files", filetypes=[("CSV Files", "*.csv")])
    return file_paths

def read_csv(file_path):
    """Reads data from a CSV file."""
    activities = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            activities.append({
                "Actividad": row["Actividad"],
                "Fecha de Inicio": row["Fecha de Inicio"],
                "Fecha de Entrega": row["Fecha de Entrega"],
            })
    return activities

def generate_calendar(activities, output_path):
    """Generates an .ics calendar file from the provided activities."""
    ics_content = "BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\n"
    for item in activities:
        start_date = datetime.strptime(item["Fecha de Inicio"], "%d/%m/%Y").strftime("%Y%m%d")
        end_date = (datetime.strptime(item["Fecha de Entrega"], "%d/%m/%Y") + timedelta(days=1)).strftime("%Y%m%d")
        event = f"""BEGIN:VEVENT\nSUMMARY:{item['Actividad']}\nDTSTART;VALUE=DATE:{start_date}\nDTEND;VALUE=DATE:{end_date}\nEND:VEVENT\n"""
        ics_content += event
    ics_content += "END:VCALENDAR"
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(ics_content)
    print(f"Calendar saved to {output_path}")

if __name__ == "__main__":
    print("Select CSV files to process...")
    file_paths = select_files()
    if not file_paths:
        print("No files selected. Exiting.")
        exit()
    
    for file_path in file_paths:
        activities = read_csv(file_path)
        output_file = os.path.splitext(file_path)[0] + ".ics"
        generate_calendar(activities, output_file)
