"""
Autor: Danibe Rodriguez 2-744-2026
Fecha: 02/04/2026
Versión: 1.0

Descripción:
Módulo que contiene funciones matemáticas básicas.
"""

def suma(a, b):
    """Devuelve la suma de dos números."""
    return a + b


def resta(a, b):
    """Devuelve la resta de dos números."""
    return a - b


def multiplicacion(a, b):
    """Devuelve la multiplicación de dos números."""
    return a * b


def division(a, b):
    """
    Devuelve la división de dos números.
    Maneja el error cuando se intenta dividir entre cero.
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        return None