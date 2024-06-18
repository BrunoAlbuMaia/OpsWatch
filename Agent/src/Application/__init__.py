from .Controllers import JobsController
from .Controllers.JobShedulerController import JobShedulerController
from .Controllers.PluginController import PluginController
from .Controllers.ServidorController import ServidorController


from .Routes.JobsRoute import router as jobs
from .Routes.JobsSchedulerRoute import router as jobsSheduler
from .Routes.PluginRoute import router as plugin
from .Routes.ServidorRoute import router as servidor


from .program import DependencyContainer