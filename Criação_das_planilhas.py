from Funções_em_diretórios import new

import openpyxl
import pandas as pd
import os
import re

wb = openpyxl.load_workbook(new + '\\Planilhas\\pacientes.xlsx')
ws_planilha_paciente = wb.active

wb2= openpyxl.load_workbook(new + '\\Planilhas\\agendamentos.xlsx')
ws_planilha_agendamentos = wb2.active

regex = r'([a-z A-Z à-ú À-Ú]+?\s*\d+)'

agendamento = {
    'Nome': [],
    'Telefone': [],
    'E-mail': [],
    'Data nascimento': [],
    'Cidade': [],
    'CPF': [],
    'Convenio':[],
    'Dentista': [],
    'Consulta': [],
    'Status': []
}
pacientes = {
    'Nome': [],
    'Telefone': [],
    'E-mail': [],
    'Data nascimento': [],
    'Cidade': [],
    'CPF': [],
    'Convenio':[]
}

planilha_todos_pacientes_com_status = {
    'Nome': [],
    'Telefone': [],
    'E_mail': [],
    'Data_nascimento': [],
    'Cidade': [],
    'CPF': [],
    'Convenio':[],
    'Data_Consulta': [],
    'Status': []
}

for a in ws_planilha_agendamentos.rows:
    for b in re.findall(regex, a[0].value):
        #Criando_planilha com todos pacientes de orto com o horario marcado
        agendamento['Nome'].append(b)
        agendamento['Telefone'].append(a[7].value)
        agendamento['E-mail'].append(None)
        agendamento['Data nascimento'].append(None)
        agendamento['Cidade'].append(None)
        agendamento['CPF'].append(None)
        agendamento['Convenio'].append(None)
        agendamento['Consulta'].append(a[1].value)
        agendamento['Status'].append(a[5].value)
        agendamento['Dentista'].append(a[6].value)
        
        #Criando_planilha com todos pacientes de orto com o horario marcado ou não
        
        planilha_todos_pacientes_com_status['Nome'].append(b)
        planilha_todos_pacientes_com_status['Telefone'].append(a[7].value)
        planilha_todos_pacientes_com_status['E_mail'].append(None)
        planilha_todos_pacientes_com_status['Data_nascimento'].append(None)
        planilha_todos_pacientes_com_status['Cidade'].append(None)
        planilha_todos_pacientes_com_status['CPF'].append(None)
        planilha_todos_pacientes_com_status['Convenio'].append(None)
        planilha_todos_pacientes_com_status['Status'].append(a[5].value)
        planilha_todos_pacientes_com_status['Data_Consulta'].append(a[1].value)
        
        
    for s in agendamento['Nome']:
        num = agendamento['Nome'].index(s)
        agendamento['Nome'][num] = re.sub(r'\s{2,}', ' ', s)
        num = planilha_todos_pacientes_com_status['Nome'].index(s)
        planilha_todos_pacientes_com_status['Nome'][num] = re.sub(r'\s{2,}', ' ', s)
        
for i in ws_planilha_paciente.rows:    
    for j in re.findall(regex, i[0].value):
        pacientes['Nome'].append(j)
        pacientes['Telefone'].append(i[3].value)
        pacientes['E-mail'].append(i[5].value)
        pacientes['Data nascimento'].append(i[6].value)
        pacientes['Cidade'].append(i[12].value)
        pacientes['CPF'].append(i[11].value)
        pacientes['Convenio'].append(i[13].value)
        if(not j in agendamento['Nome']): #Criando_planilha com todos pacientes de orto com o horario marcado ou não
            planilha_todos_pacientes_com_status['Nome'].append(j)
            planilha_todos_pacientes_com_status['Telefone'].append(i[3].value)
            planilha_todos_pacientes_com_status['E_mail'].append(i[5].value)
            planilha_todos_pacientes_com_status['Data_nascimento'].append(i[6].value)
            planilha_todos_pacientes_com_status['Cidade'].append(i[12].value)
            planilha_todos_pacientes_com_status['CPF'].append(i[11].value)
            planilha_todos_pacientes_com_status['Convenio'].append(i[13].value)
            planilha_todos_pacientes_com_status['Status'].append('Sem registro')
            planilha_todos_pacientes_com_status['Data_Consulta'].append('Sem registro')

    if i[0].value in agendamento['Nome']:
        num = agendamento['Nome'].index(i[0].value)
        agendamento['E-mail'][num] = i[5].value
        agendamento['Data nascimento'][num] = i[6].value
        agendamento['Cidade'][num] = i[12].value
        agendamento['CPF'][num] = i[11].value
        agendamento['Convenio'][num] = i[13].value

        planilha_todos_pacientes_com_status['E_mail'][num] = i[5].value
        planilha_todos_pacientes_com_status['Data_nascimento'][num] = i[6].value
        planilha_todos_pacientes_com_status['Cidade'][num] = i[12].value
        planilha_todos_pacientes_com_status['CPF'][num] = i[11].value
        planilha_todos_pacientes_com_status['Convenio'][num] = i[13].value



os.chdir(f'{new}\\Pacientes Orto')
df= pd.DataFrame.from_dict(pacientes, orient='index')
df = df.transpose()
df.to_excel('pacientes_orto.xlsx', index=False)
df.to_csv('pacientes_orto.csv', index=False)

os.chdir(f'{new}\\Agendamentos Orto')
df2 = pd.DataFrame.from_dict(agendamento, orient='index')
df2 = df2.transpose()
df2.to_excel('agendamento_orto.xlsx', index=False)
df2.to_csv('agendamento_orto.csv', index=False)

os.chdir(f'{new}\\Planilha_para_Metabase')
df3 = pd.DataFrame.from_dict(planilha_todos_pacientes_com_status, orient='index')
df3 = df3.transpose()
df3.to_excel('planilha_com_todos_pacientes_orto_com_status.xlsx', index=False)
df3.to_csv('planilha_com_todos_pacientes_orto_com_status.csv', index=False, encoding= 'utf-8')

