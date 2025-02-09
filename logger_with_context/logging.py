import logging


class ContextManager():
    data = {}

    def __init__(self):
        pass

    @staticmethod
    def getData() -> dict:
        ContextManager
        return ContextManager.data
    
    @staticmethod
    def setData(data: dict) -> None:
        ContextManager.data = data.copy()
    
    @staticmethod
    def updateData(data: dict) -> None:
        ContextManager.data.update(data)

    @staticmethod
    def clearData() -> None:
        ContextManager.data = {}


class _LoggerWithContext(logging.Logger):
    def _log(self, level, msg, args, exc_info=None, extra=None, stack_info=False, stacklevel=1):
        if extra is None:
            extra = ContextManager.getData().copy()
        else:
            new_extra = ContextManager.getData().copy()
            new_extra.update(extra)
            extra = new_extra
        super()._log(level, msg, args, exc_info, extra, stack_info, stacklevel)

    def setContext(self, context: dict) -> None:
        ContextManager.setData(context)
    
    def updateContext(self, context: dict) -> None:
        ContextManager.updateData(context)

    def clearContext(self) -> None:
        ContextManager.clearData()
        
    def getContext(self) -> dict:
        return ContextManager.getData()


def getLogger(*args, **kargs) -> _LoggerWithContext:
    logging.setLoggerClass(_LoggerWithContext)
    logger = logging.getLogger("main", *args, **kargs)
    return logger

