#BMA находит кратчайший LFSR, генерирующий входную последовательность последовательности.
inputseq = input("Введите битовую строку ")

C = B = [0]*500

C[0] = B[0] = 1
L = 0
m = -1
i = 0
n = len(inputseq)
while i < n:  #Повторение входной последовательности
    Delta = 0
    for p in range(0, L+1):
        Delta = Delta + C[p]*int(inputseq[i-p])
    if (Delta%2) == 1:
        if C[i-m] == 0:
            C[i-m] = 1
        else:
            C[i-m]= 0
        if L<=i//2:
            m = i
            L = i + 1 - L
    i = i + 1

print("Линейная сложность =",L)


result = []
#эта часть предназначена только для отображения многочлена связи в том виде, в каком он выглядит в уравнении.
for i in range(len(C)):
    if C[i] == 1:
        if i == 0:
            polyelement = "1 + "
            result.append(polyelement)
        else:
            polyelement = "x^"+str(i)+" + "
            result.append(polyelement)
result[len(result)-1] = result[len(result)-1][:-3]
for i in result:
    print(i,end='')
