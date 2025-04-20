#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Otimizador de Conteúdo para YouTube - Padre Pio (Versão Web)
Desenvolvido para otimizar conteúdo para público feminino 65+
"""

from flask import Flask, render_template, request, jsonify
import os
import json
import random
import re
import datetime
import sys

# Importa a classe YouTubeOptimizer do arquivo main.py
from main import YouTubeOptimizer

app = Flask(__name__)
app.config['SECRET_KEY'] = 'padre_pio_optimizer_secret_key'

# Cria uma instância do otimizador
otimizador = YouTubeOptimizer()

@app.route('/')
def index():
    """Rota principal que renderiza a página inicial."""
    return render_template('index.html')

@app.route('/gerar_titulo', methods=['POST'])
def gerar_titulo():
    """Rota para gerar títulos otimizados."""
    tema = request.form.get('tema', '')
    opcoes_titulos = otimizador.gerar_titulo(tema if tema else None)
    return jsonify({
        'success': True,
        'opcoes_titulos': opcoes_titulos
    })

@app.route('/gerar_thumbnail', methods=['POST'])
def gerar_thumbnail():
    """Rota para gerar sugestões de thumbnail."""
    titulo = request.form.get('titulo', '')
    if not titulo:
        return jsonify({
            'success': False,
            'error': 'Título não pode ser vazio!'
        })
    
    opcoes_thumbnails = otimizador.gerar_sugestao_thumbnail(titulo)
    return jsonify({
        'success': True,
        'opcoes_thumbnails': opcoes_thumbnails
    })

@app.route('/gerar_roteiro', methods=['POST'])
def gerar_roteiro():
    """Rota para gerar roteiro completo."""
    tema = request.form.get('tema', '')
    resultado = otimizador.gerar_roteiro_completo(tema if tema else None)
    
    # Retorna apenas os dados necessários para exibição na web
    return jsonify({
        'success': True,
        'titulo': resultado['titulo'],
        'opcoes_titulos': resultado['opcoes_titulos'],
        'sugestao_thumbnail': resultado['sugestao_thumbnail'],
        'estrutura_roteiro': [
            {
                'numero': cap['numero'],
                'titulo': cap['titulo'],
                'conteudo': cap['conteudo'][:200] + '...' if len(cap['conteudo']) > 200 else cap['conteudo']
            } for cap in resultado['estrutura_roteiro']
        ],
        'descricao': resultado['descricao'],
        'tags': resultado['tags'],
        'filepath': resultado['filepath']
    })

@app.route('/expandir_roteiro', methods=['POST'])
def expandir_roteiro():
    """Rota para expandir roteiro para áudio."""
    estrutura_json = request.form.get('estrutura', '')
    tamanho_alvo = int(request.form.get('tamanho_alvo', 3100))
    
    try:
        estrutura = json.loads(estrutura_json)
        roteiro_expandido = otimizador.expandir_roteiro_completo(estrutura, tamanho_alvo)
        
        # Cria diretório para salvar o roteiro expandido
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        dir_name = f"roteiro_expandido_{timestamp}"
        dir_path = os.path.join(otimizador.data_dir, dir_name)
        os.makedirs(dir_path, exist_ok=True)
        
        # Salva o roteiro completo em um único arquivo
        roteiro_completo_filename = "roteiro_completo.txt"
        roteiro_completo_path = os.path.join(dir_path, roteiro_completo_filename)
        
        with open(roteiro_completo_path, 'w', encoding='utf-8') as f:
            f.write(f"ROTEIRO COMPLETO\n\n")
            f.write("=" * 80 + "\n\n")
            
            for capitulo in roteiro_expandido:
                f.write(f"CAPÍTULO {capitulo['numero']}: {capitulo['titulo']}\n\n")
                f.write(capitulo['conteudo'])
                f.write("\n\n" + "-" * 80 + "\n\n")
        
        return jsonify({
            'success': True,
            'roteiro_expandido': roteiro_expandido,
            'filepath': roteiro_completo_path,
            'total_caracteres': sum(len(cap['conteudo']) for cap in roteiro_expandido),
            'media_caracteres': sum(len(cap['conteudo']) for cap in roteiro_expandido) // len(roteiro_expandido)
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/gerar_descricao_tags', methods=['POST'])
def gerar_descricao_tags():
    """Rota para gerar descrição e tags."""
    titulo = request.form.get('titulo', '')
    if not titulo:
        return jsonify({
            'success': False,
            'error': 'Título não pode ser vazio!'
        })
    
    # Cria uma estrutura mínima para a descrição
    estrutura_minima = [{"numero": 1, "titulo": "Introdução", "conteudo": ""}]
    
    descricao = otimizador.gerar_descricao_video(titulo, estrutura_minima)
    tags = otimizador.gerar_tags(titulo)
    
    # Salva em um arquivo
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"descricao_tags_{timestamp}.txt"
    filepath = os.path.join(otimizador.data_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("DESCRIÇÃO DO VÍDEO:\n\n")
        f.write(descricao + "\n\n")
        f.write("TAGS RECOMENDADAS:\n\n")
        f.write(", ".join(tags) + "\n")
    
    return jsonify({
        'success': True,
        'descricao': descricao,
        'tags': tags,
        'filepath': filepath
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
