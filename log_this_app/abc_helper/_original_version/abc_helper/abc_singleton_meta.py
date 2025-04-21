# print("abc_helper/abc_singleton_meta.py")
from abc import ABCMeta
from threading import Lock


class AbcSingletonMeta(ABCMeta):

    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        # print(f"📌 Singleton request: {cls.__name__}")
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    # print(f"✅ Vytvářím instanci: {cls.__name__} s args={args}, kwargs={kwargs}")
                    instance = super().__call__(*args, **kwargs)
                    # print(f"🎉 Instanci {cls.__name__} úspěšně vytvořena!")
                    cls._instances[cls] = instance
        else:
            # print(f"🔁 Používám existující instanci: {cls.__name__}")
            pass
        return cls._instances[cls]


    def clear_instance(cls):
        """
        Vymaže instanci singletonu - užitečné pro testování.
        """
        with cls._lock:
            if cls in cls._instances:
                del cls._instances[cls]

