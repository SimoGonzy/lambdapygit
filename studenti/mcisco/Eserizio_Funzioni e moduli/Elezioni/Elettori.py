#Elettori

def vota_candidato(lista_partiti, nome_partito: str, nome_candidato: str):
    # Cerco il partito e il candidato
    for pos_par in range(len(lista_partiti)):
        if lista_partiti[pos_par]["nome"] == nome_partito:
            for pos_cand in range(len(lista_partiti[pos_par]["candidati"])):
                if lista_partiti[pos_par]["candidati"][pos_cand]["nome"] == nome_candidato:
                    lista_partiti[pos_par]["candidati"][pos_cand]["n_voti"] +=1
                    return
                