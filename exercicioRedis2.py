import redis

re = redis.StrictRedis(host='localhost', port=6379, charset="utf-8", decode_responses=True, db=0)

re.set('candidato1', 0)
re.set('candidato2', 0)  

candidato1 = 0
candidato2 = 0 

arq = open('votacao.txt','r')
voto = arq.readlines()

for n in voto : 
    k = n.replace('\n','')
    
    if (k == 'candidato1') :
        re.incr('candidato1')

    elif (k == 'candidato2'):
        re.incr('candidato2')

candidato1 = int(re.get('candidato1'))
candidato2 = int(re.get('candidato2'))
total = candidato1 + candidato2

print ("total de votos: ", total)

print("O total de votos do candidato 1 é: ", candidato1)

print("O total de votos do candidato 2 é: ", candidato2)

if (candidato1 < candidato2) :
    print("O vencedor da eleição é o candidato 2")

elif (candidato1 > candidato2):
    print("O vencedor da eleição é o candidato 1")

else:       
    print ("Não há vencedor")
  