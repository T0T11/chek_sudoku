🧪 Kata TDD con Pytest: Preparación del entorno
Desde la carpeta donde quieres trabajar:
python3 -m venv venv
source venv/bin/activate
    💡 Asegúrate de estar en la ruta correcta antes de crear el entorno.

2️⃣ Verificar e instalar dependencias básicas

Primero revisa los paquetes instalados:
pip list
Luego instala el kernel de IPython para usar notebooks si lo necesitas:
pip install ipykernel
3️⃣ Instalar extensiones y herramientas necesarias

Instala las siguientes extensiones para trabajar cómodamente con TDD y pytest:

    Extensión de Python (si usas VS Code u otro editor)

    Compilador de Python (ya incluido si tienes Python instalado)

    Extensión de Pytest (para ejecutar tests desde el editor)

    🔧 En VS Code: ve a la pestaña de extensiones y busca Python y Pytest.
4️⃣ Instalar pytest en el entorno virtual
pip install pytest
5️⃣ Verifica que pytest funciona

Crea un archivo de prueba, por ejemplo test_sample.py:
def test_suma():
    assert 2 + 2 == 4
Ejecuta los tests:
pytest
