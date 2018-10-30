#Author guo
profit=int(input("show how much you earn"))
bonus=0
therehold=[100000,100000,200000,200000,400000]
rates=[0.1,0.075,0.05,0.03,0.015,0.01]
for i in range (len(therehold)):
    if profit<=therehold[i]:
        bonus=bonus+profit*rates[i]
        profit=0
        break
    else:
        bonus=bonus+therehold[i]*rates[i]
        profit=profit-therehold[i]
bonus=bonus+profit*rates[-1]
print(bonus)

