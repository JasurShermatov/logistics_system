"""Qo'shimcha validatsiya funksiyalari."""
from datetime import date


def validate_period_dates(start_date: date, end_date: date) -> bool:
    """Period sanalari to'g'ri ekanini tekshirish."""
    return start_date <= end_date
