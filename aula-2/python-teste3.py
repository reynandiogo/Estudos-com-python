#conceitos de converção, dados e metodos serão utilizados nessa fases

#[1] contatenação com .format()

#ex1

saudacao = 'boa noite'
print('lhe desejo {}!!'.format(saudacao)) 

# com este tipo de concatenação fica mais prático fazer mensagens, seu uso consiste em abrir chaves no lugar que corresponde ao lugar da variavel na mensagem e com o metodos .format() empilhar as variaveis conforme a ondem de aparição nas mensagens

#ex2: 

nome = 'joão'
idade = 16
peso = 70
altura = 1.86

print('olá! sou {}, tenho {} anos de idade, peso {}kg e tenho a altura de {}'.format(nome,idade,peso,altura))


#[2] como exibir um dado com type

comida = 'pão'
print(type(comida))

#com o type() pode se ver qual classe de dado o dado em si pertence

#[3] dados e manipulações de dados

#para cada dado há tipo de converções como int() para numeros inteiros , float() para numeros decimais, bool() para booleanos e str() para strings.

#ex1 

n1t = int('2')
n2t = int('7') 
s = n1t+n2t
print(s)

#ex2

VouF = bool(input())
print(VouF)

# nesse caso, seja la qual for o dado, se n houver nada ele printa False, mas se tiver ele printa True

#[4] metodos 

#para todos os dados há metodos que se tira informações a respeito.

#ex1: 

animal = 'pato'
print(animal.isalpha())

# Sobre Letras e Números
# .isalnum() (Alfanumérico): É o "vale-tudo" de letras e números. Se a string tiver só letras e números (sem espaços ou símbolos como @, #, !), ele dá OK. Muito bom para validar nomes de usuário simples.
# .isalpha() (Alfabético): Esse é exigente. Só aceita letras. Se tiver um único espaço ou um número "1" perdido lá no meio, ele já acusa False.
# .isnumeric() (Numérico): Esse aqui só quer saber de números. É ótimo para quando você recebe um CPF ou CEP (só os números) e quer ter certeza de que ninguém digitou uma letra por engano.

# Sobre o "Tamanho" das Letras
# .isupper() (Gritando): Ele checa se a pessoa escreveu tudo em MAIÚSCULO. Sabe quando alguém manda mensagem no zap parecendo que está gritando? Esse método pega isso.
# .islower() (Sussurrando): O contrário. Ele vê se está tudo em minúsculo. Se tiver uma única letra maiúscula, ele já desconsidera.
# .istitle() (Estilo Título): Ele confere se a string está "bonitinha", com a primeira letra de cada palavra maiúscula, tipo: "Nome Sobrenome".

# Sobre Espaços e "Invisíveis"
# .isspace() (Vazio): Sabe quando o usuário aperta a barra de espaço cinco vezes e dá enter? O .isspace() serve para pegar isso. Ele só dá True se a string for feita de espaços, tabs ou quebras de linha.
# .isprintable() (Visível): Esse é curioso. Ele avisa se tudo o que está na string pode ser visto na tela. Se tiver algum comando "fantasma" de sistema lá no meio (que não aparece quando você dá print), ele avisa.


#As Diferenças de Números (A parte chata que o Python resolve)
#.isdigit() e .isdecimal(): Esses dois são "irmãos" do .isnumeric(). Na maioria das vezes, você vai usar o isnumeric mesmo. A diferença é que o isdigit aceita coisas como o "2 ao quadrado" (²), e o isdecimal é o mais rigoroso de todos, aceitando só o 0 ao 9 puro.