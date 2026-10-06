from __future__ import annotations

from typing import Any, Dict

from apscheduler.schedulers.background import BackgroundScheduler


class SchedulerService:
    def __init__(self) -> None:
        self.scheduler = BackgroundScheduler()

    def start(self) -> None:
        if not self.scheduler.running:
            self.scheduler.start()

    def stop(self) -> None:
        if self.scheduler.running:
            self.scheduler.shutdown()

    def add_job(self, func, trigger: str, **kwargs) -> None:
        self.scheduler.add_job(func, trigger, **kwargs)


scheduler_service = SchedulerService()
