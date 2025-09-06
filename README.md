# 🔍 Shodan Guatemala Scan

Este proyecto implementa un script de consola en **Python** que utiliza la **API de Shodan** para realizar búsquedas dirigidas a dispositivos en **Guatemala**, aplicando filtros de localización sin usar `org:`.  

El script muestra en consola todos los resultados obtenidos e incluye un **resumen con**:
- Total de direcciones IP identificadas.  
- Total de IPs agrupadas por puerto abierto.  
- Datos del estudiante: número de carné, nombre completo, curso y sección.  

---

## 📁 Estructura del Proyecto

```
shodan-guatemala-scan/
├── shodan_scan.py        # Script principal que ejecuta la consulta y genera el resumen
├── requirements.txt      # Dependencias necesarias del proyecto
└── README.md             # Documentación del repositorio
```

### Descripción de archivos:
- **shodan_scan.py** → Contiene el código en Python que conecta con la API de Shodan, ejecuta la búsqueda y genera el resumen en consola.  
- **requirements.txt** → Lista de librerías necesarias (ejemplo: `shodan`).  
- **README.md** → Documento con la descripción del proyecto, instrucciones de uso y detalles de la entrega.  

---

## ⚙️ Instalación

1. Clonar el repositorio:  

```bash
git clone https://github.com/tu-usuario/shodan-guatemala-scan.git
cd shodan-guatemala-scan
```

2. Crear un entorno virtual (opcional, pero recomendado):  

```bash
python -m venv venv
source venv/bin/activate   # En Linux / Mac
venv\Scripts\activate      # En Windows
```

3. Instalar dependencias:  

```bash
pip install -r requirements.txt
```

---

## ▶️ Uso

1. Edita el archivo **shodan_scan.py** y coloca tu API Key de Shodan en la variable:  

```python
SHODAN_API_KEY = "TU_API_KEY"
```

2. Ejecuta el script:  

```bash
python shodan_scan.py
```

3. La salida mostrará:  
- Lista de resultados con **IP, puerto y hostnames**.  
- Resumen con el **total de IPs encontradas** y su **distribución por puerto**.  
- Datos del estudiante (**Carnet, Nombre, Curso y Sección**).  

👉 Ejemplo de salida esperada:  

```bash
============================================================
Consulta ejecutada: country:"GT"
Total de resultados: 123
============================================================
IP: 190.56.23.10 | Puerto: 80 | Hostname: ['example.gt']
IP: 190.56.23.11 | Puerto: 443 | Hostname: ['secure.gt']
...

📊 RESUMEN
Total de direcciones IP identificadas: 45
Total de IPs por puerto abierto:
 - Puerto 80: 20 IPs
 - Puerto 443: 15 IPs
 - Puerto 22: 10 IPs
============================================================
Carnet: 202012345
Nombre: Juan Pérez
Curso: Seguridad Informática
Sección: B
============================================================
```

---

## 📌 Notas

- Solo se utilizan **filtros de localización (country, city, etc.)**, cumpliendo la restricción de no usar `org:`.  
- Los resultados pueden variar dependiendo de la API Key y del plan de Shodan.  
- Para fines académicos, el script incluye la impresión de **Carnet, Nombre, Curso y Sección** al final.  
