"""
Autor: Danibe Rodriguez 2-744-2026
Fecha: 02/04/2026
Versión: 1.0

Descripción:
Módulo que contiene funciones geométricas.
"""

import math


def area_circulo(radio):
    """Devuelve el área de un círculo."""
    return math.pi * radio ** 2


def perimetro_circulo(radio):
    """Devuelve el perímetro de un círculo."""
    return 2 * math.pi * radio


def area_rectangulo(base, altura):
    """Devuelve el área de un rectángulo."""
    return base * altura


def perimetro_rectangulo(base, altura):
    """Devuelve el perímetro de un rectángulo."""
    return 2 * (base + altura)