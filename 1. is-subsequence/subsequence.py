class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        result = [] # vetor final onde vou avaliar se a ordem se manteve

        for letra in s: # olho cada letra no vetor principal "s"
            i = 0 # defino uma variavel para guardar o indice no vetor secundario "t"
            
            # encontro a letra do vetor principal "s" no vetor secundario "t"
            # alem disso se a letra não estiver no vetor ele para também
            while i < len(t) and letra != t[i]: 
                if i > len(t):
                   return False
                   
                i += 1 
                
            result.append(i) # acrecento a posição da letra do vetor secundario ao meu vetor final
    
        resposta = result == sorted(result)
        # Se o vetor estiver ordenado, ele deve retornar true, logo a ordem do subvetor se manteve
        # Se o vetor não estiver ordenado ele retorna false e a logica do subvetor não se manteve
        return resposta 