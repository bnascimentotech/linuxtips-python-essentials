**[ERRATA] No começo do vídeo eu recomendei que seria opcional pular este vídeo, porém a plataforma precisa que você complete pelo menos 90% do vídeo por conta do certificado :) assiste ai mesmo que você já tenha o Python que eu mostro meu editor neste vídeo e pode ser que você queira também utiliza-lo.**

**[Opcional] configurações do editor micro: https://github.com/rochacbruno/dotfiles/tree/master/.config/micro#readme**

# Instalação

## Python

O caminho recomendado para instalação do Python é através do site oficial http://python.org na página de downloads pode obter o instalador para o seu sistema operacional.

Para este treinamento usaremos o Python 3.6+, ou seja, qualquer versão acima do 3.6 irá funcionar.

Se estiver em um sistema Linux, provavelmente o Python já se encontra instalado ou pode obte-lo através do gerenciador de pacotes do seu sistema.

Caso não possa instalar por algum motivo, temos ainda a alternativa de usar o Python online através das ferramantar http://replit.com ou https://gitpod.io para essas 2 ferramentas é necessário ter um cadastro no Github.

## Instalando Python 3 - Windows:

1. Visite https://www.python.org/downloads/windows/
1. Clique em Latest Python 3 Release
1. No fim da página, faça o download de Windows X86-64 executable installer
1. Instale o arquivo obtido no passo 3
1. Instalando Python 3 - Linux:
1. O Python 3 já está presente nas últimas versões de usuário das distribuições mais famosas de GNU/Linux, como Ubuntu, Debian openSUSE e Fedora.

## Terminal

Você pode usar o terminal de sua preferência desde que seja compatível com Linux, no windows por exemplo pode usar o WSL (Windows Subsystem for Linux) que abre um terminal Linux dentro do windows.

A título de curiosidade, no meu ambiente utilizo Arch Linux, i3wm, Terminator, ZSH e starship.rs

## Editor

A escolha de editor é pessoal, escolha o que gostar mais e que te dê maior conforto e produtividade, eu vou recomendar que você evite neste primeiro momento o uso de IDE (Ambiente Integrado) as IDEs são muito boas mas abstraem muitas coisas e por exemplo, ao invés de ir ao terminal e dar os comandos para rodar o programa, na IDE você cai na tentação de apertar um botão "> run" que você acaba nem sabendo o que ele faz exatamente.

Minha recomendação para nosso workflow de trabalho é que você mantenha sempre 2 terminais abertos no seu sistema lado a lado, um para escrevermos o código e outro para executarmos.

No caso de editor de terminal eu recomendo usar o micro-editor pois ele é leve e tem funcionamento bem simples, mas você pode também preferir usar outros como nano, vim, neovim, emacs mas eu só os recomendo caso você já tenha algum conhecimento no funcionamento deles.

Fique a contade para usar editores gráficos como Visual Studio Code ou Sublime Text.

A título de curiosidade eu utilizo 3 editors e estou sempre alternando entre eles micro-editor, vim e vscode, dependendo da tarefa eu acabo escolhendo um deles.

**[Opcional] configurações do editor micro: https://github.com/rochacbruno/dotfiles/tree/master/.config/micro#readme**

## Python

Agora em seu terminal já pode começar a interagir com o Python diretamente através do comando python.

Para verificar a versão que está instalada use o comando

```bash
python --version
```

> É muito importante que a versão seja pelo menos 3.6 (ou maior)

Para enviar uma instrução (ou comando) para o Python, use o -c

```bash
python -c "1 + 1"
```

> No comando acima o Python recebe a expressão 1 + 1 interpreta, executa a operação matemática de adição, porém não exibe nenhum output, para ter a resposta na tela precisamos usar a função print

```bash
python -c "print(1 + 1)"
2
```

Outra maneira de se comunicar com o Python é através da execução de módulos com o -m

Para obter informações sobre os caminhos de instalação do Python

```bash
python -m site
```

> -m nome_do_modulo executa um módulo que esteja instalado e habilitado para execução direta, alguns exemplos json, http.server, pip, site

E finalmente para abrir o terminal interativo use apenas python

```python
python
>>>
```

> O sinal >>> é o prompt do Python e significa que ele está a espera de um comando ali você pode digitar 1 + 1 ou qualquer operação matemática ou fazer chamadas de funções como print("bruno".upper())
