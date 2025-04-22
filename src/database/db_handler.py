"""
Módulo responsável pela interação com o banco de dados Oracle.
"""
import cx_Oracle
from typing import Dict, Any
from datetime import datetime
from ..config.database import DB_CONFIG
import logging

logger = logging.getLogger(__name__)

class DatabaseHandler:
    def __init__(self):
        self.config = DB_CONFIG

    def _get_connection(self):
        try:
            return cx_Oracle.connect(
                user=self.config['user'],
                password=self.config['password'],
                dsn=self.config['dsn']
            )
        except cx_Oracle.Error as e:
            logger.error(f"Erro ao conectar ao banco de dados: {e}")
            raise

    def salvar_colheita(self, dados_colheita: Dict[str, Any]) -> bool:
        """
        Salva os dados da colheita no banco de dados.
        
        Args:
            dados_colheita: Dicionário com os dados da colheita
        
        Returns:
            bool: True se salvou com sucesso, False caso contrário
        """
        query = """
            INSERT INTO colheitas (
                data_colheita, area_id, colhedora_id, 
                indice_maturacao, perda_estimada, producao_total
            ) VALUES (
                :data_colheita, :area_id, :colhedora_id,
                :indice_maturacao, :perda_estimada, :producao_total
            )
        """
        
        try:
            with self._get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query, dados_colheita)
                connection.commit()
            return True
        except cx_Oracle.Error as e:
            logger.error(f"Erro ao salvar dados da colheita: {e}")
            return False

    def obter_historico_colheitas(self, data_inicio: datetime, data_fim: datetime) -> list:
        """
        Obtém o histórico de colheitas em um período específico.
        """
        query = """
            SELECT * FROM colheitas 
            WHERE data_colheita BETWEEN :data_inicio AND :data_fim
            ORDER BY data_colheita DESC
        """
        
        try:
            with self._get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query, {
                        'data_inicio': data_inicio,
                        'data_fim': data_fim
                    })
                    return cursor.fetchall()
        except cx_Oracle.Error as e:
            logger.error(f"Erro ao obter histórico de colheitas: {e}")
            return []
