import random
class pokemon
  def_init_(self, nome, vida, ataque):
  self.nome = nome
  self.vida = vida
  self.ataque = ataque
  def atacar (self, inimigo):
  dano: random.randing(self.ataque//2, self.ataque
    print(self.nome, "Atacou", inimigo.nome)
    print("Dano", dano)
    inimigo(vida = inimigo.nome)

if inimigo.vida < 0
    inimigo.vida = 0

print("Vida de", inimigo.nome,":", inimigo.vida
      print()
pikachu = pokemon("Pikachu", 100, 20)
Charmander = Pokemon("Charmander", 100, 25)
while pikachu.vida > and charmander.vida > 0
   pikachu.atacar(charmander)
if charmander.vida < = 0:
  prit("Charmander foi derrotado")
  print("Pikachu venceu")
  break
  charmander.atacar(pikachu)
  if pikachu < = 0:
    print("Pikachu" foi derrotado!)
    print("Charmander venceu!")
break
