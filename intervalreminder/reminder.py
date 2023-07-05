from datetime import datetime
from typing import Dict, List, NamedTuple


# TODO: I got next error here: ModuleNotFoundError: No module named 'database'
from . import database

class Remind(NamedTuple):
    """Структура надпоминания"""
    raw_text: str
    created: datetime
    updated: datetime
    done: bool
    repeats: int


class Reminders:
    def __init__(self):
        self._reminders: List[Remind] = self._load_reminders()

    def _load_reminders(self) -> List[Remind]:
        print(database.get_cursor, database.fetchall)
        
        reminders = database.fetchall(
            database.REMINDS_TABLE, "raw_text created updated done repeats".split()
        )
        reminds = self._fill_reminders(reminders)
        return reminds


    def _fill_reminders(self, reminders: List[Dict]) -> List[Remind]:
        date_format = '%Y-%m-%d %H:%M:%S'
        reminds = []
        for _, remind in enumerate(reminders):
            reminds.append(Remind(
                remind["raw_text"],
                datetime.strptime(remind["created"], date_format),
                datetime.strptime(remind["updated"], date_format),
                remind["done"],
                remind["repeats"])
            )
        return reminds
    

    def get_all_reminders(self) -> List[Remind]:
        """Возвращает справочник надпоминаний"""
        return self._reminders
    

    def get_remind(self, id):
        pass

