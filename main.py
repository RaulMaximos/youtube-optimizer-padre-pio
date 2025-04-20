#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Otimizador de Conteúdo para YouTube - Padre Pio (Versão Atualizada)
Desenvolvido para otimizar conteúdo para público feminino 65+
"""

import os
import json
import random
import re
import datetime
import sys
from colorama import Fore, Back, Style, init

# Inicializa colorama para formatação de texto colorido
init(autoreset=True)

class YouTubeOptimizer:
    """Classe principal para otimização de conteúdo do YouTube."""
    
    def __init__(self):
        """Inicializa o otimizador com dados de configuração."""
        self.data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Carrega ou cria dados de configuração
        self.titulos_impactantes = self._carregar_ou_criar_dados('titulos_impactantes.json', [
            "🔥 O ALERTA DE PADRE PIO ✝️ QUE ESTÁ SE CUMPRINDO AGORA! 😱",
            "⚠️ PADRE PIO REVELOU ISTO ANTES DE MORRER E POUCOS SABEM! 🙏",
            "😱 A PROFECIA DE PADRE PIO QUE ESTÁ ACONTECENDO NESTE MOMENTO! ✝️",
            "🔴 URGENTE: A MENSAGEM DE PADRE PIO QUE A IGREJA ESCONDEU! ⚠️",
            "✝️ O MILAGRE DE PADRE PIO QUE MÉDICOS NÃO CONSEGUEM EXPLICAR! 🙏",
            "⚠️ ATENÇÃO: PADRE PIO ALERTOU SOBRE ISTO HÁ 50 ANOS! 😱",
            "🔥 O SEGREDO DE PADRE PIO QUE MUDARÁ SUA VIDA PARA SEMPRE! ✝️",
            "😱 PADRE PIO PREVIU O QUE ACONTECERIA EM 2025! CONFIRA! 🔮",
            "✝️ A ORAÇÃO PODEROSA DE PADRE PIO QUE FAZ MILAGRES! 🙏",
            "⚠️ NÃO IGNORE ESTE AVISO DE PADRE PIO! SUA SALVAÇÃO DEPENDE DISTO! 🔥"
        ])
        self.frases_impacto = self._carregar_ou_criar_dados('frases_impacto.json', [
            "O que você vai descobrir hoje mudará sua vida para sempre!",
            "Ninguém está preparado para o que vou revelar agora!",
            "Esta revelação de Padre Pio foi mantida em segredo por décadas!",
            "Os médicos ficaram chocados quando viram isto acontecer!",
            "A Igreja tentou esconder esta mensagem poderosa!",
            "Milhares de pessoas já foram abençoadas após conhecerem este segredo!",
            "O que Padre Pio revelou em seu leito de morte vai te surpreender!",
            "Esta profecia está se cumprindo diante dos nossos olhos!",
            "Você não vai acreditar no que aconteceu depois desta oração!",
            "Este é o alerta mais importante que você receberá hoje!"
        ])
        
        self.sugestoes_thumbnail = self._carregar_ou_criar_dados('sugestoes_thumbnail.json', [
            {
                "cor_fundo": "Preto (#000000)",
                "cor_texto": "Amarelo brilhante (#FFFF00)",
                "texto_principal": "ALERTA DE PADRE PIO!",
                "estilo_texto": "Fonte grande, negrito, com contorno vermelho",
                "posicionamento": "Texto centralizado na parte superior",
                "elementos_visuais": [
                    "Imagem de Padre Pio com expressão séria",
                    "Símbolo de alerta (⚠️) grande e visível",
                    "Efeito de brilho ao redor da imagem de Padre Pio"
                ]
            },
            {
                "cor_fundo": "Vermelho escuro (#990000)",
                "cor_texto": "Branco (#FFFFFF)",
                "texto_principal": "PROFECIA REVELADA!",
                "estilo_texto": "Fonte impactante, todas maiúsculas",
                "posicionamento": "Texto dividido em duas linhas para maior impacto",
                "elementos_visuais": [
                    "Imagem de Padre Pio com as mãos erguidas em oração",
                    "Efeito de luz divina descendo sobre a imagem",
                    "Pequenas chamas nas bordas da thumbnail"
                ]
            }
        ])
        # Novos dados baseados na análise de vídeos populares
        self.titulos_milhoes_views = self._carregar_ou_criar_dados('titulos_milhoes_views.json', [
            "🔥 A PROFECIA DE PADRE PIO QUE ESTÁ SE CUMPRINDO AGORA! (3.2M visualizações)",
            "⚠️ PADRE PIO REVELOU O SEGREDO DA SALVAÇÃO! ASSISTA AGORA! (2.8M visualizações)",
            "😱 O MILAGRE QUE NINGUÉM CONSEGUE EXPLICAR! PADRE PIO REVELOU! (4.1M visualizações)",
            "✝️ A ÚLTIMA MENSAGEM DE PADRE PIO ANTES DE MORRER! (5.3M visualizações)",
            "⚠️ ATENÇÃO: PADRE PIO ALERTOU SOBRE O FIM DOS TEMPOS! (3.7M visualizações)"
        ])
        
        # Palavras de alto impacto baseadas nos livros e materiais fornecidos
        self.palavras_alto_impacto = self._carregar_ou_criar_dados('palavras_alto_impacto.json', [
            # Gatilhos de escassez
            "ÚLTIMA CHANCE", "REVELADO HOJE", "QUASE NINGUÉM SABE", "RARO", "EXCLUSIVO",
            # Gatilhos de urgência
            "URGENTE", "ATENÇÃO", "AGORA", "IMEDIATAMENTE", "NÃO ESPERE",
            # Gatilhos de curiosidade
            "SEGREDO", "REVELADO", "DESCOBERTO", "SURPREENDENTE", "INACREDITÁVEL"
        ])
        
        # Técnicas de persuasão baseadas nos livros "As Armas da Persuasão" e "Gatilhos Mentais"
        self.tecnicas_persuasao = self._carregar_ou_criar_dados('tecnicas_persuasao.json', [
            {
                "nome": "Reciprocidade",
                "aplicacao": "Oferecer valor espiritual antes de pedir engajamento",
                "exemplo": "Compartilho esta poderosa oração de Padre Pio gratuitamente. Se ela tocar seu coração, deixe seu comentário."
            },
            {
                "nome": "Compromisso e Coerência",
                "aplicacao": "Fazer o espectador concordar com algo simples no início",
                "exemplo": "Se você acredita no poder da oração, esta mensagem de Padre Pio mudará sua vida."
            },
            {
                "nome": "Prova Social",
                "aplicacao": "Mostrar que muitas pessoas já foram beneficiadas",
                "exemplo": "Milhares de fiéis já relataram graças após conhecerem esta revelação de Padre Pio."
            }
        ])
        # Métricas de desempenho para previsões
        self.metricas_desempenho = self._carregar_ou_criar_dados('metricas_desempenho.json', {
            "padrao_titulo": {
                "alerta_emoji_inicio_fim": {"ctr": 0.91, "taxa_click": 0.80, "engajamento": 0.75},
                "profecia_revelacao": {"ctr": 0.88, "taxa_click": 0.78, "engajamento": 0.72},
                "milagre_inexplicavel": {"ctr": 0.85, "taxa_click": 0.76, "engajamento": 0.70},
                "mensagem_urgente": {"ctr": 0.83, "taxa_click": 0.74, "engajamento": 0.68},
                "segredo_revelado": {"ctr": 0.80, "taxa_click": 0.72, "engajamento": 0.65}
            },
            "elementos_thumbnail": {
                "padre_pio_expressao_seria": {"ctr": 0.89, "taxa_click": 0.79, "engajamento": 0.73},
                "simbolo_alerta": {"ctr": 0.87, "taxa_click": 0.77, "engajamento": 0.71},
                "efeito_luz_divina": {"ctr": 0.84, "taxa_click": 0.75, "engajamento": 0.69},
                "estigmas_visiveis": {"ctr": 0.82, "taxa_click": 0.73, "engajamento": 0.67},
                "texto_impactante_amarelo": {"ctr": 0.90, "taxa_click": 0.81, "engajamento": 0.76}
            }
        })
    
    def _carregar_ou_criar_dados(self, nome_arquivo, dados_padrao):
        """Carrega dados de um arquivo JSON ou cria com valores padrão."""
        caminho_arquivo = os.path.join(self.data_dir, nome_arquivo)
        
        if os.path.exists(caminho_arquivo):
            try:
                with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Erro ao carregar {nome_arquivo}: {e}")
                return dados_padrao
        else:
            try:
                with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                    json.dump(dados_padrao, f, ensure_ascii=False, indent=4)
                return dados_padrao
            except Exception as e:
                print(f"Erro ao criar {nome_arquivo}: {e}")
                return dados_padrao
    def _salvar_dados(self, nome_arquivo, dados):
        """Salva dados em um arquivo JSON."""
        caminho_arquivo = os.path.join(self.data_dir, nome_arquivo)
        
        try:
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                json.dump(dados, f, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            print(f"Erro ao salvar {nome_arquivo}: {e}")
            return False
    
    def _avaliar_titulo(self, titulo):
        """Avalia o potencial de desempenho de um título."""
        metricas = {"ctr": 0.70, "taxa_click": 0.60, "engajamento": 0.50}
        
        # Verifica padrões no título
        for padrao, valores in self.metricas_desempenho["padrao_titulo"].items():
            if padrao == "alerta_emoji_inicio_fim" and re.search(r'^[⚠️🔥✝️😱🔴🙏]+.*[⚠️🔥✝️😱🔴🙏]+$', titulo):
                metricas = valores
                break
            elif padrao == "profecia_revelacao" and ("PROFECIA" in titulo or "REVELAÇÃO" in titulo or "REVELADO" in titulo):
                metricas = valores
                break
            elif padrao == "milagre_inexplicavel" and ("MILAGRE" in titulo or "INEXPLICÁVEL" in titulo):
                metricas = valores
                break
            elif padrao == "mensagem_urgente" and ("URGENTE" in titulo or "ATENÇÃO" in titulo or "ALERTA" in titulo):
                metricas = valores
                break
            elif padrao == "segredo_revelado" and ("SEGREDO" in titulo or "REVELADO" in titulo):
                metricas = valores
                break
        
        # Ajusta com base em palavras de alto impacto
        palavras_impacto = sum(1 for palavra in self.palavras_alto_impacto if palavra in titulo.upper())
        metricas["ctr"] += min(palavras_impacto * 0.01, 0.05)
        metricas["taxa_click"] += min(palavras_impacto * 0.01, 0.05)
        metricas["engajamento"] += min(palavras_impacto * 0.01, 0.05)
        
        # Limita os valores a 0.99
        metricas = {k: min(v, 0.99) for k, v in metricas.items()}
        
        return metricas
    def gerar_titulo(self, tema=None):
        """Gera um título otimizado para vídeo do YouTube."""
        if not tema:
            return random.choice(self.titulos_impactantes)
        
        # Gera 5 opções de títulos baseados no tema
        opcoes_titulos = []
        
        # Opção 1: Alerta com emojis no início e fim
        opcao1 = f"⚠️ ALERTA DE PADRE PIO: {tema.upper()}! 😱"
        opcoes_titulos.append({"titulo": opcao1, "metricas": self._avaliar_titulo(opcao1)})
        
        # Opção 2: Profecia/Revelação
        opcao2 = f"🔥 A PROFECIA DE PADRE PIO SOBRE {tema.upper()}! ✝️"
        opcoes_titulos.append({"titulo": opcao2, "metricas": self._avaliar_titulo(opcao2)})
        
        # Opção 3: Segredo revelado
        opcao3 = f"😱 O SEGREDO DE PADRE PIO SOBRE {tema.upper()} REVELADO! 🙏"
        opcoes_titulos.append({"titulo": opcao3, "metricas": self._avaliar_titulo(opcao3)})
        
        # Opção 4: Mensagem urgente
        opcao4 = f"🔴 URGENTE: PADRE PIO REVELOU ISTO SOBRE {tema.upper()}! ⚠️"
        opcoes_titulos.append({"titulo": opcao4, "metricas": self._avaliar_titulo(opcao4)})
        
        # Opção 5: Milagre/Inexplicável
        opcao5 = f"✝️ O MILAGRE DE PADRE PIO RELACIONADO A {tema.upper()} QUE NINGUÉM EXPLICA! 🔥"
        opcoes_titulos.append({"titulo": opcao5, "metricas": self._avaliar_titulo(opcao5)})
        
        # Ordena as opções por CTR estimado
        opcoes_titulos.sort(key=lambda x: x["metricas"]["ctr"], reverse=True)
        
        return opcoes_titulos
    def gerar_sugestao_thumbnail(self, titulo):
        """Gera sugestões para thumbnail baseadas no título."""
        # Gera 5 opções de thumbnails
        opcoes_thumbnails = []
        
        for sugestao_base in self.sugestoes_thumbnail:
            # Cria uma cópia da sugestão base
            sugestao = sugestao_base.copy()
            
            # Adapta o texto principal baseado no título
            palavras_chave = re.findall(r'[A-ZÀ-Ú]{2,}', titulo)
            if palavras_chave:
                palavras_destaque = [palavra for palavra in palavras_chave if len(palavra) > 3][:2]
                if palavras_destaque:
                    sugestao["texto_principal"] = " ".join(palavras_destaque)
            
            # Avalia o potencial da thumbnail
            metricas = {"ctr": 0.70, "taxa_click": 0.60, "engajamento": 0.50}
            
            # Verifica elementos na thumbnail
            for elemento, valores in self.metricas_desempenho["elementos_thumbnail"].items():
                for el in sugestao["elementos_visuais"]:
                    if elemento.lower() in el.lower():
                        metricas = valores
                        break
            
            # Ajusta com base nas cores
            if "amarelo" in sugestao["cor_texto"].lower() and "preto" in sugestao["cor_fundo"].lower():
                metricas["ctr"] += 0.05
                metricas["taxa_click"] += 0.05
            
            # Limita os valores a 0.99
            metricas = {k: min(v, 0.99) for k, v in metricas.items()}
            
            sugestao["metricas"] = metricas
            opcoes_thumbnails.append(sugestao)
        
        # Ordena as opções por CTR estimado
        opcoes_thumbnails.sort(key=lambda x: x["metricas"]["ctr"], reverse=True)
        
        return opcoes_thumbnails
    def gerar_estrutura_roteiro(self, titulo=None):
        """Gera uma estrutura de roteiro baseada no título."""
        # Seleciona uma estrutura base
        estrutura_base = random.choice(self.estruturas_capitulos)
        
        # Adapta a estrutura se um título for fornecido
        if titulo:
            palavras_chave = re.findall(r'[A-ZÀ-Ú]{2,}', titulo)
            if palavras_chave:
                # Adapta alguns capítulos para incluir palavras-chave do título
                for i in range(min(3, len(estrutura_base))):
                    idx = random.randint(0, len(estrutura_base) - 1)
                    palavra = random.choice(palavras_chave)
                    estrutura_base[idx]["titulo"] = f"{estrutura_base[idx]['titulo']} sobre {palavra}"
        
        # Gera 5 opções de estruturas de roteiro
        opcoes_estruturas = []
        
        # Opção 1: Estrutura padrão (começa com alerta, termina com esperança)
        opcao1 = estrutura_base.copy()
        opcao1[0]["titulo"] = "O alerta urgente de Padre Pio para nossos tempos"
        opcao1[-1]["titulo"] = "A mensagem de esperança para os fiéis"
        metricas1 = self.metricas_desempenho["estrutura_roteiro"]["comeca_alerta_termina_esperanca"]
        opcoes_estruturas.append({"estrutura": opcao1, "metricas": metricas1})
        
        # Ordena as opções por retenção estimada
        opcoes_estruturas.sort(key=lambda x: x["metricas"]["retencao"], reverse=True)
        
        return opcoes_estruturas
    def gerar_conteudo_capitulo(self, titulo_capitulo):
        """Gera conteúdo para um capítulo do roteiro."""
        # Seleciona frases de impacto aleatórias
        frases = random.sample(self.frases_impacto, 3)
        
        # Gera um conteúdo básico para o capítulo
        conteudo = f"Neste capítulo, vamos explorar {titulo_capitulo.lower()}. "
        conteudo += f"{frases[0]} "
        conteudo += f"Padre Pio, em sua sabedoria divina, nos deixou ensinamentos profundos sobre este tema. "
        conteudo += f"{frases[1]} "
        conteudo += f"Vamos descobrir juntos o que isso significa para nossa vida espiritual hoje. "
        conteudo += f"{frases[2]}"
        
        return conteudo
    
    def expandir_capitulo(self, capitulo, tamanho_alvo=3100):
        """Expande o conteúdo de um capítulo para o tamanho alvo."""
        titulo = capitulo["titulo"]
        conteudo_base = capitulo.get("conteudo", self.gerar_conteudo_capitulo(titulo))
        
        # Seleciona técnicas de persuasão aleatórias
        tecnicas = random.sample(self.tecnicas_persuasao, 3)
        
        # Expande o conteúdo
        conteudo_expandido = f"{conteudo_base}\n\n"
        
        # Adiciona conteúdo baseado no título do capítulo
        if "vida" in titulo.lower() or "história" in titulo.lower():
            conteudo_expandido += """
Padre Pio nasceu em 25 de maio de 1887 em Pietrelcina, Itália, com o nome de Francesco Forgione. Desde muito jovem, demonstrou uma profunda devoção e espiritualidade. Aos 15 anos, ingressou na Ordem dos Frades Menores Capuchinhos, onde recebeu o nome de Frei Pio.
"""
        
        # Ajusta o tamanho do conteúdo para atingir o tamanho alvo
        while len(conteudo_expandido) < tamanho_alvo:
            # Adiciona mais conteúdo
            frases_adicionais = random.sample(self.frases_impacto, 2)
            conteudo_expandido += f"\n\n{frases_adicionais[0]} {frases_adicionais[1]}\n\n"
        
        return conteudo_expandido
    def expandir_roteiro_completo(self, estrutura_roteiro, tamanho_alvo=3100):
        """Expande todos os capítulos de um roteiro para o tamanho alvo."""
        roteiro_expandido = []
        
        for capitulo in estrutura_roteiro:
            capitulo_expandido = capitulo.copy()
            capitulo_expandido["conteudo"] = self.expandir_capitulo(capitulo, tamanho_alvo)
            roteiro_expandido.append(capitulo_expandido)
        
        return roteiro_expandido
    
    def gerar_tags(self, titulo):
        """Gera tags otimizadas para SEO baseadas no título."""
        # Tags básicas sempre presentes
        tags_base = [
            "Padre Pio", "São Pio de Pietrelcina", "santo", "milagre", "católico",
            "estigmas", "profecia", "oração", "fé", "espiritualidade",
            "igreja católica", "intercessão", "bênção", "graça", "conversão"
        ]
        
        # Extrai palavras-chave do título
        palavras_chave = re.findall(r'[A-ZÀ-Úa-zà-ú]{4,}', titulo)
        palavras_chave = [palavra.lower() for palavra in palavras_chave if palavra.lower() not in ["padre", "pio", "que", "para", "como", "sobre", "este", "esta", "isto"]]
        
        # Combina palavras-chave com "Padre Pio"
        tags_combinadas = [f"Padre Pio {palavra}" for palavra in palavras_chave]
        
        # Combina todas as tags e remove duplicatas
        todas_tags = tags_base + palavras_chave + tags_combinadas
        todas_tags = list(dict.fromkeys(todas_tags))  # Remove duplicatas mantendo a ordem
        
        return todas_tags[:30]  # Limita a 30 tags
    def gerar_descricao_video(self, titulo, estrutura_roteiro):
        """Gera uma descrição otimizada para o vídeo."""
        # Extrai palavras-chave do título
        palavras_chave = re.findall(r'[A-ZÀ-Úa-zà-ú]{4,}', titulo)
        palavras_chave = [palavra.lower() for palavra in palavras_chave if palavra.lower() not in ["padre", "pio", "que", "para", "como", "sobre", "este", "esta", "isto"]]
        
        # Seleciona técnicas de persuasão aleatórias
        tecnicas = random.sample(self.tecnicas_persuasao, 2)
        
        # Cria a descrição
        descricao = f"{titulo}\n\n"
        
        # Adiciona introdução com palavras-chave
        descricao += f"Neste vídeo revelador sobre Padre Pio, você descobrirá {', '.join(palavras_chave[:3])} e muito mais! "
        descricao += "Uma mensagem espiritual poderosa que pode transformar sua vida e fortalecer sua fé.\n\n"
        
        # Adiciona conteúdo baseado nas técnicas de persuasão
        for tecnica in tecnicas:
            descricao += f"{tecnica['exemplo']}\n\n"
        
        # Adiciona índice dos capítulos
        descricao += "ÍNDICE DO VÍDEO:\n"
        for capitulo in estrutura_roteiro:
            minuto = capitulo["numero"] * 2 - 1
            descricao += f"⏱️ {minuto:02d}:{00:02d} - {capitulo['titulo']}\n"
        
        # Adiciona chamadas para ação
        descricao += "\n🙏 ORAÇÕES E DEVOÇÕES:\n"
        descricao += "Reze diariamente a Padre Pio por sua intercessão poderosa. Visite nosso site para mais orações: [seu site]\n\n"
        
        descricao += "✝️ COMUNIDADE:\n"
        descricao += "Junte-se à nossa comunidade de devotos de Padre Pio. Compartilhe suas experiências nos comentários!\n\n"
        
        # Adiciona hashtags
        tags = self.gerar_tags(titulo)[:10]  # Limita a 10 hashtags
        descricao += " ".join([f"#{tag.replace(' ', '')}" for tag in tags])
        
        return descricao
    def gerar_roteiro_completo(self, tema=None):
        """Gera um roteiro completo para vídeo do YouTube."""
        # Gera título otimizado
        opcoes_titulos = self.gerar_titulo(tema)
        titulo_escolhido = opcoes_titulos[0]["titulo"]  # Escolhe o título com melhor métrica
        
        # Gera sugestões para thumbnail
        opcoes_thumbnails = self.gerar_sugestao_thumbnail(titulo_escolhido)
        thumbnail_escolhida = opcoes_thumbnails[0]  # Escolhe a thumbnail com melhor métrica
        
        # Gera estrutura do roteiro
        opcoes_estruturas = self.gerar_estrutura_roteiro(titulo_escolhido)
        estrutura_escolhida = opcoes_estruturas[0]["estrutura"]  # Escolhe a estrutura com melhor métrica
        
        # Gera conteúdo para cada capítulo
        for capitulo in estrutura_escolhida:
            capitulo["conteudo"] = self.gerar_conteudo_capitulo(capitulo["titulo"])
        
        # Gera descrição e tags
        descricao = self.gerar_descricao_video(titulo_escolhido, estrutura_escolhida)
        tags = self.gerar_tags(titulo_escolhido)
        
        # Cria um arquivo com o roteiro completo
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"roteiro_otimizado_{timestamp}.txt"
        filepath = os.path.join(self.data_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("ROTEIRO OTIMIZADO PARA YOUTUBE - PADRE PIO\n")
            f.write("=" * 80 + "\n\n")
            
            f.write("TÍTULO OTIMIZADO:\n")
            f.write(titulo_escolhido + "\n\n")
            
            f.write("OPÇÕES DE TÍTULOS (ORDENADOS POR POTENCIAL):\n")
            for i, opcao in enumerate(opcoes_titulos, 1):
                f.write(f"{i}. {opcao['titulo']}\n")
                f.write(f"   📈 CTR estimado: {opcao['metricas']['ctr']:.0%}\n")
                f.write(f"   📍 TAXA DE CLICK: {opcao['metricas']['taxa_click']:.0%}\n")
                f.write(f"   👍 Engajamento: {opcao['metricas']['engajamento']:.0%}\n\n")
            
            f.write("SUGESTÕES PARA THUMBNAIL:\n")
            f.write(f"Cor de fundo: {thumbnail_escolhida['cor_fundo']}\n")
            f.write(f"Cor do texto: {thumbnail_escolhida['cor_texto']}\n")
            f.write(f"Texto principal: {thumbnail_escolhida['texto_principal']}\n")
            
            f.write("\n" + "-" * 80 + "\n\n")
            
            f.write("ESTRUTURA DO ROTEIRO:\n\n")
            for capitulo in estrutura_escolhida:
                f.write(f"CAPÍTULO {capitulo['numero']}: {capitulo['titulo']}\n\n")
                f.write(f"{capitulo['conteudo']}\n\n")
            
            f.write("DESCRIÇÃO DO VÍDEO:\n\n")
            f.write(descricao + "\n\n")
            
            f.write("TAGS RECOMENDADAS:\n\n")
            f.write(", ".join(tags) + "\n\n")
            f.write("=" * 80 + "\n")
        
        return {
            "titulo": titulo_escolhido,
            "opcoes_titulos": opcoes_titulos,
            "sugestao_thumbnail": thumbnail_escolhida,
            "opcoes_thumbnails": opcoes_thumbnails,
            "estrutura_roteiro": estrutura_escolhida,
            "descricao": descricao,
            "tags": tags,
            "filepath": filepath
        }


def exibir_menu():
    """Exibe o menu principal."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 80)
    print(f"{Fore.MAGENTA}{Style.BRIGHT}{'OTIMIZADOR DE CONTEÚDO PARA YOUTUBE - PADRE PIO':^80}{Style.RESET_ALL}")
    print("=" * 80)
    print("Desenvolvido para otimizar conteúdo para público feminino 65+")
    print("\n")
    
    print("=" * 80)
    print(f"{Fore.CYAN}{Style.BRIGHT}{'MENU PRINCIPAL':^80}{Style.RESET_ALL}")
    print("=" * 80)
    print()
    print("1. Gerar apenas título otimizado")
    print("2. Gerar apenas sugestões para thumbnail")
    print("3. Gerar roteiro completo")
    print("4. Expandir roteiro para áudio")
    print("5. Gerar apenas descrição e tags")
    print("0. Sair")
    print()


def main():
    """Função principal."""
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            # Gerar apenas título otimizado
            tema = input("\nInforme o tema principal (deixe em branco para tema aleatório): ")
            print("\nGerando títulos otimizados...\n")
            
            otimizador = YouTubeOptimizer()
            opcoes_titulos = otimizador.gerar_titulo(tema if tema else None)
            
            print(f"{Fore.GREEN}{Style.BRIGHT}TÍTULOS OTIMIZADOS (ORDENADOS POR POTENCIAL):{Style.RESET_ALL}\n")
            for i, opcao in enumerate(opcoes_titulos, 1):
                print(f"{Fore.YELLOW}{Style.BRIGHT}{i}. {opcao['titulo']}{Style.RESET_ALL}")
                print(f"   📈 CTR estimado: {opcao['metricas']['ctr']:.0%}")
                print(f"   📍 TAXA DE CLICK: {opcao['metricas']['taxa_click']:.0%}")
                print(f"   👍 Engajamento: {opcao['metricas']['engajamento']:.0%}\n")
        
        elif opcao == "0":
            # Sair
            print("\nObrigado por usar o Otimizador de Conteúdo para YouTube - Padre Pio!")
            sys.exit(0)
        
        input("\nPressione Enter para continuar...")


if __name__ == "__main__":
    main()
