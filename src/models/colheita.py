"""
Módulo que contém as classes principais do sistema de colheita.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List, Dict

@dataclass
class Colhedora:
    id: str
    capacidade: float
    status: str = "disponível"
    manutencao_proxima: Optional[datetime] = None

    def necessita_manutencao(self) -> bool:
        if not self.manutencao_proxima:
            return False
        return datetime.now() >= self.manutencao_proxima

@dataclass
class AreaColheita:
    id: str
    tamanho: float
    indice_maturacao: float
    data_medicao: datetime
    localizacao: Dict[str, float]  # latitude e longitude
    status: str = "pendente"

class GerenciadorColheita:
    VALOR_IDEAL_MATURACAO = 18.0

    def __init__(self):
        self.areas: List[AreaColheita] = []
        self.colhedoras: List[Colhedora] = []
        self._historico_colheita = []

    def adicionar_area(self, area: AreaColheita) -> None:
        self.areas.append(area)

    def adicionar_colhedora(self, colhedora: Colhedora) -> None:
        self.colhedoras.append(colhedora)

    def calcular_prioridade_colheita(self) -> List[AreaColheita]:
        """Calcula a ordem de prioridade das áreas para colheita."""
        areas_prontas = [
            area for area in self.areas 
            if area.indice_maturacao >= self.VALOR_IDEAL_MATURACAO
        ]
        return sorted(areas_prontas, key=lambda x: x.indice_maturacao, reverse=True)

    def alocar_colhedoras(self) -> Dict[str, str]:
        """Aloca colhedoras para áreas considerando diversos fatores."""
        alocacao = {}
        colhedoras_disponiveis = [c for c in self.colhedoras if not c.necessita_manutencao()]
        areas_prioritarias = self.calcular_prioridade_colheita()

        for area in areas_prioritarias:
            for colhedora in colhedoras_disponiveis:
                if colhedora.capacidade >= area.tamanho:
                    alocacao[area.id] = colhedora.id
                    colhedoras_disponiveis.remove(colhedora)
                    break

        return alocacao
