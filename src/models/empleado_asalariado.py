"""
Clase para empleados con salario fijo mensual.
"""

from datetime import date
from .empleado import Empleado


class EmpleadoAsalariado(Empleado):
    """
    Representa un empleado con salario fijo mensual.
    
    Reglas de negocio:
    - Salario fijo mensual
    - Bono del 10% del salario si tiene más de 5 años de antigüedad
    - Bono de alimentación de $1,000,000/mes
    """
    
    # Constantes de la clase
    BONO_ALIMENTACION = 1_000_000
    PORCENTAJE_BONO_ANTIGUEDAD = 0.10
    AÑOS_MINIMOS_BONO = 5
    
    def __init__(self, id_empleado: str, nombre: str, fecha_ingreso: date, salario_mensual: float):
        """
        Constructor del empleado asalariado.
        
        Args:
            id_empleado (str): ID único del empleado
            nombre (str): Nombre del empleado
            fecha_ingreso (date): Fecha de ingreso
            salario_mensual (float): Salario fijo mensual
            
        Raises:
            ValueError: Si el salario es negativo o cero
        """
        super().__init__(id_empleado, nombre, fecha_ingreso)
        
        if salario_mensual <= 0:
            raise ValueError("El salario mensual debe ser mayor a cero")
        
        self._salario_mensual = salario_mensual
    
    def calcular_salario_bruto(self) -> float:
        """
        Calcula el salario bruto del empleado asalariado.
        
        Returns:
            float: Salario mensual fijo
        """
        return self._salario_mensual
    
    def _calcular_bono_antiguedad(self) -> float:
        """
        Calcula el bono por antigüedad.
        Se otorga 10% del salario si tiene más de 5 años.
        
        Returns:
            float: Monto del bono por antigüedad
        """
        if self.obtener_antiguedad_años() > self.AÑOS_MINIMOS_BONO:
            return self._salario_mensual * self.PORCENTAJE_BONO_ANTIGUEDAD
        return 0
    
    def calcular_beneficios(self) -> float:
        """
        Calcula los beneficios totales del empleado asalariado.
        Incluye: bono de alimentación + bono por antigüedad (si aplica)
        
        Returns:
            float: Total de beneficios
        """
        bono_antiguedad = self._calcular_bono_antiguedad()
        return self.BONO_ALIMENTACION + bono_antiguedad
    
    @property
    def salario_mensual(self) -> float:
        """Getter del salario mensual"""
        return self._salario_mensual
    
    def obtener_detalle_nomina(self) -> dict:
        """
        Genera un diccionario con el detalle completo de la nómina.
        
        Returns:
            dict: Diccionario con todos los conceptos de pago
        """
        salario_bruto = self.calcular_salario_bruto()
        bono_antiguedad = self._calcular_bono_antiguedad()
        deducciones = self.calcular_deducciones(salario_bruto)
        
        return {
            'empleado': self.nombre,
            'tipo': 'Asalariado',
            'salario_bruto': salario_bruto,
            'bono_alimentacion': self.BONO_ALIMENTACION,
            'bono_antiguedad': bono_antiguedad,
            'deducciones': deducciones,
            'salario_neto': self.calcular_salario_neto()
        }