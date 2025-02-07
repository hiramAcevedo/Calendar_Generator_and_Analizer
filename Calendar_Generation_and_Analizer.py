import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import os
from datetime import datetime, timedelta

def select_files(file_type):
    """Open a file dialog to select multiple files."""
    root = tk.Tk()
    root.withdraw()
    file_types = [("CSV Files", "*.csv")] if file_type == "csv" else [("ICS Files", "*.ics")]
    return filedialog.askopenfilenames(title=f"Select {file_type.upper()} files", filetypes=file_types)

def select_output_folder():
    """Open a dialog to select an output folder."""
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory(title="Select output folder")

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

def extract_deadlines(file_paths):
    """Extracts deadline dates and start dates from multiple .ics files."""
    deadlines = set()
    start_dates = set()
    for file_path in file_paths:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("DTEND;VALUE=DATE:"):
                    date_str = line.strip().split(":")[1]
                    date = datetime.strptime(date_str, "%Y%m%d").date() - timedelta(days=1)
                    deadlines.add(date)
                elif line.startswith("DTSTART;VALUE=DATE:"):
                    date_str = line.strip().split(":")[1]
                    date = datetime.strptime(date_str, "%Y%m%d").date()
                    start_dates.add(date)
    return sorted(deadlines), min(start_dates) if start_dates else datetime.now().date()

def analyze_calendars(file_paths, output_folder):
    deadlines, first_start_date = extract_deadlines(file_paths)
    year = max(date.year for date in deadlines) if deadlines else datetime.now().year
    
    # Calculate days from first activity to end of year
    days_range = (datetime(year, 12, 31).date() - first_start_date).days + 1
    all_days = set(first_start_date + timedelta(days=i) for i in range(days_range))
    free_days = sorted(all_days - set(deadlines))
    
    # Generate calendar files
    generate_calendar([{"Actividad": "Día de Entrega", "Fecha de Inicio": d.strftime("%d/%m/%Y"), 
                    "Fecha de Entrega": d.strftime("%d/%m/%Y")} for d in deadlines], 
                    os.path.join(output_folder, "Dias_Ocupados.ics"))
    generate_calendar([{"Actividad": "Día Libre", "Fecha de Inicio": d.strftime("%d/%m/%Y"), 
                    "Fecha de Entrega": d.strftime("%d/%m/%Y")} for d in free_days], 
                    os.path.join(output_folder, "Dias_Libres.ics"))
    
    # Simplified CSV generation question
    option = messagebox.askquestion("Guardar CSV", 
                                "¿Deseas generar archivos CSV con el listado de días?")
    if option == 'yes':
        with open(os.path.join(output_folder, "Dias_Ocupados.csv"), "w", 
                encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Fecha", "Tipo"])
            for d in deadlines:
                writer.writerow([d.strftime("%d/%m/%Y"), "Día de Entrega"])
        
        with open(os.path.join(output_folder, "Dias_Libres.csv"), "w", 
                encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Fecha", "Tipo"])
            for d in free_days:
                writer.writerow([d.strftime("%d/%m/%Y"), "Día Libre"])

def main():
    root = tk.Tk()
    root.withdraw()
    option = messagebox.askquestion("Seleccionar opción", "¿Qué deseas hacer?", icon='question', type='yesno', 
                                    detail="Presiona 'Sí' para generar calendarios desde CSV o 'No' para analizar calendarios ICS.")
    if option == 'yes':
        csv_files = select_files("csv")
        if csv_files:
            output_folder = select_output_folder()
            for file_path in csv_files:
                activities = read_csv(file_path)
                output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(file_path))[0] + ".ics")
                generate_calendar(activities, output_file)
            messagebox.showinfo("Éxito", "Calendarios generados correctamente.")
    else:
        ics_files = select_files("ics")
        if ics_files:
            output_folder = select_output_folder()
            analyze_calendars(ics_files, output_folder)
            messagebox.showinfo("Éxito", "Análisis de calendarios completado.")

if __name__ == "__main__":
    main()
