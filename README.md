
# 🎮 Análise de Vendas e Metadados do PlayStation

**Uma análise abrangente, orientada por dados, sobre a dinâmica do ecossistema PlayStation ao longo de três gerações (PS3, PS4 e PS5)**

---

## 📋 Índice

- [Visão Geral do Projeto](#-visão-geral-do-projeto)
- [Principais Descobertas](#-principais-descobertas)
- [Descrição do Dataset](#-descrição-do-dataset)
- [Stack Técnico](#-stack-tecnico)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Instalação e Configuração](#-instalação-e-configuração)
- [Como Utilizar](#-como-utilizar)
- [Análise e Insights](#-análise-e-insights)
- [Recomendações Estratégicas](#-recomendações-estratégicas)
- [Limitações e Trabalhos Futuros](#-limitações-e-trabalhos-futuros)
- [Autor](#-autor)

---

## 🎯 Visão Geral do Projeto

Este projeto realiza uma **análise aprofundada** do ecossistema de jogos do PlayStation, explorando as relações entre **qualidade dos jogos (avaliações), desempenho comercial (vendas)** e **dinâmicas de mercado** ao longo de três gerações de consoles.

### Hipótese Central

> **Qualidade, por si só, NÃO garante sucesso comercial.** Marketing, timing de lançamento, força da marca e posicionamento estratégico são fatores tão — ou mais — relevantes para o desempenho de um jogo.

### Objetivos de Negócio

✅ Identificar padrões de sucesso além da aclamação da crítica  
✅ Analisar a evolução dos gêneros e preferências do consumidor  
✅ Comparar estratégias e métricas de desempenho de publishers  
✅ Fornecer recomendações estratégicas baseadas em dados
✅ Desenvolver um dashboard interativo para exploração do mercado 

---

## 📊 Principais Descobertas

### 1. **Correlação Fraca: Avaliação vs. Vendas (ρ ≈ 0,29)**

Jogos bem avaliados nem sempre vendem bem. Esse resultado indica que:
- **Reconhecimento de marca** pesa mais do que a nota crítica
- **Campanhas de marketing** impulsionam adoção independentemente da avaliação
- **Timing de lançamento** (especialmente no Q4) é decisivo
- **Tamanho do público-alvo** supera a qualidade percebida

**Implicação:** Publishers devem equilibrar qualidade técnica com execução comercial.

---

### 2. **Ação Domina Todas as Gerações**

O gênero **Action** lidera consistentemente as vendas no PS3, PS4 e PS5:
- Representa cerca de 25% da receita total
- Mantém liderança mesmo com mudanças no mercado
- Outros gêneros fortes: Shooter, RPG e Sports

**Insight:** gêneros de nicho crescem em diversidade, mas não em volume de vendas.

---

### 3. **PS5: Maior Qualidade, Dados Incompletos**

O PS5 apresenta:
- **Mediana de avaliação: 3,67** (vs. 3,5–3,6 nas gerações anteriores) → Catálogo de maior qualidade
- **Coleta de dados:** Somente até outubro de 2025 → Insuficiente para comparações de vendas robustas
- **Padrão de adoção:** Mais lento que o PS3/PS4, sugerindo necessidade de revisão da estratégia de exclusividade

⚠️ **Cuidado:** análises de vendas do PS5 ainda não são conclusivas.

---

### 4. **O Efeito do Lançamento no Q4 é Real**

Distribuição por trimestre mostra que:
- **Pico de lançamentos:** novembro e dezembro
- **Alinhamento de Marketing:** Coincide com as épocas festivas e oportunidades de venda conjunta de produtos.
- **Consequência:** O primeiro trimestre (janeiro a março) apresenta menos lançamentos e menor potencial de vendas.

📌 **Oportunidade:** otimizar calendários globais de lançamento para o Q4.

---

### 5. **Estratégias Distintas de Publishers**

Dois modelos de negócio se destacam:

| Modelo | Exemplo | Estratégia |
|-------|---------|----------|
| **Premium** | Rockstar, Atlus | Poucos títulos, alta qualidade, preço premium |
| **Alto Volume** | Activision, EA | Muitos títulos, qualidade variável, alcance massivo |

Ambos funcionam quando aplicados de forma consistente.

---

## 📦 Descrição do Dataset

**Fonte:** [Kaggle – PlayStation Sales and Metadata](https://www.kaggle.com/datasets/gvidalguiresse/playstation-sales-and-metadata-ps3ps4ps5)

**Provedores:** VGChartz + RAWG API

### Composição dos Dados

| Métrica | Valor |
|--------|-------|
| **Total de Jogos** | 4.421 |
| **Consoles** | PS3, PS4, PS5 |
| **Período** | Nov 2006 – Oct 2025 |
| **Gêneros Únicos** | 19 |
| **Distribuição de Jogos** | PS4: 1.991 | PS3: 1.892 | PS5: 1.080 |

### Principais Variáveis

| Coluna | Tipo | Descrição |
|--------|------|-------------|
| `Name` | String | Nome do jogo |
| `Console` | Categórico | PS3, PS4 ou PS5 |
| `Rating` | Float | Avaliação crítica (1–5) |
| `Total Sales` | Float | Vendas globais (milhões) |
| `Release Date` | Data | Data de lançamento |
| `Publisher` | String | Estúdio de publicação |
| `Developer` | String | Estúdio de desenvolvimento |
| `Genres` | String | Lista de gêneros separados por vírgula |

### Pipeline de Limpeza

✅ Remoção de colunas com >40% de dados ausentes (`platforms`, `metacritic`)  
✅ Tratamento de avaliações inválidas (Rating = 0.0) como dados ausentes  
✅ Extração do `Release Year` a partir de `Release Date`  
✅ Expansão de `Genres` para análise granular  
✅ Criação do indicador binário `Has Score`  
✅ Categorização das avaliações em faixas (1.0–1.9, 2.0–2.9, etc.)

---

## 🛠️ Stack Técnico

### Processamento de Dados
- **Python 3.10+**
- **Pandas** – Manipulação e agregação de dados
- **NumPy** – Operações numéricas

### Visualização
- **Matplotlib** – Gráficos estáticos com qualidade para publicação
- **Seaborn** – Visualizações estatísticas
- **Plotly** – Dashboard web interativo 

### Aplicação Web
- **Streamlit** – Framework para desenvolvimento de dashboards interativos
- **Streamlit Navigation** – Arquitetura de aplicativo com multi-páginas

### Ferramentas
- **Jupyter Notebook** – Análise exploratória de dados
- **Python-dotenv** – Configuração do ambiente
- **Git** – Controle de versão

---

## 📁 Estrutura do Projeto

```
metadados-playstation/
│
├── README.md                                  # Documentação (este arquivo)
├── requirements.txt                           # Dependências do Python
│
├── data/
│   ├── raw/
│   │   └── PlayStation_Metadata.csv           # Dataset original
│   └── cleaned/
│       └── PlayStation_Metadata_treated.csv   # Dataset processado
│       └── *.png                              # Visualizações geradas
│
├── notebooks/
│   └── analysis.ipynb                         # EDA e análise estatística
│
├── app/
│   ├── app.py                                 # Aplicativo principal Streamlit
│   └── views/
│       ├── home.py                            # Página de destino com insights
│       ├── overviews.py                       # Análise de qualidade e vendas
│       ├── market_trends.py                   # Análise de gênero e temporal
│       └── publishers.py                      # Comparação de publishers
│
└── utils/
    ├── __init__.py
    ├── utils.py                               # Utilitários de transformação de dados
    ├── data_utils.py                          # Funções específicas do Streamlit
    └── plotly_utils.py                        # Geração de gráficos interativos
```

---

## 🚀 Instalação e Configuração

### Pré-requisitos
- Python 3.10 ou superior
- gerenciador de pacotes pip
- Git (opcional, para clonagem)

### Etapa 1: Clonar o repositório
```bash
git clone https://github.com/uAugustoVR/metadados-playstation.git
cd metadados-playstation
```

### Etapa 2: Criar Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Etapa 3: Instalar as dependências
```bash
pip install -r requirements.txt
pip install -e .    # Instala o pacote local em modo editável
```

### Etapa 4: Configurar o ambiente (Opcional)
Crie o arquivo `.env` na raiz do projeto:
```env
cleaned_data_path=./data/cleaned
raw_data_path=./data/raw
```

### Etapa 5: Verificar a instalação
```bash
python -c "import pandas, streamlit, plotly; print('✅ Todas as dependências instaladas')"
```

---

## 📊 Como Utilizar

### Dashboard Interativo (Recomendado)
```bash
streamlit run app/app.py
```
Acesse em `http://localhost:8501`

**Funcionalidades:**
- Navegação por páginas (Página Inicial → Visão Geral → Mercado & Tendências → Publishers)
- Filtros dinâmicos: Console, Ano, Gênero
- Gráficos interativos
- KPIs estratégicos

---

## 🔍 Análise e Insights

### 1. Qualidade vs. Sucesso Comercial

**Resultados:**
- Coeficiente de correlação de Spearman: **ρ = 0.29** (fraco a moderado)
- Jogos com Avaliação ≥4,0 representam apenas cerca de 12% do catálogo, mas possuem uma presença significativa no mercado
- Outliers: Jogos de alta qualidade com baixas vendas (títulos de nicho) e jogos de baixa qualidade com altas vendas (franquias impulsionadas por marcas)

**Visualização:** `scatterplot_metascore_sales.png`

---

### 2. Evolução dos Gêneros ao Longo das Gerações

**Principais Tendências:**
- **Action** mantém continuamente uma participação de mercado superior a 25%
- **Indie** e **Puzzle** estão crescendo em diversidade de catálogo, mas não em receita.
- **Sports** forte desempenho associado a franquias (FIFA)

**Padrão Temporal :** As mudanças na liderança de gênero coincidem com os principais lançamentos de IPs e ciclos de atualização de consoles

**Visualização:** `top_evolution_genres_by_sales.png`

---

### 3. Impacto do Momento do lançamento

**Distribuição por trimestre:**
| Trimestre  | Participação | Análise  |
|---------|-------|---------|
| Q1 | 21% | Menor atividade, "queda nos lançamentos de inverno" |
| Q2 | 22% | Campanhas moderadas, pós-primavera |
| Q3 | 26% | Impulso crescente  |
| **Q4** | **31%** | **Alta temporada — pacotes de fim de ano e lançamentos de Jogo do Ano (GOTY)** |

**Implicação Estratégica:** Coordenar lançamentos globais para a janela de Q4 quando possível.

### 4. Análise de Desempenho de Publisher

**Líderes em Qualidade:**
1. **Rockstar** – Avaliação mediana: 4,26 (menos títulos, estratégia ultra-premium)
2. **Atlus** – Avaliação mediana: 4,10 (público de nicho, mas fiel)
3. **Bethesda** – Avaliação mediana: 4,02 (forte foco narrativo)

**Líderes em Volume:**
1. **Activision** – 205,9 milhões de vendas totais (franquias: CoD , Diablo, WoW)
2. **EA** – 187,3 milhões em vendas totais (franquias: FIFA, Madden, Battlefield)
3. **Sega** – 105,2 milhões de vendas totais (catalogo diversificado)

**Observação:** Os dados indicam que não existe um modelo único vencedor; o sucesso está na consistência estratégica e na coerência entre volume, qualidade e posicionamento de mercado.

---

### 5. Comparação de Gerações de Consoles

**PS3 (2006-2017):**
- 1.892 jogos | Avaliação mediana: 3,54 | Vendas totais: 839,66M
- Catálogo consolidado, franquias estabelecidas, crescimento orgânico

**PS4 (2013-Presente):**
- 1.991 jogos | Avaliação mediana: 3,57 | Vendas totais: 653,66M
- Maior biblioteca de geração única, adoção digital em massa
- Nota: Dados de vendas incompletos para lançamentos recentes

**PS5 (2020-Presente):**
- 1.080 jogos | Avaliação mediana: 3,67 | Vendas totais: Incompletas
- Menor catálogo (console ainda em fase de desenvolvimento)
- Média de qualidade mais alta - indica abordagem selecionada/que prioriza a qualidade
- Política de exclusividade do PS5 não clara; portabilidade entre gerações comum
---

## 💡 Recomendações Estratégicas

### Para Publishers

1. **Não depender apenas da qualidade**
   - Investir menor parte orçamental em qualidade e maior em marketing/posicionamento.
   - Avaliações positivas amplificam um bom marketing; marketing ruim desperdiça bons jogos.

2. **A escolha do gênero importa**
   - Action/Adventure: Aposta mais segura, demanda comprovada, competitivo
   - RPG/Shooter: Ótimas opções secundárias, público-alvo específico
   - Evitar: Puzzle/Strategy (nicho, menor receita)

3. **Otimizar a janela de lançamento**
   - Priorizar lançamentos no Q4 sempre que possível
   - Caso o Q4 não esteja disponível, posicione-se em Q3 (impulso no fim do trimestre)
   - Evite lançamentos em Q1 a menos que sejam direcionados a públicos-alvo específicos

4. **Estratégia de Portfólio por Segmento**
   - **AAA:** 2 a 3 títulos de ação/aventura por ano (foco no 4º trimestre)
   - **Intermediário:** 5 a 7 títulos de RPG/indie (distribuídos ao longo do ano)
   - **Nicho:** Exclusivamente digital, voltado para a comunidade (lançamento flexível)

---

### Para a Sony

1. **Revisão da estratégia para PS5**
   - Os dados atuais sugerem que a política exclusiva está subdesenvolvida
   - Recomendação: Negociar mais conteúdo exclusivo e destacar roteiro de desenvolvimento próprio
   - Benchmark: Os jogos exclusivos da PlayStation deveriam ocupar mais de 30% das prateleiras de produtos premium

2. **Otimização da Transição de Gerações**
   - PS3→PS4 declínio gradual na adoção; PS5 declínio mais acentuado até o momento
   - Recomendação: Lançar experiências exclusivas mais cedo no ciclo de vida do console

3. **Aprimoramento da Coleta de Dados**
   - Os dados atuais de vendas do PS5 ainda são muito imaturos para decisões estratégicas
   - Recomendação: Estabelecer um painel de vendas em tempo real para 2026 e anos seguintes

---

### Para Investidores

1. **Estratégia de Diversificação**
   - Indies demonstram qualidade de exposição, mas não volume de vendas; requer um portfólio com vários títulos
   - Franquias AAA apresentam volume, mas alto risco de execução
   - Equilibrado: 70% AAA, 30% indie

2. **Considerações**
   - Análise focada no agregado global; recomenda-se análise regional (NA/EU/Japan)
   - Ação domina globalmente; estratégia varia por região
---

## ⚠️ Limitações e Trabalhos Futuros

### Limitações atuais

🔴 Dados de vendas do PS5 ainda imaturos
🔴 DLCs e serviços de assinatura não considerados
🔴 Falta de métricas de marketing e comunidade

### Melhorias Futuras Recomendadas

✨ Previsão de Séries Temporais
✨ Segmentação Geográfica
✨ Análise de Redes
✨ Modelos causais

---

## 📚 Referências e fontes de dados

- **Dataset:** [Kaggle – PlayStation Sales and Metadata](https://www.kaggle.com/datasets/gvidalguiresse/playstation-sales-and-metadata-ps3ps4ps5)
- **VGChartz:** Rastreamento de vendas de videogames
- **RAWG API:** Metadados e classificações de jogos
- **Metodologia de análise:** Correlação de Spearman, análise de percentis, decomposição da tendência temporal

---

## 📄 Licença

Projeto disponibilizado para fins educacionais e de portfólio.

---

## 👤 Autor

**Augusto Rodrigues**

- 🔗 GitHub: [@uAugustoVR](https://github.com/uAugustoVR)
- 📧 LinkedIn: [Augusto Rodrigues](https://www.linkedin.com/in/augustovrodrigues)
- 📌 Data do Projeto: 12/2025

---

## 🙏 Agradecimentos

- **VGChartz e RAWG** API pela coleta e disponibilização dos dados
- **Kaggle** pela disponibilização do dataset
- **Comunidade Open Source** por ferramentas e bibliotecas essenciais

---

**Última atualização:** Dezembro de 2025

**Status:** ✅ Concluído

---