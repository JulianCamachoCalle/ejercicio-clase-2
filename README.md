# github-actions-py

Proyecto muy basico de Python con GitHub Actions.

## Que hace

- `calculadora.py`: cuatro funciones (sumar, restar, multiplicar, dividir).
- `test_calculadora.py`: tests con pytest.
- `.github/workflows/ci.yml`: workflow que instala Python, instala las
  dependencias y ejecuta los tests en cada push y pull request.

## Uso local

```bash
pip install -r requirements.txt
python calculadora.py   # ejecuta el ejemplo
pytest -v               # ejecuta los tests
```

## CI

El workflow se llama **CI** y corre en `ubuntu-latest` con Python 3.12.
Se puede lanzar tambien a mano desde la pestana *Actions* de GitHub
(`workflow_dispatch`).
