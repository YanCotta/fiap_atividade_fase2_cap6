"""
Módulo com funções auxiliares para o sistema.
"""
import json
from typing import Any, Dict
from datetime import datetime
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def configurar_logging():
    """Configura o sistema de logging."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('colheita.log'),
            logging.StreamHandler()
        ]
    )

def validar_data(data_str: str) -> datetime:
    """Valida e converte uma string de data para objeto datetime."""
    try:
        return datetime.strptime(data_str, "%d/%m/%Y")
    except ValueError as e:
        raise ValueError("Data inválida. Use o formato DD/MM/YYYY.") from e

def carregar_json(arquivo: str) -> Dict[str, Any]:
    """Carrega dados de um arquivo JSON."""
    caminho = Path(arquivo)
    if not caminho.exists():
        return {}
    
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f"Erro ao ler arquivo JSON {arquivo}: {e}")
        return {}

def salvar_json(dados: Dict[str, Any], arquivo: str) -> bool:
    """Salva dados em um arquivo JSON."""
    try:
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        logger.error(f"Erro ao salvar arquivo JSON {arquivo}: {e}")
        return False

def calcular_eficiencia_colheita(producao_real: float, producao_estimada: float) -> float:
    """Calcula a eficiência da colheita."""
    if producao_estimada == 0:
        return 0
    return (producao_real / producao_estimada) * 100

def validar_coordenadas(lat: float, lon: float) -> bool:
    """Valida coordenadas geográficas."""
    return -90 <= lat <= 90 and -180 <= lon <= 180
