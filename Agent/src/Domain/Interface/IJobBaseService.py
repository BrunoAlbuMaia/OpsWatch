from abc import ABC,abstractmethod
from typing	 import Dict, Any
class IJobBaseService(ABC):
    @abstractmethod
    async def execute_job(self,job:Dict[str,Any]):
        pass
    