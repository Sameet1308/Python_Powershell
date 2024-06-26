import nbconvert
import sys

# Check if notebook path is provided
if len(sys.argv) < 2:
    print("Usage: python convert_notebook.py <path_to_notebook.ipynb>")
    sys.exit(1)

notebook_path = sys.argv[1]

# Convert the notebook to a Python script
exporter = nbconvert.PythonExporter()
output, resources = exporter.from_filename(notebook_path)

# Write the output to a .py file
script_path = notebook_path.replace('.ipynb', '.py')
with open(script_path, 'w', encoding='utf-8') as f:
    f.write(output)

print(f"Notebook converted to {script_path}")