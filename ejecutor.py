import subprocess

ruta_html = "/home/impy/Escritorio/plataforma/sitios/reportes/reporte1/index.html"

# Ejecutable principal de Chrome en Ubuntu
chrome = "/usr/bin/google-chrome-stable"

subprocess.Popen([chrome, "--incognito", f"file://{ruta_html}"])