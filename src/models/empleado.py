"""
Clase base abstracta para todos los tipos de empleados.
Implementa principios SOLID: Single Responsibility y Open/Closed.
"""

from abc import ABC, abstractmethod
from datetime import date

class Empleado(ABC):
    """
    Clase base abstracta que representa un empleado genérico.
    Define los atributos y métodos comunes a todos los empleados.
    """
    
    def __init__(self, id_empleado: str, nombre: str, fecha_ingreso: date):
        """
        Constructor de la clase Empleado.
        
        Args:
            id_empleado (str): Identificador único del empleado
            nombre (str): Nombre completo del empleado
            fecha_ingreso (date): Fecha de ingreso a la empresa
        """
        self._id_empleado = id_empleado
        self._nombre = nombre
        self._fecha_ingreso = fecha_ingreso
        self._validar_datos()
    
    def _validar_datos(self):
        """
        Valida que los datos básicos del empleado sean correctos.
        
        Raises:
            ValueError: Si algún dato es inválido
        """
        if not self._id_empleado or not self._nombre:
            raise ValueError("ID y nombre son obligatorios")
        
        if self._fecha_ingreso > date.today():
            raise ValueError("La fecha de ingreso no puede ser futura")
    
    @abstractmethod
    def calcular_salario_bruto(self) -> float:
        """
        Método abstracto para calcular el salario bruto.
        Cada tipo de empleado implementará su propia lógica.
        
        Returns:
            float: Salario bruto del empleado
        """
        pass
    
    @abstractmethod
    def calcular_beneficios(self) -> float:
        """
        Método abstracto para calcular beneficios adicionales.
        
        Returns:
            float: Total de beneficios
        """
        pass
    
    def calcular_deducciones(self, salario_bruto: float) -> float:
        """
        Calcula las deducciones obligatorias.
        Seguro Social y Pensión: 4% del salario bruto.
        
        Args:
            salario_bruto (float): Salario bruto del empleado
            
        Returns:
            float: Total de deducciones
        """
        return salario_bruto * 0.04
    
    def calcular_salario_neto(self) -> float:
        """
        Calcula el salario neto del empleado.
        Salario Neto = Salario Bruto + Beneficios - Deducciones
        
        Returns:
            float: Salario neto (nunca negativo)
        """
        salario_bruto = self.calcular_salario_bruto()
        beneficios = self.calcular_beneficios()
        deducciones = self.calcular_deducciones(salario_bruto)
        
        salario_neto = salario_bruto + beneficios - deducciones
        
        # Validación: el salario neto no puede ser negativo
        return max(0, salario_neto)
    
    def obtener_antiguedad_años(self) -> int:
        """
        Calcula los años de antigüedad del empleado.
        
        Returns:
            int: Años completos trabajados
        """
        hoy = date.today()
        años = hoy.year - self._fecha_ingreso.year
        
        # Ajustar si aún no ha cumplido años este año
        if (hoy.month, hoy.day) < (self._fecha_ingreso.month, self._fecha_ingreso.day):
            años -= 1
        
        return años
    
    # Getters
    @property
    def id_empleado(self) -> str:
        return self._id_empleado
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def fecha_ingreso(self) -> date:
        return self._fecha_ingreso
    
    def __str__(self) -> str:
        """Representación en string del empleado"""
        return f"{self.__class__.__name__}: {self._nombre} (ID: {self._id_empleado})"