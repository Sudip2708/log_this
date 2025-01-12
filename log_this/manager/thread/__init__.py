from .thread_context import ThreadContext, thread

__all__ = [
    "ThreadContext",  # Singleton třída spravující vlákno pro logování.
    "thread",  # Singleton instanci třífy ThreadContext
]