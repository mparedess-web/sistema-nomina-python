"""
Clase para empleados que cobran por horas trabajadas.
"""

from datetime import date
from .empleado import Empleado


class EmpleadoPorHoras(Empleado):
    """
    Representa un empleado que cobra por horas trabajadas.
    
    Reglas de negocio:
    - Pago por horas trabajadas a tarifa base
    - Horas extras (más de 40) se pagan a 1.5x la tarifa normal
    - No recibe bonos
    - Con más de 1 año: acceso a fondo de ahorro (2% del salario)
    """
    
    # Constantes
    HORAS_NORMALES_LIMITE = 40
    MULTIPLICADOR_HORAS_EXTRAS = 1.5
    PORCENTAJE_FONDO_AHORRO = 0.02
    AÑOS_MINIMOS_FONDO = 1
    
    def __init__(self, id_empleado: str, nombre: str, fecha_ingreso: date, 
                 tarifa_por_hora: float, horas_trabajadas: float, 
                 acepta_fondo_ahorro: bool = False):
        """
        Constructor del empleado por horas.
        
        Args:
            id_empleado (str): ID único del empleado
            nombre (str): Nombre del empleado
            fecha_ingreso (date): Fecha de ingreso
            tarifa_por_hora (float): Tarifa base por hora
            horas_trabajadas (float): Horas trabajadas en el mes
            acepta_fondo_ahorro (bool): Si acepta el fondo de ahorro
            
        Raises:
            ValueError: Si la tarifa o las horas son negativas
        """
        super().__init__(id_empleado, nombre, fecha_ingreso)
        
        if tarifa_por_hora <= 0:
            raise ValueError("La tarifa por hora debe ser mayor a cero")
        
        if horas_trabajadas < 0:
            raise ValueError("Las horas trabajadas no pueden ser negativas")
        
        self._tarifa_por_hora = tarifa_por_hora
        self._horas_trabajadas = horas_trabajadas
        self._acepta_fondo_ahorro = acepta_fondo_ahorro
    
    def _calcular_horas_normales(self) -> float:
        """
        Calcula las horas trabajadas a tarifa normal.
        
        Returns:
            float: Horas normales (máximo 40)
        """
        return min(self._horas_trabajadas, self.HORAS_NORMALES_LIMITE)
    
    def _calcular_horas_extras(self) -> float:
        """
        Calcula las horas extras trabajadas.
        
        Returns:
            float: Horas extras (si trabajó más de 40 horas)
        """
        if self._horas_trabajadas > self.HORAS_NORMALES_LIMITE:
            return self._horas_trabajadas - self.HORAS_NORMALES_LIMITE
        return 0
    
    def calcular_salario_bruto(self) -> float:
        """
        Calcula el salario bruto del empleado por horas.
        Incluye pago de horas normales + horas extras (1.5x).
        
        Returns:
            float: Salario bruto total
        """
        horas_normales = self._calcular_horas_normales()
        horas_extras = self._calcular_horas_extras()
        
        pago_normal = horas_normales * self._tarifa_por_hora
        pago_extras = horas_extras * self._tarifa_por_hora * self.MULTIPLICADOR_HORAS_EXTRAS
        
        return pago_normal + pago_extras
    
    def _calcular_fondo_ahorro(self) -> float:
        """
        Calcula el aporte al fondo de ahorro.
        Solo aplica si tiene más de 1 año y aceptó el fondo.
        
        Returns:
            float: Monto del fondo de ahorro (beneficio)
        """
        if (self.obtener_antiguedad_años() > self.AÑOS_MINIMOS_FONDO 
            and self._acepta_fondo_ahorro):
            salario_bruto = self.calcular_salario_bruto()
            return salario_bruto * self.PORCENTAJE_FONDO_AHORRO
        return 0
    
    def calcular_beneficios(self) -> float:
        """
        Calcula los beneficios del empleado por horas.
        Solo incluye fondo de ahorro si califica.
        
        Returns:
            float: Total de beneficios
        """
        return self._calcular_fondo_ahorro()
    
    @property
    def tarifa_por_hora(self) -> float:
        """Getter de la tarifa por hora"""
        return self._tarifa_por_hora
    
    @property
    def horas_trabajadas(self) -> float:
        """Getter de horas trabajadas"""
        return self._horas_trabajadas
    
    @horas_trabajadas.setter
    def horas_trabajadas(self, horas: float):
        """
        Setter de horas trabajadas con validación.
        
        Args:
            horas (float): Nuevas horas trabajadas
            
        Raises:
            ValueError: Si las horas son negativas
        """
        if horas < 0:
            raise ValueError("Las horas trabajadas no pueden ser negativas")
        self._horas_trabajadas = horas
    
    def obtener_detalle_nomina(self) -> dict:
        """
        Genera un diccionario con el detalle completo de la nómina.
        
        Returns:
            dict: Diccionario con todos los conceptos de pago
        """
        salario_bruto = self.calcular_salario_bruto()
        fondo_ahorro = self._calcular_fondo_ahorro()
        deducciones = self.calcular_deducciones(salario_bruto)
        
        return {
            'empleado': self.nombre,
            'tipo': 'Por Horas',
            'horas_normales': self._calcular_horas_normales(),
            'horas_extras': self._calcular_horas_extras(),
            'salario_bruto': salario_bruto,
            'fondo_ahorro': fondo_ahorro,
            'deducciones': deducciones,
            'salario_neto': self.calcular_salario_neto()
        }