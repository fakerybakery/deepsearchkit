class DSKUndefinedVariableError(Exception):
    """Custom DeepSearchKit error: Undefined variable"""
    pass
class DSKEmptyDataError(Exception):
    """Custom DeepSearchKit error: Empty dataset"""
    pass
class DSKUnindexedError(Exception):
    """Custom DeepSearchKit error: Index hasn't been created yet"""
    pass
class DSKFeatureNotSupportedError(Exception):
    """Custom DeepSearchKit error: Unsupported feature/WIP feature"""
    pass
