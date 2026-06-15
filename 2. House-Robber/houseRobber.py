class Solution:
    def rob(self, nums: List[int]) -> int:
        # Caso base, (1 ou 2  casas)
        if len(nums) == 1:
            return nums[0] # pega valor da unica casa
        if len(nums) == 2:
            return max(nums[0], nums[1]) # pega o maior valor das duas casas disponiveis

        CasasRoubadas = [0] * len(nums) # CasasRoubadas representa o melhor valor que já possuo
        
        # Primeira casa é melhor do que nada
        CasasRoubadas[0] = nums[0]

        # Segunda casa, só se for melhor que a primeira
        if nums[1] > nums[0]:
            CasasRoubadas[1] = nums[1]
        else:
            CasasRoubadas[1] = nums[0]

        for i in range(2, len(nums)):

            roubar = CasasRoubadas[i-2] + nums[i] # cenario de roubo

            pular = CasasRoubadas[i-1] # cenario de pular

            if roubar > pular:
                CasasRoubadas[i] = roubar
            else:
                CasasRoubadas[i] = pular

        return CasasRoubadas[-1]