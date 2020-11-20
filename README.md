##Comandos utilizados
 
Treinar o bot:
~~~
rasa train

rasa train --domain domains/
~~~



## Domain

O dominio define o universo em que o seu assitente opera. Ele que define as intents, entities, slots, responses, forms e actions que o seu bot deve conhecer.
Ele também define a configuração para sessões de conversação.
Um domain pode ser definido em um único yml ou pode ser separado em vários arquivos no diretório. Em nosso caso, todos os domains estão na pasta chamada domains.

## Intents
A chave intent dentro do seu domínio, lista todas as intents utilizadas pela sua NLU e dados de treinamento de conversassão.

Entities são peças de uma conversa que a assistente pode precisar em um certo contexto. Por exemplo, na frase "Meu nome é alini", 
A assistente deve conseguir extrair o nome da frase e lembrar durante a conversa para manter a interação natural.


## Slots
Slots são a memória de seu bot. Eles agem como chave-valor e podem ser utilizados para armazzenar dados que o usuário pode informar.

## Resumo do fluxo

1 - Componente NLU: permite que seu assistente entenda o que o usuário fala
2 - O Core(Dialog managment component) prevê como o assistnete deve responder, com base no estado atual da conversa 
3 - Rasa x: Permite que seu assistente continue aprendendo com dados de conversassão reais.

Todos estes componentes trabalham juntos para que podemos criar otimos asisstentes contextuais.


## Desenvolvendo nossa assistente

O desenvolvimento de uma assistente deve normalmente se iniciar com o design conversassional.

O design conversasional é um processo de responder as perguntas:
 - Quem são seus usuários??
 - Para que os usuários irão utilizar a assistente?
 - Lapidar as conversas que gostariamos que a nossa assistente tenha.
 
 Este é um passo importante que irá ajudar a entender melhor a proposta e usabilidade de sua assistente e fará o processo de criação e treinamento mais fácil e eficiente.
 
 
 Regras são utilizadas para quando a intenção não tem ramificação, como uma pergunta/resposta de FAQ.
 Regras sao utiliadas para uma ação quando o contexto é insignificante. 
 
 Uma regra sobrescreve uma storie, ao contratio não.
 
## Actions

Actions são um server que o Rasa roda, para executar ações customizadas.
Ao implementar uma classe de ação, para iniciar o servidor, deve ser rodado o comando:
~~~
rasa run actions
~~~
