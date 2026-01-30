"""Period export (CSV/Excel)."""
import csv
from typing import List, Dict
from io import StringIO


def export_to_csv(data: List[Dict], headers: List[str]) -> str:
    """CSV export qilish."""
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)
    return output.getvalue()
