from .base import *

if APP_INSTANCE == 'dev':
    from .dev import *
else:
    from .prod import *
