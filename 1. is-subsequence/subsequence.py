class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        result = [] # vetor final onde vou avaliar se a ordem se manteve
        
        i = 0 # defino a variavel do for para guardar o progresso no vetor secundario "t"

        for letra in s: # olho cada letra no vetor principal "s"
            
            # encontro a letra do vetor principal "s" no vetor secundario "t"
            # alem disso se a letra não estiver no vetor ele para também
            while i < len(t) and letra != t[i]: 
                i += 1 
                
            if i == len(t): # if corrigido: se o i chegou ao tamanho de t, a letra não existe
                return False
                
            result.append(i) # acrecento a posição da letra do vetor secundario ao meu vetor final
            i += 1 # avanço o i aqui para a próxima letra de 's' não usar a mesma posição
    
        resposta = result == sorted(result)
        # Se o vetor estiver ordenado, ele deve retornar true, logo a ordem do subvetor se manteve
        # Se o vetor não estiver ordenado ele retorna false e a logica do subvetor não se manteve
        return resposta