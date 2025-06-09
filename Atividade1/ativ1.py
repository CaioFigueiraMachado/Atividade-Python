#Caio Figueira Machado 2BDEV
def criar_personagem():
    nome = input("Digite o nome do personagem: ")
    idade = input("Digite a idade do personagem: ")
    tipo = input("Digite o tipo do personagem (ex: guerreiro, mago, arqueiro): ")
    
   
    if tipo.lower() == 'guerreiro':
        vida = 120
        ataque = 18
        defesa = 10
    elif tipo.lower() == 'mago':
        vida = 80
        ataque = 25
        defesa = 5
    elif tipo.lower() == 'arqueiro':
        vida = 100
        ataque = 20
        defesa = 7
    else:
        print("Tipo desconhecido, usando atributos padrão.")
        vida = 100
        ataque = 15
        defesa = 5
    
    return {
        'nome': nome,
        'idade': idade,
        'tipo': tipo,
        'vida': vida,
        'ataque': ataque,
        'defesa': defesa
    }

def atacar(atacante, defensor):
    dano = atacante['ataque'] - defensor['defesa']
    if dano < 0:
        dano = 0
    defensor['vida'] -= dano
    print(f"\n{atacante['nome']} atacou {defensor['nome']} causando {dano} de dano!")

def exibir_status(personagem):
    print(f"\nStatus de {personagem['nome']}:")
    print(f"  Idade: {personagem['idade']}")
    print(f"  Tipo: {personagem['tipo']}")
    print(f"  Vida: {personagem['vida']}")
    print(f"  Ataque: {personagem['ataque']}")
    print(f"  Defesa: {personagem['defesa']}")
    print("-" * 30)


print("Criação do Personagem 1")
personagem1 = criar_personagem()

print("\nCriação do Personagem 2")
personagem2 = criar_personagem()

while True:
    print("\n--- Menu ---")
    print("1. Exibir status dos personagens")
    print("2. Personagem 1 ataca Personagem 2")
    print("3. Personagem 2 ataca Personagem 1")
    print("4. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        exibir_status(personagem1)
        exibir_status(personagem2)
    elif escolha == '2':
        atacar(personagem1, personagem2)
    elif escolha == '3':
        atacar(personagem2, personagem1)
    elif escolha == '4':
        print("Saindo do jogo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
