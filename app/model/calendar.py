from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import ClassVar

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error


# TODO: Implement Reminder class here
@dataclass
class Reminder:
    EMAIL: ClassVar[str] = 'email'
    SYSTEM: ClassVar[str] = 'system'
    date_time: datetime
    type: str = EMAIL

    def __str__(self) -> str:
        return f"Reminder on {self.date_time} of type {self.type}"


@dataclass
class Event:
    title: str
    description: str
    date_: date
    start_at: time
    end_at: time
    reminders: list[Reminder] = field(init=False, default_factory=list)
    id: str = generate_unique_id()

    def add_reminder(self, date_time: datetime, reminder_type: str):
        self.reminders.append(Reminder(date_time, reminder_type))

    def delete_reminder(self, reminder_index: int):
        if reminder_index <= (len(self.reminders) - 1):
            self.reminders.pop(reminder_index)
        else:
            reminder_not_found_error()

    def __str__(self):
        return (f"ID: {self.id}\nEvent title: {self.title}\nDescription: {self.description}\nTime: {self.start_at} -"
                f" {self.end_at}")
