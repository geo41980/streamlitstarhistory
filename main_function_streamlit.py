import pandas as pd
import streamlit as st
import altair as alt


def main():

	page = st.sidebar.selectbox("Choose the Test Type", ["PCR","Rapid"])

	if page == 'PCR':
		df = load_data(type_='PCR')
	elif page == 'Rapid':
		df = load_data(type_='Rapid')

	st.title("{} Test Monitoring Dashboard".format(page))
	
	viz_type_filter = st.selectbox("Viz Type Filter", ['Daily','Cummulative'],0)

	if viz_type_filter == 'Daily':
		st.markdown("> Chart in this page shows the comparison of number of respondents who is tested and not tested")
		st.write("#Respondents: {}".format(len(df)))
		
		variable_filter = st.selectbox("Variable Filter", ['No Filter','Region',"Respondent's Age","Respondent's Gender","Respondent's Wage"],0)

		if variable_filter == 'No Filter':
			visualize_is_tested_comparison(df,None)
		elif variable_filter == 'Region':
			visualize_is_tested_comparison(df,'region')
		elif variable_filter == "Respondent's Age":
			visualize_is_tested_comparison(df,'age')
		elif variable_filter == "Respondent's Gender":
			visualize_is_tested_comparison(df,'gender')
		elif variable_filter == "Respondent's Wage":
			visualize_is_tested_comparison(df,'wage')
		else:
			st.write("Work in Progress..")


	elif viz_type_filter == 'Cummulative':
		st.markdown("> Charts in this page are generated based on accumulated data up to the desired date filter")

		date_filter = st.date_input('Date', max(df['date']))

		df_filter = df[df['date']<=date_filter]

		#Show Total Survey Data
		st.write("#Respondents: {}".format(len(df_filter)))

		#Show Cummulative Charts
		visualize_cummulative_charts(df_filter)
