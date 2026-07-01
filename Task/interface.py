import streamlit as st
import pandas as pd

@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    
    if 'FINANCIAL_ITEM_NAME_TR' in df.columns:
        df = df.drop(columns=['FINANCIAL_ITEM_NAME_TR'])

    periods=['2025/3', '2025/6', '2025/9', '2025/12']
    for p in periods:
        if p in df.columns:
            df[p] = pd.to_numeric(df[p], errors='coerce')
    
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)

    string_cols = df.select_dtypes(include=['object', 'string']).columns
    df[string_cols] = df[string_cols].fillna("-")
    
    return df

DATA_URL = "BIST_2025_All_Financials.csv"
df = load_data(DATA_URL)

st.set_page_config(page_title="BIST 2025 Financials", layout="wide")
st.title("BIST 2025 Financials")

tab1,tab2 = st.tabs(["Performans", "Raw Data"])

with tab1:
    st.subheader("Multi-Company Comparisen")
    c1,c2 = st.columns([2,2])
    with c1:
        comp_tickers=st.multiselect(
            "Select Companies:",
            options=df['Ticker'].unique()
        )

    with c2:
        comp_item = st.selectbox(
            "Select Metric:",
            options=df['FINANCIAL_ITEM_NAME_EN'].unique(),
            index =0
        )
    
    if comp_tickers and comp_item:
        compare_df = df[(df['Ticker'].isin(comp_tickers)) & (df['FINANCIAL_ITEM_NAME_EN'] == comp_item)]
        
        st.write("### Q4 Snapshot (2025/12)")
        metric_cols = st.columns(len(comp_tickers))
        
        for idx, ticker in enumerate(comp_tickers):
            ticker_data = compare_df[compare_df['Ticker'] == ticker]
            if not ticker_data.empty:
                q1_val = float(ticker_data['2025/3'].values[0])
                q4_val = float(ticker_data['2025/12'].values[0])
                
                growth = ((q4_val - q1_val) / q1_val * 100) if q1_val != 0 else 0
                
                with metric_cols[idx]:
                    st.metric(
                        label=f"{ticker} - {comp_item}", 
                        value=f"{q4_val:,.0f}", 
                        delta=f"{growth:.2f}% since Q1"
                    )
        
        st.write("### Trend Lines Across 2026 Periods")
        
        periods = ['2025/3', '2025/6', '2025/9', '2025/12']
        melted = compare_df.melt(
            id_vars=['Ticker'], 
            value_vars=periods, 
            var_name='Period', 
            value_name='Value'
        )
        
        chart_pivot = melted.pivot(index='Period', columns='Ticker', values='Value')
        st.line_chart(chart_pivot, use_container_width=True)
        
        st.write(" Automated Financial Analysis")
        
        insights = []
        for ticker in comp_tickers:
            ticker_data = compare_df[compare_df['Ticker'] == ticker]
            if not ticker_data.empty:
                q1 = float(ticker_data['2025/3'].values[0])
                q4 = float(ticker_data['2025/12'].values[0])
                
                if q4 > q1 and q1 > 0:
                    insights.append(f"**{ticker}** demonstrates a positive trajectory for *{comp_item}*, scaling up by **{((q4-q1)/q1)*100:.1f}%** over the year. This suggests strong operational velocity.")
                elif q4 < q1 and q1 > 0:
                    insights.append(f"**{ticker}** shows a contraction in *{comp_item}*, dropping by **{((q1-q4)/q1)*100:.1f}%**. Target this for risk mitigation or liquidity check.")
                else:
                    insights.append(f"**{ticker}** remained flat or started with a baseline of zero for *{comp_item}* throughout 2025.")
                    
        st.info("\n\n".join(insights))
        
    else:
        st.warning("Please select at least one company and a financial metric to generate the comparison matrix.")


with tab2:
    st.subheader("Data Grid Slicing")
    col1, col2 = st.columns(2)

    with col1:
        unique_tickers = df['Ticker'].dropna().unique()
        selected_tickers = st.multiselect("Filter Table by Companies:", unique_tickers, key="grid_tickers")

    with col2:
        unique_items = df['FINANCIAL_ITEM_NAME_EN'].dropna().unique()
        selected_items = st.multiselect("Filter Table by Financial Items:", unique_items, key="grid_items")

    filtered_df = df.copy()

    if selected_tickers:
        filtered_df = filtered_df[filtered_df['Ticker'].isin(selected_tickers)]

    if selected_items:
        filtered_df = filtered_df[filtered_df['FINANCIAL_ITEM_NAME_EN'].isin(selected_items)]

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )