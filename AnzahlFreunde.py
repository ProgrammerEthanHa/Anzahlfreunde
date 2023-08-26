import streamlit as st
import pandas as pd
import altair as alt

st.header("Ein Freund, ein guter Freund")
st.subheader("Anzahl der engen Freundinnen und Freunde der Befragten")

source = pd.DataFrame({
        'Anteil(%)': [40, 33, 9, 2, 11, 5],
        'Anzahl': ['1 bis 2', '3 bis 4', '5 bis 9', 'Mehr als 10', 'keine', 'Weiß nicht']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Anzahl:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis n=2046 Befragte (ab 18 Jahren) in Deutschland; 2019
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle:  YouGov")