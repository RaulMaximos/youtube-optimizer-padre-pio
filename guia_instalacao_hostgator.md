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
