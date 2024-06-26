import nbformat
from nbconvert import PythonExporter
import os

def convert_ipynb_to_py(ipynb_path, output_path):
    # Read the notebook content
    with open(ipynb_path, 'r', encoding='utf-8') as f:
        notebook_content = nbformat.read(f, as_version=4)
    
    # Convert to .py format
    python_exporter = PythonExporter()
    script, _ = python_exporter.from_notebook_node(notebook_content)
    
    # Write the script to the output path
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(script)

# Example usage
ipynb_path = '/shared/location/your_notebook.ipynb'
output_path = '/shared/location/your_script.py'
convert_ipynb_to_py(ipynb_path, output_path)