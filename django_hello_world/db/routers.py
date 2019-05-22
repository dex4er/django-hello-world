from django.conf import settings


class MultiDBRouter:
    @staticmethod
    def db_for_read(model, **_hints):
        return settings.DATABASE_APPS.get(
            model._meta.app_label, settings.DATABASE_APPS.get("*", "default")
        )

    @staticmethod
    def db_for_write(model, **_hints):
        return settings.DATABASE_APPS.get(
            model._meta.app_label, settings.DATABASE_APPS.get("*", "default")
        )

    @staticmethod
    def allow_relation(obj1, obj2, **_hints):
        if (
            obj1._meta.app_label in settings.PROJECT_APPS
            or obj2._meta.app_label in settings.PROJECT_APPS
        ):
            return True

        return None

    @staticmethod
    def allow_migrate(db, app_label, _model=None, **_hints):
        if app_label in settings.PROJECT_APPS:
            return db == settings.DATABASE_APPS[app_label]

        return db == settings.DATABASE_APPS.get("*", "default")
