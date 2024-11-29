import os

user = os.getlogin()
new = f'C:\\guiaOrto'
old = f'C:\\Users\\{user}\\Downloads'

def Limpeza_de_downloads_antigos():
#limpando diretório downloads
    for arquivo in os.listdir(old):
        if (arquivo == 'pacientes.xlsx' or arquivo == 'agendamentos.xlsx'):
            os.chdir(old)
            os.remove(arquivo)

def Limpeza_da_pasta_do_programa():
    os.chdir(f'{new}\\Planilhas')
    lista = os.listdir()
    for item in lista:
        os.remove(item)

def Criacao_de_diretorio_e_pastas_do_Programa():
    os.mkdir('C:\\guiaOrto')
    os.mkdir('C:\\guiaOrto\\Planilhas')
    os.mkdir('C:\\guiaOrto\\Agendamentos Orto')
    os.mkdir('C:\\guiaOrto\\Pacientes Orto')
    os.mkdir('C:\\guiaOrto\\Planilha_para_Metabase')


def Mover_arquivos_para_Diretorio_do_programa():
    #movendo o download recém baixado
    for arquivo in os.listdir(old):
        if(arquivo == 'pacientes.xlsx'):
            os.rename(old + '\\pacientes.xlsx', new + '\\Planilhas\\pacientes.xlsx')
        if(arquivo == 'agendamentos.xlsx'):
            os.rename(old + '\\agendamentos.xlsx', new + '\\Planilhas\\agendamentos.xlsx')
