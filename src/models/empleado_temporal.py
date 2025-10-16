"""
Clase para empleados temporales con contrato por tiempo definido.
"""

from datetime import date
from .empleado import Empleado


class EmpleadoTemporal(Empleado):
    """
    Representa un empleado temporal con contrato por tiempo definido.
    
    Reglas de negocio:
    - Salario fijo mensual
    - Contrato por tiempo definido
    - No aplican bonos ni beneficios adicionales
    """
    
    def __init__(self, id_empleado: str, nombre: str, fecha_ingreso: date,
                 salario_mensual: float, fecha_fin_contrato: date):
        """
        Constructor del empleado temporal.
        
        Args:
            id_empleado (str): ID único del empleado
            nombre (str): Nombre del empleado
            fecha_ingreso (date): Fecha de inicio del contrato
            salario_mensual (float): Salario fijo mensual
            fecha_fin_contrato (date): Fecha de fin del contrato
            
        Raises:
            ValueError: Si el salario es inválido o las fechas no son coherentes
        """
        super().__init__(id_empleado, nombre, fecha_ingreso)
        
        if salario_mensual <= 0:
            raise ValueError("El salario mensual debe ser mayor a cero")
        
        if fecha_fin_contrato <= fecha_ingreso:
            raise ValueError("La fecha de fin debe ser posterior a la fecha de ingreso")
        
        self._salario_mensual = salario_mensual
        self._fecha_fin_contrato = fecha_fin_contrato
    
    def calcular_salario_bruto(self) -> float:
        """
        Calcula el salario bruto del empleado temporal.
        
        Returns:
            float: Salario mensual fijo
        """
        return self._salario_mensual
    
    def calcular_beneficios(self) -> float:
        """
        Calcula los beneficios del empleado temporal.
        Los empleados temporales no reciben beneficios adicionales.
        
        Returns:
            float: 0 (sin beneficios)
        """
        return 0
    
    def contrato_vigente(self) -> bool:
        """
        Verifica si el contrato del empleado está vigente.
        
        Returns:
            bool: True si el contrato está vigente, False si ya venció
        """
        return date.today() <= self._fecha_fin_contrato
    
    def dias_restantes_contrato(self) -> int:
        """
        Calcula los días restantes del contrato.
        
        Returns:
            int: Días restantes (puede ser negativo si el contrato venció)
        """
        diferencia = self._fecha_fin_contrato - date.today()
        return diferencia.days
    
    @property
    def salario_mensual(self) -> float:
        """Getter del salario mensual"""
        return self._salario_mensual
    
    @property
    def fecha_fin_contrato(self) -> date:
        """Getter de la fecha de fin del contrato"""
        return self._fecha_fin_contrato
    
    def obtener_detalle_nomina(self) -> dict:
        """
        Genera un diccionario con el detalle completo de la nómina.
        
        Returns:
            dict: Diccionario con todos los conceptos de pago
        """
        salario_bruto = self.calcular_salario_bruto()
        deducciones = self.calcular_deducciones(salario_bruto)
        
        return {
            'empleado': self.nombre,
            'tipo': 'Temporal',
            'salario_bruto': salario_bruto,
            'beneficios': 0,
            'deducciones': deducciones,
            'salario_neto': self.calcular_salario_neto(),
            'fecha_fin_contrato': self._fecha_fin_contrato.strftime('%Y-%m-%d'),
            'contrato_vigente': self.contrato_vigente(),
            'dias_restantes': self.dias_restantes_contrato()
        }