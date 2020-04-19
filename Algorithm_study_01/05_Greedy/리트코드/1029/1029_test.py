# -*- coding: utf-8 -*-
import sys
class Solution:
    def twoCitySchedCost(self, costs):
        result=0
        print(costs)
        costs= sorted(costs, key=lambda x: min(x[0], x[1]), reverse=True)
        print(costs)

        cnt={'a':0, 'b':0}
        N=len(costs)//2
        for cost in costs:
            print('\ncnt: ',cnt)
            print('result: ',result)
            if cnt['a']<N and cnt['b']<N:
                result+=min(cost)
                if cost[0]>cost[1]:
                    cnt['a']+=1
                else:
                    cnt['b']+=1

            if cnt['a']>=N:
                result+=cost[1]
            elif cnt['b']>=N:
                result+=cost[0]
        return result

def main():
    costs=[ [259, 770], [448,54], [926,667], [184, 139], [840,118], [577,469] ]
    s=Solution()
    print(s.twoCitySchedCost(costs))

if __name__=='__main__':
          main()
