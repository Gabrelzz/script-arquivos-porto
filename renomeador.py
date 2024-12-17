import pandas as pd
import os

arquivos_renomear = {
    "EvolucaoVidas": "[1] - Evolucao_de_Vidas.csv",
    "EvolucaoSinistralidade": "[2] - Sinistralidade_Geral.csv",
    "ApoliceVersusExperiencia": "[3] - Eventos_Sinistros.csv",
    "RankingMaiorNumeroConsultas": "[4] - Hiperconsultores.csv",
    "RankingMaiorSinistralidade": "[5] - High_Users.csv",
    "RankingMaisReembolsados": "[6] - Reembolso.csv",
    "RankingPontosSocorros": "[7] - Pronto_Socorros.csv",
    "RankingConsultorioClinicaAmbulatorio": "[8] - Clínicas.csv",
    "RankingLaboratorios": "[9] - Laboratórios.csv",
    "RankingHospitaisMaternidades": "[10] - Hospitais.csv",

    }
    
def renomear():
    for arquivo in os.listdir():
        for prefixo, novo_nome in arquivos_renomear.items():
                if arquivo.startswith(prefixo) and arquivo.endswith('.csv'):
                    os.rename(arquivo, novo_nome)
                    arquivo = novo_nome
renomear()