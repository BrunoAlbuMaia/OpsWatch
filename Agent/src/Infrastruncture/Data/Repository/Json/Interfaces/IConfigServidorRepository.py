import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from abc import ABC, abstractmethod
from typing import Dict,Any

class IConfigServidorRepository:
    @abstractmethod
    async def get_dados(self):
        pass
    @abstractmethod
    async def update_dados(self,dados: Dict[str, Any]):
        pass