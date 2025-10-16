"""
Pruebas unitarias para el sistema de nómina.
Implementa pruebas para todos los tipos de empleados y sus reglas de negocio.
"""

import pytest
from datetime import date
from src.models.empleado_asalariado import EmpleadoAsalariado
from src.models.empleado_por_horas import EmpleadoPorHoras
from src.models.empleado_por_comision import EmpleadoPorComision
from src.models.empleado_temporal import EmpleadoTemporal


class TestEmpleadoAsalariado:
    """Pruebas para EmpleadoAsalariado"""
    
    def test_creacion_empleado_asalariado(self):
        """Verifica que se puede crear un empleado asalariado correctamente"""
        emp = EmpleadoAsalariado("001", "Juan Pérez", date(2020, 1, 1), 5_000_000)
        assert emp.nombre == "Juan Pérez"
        assert emp.salario_mensual == 5_000_000
    
    def test_salario_bruto_asalariado(self):
        """Verifica el cálculo del salario bruto"""
        emp = EmpleadoAsalariado("001", "Juan Pérez", date(2020, 1, 1), 5_000_000)
        assert emp.calcular_salario_bruto() == 5_000_000
    
    def test_bono_antiguedad_mas_5_años(self):
        """Verifica que se otorga bono por antigüedad si tiene más de 5 años"""
        emp = EmpleadoAsalariado("001", "Juan Pérez", date(2018, 1, 1), 5_000_000)
        beneficios = emp.calcular_beneficios()
        # Bono alimentación (1M) + bono antigüedad (10% de 5M = 500K) = 1.5M
        assert beneficios == 1_500_000
    
    def test_sin_bono_antiguedad_menos_5_años(self):
        """Verifica que NO se otorga bono por antigüedad si tiene menos de 5 años"""
        emp = EmpleadoAsalariado("001", "Juan Pérez", date(2022, 1, 1), 5_000_000)
        beneficios = emp.calcular_beneficios()
        # Solo bono alimentación (1M)
        assert beneficios == 1_000_000
    
    def test_deducciones_asalariado(self):
        """Verifica el cálculo de deducciones (4% del salario bruto)"""
        emp = EmpleadoAsalariado("001", "Juan Pérez", date(2020, 1, 1), 5_000_000)
        deducciones = emp.calcular_deducciones(5_000_000)
        assert deducciones == 200_000  # 4% de 5M
    
    def test_salario_neto_positivo(self):
        """Verifica que el salario neto nunca sea negativo"""
        emp = EmpleadoAsalariado("001", "Juan Pérez", date(2020, 1, 1), 5_000_000)
        salario_neto = emp.calcular_salario_neto()
        assert salario_neto >= 0
    
    def test_salario_invalido(self):
        """Verifica que no se pueda crear empleado con salario inválido"""
        with pytest.raises(ValueError):
            EmpleadoAsalariado("001", "Juan Pérez", date(2020, 1, 1), -1000)


class TestEmpleadoPorHoras:
    """Pruebas para EmpleadoPorHoras"""
    
    def test_creacion_empleado_por_horas(self):
        """Verifica que se puede crear un empleado por horas correctamente"""
        emp = EmpleadoPorHoras("002", "María García", date(2022, 1, 1), 50_000, 40)
        assert emp.nombre == "María García"
        assert emp.tarifa_por_hora == 50_000
        assert emp.horas_trabajadas == 40
    
    def test_salario_sin_horas_extras(self):
        """Verifica el cálculo cuando NO hay horas extras"""
        emp = EmpleadoPorHoras("002", "María García", date(2022, 1, 1), 50_000, 35)
        salario_bruto = emp.calcular_salario_bruto()
        assert salario_bruto == 1_750_000  # 35 * 50K
    
    def test_salario_con_horas_extras(self):
        """Verifica el cálculo con horas extras (1.5x)"""
        emp = EmpleadoPorHoras("002", "María García", date(2022, 1, 1), 50_000, 45)
        salario_bruto = emp.calcular_salario_bruto()
        # 40 horas normales (2M) + 5 extras a 1.5x (375K) = 2.375M
        assert salario_bruto == 2_375_000
    
    def test_fondo_ahorro_con_mas_1_año(self):
        """Verifica el fondo de ahorro si tiene más de 1 año y lo acepta"""
        emp = EmpleadoPorHoras("002", "María García", date(2022, 1, 1), 50_000, 40, True)
        beneficios = emp.calcular_beneficios()
        # 2% de 2M = 40K
        assert beneficios == 40_000
    
    def test_sin_fondo_ahorro_menos_1_año(self):
        """Verifica que NO hay fondo si tiene menos de 1 año"""
        emp = EmpleadoPorHoras("002", "María García", date(2024, 10, 1), 50_000, 40, True)
        beneficios = emp.calcular_beneficios()
        assert beneficios == 0
    
    def test_sin_fondo_ahorro_no_acepta(self):
        """Verifica que NO hay fondo si no lo acepta"""
        emp = EmpleadoPorHoras("002", "María García", date(2022, 1, 1), 50_000, 40, False)
        beneficios = emp.calcular_beneficios()
        assert beneficios == 0
    
    def test_horas_negativas(self):
        """Verifica que no se puedan ingresar horas negativas"""
        with pytest.raises(ValueError):
            EmpleadoPorHoras("002", "María García", date(2022, 1, 1), 50_000, -10)


class TestEmpleadoPorComision:
    """Pruebas para EmpleadoPorComision"""
    
    def test_creacion_empleado_comision(self):
        """Verifica que se puede crear un empleado por comisión correctamente"""
        emp = EmpleadoPorComision("003", "Carlos López", date(2020, 1, 1), 
                                  2_000_000, 0.05, 15_000_000)
        assert emp.nombre == "Carlos López"
        assert emp.salario_base == 2_000_000
        assert emp.porcentaje_comision == 0.05
    
    def test_salario_bruto_con_comision(self):
        """Verifica el cálculo de salario bruto (base + comisión)"""
        emp = EmpleadoPorComision("003", "Carlos López", date(2020, 1, 1),
                                  2_000_000, 0.05, 10_000_000)
        salario_bruto = emp.calcular_salario_bruto()
        # 2M base + 5% de 10M (500K) = 2.5M
        assert salario_bruto == 2_500_000
    
    def test_bono_ventas_altas(self):
        """Verifica el bono adicional si ventas > $20M"""
        emp = EmpleadoPorComision("003", "Carlos López", date(2020, 1, 1),
                                  2_000_000, 0.05, 25_000_000)
        beneficios = emp.calcular_beneficios()
        # Bono alimentación (1M) + 3% de 25M (750K) = 1.75M
        assert beneficios == 1_750_000
    
    def test_sin_bono_ventas_bajas(self):
        """Verifica que NO hay bono adicional si ventas < $20M"""
        emp = EmpleadoPorComision("003", "Carlos López", date(2020, 1, 1),
                                  2_000_000, 0.05, 15_000_000)
        beneficios = emp.calcular_beneficios()
        # Solo bono alimentación (1M)
        assert beneficios == 1_000_000
    
    def test_ventas_negativas(self):
        """Verifica que no se puedan ingresar ventas negativas"""
        with pytest.raises(ValueError):
            EmpleadoPorComision("003", "Carlos López", date(2020, 1, 1),
                               2_000_000, 0.05, -1000)


class TestEmpleadoTemporal:
    """Pruebas para EmpleadoTemporal"""
    
    def test_creacion_empleado_temporal(self):
        """Verifica que se puede crear un empleado temporal correctamente"""
        emp = EmpleadoTemporal("004", "Ana Ruiz", date(2024, 1, 1),
                              3_000_000, date(2025, 12, 31))
        assert emp.nombre == "Ana Ruiz"
        assert emp.salario_mensual == 3_000_000
    
    def test_sin_beneficios_temporal(self):
        """Verifica que los empleados temporales NO tienen beneficios"""
        emp = EmpleadoTemporal("004", "Ana Ruiz", date(2024, 1, 1),
                              3_000_000, date(2025, 12, 31))
        beneficios = emp.calcular_beneficios()
        assert beneficios == 0
    
    def test_contrato_vigente(self):
        """Verifica que se puede consultar si el contrato está vigente"""
        emp = EmpleadoTemporal("004", "Ana Ruiz", date(2024, 1, 1),
                              3_000_000, date(2025, 12, 31))
        assert emp.contrato_vigente() == True
    
    def test_dias_restantes_contrato(self):
        """Verifica el cálculo de días restantes del contrato"""
        emp = EmpleadoTemporal("004", "Ana Ruiz", date(2024, 1, 1),
                              3_000_000, date(2025, 12, 31))
        dias = emp.dias_restantes_contrato()
        assert dias > 0
    
    def test_fecha_fin_invalida(self):
        """Verifica que la fecha de fin debe ser posterior a la de inicio"""
        with pytest.raises(ValueError):
            EmpleadoTemporal("004", "Ana Ruiz", date(2024, 1, 1),
                           3_000_000, date(2023, 12, 31))


class TestValidacionesGenerales:
    """Pruebas de validaciones generales para todos los empleados"""
    
    def test_fecha_ingreso_futura(self):
        """Verifica que no se puede ingresar una fecha futura"""
        fecha_futura = date(2030, 1, 1)
        with pytest.raises(ValueError):
            EmpleadoAsalariado("001", "Juan Pérez", fecha_futura, 5_000_000)
    
    def test_nombre_vacio(self):
        """Verifica que el nombre no puede estar vacío"""
        with pytest.raises(ValueError):
            EmpleadoAsalariado("001", "", date(2020, 1, 1), 5_000_000)
    
    def test_id_vacio(self):
        """Verifica que el ID no puede estar vacío"""
        with pytest.raises(ValueError):
            EmpleadoAsalariado("", "Juan Pérez", date(2020, 1, 1), 5_000_000)