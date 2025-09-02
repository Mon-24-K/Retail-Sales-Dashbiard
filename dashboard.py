import streamlit as st
import pandas as pd
import plotly.express as px

data=pd.DataFrame({
    "Month":["Jan","Feb","March","April","May","Jun","Jul","Aug"],
    "Sales":[15000,18000,12000,22000,19000,24000,21000,26000],
    "Profit":[4000,5000,3000,7000,6000,8000,7500,9000],
    "Region":["North","South","East","West","North","South","East","West"],
    "Category":["Electronics","Fashion","Groceries","Electronics","Fashion","Groceries","Electronics","Fashion"]
})

#Dashboard Title
st.set_page_config(page_title="Retail Sales Dashboard",layout="wide")
st.title("✨Retail Sales Dashboard✨")

#filters (top panel)
with st.expander("Filters",expanded=True):
    col1,col2=st.columns(2) 
    with col1:
        regions=st.multiselect(
            "Select Region(s)",
            options=data["Region"].unique(),
            default=list(data["Region"].unique())
        )
    with col2:
        categories=st.multiselect(
            "Select Categorie(s)",
            options=data["Category"].unique(),
            default=list(data["Category"].unique())
        )

#filtered data
filtered =data[(data["Region"].isin(regions))&(data["Category"].isin(categories))]

#KPIs(Top Row)
col1,col2=st.columns(2) # 2 columns are total profit and total sales
with col1:
    st.metric("💰Total Sales",value=filtered["Sales"].sum())
with col2:
    st.metric("Total Profit",value=filtered["Profit"].sum())
     

st.markdown("### Sales Analysis")

col1,col2=st.columns(2)
with col1:
    fig1=px.line(filtered, x="Month",y="Sales",color="Region",title="Sales Trend Over Time")
    st.plotly_chart(fig1,use_container_width=True)

with col2:
    fig2=px.bar(filtered,x="Category",y="Sales",color="Region",
                barmode="group",title="Sales by Caregory")
    st.plotly_chart(fig2,use_container_width=True)

col3,col4=st.columns(2)
with col3:
    fig3=px.pie(filtered, values="Sales",names="Region",
                title="Sales Share by Region")
    st.plotly_chart(fig3,use_container_width=True)

with col4:
    fig4=px.scatter(filtered,x="Sales",y="Profit",color="Category",
                    size="Sales",hover_data=["Month"],
                    title="Sales vs Profit")
    st.plotly_chart(fig4,use_container_width=True)

#start -> anaconda prompt -> streamlit run *filename*.py -> enter   

    
