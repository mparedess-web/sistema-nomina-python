"""
Clase para empleados que cobran salario base más comisiones por ventas.
"""

from datetime import date
from .empleado import Empleado


class EmpleadoPorComision(Empleado):
    """
    Representa un empleado con salario base más comisiones.
    
    Reglas de negocio:
    - Salario base + porcentaje de comisión sobre ventas
    - Si ventas > $20,000,000: bono adicional del 3% sobre ventas
    - Bono de alimentación de $1,000,000/mes
    """
    
    # Constantes
    BONO_ALIMENTACION = 1_000_000
    VENTAS_MINIMAS_BONO = 20_000_000
    PORCENTAJE_BONO_VENTAS = 0.03
    
    def __init__(self, id_empleado: str, nombre: str, fecha_ingreso: date,
                 salario_base: float, porcentaje_comision: float, ventas_mes: float):
        """
        Constructor del empleado por comisión.
        
        Args:
            id_empleado (str): ID único del empleado
            nombre (str): Nombre del empleado
            fecha_ingreso (date): Fecha de ingreso
            salario_base (float): Salario base mensual
            porcentaje_comision (float): Porcentaje de comisión (ej: 0.05 = 5%)
            ventas_mes (float): Total de ventas del mes
            
        Raises:
            ValueError: Si algún valor monetario es negativo o inválido
        """
        super().__init__(id_empleado, nombre, fecha_ingreso)
        
        if salario_base <= 0:
            raise ValueError("El salario base debe ser mayor a cero")
        
        if porcentaje_comision < 0 or porcentaje_comision > 1:
            raise ValueError("El porcentaje de comisión debe estar entre 0 y 1")
        
        if ventas_mes < 0:
            raise ValueError("Las ventas no pueden ser negativas")
        
        self._salario_base = salario_base
        self._porcentaje_comision = porcentaje_comision
        self._ventas_mes = ventas_mes
    
    def _calcular_comision(self) -> float:
        """
        Calcula la comisión sobre las ventas.
        
        Returns:
            float: Monto de la comisión
        """
        return self._ventas_mes * self._porcentaje_comision
    
    def _calcular_bono_ventas(self) -> float:
        """
        Calcula el bono adicional por ventas altas.
        Se otorga 3% adicional si las ventas superan $20,000,000.
        
        Returns:
            float: Monto del bono por ventas
        """
        if self._ventas_mes > self.VENTAS_MINIMAS_BONO:
            return self._ventas_mes * self.PORCENTAJE_BONO_VENTAS
        return 0
    
    def calcular_salario_bruto(self) -> float:
        """
        Calcula el salario bruto del empleado por comisión.
        Incluye: salario base + comisión sobre ventas.
        
        Returns:
            float: Salario bruto total
        """
        comision = self._calcular_comision()
        return self._salario_base + comision
    
    def calcular_beneficios(self) -> float:
        """
        Calcula los beneficios del empleado por comisión.
        Incluye: bono de alimentación + bono por ventas altas (si aplica).
        
        Returns:
            float: Total de beneficios
        """
        bono_ventas = self._calcular_bono_ventas()
        return self.BONO_ALIMENTACION + bono_ventas
    
    @property
    def salario_base(self) -> float:
        """Getter del salario base"""
        return self._salario_base
    
    @property
    def porcentaje_comision(self) -> float:
        """Getter del porcentaje de comisión"""
        return self._porcentaje_comision
    
    @property
    def ventas_mes(self) -> float:
        """Getter de las ventas del mes"""
        return self._ventas_mes
    
    @ventas_mes.setter
    def ventas_mes(self, ventas: float):
        """
        Setter de ventas con validación.
        
        Args:
            ventas (float): Nuevas ventas del mes
            
        Raises:
            ValueError: Si las ventas son negativas
        """
        if ventas < 0:
            raise ValueError("Las ventas no pueden ser negativas")
        self._ventas_mes = ventas
    
    def obtener_detalle_nomina(self) -> dict:
        """
        Genera un diccionario con el detalle completo de la nómina.
        
        Returns:
            dict: Diccionario con todos los conceptos de pago
        """
        salario_bruto = self.calcular_salario_bruto()
        comision = self._calcular_comision()
        bono_ventas = self._calcular_bono_ventas()
        deducciones = self.calcular_deducciones(salario_bruto)
        
        return {
            'empleado': self.nombre,
            'tipo': 'Por Comisión',
            'salario_base': self._salario_base,
            'ventas': self._ventas_mes,
            'comision': comision,
            'salario_bruto': salario_bruto,
            'bono_alimentacion': self.BONO_ALIMENTACION,
            'bono_ventas': bono_ventas,
            'deducciones': deducciones,
            'salario_neto': self.calcular_salario_neto()
        }