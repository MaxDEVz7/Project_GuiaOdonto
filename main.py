from login import *
from downloads_automação import *
from Criação_das_planilhas import *

import sqlite3
import csv

# Importando CSV
arquivo_csv = new + '\\Planilha_para_Metabase\\planilha_com_todos_pacientes_orto_com_status.csv'
db = r"C:\Users\maxwi\Esamc_PERIODO1_SI\Esamc inovação e comunicação\code\ProjetoGuiaOdonto.db"

# Conectando ao banco de dados
conn = sqlite3.connect(db)
cursor = conn.cursor()

# Verificar se a tabela existe e apagá-la, se necessário
cursor.execute("DROP TABLE IF EXISTS agendamentos_auto")

# Criando tabela com as colunas correspondentes ao CSV
cursor.execute('''
CREATE TABLE agendamentos_auto (
    Nome TEXT,
    Telefone TEXT,
    E_mail TEXT,
    Data_nascimento TEXT, 
    Cidade TEXT,
    CPF TEXT,
    Convenio TEXT,
    Status TEXT,
    Data_Consulta TEXT
)
''')

# Lendo o CSV com codificação ajustada
with open(arquivo_csv, newline='', encoding='utf-8') as csvfile:  # Use 'latin1' ou outra codificação identificada
    leitor = csv.reader(csvfile)
    colunas = next(leitor)  # Lê o cabeçalho do CSV
    

    
    # Garantir que o número de colunas no CSV é o mesmo da tabela
    if len(colunas) != 9:
        raise ValueError(f"CSV possui {len(colunas)} colunas, mas a tabela exige 9 colunas!")

    # Gerar query dinamicamente com base nas colunas
    query_inserir = f"INSERT INTO agendamentos_auto ({', '.join(colunas)}) VALUES ({', '.join('?' for _ in colunas)})"
    
    # Inserir os dados diretamente sem substituições
    for linha in leitor:
        # try:
            # Substituir valores vazios ('') por None (NULL no SQLite)
            linha = [None if valor.strip() == '' else valor for valor in linha]

             # Substituindo valores de uma coluna específica (por exemplo, coluna 'Status')
            for i, valor in enumerate(linha):
                # Verifique a coluna de interesse (exemplo: Status está na última coluna)
                if colunas[i] == 'Data_Consulta':
                    if valor == 'Sem Registro':
                        linha[i] = None
                              
            cursor.execute(query_inserir, linha)
        # except sqlite3.OperationalError as e:
        #     print(f"Erro ao inserir linha {linha}: {e}")
        # except Exception as ex:
        #     print(f"Erro inesperado ao inserir linha {linha}: {ex}")

# Salvar alterações e fechar conexão
conn.commit()
conn.close()

print("CSV importado com sucesso para o SQLite!")
