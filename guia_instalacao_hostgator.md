# Guia de Instalação na Hostgator

Este guia explica como instalar a versão web do Otimizador de Conteúdo para YouTube - Padre Pio em sua conta da Hostgator.

## Pré-requisitos

- Conta na Hostgator com suporte a Python
- Acesso SSH à sua conta (opcional, mas recomendado)
- Conhecimentos básicos de linha de comando

## Passo 1: Fazer upload dos arquivos

1. Faça login no cPanel da sua conta Hostgator
2. Acesse o Gerenciador de Arquivos
3. Navegue até a pasta `public_html` ou crie uma subpasta específica para a aplicação
4. Faça upload de todos os arquivos do repositório para esta pasta

## Passo 2: Configurar ambiente Python

1. No cPanel, procure por "Setup Python App"
2. Clique em "Create Application"
3. Preencha os campos:
   - Application root: /home/username/public_html/pasta_da_aplicacao
   - Application URL: seu_dominio.com/pasta_da_aplicacao
   - Python version: 3.8 ou superior
   - Application startup file: app.py
   - Application Entry point: app
4. Clique em "Create"

## Passo 3: Instalar dependências
1. Acesse sua conta via SSH:
ssh username@seu_dominio.com
2. Navegue até a pasta da aplicação:
cd public_html/pasta_da_aplicacao
3. Instale as dependências:
pip install -r requirements.txt
## Passo 4: Configurar passenger_wsgi.py

1. Crie ou edite o arquivo `passenger_wsgi.py` na pasta da aplicação
2. Adicione o seguinte conteúdo:

python
import sys, os

INTERP = os.path.join(os.environ['HOME'], 'python-app', 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

from app import app as application

Passo 5: Reiniciar a aplicação
No cPanel, volte para "Setup Python App"
Encontre sua aplicação na lista
Clique em "Restart"
Passo 6: Acessar a aplicação
Acesse sua aplicação através do URL configurado:
https://seu_dominio.com/pasta_da_aplicacao
Solução de problemas
Se encontrar problemas, verifique:
Logs de erro no cPanel (seção "Logs")
Permissões de arquivos (todos os arquivos devem ter permissão 644 e diretórios 755)
Versão do Python (deve ser compatível com as dependências)
Para mais ajuda, entre em contato com o suporte da Hostgator.
