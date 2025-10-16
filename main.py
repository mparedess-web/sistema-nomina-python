"""
Sistema de Nómina - Archivo Principal
Demuestra el funcionamiento del sistema con ejemplos de todos los tipos de empleados.
"""

from datetime import date
from src.models.empleado_asalariado import EmpleadoAsalariado
from src.models.empleado_por_horas import EmpleadoPorHoras
from src.models.empleado_por_comision import EmpleadoPorComision
from src.models.empleado_temporal import EmpleadoTemporal


def imprimir_separador():
    """Imprime una línea separadora para mejor visualización"""
    print("\n" + "=" * 80 + "\n")


def mostrar_detalle_nomina(empleado):
    """
    Muestra el detalle completo de la nómina de un empleado.
    
    Args:
        empleado: Instancia de cualquier tipo de empleado
    """
    print(f"📋 DETALLE DE NÓMINA")
    print(f"{'─' * 80}")
    
    detalle = empleado.obtener_detalle_nomina()
    
    for clave, valor in detalle.items():
        if isinstance(valor, float):
            print(f"{clave.replace('_', ' ').title():.<40} ${valor:,.2f}")
        else:
            print(f"{clave.replace('_', ' ').title():.<40} {valor}")
    
    imprimir_separador()


def main():
    """Función principal que demuestra el uso del sistema de nómina"""
    
    print("\n🏢 SISTEMA DE NÓMINA - DEMOSTRACIÓN")
    imprimir_separador()
    
    # =============================================================================
    # EJEMPLO 1: Empleado Asalariado
    # =============================================================================
    print("👤 EJEMPLO 1: EMPLEADO ASALARIADO")
    print("Salario fijo con bono por antigüedad (si > 5 años)")
    imprimir_separador()
    
    # Empleado con más de 5 años (recibe bono de antigüedad)
    emp_asalariado1 = EmpleadoAsalariado(
        id_empleado="001",
        nombre="Juan Pérez",
        fecha_ingreso=date(2018, 1, 15),  # Más de 5 años
        salario_mensual=5_000_000
    )
    
    print(f"Empleado: {emp_asalariado1.nombre}")
    print(f"Antigüedad: {emp_asalariado1.obtener_antiguedad_años()} años")
    mostrar_detalle_nomina(emp_asalariado1)
    
    # Empleado con menos de 5 años (NO recibe bono de antigüedad)
    emp_asalariado2 = EmpleadoAsalariado(
        id_empleado="002",
        nombre="María González",
        fecha_ingreso=date(2022, 6, 1),  # Menos de 5 años
        salario_mensual=4_500_000
    )
    
    print(f"Empleado: {emp_asalariado2.nombre}")
    print(f"Antigüedad: {emp_asalariado2.obtener_antiguedad_años()} años")
    mostrar_detalle_nomina(emp_asalariado2)
    
    # =============================================================================
    # EJEMPLO 2: Empleado Por Horas
    # =============================================================================
    print("👤 EJEMPLO 2: EMPLEADO POR HORAS")
    print("Pago por horas + horas extras (1.5x) + fondo de ahorro (si > 1 año)")
    imprimir_separador()
    
    # Empleado con horas extras y fondo de ahorro
    emp_por_horas1 = EmpleadoPorHoras(
        id_empleado="003",
        nombre="Carlos Rodríguez",
        fecha_ingreso=date(2022, 3, 10),  # Más de 1 año
        tarifa_por_hora=50_000,
        horas_trabajadas=45,  # 5 horas extras
        acepta_fondo_ahorro=True
    )
    
    print(f"Empleado: {emp_por_horas1.nombre}")
    print(f"Tarifa por hora: ${emp_por_horas1.tarifa_por_hora:,.2f}")
    print(f"Horas trabajadas: {emp_por_horas1.horas_trabajadas}")
    mostrar_detalle_nomina(emp_por_horas1)
    
    # Empleado sin horas extras
    emp_por_horas2 = EmpleadoPorHoras(
        id_empleado="004",
        nombre="Ana Martínez",
        fecha_ingreso=date(2024, 8, 1),  # Menos de 1 año
        tarifa_por_hora=45_000,
        horas_trabajadas=35,  # Sin horas extras
        acepta_fondo_ahorro=False
    )
    
    print(f"Empleado: {emp_por_horas2.nombre}")
    print(f"Tarifa por hora: ${emp_por_horas2.tarifa_por_hora:,.2f}")
    print(f"Horas trabajadas: {emp_por_horas2.horas_trabajadas}")
    mostrar_detalle_nomina(emp_por_horas2)
    
    # =============================================================================
    # EJEMPLO 3: Empleado Por Comisión
    # =============================================================================
    print("👤 EJEMPLO 3: EMPLEADO POR COMISIÓN")
    print("Salario base + comisión + bono por ventas altas (si > $20M)")
    imprimir_separador()
    
    # Empleado con ventas altas (recibe bono adicional)
    emp_comision1 = EmpleadoPorComision(
        id_empleado="005",
        nombre="Luis Torres",
        fecha_ingreso=date(2020, 5, 20),
        salario_base=2_000_000,
        porcentaje_comision=0.05,  # 5%
        ventas_mes=25_000_000  # Supera los $20M
    )
    
    print(f"Empleado: {emp_comision1.nombre}")
    print(f"Salario base: ${emp_comision1.salario_base:,.2f}")
    print(f"Comisión: {emp_comision1.porcentaje_comision * 100}%")
    print(f"Ventas del mes: ${emp_comision1.ventas_mes:,.2f}")
    mostrar_detalle_nomina(emp_comision1)
    
    # Empleado con ventas bajas (NO recibe bono adicional)
    emp_comision2 = EmpleadoPorComision(
        id_empleado="006",
        nombre="Patricia Silva",
        fecha_ingreso=date(2021, 9, 15),
        salario_base=2_500_000,
        porcentaje_comision=0.04,  # 4%
        ventas_mes=15_000_000  # No supera los $20M
    )
    
    print(f"Empleado: {emp_comision2.nombre}")
    print(f"Salario base: ${emp_comision2.salario_base:,.2f}")
    print(f"Comisión: {emp_comision2.porcentaje_comision * 100}%")
    print(f"Ventas del mes: ${emp_comision2.ventas_mes:,.2f}")
    mostrar_detalle_nomina(emp_comision2)
    
    # =============================================================================
    # EJEMPLO 4: Empleado Temporal
    # =============================================================================
    print("👤 EJEMPLO 4: EMPLEADO TEMPORAL")
    print("Contrato por tiempo definido, sin bonos ni beneficios")
    imprimir_separador()
    
    emp_temporal = EmpleadoTemporal(
        id_empleado="007",
        nombre="Roberto Díaz",
        fecha_ingreso=date(2024, 10, 1),
        salario_mensual=3_000_000,
        fecha_fin_contrato=date(2025, 12, 31)
    )
    
    print(f"Empleado: {emp_temporal.nombre}")
    print(f"Salario: ${emp_temporal.salario_mensual:,.2f}")
    print(f"Contrato vigente: {'Sí' if emp_temporal.contrato_vigente() else 'No'}")
    print(f"Días restantes: {emp_temporal.dias_restantes_contrato()}")
    mostrar_detalle_nomina(emp_temporal)
    
    # =============================================================================
    # RESUMEN FINAL
    # =============================================================================
    print("📊 RESUMEN DE NÓMINA TOTAL")
    imprimir_separador()
    
    empleados = [
        emp_asalariado1, emp_asalariado2,
        emp_por_horas1, emp_por_horas2,
        emp_comision1, emp_comision2,
        emp_temporal
    ]
    
    total_salarios = sum(emp.calcular_salario_neto() for emp in empleados)
    
    print(f"{'Total de empleados:':.<40} {len(empleados)}")
    print(f"{'Total de nómina mensual:':.<40} ${total_salarios:,.2f}")
    
    imprimir_separador()
    print("✅ Sistema de nómina funcionando correctamente")
    print("📝 Todos los principios SOLID implementados")
    print("🧪 Listo para pruebas unitarias\n")


if __name__ == "__main__":
    main()