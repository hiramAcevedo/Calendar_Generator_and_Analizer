# 📅 Generador y Analizador de Calendarios

¡Convierte tus archivos CSV en calendarios funcionales! Este repositorio contiene tres scripts en Python para generar y analizar calendarios en formato `.ics` a partir de archivos `.csv`. ¡Perfecto para estudiantes y profesionales que necesitan organizar y compartir sus horarios! 🚀

## 📁 Estructura del Repositorio

```
├── Calendar_CSV_to_ICS.py            # ¡Magia de conversión CSV → ICS!
├── Free_Busy_Days_Analizer.py        # Encuentra tus días libres y ocupados
├── Calendar_Generation_and_Analizer.py # ¡La solución todo en uno!
├── examples/                          # Archivos de ejemplo para empezar
│   ├── proyecto_3.csv                # CSV de ejemplo para importar
│   ├── proyecto_3.ics                # ICS generado desde el CSV
│   ├── dias_libres.ics              # Calendario de días libres
│   ├── dias_ocupados.ics            # Calendario de días ocupados
│   ├── dias_libres.csv              # Lista detallada de días libres para consulta y compartir
│   ├── dias_ocupados.csv            # Lista detallada de días ocupados para consulta y compartir
```

## 🛠️ Funcionamiento de los Scripts

### 1. `Calendar_CSV_to_ICS.py`

Transforma tus archivos CSV en calendarios `.ics` compatibles con la mayoría de las aplicaciones de calendario. Selecciona múltiples archivos CSV y obtén un `.ics` por cada uno.

#### **Formato Necesario del CSV**

Tu CSV debe tener estas columnas:

```
Actividad,Fecha de Inicio,Fecha de Entrega
"Actividad 1", "16/01/2025", "22/01/2025"
"Actividad 2", "23/01/2025", "29/01/2025"
```

- **Actividad**: Nombre de tu tarea o evento
- **Fecha de Inicio**: Fecha de comienzo (`DD/MM/YYYY`)
- **Fecha de Entrega**: Último día (`DD/MM/YYYY`)

### 2. `Free_Busy_Days_Analizer.py`

Un analizador inteligente de calendarios que:
- Detecta tus fechas ocupadas
- Crea calendarios separados para días ocupados (`dias_ocupados.ics`) y libres (`dias_libres.ics`)
- Maneja múltiples archivos `.ics` a la vez para un análisis completo de tu disponibilidad

### 3. `Calendar_Generation_and_Analizer.py`

¡La herramienta definitiva para calendarios! Características:
- **Conversión CSV → ICS** con carpeta de salida personalizable
- **Análisis de calendarios** con opciones para:
  - Generación de ICS para importación directa a tu calendario
  - Exportación a CSV (días libres, ocupados o ambos) en formato de lista detallada, perfecta para compartir con colaboradores, compañeros de equipo o amigos, o para tener una referencia rápida de tu disponibilidad
  - Ubicación de guardado personalizable para mantener tus archivos organizados

## ⚡ Inicio Rápido

1. **Instala Python**
   Descárgalo de [python.org](https://www.python.org/) (¡no olvides agregarlo al PATH!)

2. **Ejecuta los Scripts**
   ```bash
   python Calendar_CSV_to_ICS.py
   python Free_Busy_Days_Analizer.py
   python Calendar_Generation_and_Analizer.py
   ```

## 💡 Consejos Pro

- ¡Usa `Calendar_Generation_and_Analizer.py` para la mejor experiencia!
- **Organización de CSV**: Mantén calendarios separados (por ejemplo, un CSV por materia o proyecto) para mejor organización y facilidad de actualización
- **Creación de CSV**: No pierdas tiempo creando CSVs manualmente 💀 - Usa herramientas de IA con este prompt:
  ```
  Extrae los datos y genera un CSV con el formato:
  Actividad,Fecha de Inicio,Fecha de Entrega
  "Actividad 1", "16/01/2025", "22/01/2025"
  Usa el formato de fecha DD/MM/YYYY.
  ```

## 🤝 Contribuciones

¿Quieres mejorar esto? ¡Genial! Así puedes hacerlo:
1. Haz un fork del repositorio
2. Realiza tus mejoras
3. Envía un pull request

¿Encontraste un error? ¡Abre un issue y cuéntanos! 🐛

## 📝 Licencia

**Licencia MIT** - ¡Úsalo, modifícalo, compártelo! ¡Hagamos que la gestión de calendarios sea más eficiente! 🎉