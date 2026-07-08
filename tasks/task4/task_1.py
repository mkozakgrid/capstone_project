from datetime import datetime

def calculate_days(from_date: str) -> int:
    try:
        formatted_date = datetime.strptime(from_date, "%Y-%m-%d")
        return (datetime.now() - datetime.strptime(from_date, formatted_date)).days()
    except ValueError:
        raise ValueError("Invalid date format")