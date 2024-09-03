# Fazendo uma aplicação streamlit

import streamlit as st
import pandas as pd
import plotly.express as px

# Configurando a página para usar toda a largura da tela
st.set_page_config(layout="wide")

# Título da análise sobre o território do município do Rio de Janeiro com dados do censo e cruzamento de dados
st.title('📊 Análise do Território do Município do Rio de Janeiro')

# Subtítulo
st.write("""
**Bem-vindo ao aplicativo Streamlit desenvolvido para analisar o território do município do Rio de Janeiro, com foco na comparação e impacto do transporte público.** 

Este projeto foi criado por **Christian Basilio Oliveira**, Gestor Público e Pós-graduando em Comunicação Política na ESPM.

[LinkedIn](https://www.linkedin.com/in/christianbasilioo/).
""")
# Carregando os dados dos dois primeiros gráficos que vão ficar em paralelo em 2 colunas
# Carregando os dados do primeiro gráfico
bairrosMediaDense = pd.read_excel('bairros_media_dense.xlsx')

fig = px.bar(
    bairrosMediaDense, 
    x='NM_SUBDIST', 
    y='densidade', 
    title='Densidade média por Subdistrito da Cidade do Rio em 2022',
    labels={'NM_SUBDIST': 'Subdistrito', 'densidade': 'Densidade'},
    color='densidade',
    color_continuous_scale='RdYlGn_r'  # Inverted Red-Yellow-Green scale
)

fig.update_layout(
    title_font_size=20,
    xaxis_title_font_size=16,
    yaxis_title_font_size=16,
    # diminuindo os valores do eixo x
    xaxis_tickangle=90,
    template='plotly_white',
    showlegend=False  # Hide the legend
    , xaxis = dict(tickfont = dict(size = 10))
)

#fig.update_traces(texttemplate='%{y:.2f}', textposition='outside')
fig.update_traces(hovertemplate='Subdistrito: %{x}<br>Densidade: %{y:.2f}')


# Carregando os dados do segundo gráfico
onibus_media = pd.read_excel('onibus_media.xlsx')

fig_2 = px.bar(
    onibus_media, 
    x='NM_SUBDIST', 
    y='onibus', 
    title='Média de rotas de ônibus por Subdistrito em 2022',
    labels={'NM_SUBDIST': 'Subdistrito', 'onibus': 'Ônibus'},
    color='onibus',
    color_continuous_scale='RdYlBu',  # Red-Yellow-Blue scale
)

fig_2.update_layout(
    title_font_size=20,
    xaxis_title_font_size=16,
    yaxis_title_font_size=16,
    xaxis_tickangle=90,
    template='plotly_white',
    showlegend=False,  # Hide the legend
    xaxis=dict(tickfont=dict(size=10))  # Ajustar o tamanho da fonte do eixo x
)

fig_2.update_traces(hovertemplate='Subdistrito: %{x}<br>Total de Rotas de Onibus: %{y:.2f}')


# Colocando os gráficos lado a lado
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig)

with col2:
    st.plotly_chart(fig_2)



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
st.subheader('Análise de acesso de Onibus e Trem')

# criando grafico
trem_ou_nao = pd.read_excel('trem_ou_nao.xlsx')

# Fazendo grafico de trem ou nao
fig_3 = px.bar(
    trem_ou_nao, 
    x='trem_ou_nao', 
    y='Porcentagem', 
    title='Percentual de Acesso a trem no município do Rio de Janeiro em 2022',
    labels={'trem_ou_nao': ' ', 'v0001': 'Total de pessoas'},
    category_orders={'trem_ou_nao': ['Com acesso', 'Sem acesso']}
)

fig_3.update_layout(
    title_font_size=16,
    xaxis_title_font_size=1,
    yaxis_title_font_size=1,
    xaxis_tickangle=0,
    template='plotly_white',
    showlegend=False  # Hide the legend
)

fig_3.update_traces(texttemplate='%{y:.2f}%', textposition='outside')
fig_3.update_traces(hovertemplate='%{y:.2f}%')

#_--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Criando segundo grafico
onibus_15 = pd.read_excel('onibus_15.xlsx')


# criando o grafico com a porcentagem, sendo simples

fig_4 = px.bar(
    onibus_15, 
    x='onibus_ou_nao', 
    y='Porcentagem', 
    title='Percentual de Acesso a ônibus no município do Rio de Janeiro em 2022',
    labels={'onibus_ou_nao': 'Utiliza ônibus', 'Porcentagem': 'Porcentagem'}
)

fig_4.update_layout(
    title_font_size=16,
    xaxis_title_font_size=16,
    yaxis_title_font_size=1,
    xaxis_tickangle=0,
    template='plotly_white',
    showlegend=False  # Hide the legend
)

# Adicionando rótulos de dados
fig_4.update_traces(texttemplate='%{y:.2f}%', textposition='outside')
fig_4.update_traces(hovertemplate='%{y:.2f}%')



col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(fig_3)

with col4:
    st.plotly_chart(fig_4)

# Mapa 1 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import geopandas as gpd


df = gpd.read_file('dados_filtrados_rj_2FC_v2.shp')


# Definir uma escala de cores personalizada com duas cores
color_scale = ["#D32F2F", "#388E3C"]  # Vermelho e Verde, por exemplo
# Mostrar o mapa no app Streamlit

# Mapa 2 ---------
# Criar o mapa
# Definir uma escala de cores personalizada com duas cores


st.subheader('🚌 Mapa de Acesso a Ônibus a Menos de 500 Metros por Setor Censitário no Rio de Janeiro 🗺️\n\n')

st.text("""
### Informações sobre os Setores e Cálculo de Distância

Os setores censitários são as menores unidades territoriais utilizadas pelo Instituto Brasileiro 
de Geografia e Estatística (IBGE) para a coleta de dados censitários. Cada setor censitário é 
delimitado de forma a facilitar a coleta de informações e garantir a representatividade dos dados.

Neste estudo, o cálculo da distância dos ônibus é realizado a partir do ponto onde passam os ônibus 
em direção ao centro do setor censitário. Isso significa que a análise considera a proximidade dos 
pontos de ônibus em relação ao centro de cada setor, permitindo uma avaliação precisa do acesso ao 
transporte público em diferentes regiões do município do Rio de Janeiro.

A visualização dos dados no mapa e nos gráficos permite identificar áreas com maior ou menor acesso 
ao transporte público, auxiliando na tomada de decisões para melhorias na infraestrutura e no 
planejamento urbano.
""")
# Adicionar um slider para o filtro
min_rotas = st.slider("Selecione o número mínimo de rotas de ônibus", min_value=0, max_value=int(df["onibus"].max()), value=3)

# Filtro de linhas de ônibus
df_linhas_bus_nogeo = pd.read_excel('onibus_linhas_nogeo.xlsx')


# Filtro para selecionar linhas de ônibus específicas
linhas_disponiveis = df_linhas_bus_nogeo['servico'].unique()
linhas_selecionadas = st.multiselect('Selecione as linhas de ônibus para visualizar', options=linhas_disponiveis)

# Filtrar o DataFrame com base na seleção do usuário
df_filtrado = df[df["onibus"] >= min_rotas]

# Aplicar o filtro de linhas de ônibus
if linhas_selecionadas:
    df_filtrado = df_filtrado[df_filtrado['linhas_oni'].apply(
        lambda x: any(linha in x.split(',') for linha in linhas_selecionadas) if pd.notnull(x) else False)]


# Criar o mapa com os dados filtrados
map_2 = px.choropleth_mapbox(df_filtrado,
                             geojson=df_filtrado.geometry,
                             locations=df_filtrado.index,
                             color="onibus",
                             mapbox_style="carto-positron",
                             hover_name="densidade",
                             hover_data={
                                 "NM_SUBDIST": True,  # Não mostrar o nome do distrito duas vezes
                                 "v0001": ":,.0f",  # Formatar como número inteiro com separador de milhar
                                 "densidade": ":,.2f",  # Formatar com duas casas decimais
                                 "onibus": True,
                                 'linhas_oni': True
                             },
                             labels={
                                 "v0001": "Total da População",
                                 "densidade": "Densidade (hab/km²)",
                                 'onibus': 'Total de Onibus',
                                 'NM_SUBDIST': 'Subdistrito',
                                    'linhas_oni': 'Linhas de Ônibus'
                             },
                             center={"lat": -22.913732, "lon": -43.348177},  # Localização central ajustada
                             zoom=10,
                             opacity=0.6,  # Usar a escala de cores padrão
                             color_continuous_scale=px.colors.sequential.Viridis)  # Usar a escala de cores personalizada

# Ajustar layout
map_2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Melhorando os popups
map_2.update_traces(
    marker_line_width=0,
    selector=dict(type='choropleth'),
    hovertemplate='<b>Bairro: %{customdata[3]}</b><br><br>' +
                  'Total de Ônibus: %{customdata[1]:,.0f}<br>' +
                  'Densidade: %{customdata[2]:,.2f} hab/km²<br>' +
                  'Total de Pessoas: %{customdata[0]:,.0f}<br>' +
                'Linhas de Ônibus: %{customdata[4]}<br>' +  # Adicionar linhas_onibus ao hover template
                  '<extra></extra>'
)

# Exibir o mapa no Streamlit
st.plotly_chart(map_2)

