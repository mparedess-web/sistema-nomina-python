# 🏢 Sistema de Nómina - CIPA

Sistema de gestión de nómina empresarial desarrollado en Python aplicando principios SOLID, código limpio y buenas prácticas de programación orientada a objetos.

## 📋 Descripción

Este sistema permite calcular la nómina de diferentes tipos de empleados, cada uno con sus propias reglas de cálculo de salario, beneficios y deducciones.

## 👥 Tipos de Empleados

### 1. Empleado Asalariado
- Salario fijo mensual
- **Beneficios:**
  - Bono mensual del 10% del salario si tiene más de 5 años en la empresa
  - Bono de alimentación: $1,000,000/mes

### 2. Empleado por Horas
- Pago por horas trabajadas (tarifa base por hora)
- Horas extras (más de 40 horas) se pagan a 1.5x la tarifa normal
- **Beneficios:**
  - Fondo de ahorro (2% del salario) si tiene más de 1 año y lo acepta
- **No recibe bonos**

### 3. Empleado por Comisión
- Salario base + porcentaje de comisión sobre ventas
- **Beneficios:**
  - Si las ventas superan $20,000,000: bono adicional del 3% sobre ventas
  - Bono de alimentación: $1,000,000/mes

### 4. Empleado Temporal
- Salario fijo mensual
- Contrato por tiempo definido
- **No aplican bonos ni beneficios adicionales**

## 💰 Deducciones

Todos los empleados tienen:
- **Seguro Social y Pensión:** 4% del salario bruto
- **ARL:** Según corresponda

## 🎯 Principios SOLID Aplicados

### S - Single Responsibility Principle
- Cada clase tiene una única responsabilidad bien definida

### O - Open/Closed Principle
- El sistema está abierto a extensión, cerrado a modificación

### L - Liskov Substitution Principle
- Todas las clases derivadas pueden sustituir a la clase base

### I - Interface Segregation Principle
- Interfaces específicas para cada necesidad

### D - Dependency Inversion Principle
- Las clases dependen de abstracciones, no de implementaciones

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.14.0
- **Testing:** pytest
- **Control de versiones:** Git/GitHub

## 📁 Estructura del Proyecto
```
sistema-nomina-python/
├── src/
│   ├── interfaces/
│   │   └── icalculable.py
│   ├── models/
│   │   ├── empleado.py
│   │   ├── empleado_asalariado.py
│   │   ├── empleado_por_horas.py
│   │   ├── empleado_por_comision.py
│   │   └── empleado_temporal.py
│   └── services/
├── tests/
│   └── test_empleados.py
├── main.py
└── README.md
```

## 🚀 Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/sistema-nomina-python.git
cd sistema-nomina-python
```

### 2. Crear entorno virtual
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install pytest
```

### 4. Ejecutar el sistema
```bash
python main.py
```

### 5. Ejecutar pruebas
```bash
python -m pytest tests/ -v
```

## 📊 Ejemplo de Uso
```python
from datetime import date
from src.models.empleado_asalariado import EmpleadoAsalariado

empleado = EmpleadoAsalariado(
    id_empleado="001",
    nombre="Juan Pérez",
    fecha_ingreso=date(2018, 1, 15),
    salario_mensual=5_000_000
)

salario_neto = empleado.calcular_salario_neto()
print(f"Salario neto: ${salario_neto:,.2f}")
```

## ✅ Validaciones

- Salario neto nunca negativo
- Horas trabajadas no negativas
- Ventas no negativas
- Fecha de ingreso no futura

## 🧪 Pruebas Unitarias

27+ pruebas unitarias que cubren:
- Creación de empleados
- Cálculo de salarios
- Beneficios y deducciones
- Validaciones

## 👥 Equipo CIPA

- [Raul Armando Valencia Zuluaga ]
- [Danny Jose Salgado Guzman]
- [Luis Angel Gomez Altamiranda]
- [Maria Jose Paredes Sevilla]
