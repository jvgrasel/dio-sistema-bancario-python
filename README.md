# Desafio Criando Sistema Bancário em Python

### Desafio Sistema bancário em Python V2

Deixar o código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar extrato. Além disso, para a versão 2 do nosso sistema, precisamos criar duas novas funções: **criar usuário (cliente banco) e criar conta corrente (vincular com usuário).**

###### Operações

- Função Saque: deve receber os argumentos apenas por nome (keyword only). 
- Função Depósito: deve receber os argumentos apenas por posição(positional only).
- Função Extrato: deve receber os argumentos por posição e nome (positional only e keyword only).
- Criar Usuário: o programa deve armazenar uma lista com os dados do cliente, não pode haver dois clientes com o mesmo cpf.
- Criar Conta Corrente: o programa deve armazenar uma lista de contas, composta por agência, número da conta. O usuário pode ter mais de uma conta, mas a conta só pode ter um usuário.



#### Conclusão V2
 Para aprimorar o código e torná-lo mais modularizado, criei funções dedicadas para as operações essenciais, como saque, depósito e visualização de extrato. Na versão 2 do sistema, também desenvolvi funcionalidades para criar usuário e criar conta corrente, o que permite vincular contas a usuários específicos. Essas melhorias não só organizam o código de maneira mais eficiente, mas também facilitam a manutenção e a expansão futura do sistema.
 Não fiquei totalmente satisfeito com o resultado, mas voltarei a trabalhar nele em breve.


__________________________________________________________________________
### Desafio Sistema bancário em Python V1

Fomos contratados por um grande banco para desenvolver seu novo sistema.   Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: **depósito, saque e extrato.**

###### Operações

- Operação de depósito
Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

- Operação de saque: O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.


- Operação de extrato: Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45

#### Conclusão V1

Desenvolvi o sistema bancário v1 em Python conforme as orientações do desafio.  
Consegui seguir todos os requisitos propostos nesta primeira parte do desafio e estou satisfeito com o resultado. 
