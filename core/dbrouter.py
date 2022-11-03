from typing import Optional


class MultiDBRouter:
    def __init__(self) -> None:
        self.model_list = ["default", "alertdb"]

    def db_for_read(self, model, **hints) -> Optional[str]:
        return model._meta.app_label if model._meta.app_label in self.model_list else None

    def db_for_write(self, model, **hints) -> None:
        return model._meta.app_label if model._meta.app_label in self.model_list else None

    def allow_relation(self, obj1, obj2, **hints) -> Optional[bool]:
        if obj1._meta.app_label in self.model_list or obj2._meta.app_label in self.model_list:
            return True

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints) -> Optional[bool]:
        if app_label == "alert":
            return db == "alertdb"

        return None
