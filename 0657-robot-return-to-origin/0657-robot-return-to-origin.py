class Solution(object):
    def judgeCircle(self, moves):
        L,R,U,D=0,0,0,0
        for i in moves:
            if i=='U':
                U+=1
            elif i=='D':
                D+=1
            elif i=="L":
                L+=1
            else:
                R+=1
        if L==R and U==D:
            return True
        return False