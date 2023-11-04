import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import pandas as pd

def compare_equities(df:pd.DataFrame, eq1:str, eq2:str):
    """Genera un gráfico comparativo de dos activos financieros.

    Args:
        df (pd.DataFrame): DataFrame con los datos de los activos financieros.
        eq1 (str): Primer activo financiero.
        eq2 (str): Segundo activo financiero.
    """
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df.index.values, y=df[eq1],
                             mode='lines',
                             name=eq1))

    fig.add_trace(go.Scatter(x=df.index.values, y=df[eq2],
                             mode='lines',
                             name=eq2,
                             line_color='green'))

    fig.add_trace(go.Scatter(x=df.index.values, 
                             y=df[eq2],
                             fill=None,
                             mode='lines',
                             line_color='rgba(255, 0, 0, 0)',
                             name='Area',
                             showlegend=False))
    fig.add_trace(go.Scatter(x=df.index.values, 
                             y=df[eq1],
                             fill='tonexty',
                             fillcolor='rgba(255, 0, 0, 0.2)',
                             mode='lines',
                             line_color='rgba(255, 0, 0, 0)',
                             showlegend=False))

    fig.update_layout(title={'text': f'Comparación de {eq1} vs {eq2}', 'x':0.5, 'xanchor': 'center'}, 
                      title_font=dict(size=24),
                      xaxis_title='Fecha',
                      yaxis_title='Precio',
                      height=500,
                      width=1000,
                      margin=dict(l=40, r=40, t=40, b=40))

    fig.show()



def plot_equities_dividends_splits(df:pd.DataFrame, title:str):
    """Crea un gráfico con 3 subplots.
    1. Close vs Adj Close
    2. Dividends
    3. Stock Splits

    Args:
        df (pd.DataFrame): DataFrame con los datos de los activos financieros.
        title (str): Título del gráfico.
    """
    # Create a figure with 3 subplots
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))

    # Plot "Close" and "Adj Close" on the first subplot
    sns.lineplot(data=df, x='Date', y='Close', label='Close', ax=ax1)
    sns.lineplot(data=df, x='Date', y='Adj Close', label='Adj Close', ax=ax1)

    # Plot "Dividends" on the second subplot
    sns.lineplot(data=df, x='Date', y='Dividends', style=True, markers=True, dashes=False, ax=ax2)

    # Plot "Stock Splits" on the third subplot
    sns.lineplot(data=df, x='Date', y='Stock Splits', style=True, markers=True, dashes=False, ax=ax3)

    # Adjust the layout
    fig.suptitle(title)
    fig.tight_layout()

    # Show the figure
    plt.show()
