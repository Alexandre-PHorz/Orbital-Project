from datetime import datetime, timedelta
import locale

# Configura o idioma para português para pegar "Sexta-feira" em vez de "Friday"
# No Windows use: locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')
# No Linux use:
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except:
    locale.setlocale(locale.LC_ALL, '') # Fallback caso o sistema não tenha o pacote pt_BR

def get_semana_atual():
    hoje = datetime.now()
    
    # Encontra o domingo desta semana
    # weekday() retorna 0 para Segunda e 6 para Domingo. 
    # Para considerar Domingo como início (índice 0), usamos o cálculo abaixo:
    dias_para_tras = (hoje.weekday() + 1) % 7
    domingo = hoje - timedelta(days=dias_para_tras)
    
    semana = []
    
    for i in range(7):
        dia_da_semana = domingo + timedelta(days=i)
        
        # Formata os dados
        dados_dia = {
            "data": dia_da_semana.strftime("%Y-%m-%d"), # Formato 2025-01-16
            "dia_semana": dia_da_semana.strftime("%A").split('-')[0].capitalize() # Nome do dia
        }
        semana.append(dados_dia)
        
    return semana

# Testando
lista_datas = get_semana_atual()
for d in lista_datas:
    print(f"{d['data']} - {d['dia_semana']}")