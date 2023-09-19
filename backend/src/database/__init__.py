import time
from datetime import datetime
import decouple
from supabase_py import create_client


class SupabaseConnect:
    """Classe para gerenciar a conexão com a base de dados"""

    def __init__(self) -> None:
        """Metodo para iniciar conexão com a base inmemory SQLite"""
        try:
            self.url = decouple.config("SUPABASE_URL")
            self.key = decouple.config("SUPABASE_KEY_PUB")
        except Exception as e:
            raise Exception("Erro de leitura do .env" + f"{e}")
        self.max_tentativas = 3
        self.retry_delay = 5

    def criar_client(self):
        """Criar conexão com a base de dados
        com mecanismo de retry e controle de pool
        utilizando base de dados in-memory para teste local de funcionalidades
        :return: Client Supabase
        :rtype: <class 'postgrest.base_request_builder.APIResponse'>
        """
        for tentativa in range(1, self.max_tentativas + 1):
            try:
                supabase = create_client(supabase_url=self.url, supabase_key=self.key)
                print(
                    f"[{datetime.now()}] [SC-RIDE] DB CONECTADO: ",
                    supabase,
                )
                return supabase
            except Exception as e:
                # Handle the exception
                print(
                    "Error de conexão"
                    + f"(tentativa {tentativa}/{self.max_tentativas}): {e}"
                )
                if tentativa < self.max_tentativas:
                    print(f"Tentando novamente em {self.retry_delay} segundos...")
                    time.sleep(self.retry_delay)
                else:
                    print("Número máximo de tentativas atingido. Saindo...")
                    raise Exception("Erro de conexão com Base de Dados" + f"{e}")


class ObjetoSQL:
    """Classe para gerenciar as operações de CRUD nos objetos SQL"""

    def __init__(self):
        self.obj_connect = SupabaseConnect()
        self.client = self.obj_connect.criar_client()

    def processar_query_select(self, tabela: str, query='*') -> dict:
        """Metodo para aplicar select em uma tabela
        :return: retorno após rodar a query
        :rtype: <string>
        """
        try:
            output = self.client.table(tabela).select(query).execute()
        except Exception as e:
            del self.obj_connect
            raise Exception("Erro ao tentar executar select" + f"{e}")
        return output

    def processar_query_insert(self, tabela: str, dados: dict):
        """Metodo para aplicar inserção de informações em uma tabela
        :return: retorno após rodar a query
        :rtype: <string>
        """
        try:
            data, _ = self.client.table(tabela).insert(dados).execute()
        except Exception:
            del self.obj_connect
            raise Exception("Erro ao tentar executar insert" + f"{e}")
        return data

    def encerrar(self):
        """Metodo para encerrrar conexão com base de dados e limpar os objetos em memória"""
        del self.obj_connect
