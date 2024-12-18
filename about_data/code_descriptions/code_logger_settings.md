Import závislostí:

    import logging
    
Definice funkce:

    def loger_settings():

Nastavení loggeru:
    
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(message)s',
            handlers=[logging.StreamHandler()]
        )
    
Vrácení logeru:

        return logging.getLogger('LogThis')