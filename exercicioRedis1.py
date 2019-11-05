import redis 

r = redis.StrictRedis(host='localhost', port=6379, charset="utf-8", decode_responses=True, db=0)
    
r.set('A', 'candidato1')
r.set('B', 'candidato1')
r.set('C', 'candidato2')
r.set('D', 'candidato1')
r.set('E', 'candidato2')
r.set('F', 'candidato2')
r.set('G', 'candidato1')
r.set('H', 'candidato1')
r.set('I', 'candidato1')

chaves = r.keys('*')
candidato01 = 0 
candidato02 = 0

for n in chaves :
   if(r.get(n)=='candidato1'):
       candidato01 = candidato01 + 1
   else :
       candidato02 = candidato02 + 1

if (candidato01 > candidato02) :
    print (" O vencedor da eleição é o candidato 1 com: ", candidato01, " votos")

elif (candidato01 < candidato02) :
    print (" O vencedor da eleição é o candidato 2 com: ", candidato02, " votos")

else : 
    print ("Houve um empate entre os candidatos")
