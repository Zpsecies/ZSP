import streamlit as st
import plotly.express as px
import pandas as pd
import altair as alt
import os
import warnings

warnings.filterwarnings('ignore')


st.set_page_config(page_title="User Performance Analysis", page_icon=":chart_with_upwards_trend:", layout="wide")
st.title(":chart_with_upwards_trend: User Performance Analysis")
st.sidebar.header("**BIM Analyzer_Zspecies_0.01**")
st.divider()

# project details 

st.subheader(":building_construction: SP01_ID_OFFICE_2024")

cl1,cl2 = st.columns((2))


with cl2:
    st.image("/Users/apple/Desktop/untitled folder/fotor-ai-20240207162856.jpg", width=400, caption="SP[]_Tower03")
     
with cl1: 
    st.markdown(''':wrench: **Scope Of Work :** <p style='color: #00FFFF;'>   <em> Wall, Floor, Room, Coloumn,Beam,Door,Window,Stair</p>''', unsafe_allow_html=True) 
    st.markdown(''':male-office-worker: **Users :**  <p style='color: #00FFFF;'> <em>User_ A, User_ B, User_ C, User_ D, User_ E,User_ F, User_ G, User_ H, User_ I, User_ J, User_ K</p>''',unsafe_allow_html= True)
    st.markdown("**Star Date :**   Nov3,2023")
    st.markdown("**Planned End Date :**   Feb3,2024")
st.divider()

st.subheader(''' :sky[Select Start & End Date For Categorty Wise Data]''')




def element_data(elem_selected_df,elem_selected_df_lastdate,slecet_element, ele_hours):
    ## element data 
    ## data for pie chart /// Element Created By Users
    user_elem_data =  elem_selected_df.groupby( by=["User"], as_index = False)[slecet_element].sum()
    user_elem_data_lastdate = elem_selected_df_lastdate.groupby( by = ["User"], as_index = False)[slecet_element].sum()

    date_elem_data =  elem_selected_df.groupby( by = ["Date"], as_index = False)[slecet_element].sum()
    user_elemhour_data =  elem_selected_df.groupby( by = ["User"], as_index = False)[ele_hours].sum()

    ### max element creator 
    max_elem_index  =  user_elem_data[slecet_element].idxmax()
    max_elem_owner =  user_elem_data.loc[ max_elem_index, "User"]
    max_elem_bycreator = elem_selected_df_lastdate.loc[max_elem_index, slecet_element]
    

    ### min element creator 
    min_elem_index  =  user_elem_data[slecet_element].idxmin()
    min_elem_owner =  user_elem_data.loc[ min_elem_index, "User"]
    min_elem_bycreator = elem_selected_df_lastdate.loc[min_elem_index, slecet_element]

    ## per houre performance to model elements 
    elem_hr_result =  user_elem_data.copy()
    elem_hr_result["Per_Houre_Performance"]= user_elem_data[slecet_element]/ user_elemhour_data[ele_hours]
    
    
    ### max performing user 
    max_elemperhr_user_index = elem_hr_result["Per_Houre_Performance"].idxmax()
    max_elemperhr_user = elem_hr_result.loc[max_elemperhr_user_index,"User"]
    max_elemperhr = round(elem_hr_result.loc[max_elemperhr_user_index, "Per_Houre_Performance"])

    ### min performing user 
    min_elemperhr_user_index = elem_hr_result["Per_Houre_Performance"].idxmin()
    min_elemperhr_user = elem_hr_result.loc[min_elemperhr_user_index,"User"]
    min_elemperhr = round(elem_hr_result.loc[min_elemperhr_user_index, "Per_Houre_Performance"] )

    elem_col1, elem_col2 = st.columns(2)

    with elem_col2:
        st.subheader(" :bar_chart: Element Developed With Time")
        fig_elem_pie = px.pie(user_elem_data_lastdate, values = slecet_element, names= "User"  , hole=0.5)
        fig_elem_pie.update_traces(textposition='outside', textinfo='percent+label')
        st.plotly_chart(fig_elem_pie, use_container_width=True)

    with elem_col1:
        st.subheader(":label: Element Created By Users")
        fig_elem_bar  = px.bar(date_elem_data , x = "Date", y = slecet_element,text = ['{:}'.format(x) for x in date_elem_data[slecet_element]],
                    template = "seaborn")
        st.plotly_chart( fig_elem_bar, use_container_width= True)

    
        elem_col1_01, elem_col1_02 = st.columns(2)

        with elem_col1_01:
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown(f"<span style='color:Azure; font-size: x-large; font-weight: Normal'>Maximum No. Of Elements Created By:</span>", unsafe_allow_html=True)
        with elem_col1_02:
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown(f"<span style='color:Azure; font-size: x-large; font-weight: Normal'>Minimum No. Of Elements Created By:</span>", unsafe_allow_html=True)

        elem_col1_sub_01,elem_col1_sub_02,elem_col1_sub_03,elem_col1_sub_04 = st.columns(4)

        with elem_col1_sub_01:
            st.markdown("")
            st.markdown(f"<span style='color:BurlyWood; font-size: xx-large; font-weight: bold'>{max_elem_owner}</span>", unsafe_allow_html=True)

        with elem_col1_sub_02:
            st.markdown("")   
            st.markdown(f"<span style='color:BurlyWood; font-size: xx-large; font-weight: bold'>{max_elem_bycreator}</span>", unsafe_allow_html=True)

        with elem_col1_sub_03:
             st.markdown("")
             st.markdown(f"<span style='color:OrangeRed; font-size: xx-large; font-weight: bold'>{min_elem_owner}</span>", unsafe_allow_html=True)

        with elem_col1_sub_04:
            st.markdown("")   
            st.markdown(f"<span style='color:red; font-size: xx-large; font-weight: bold'> {min_elem_bycreator} </span>", unsafe_allow_html=True)
  
        elem_col1_03, elem_col1_04 = st.columns(2)

        with elem_col1_03:
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown(f"<span style='color:Azure; font-size: x-large; font-weight: Normal'>Efficiency_Maximum</span>", unsafe_allow_html=True)
        with elem_col1_04:
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.markdown(f"<span style='color:Azure; font-size: x-large; font-weight: Normal'>Efficiency_Minimum</span>", unsafe_allow_html=True)

        elem_col1_sub_05,elem_col1_sub_06,elem_col1_sub_07,elem_col1_sub_08 = st.columns(4)

        with elem_col1_sub_05:
            st.markdown("")   
            st.markdown(f"<span style='color:BurlyWood; font-size: xx-large; font-weight: bold'> {max_elemperhr_user} </span>", unsafe_allow_html=True)
        with elem_col1_sub_06:
            st.markdown("")   
            st.markdown(f"<span style='color:BurlyWood; font-size: xx-large; font-weight: bold'> {max_elemperhr}/hour</span>", unsafe_allow_html=True)
  
        with elem_col1_sub_07:
            st.markdown("")   
            st.markdown(f"<span style='color:BurlyWood; font-size: xx-large; font-weight: bold'>{min_elemperhr_user}</span>", unsafe_allow_html=True)
        with elem_col1_sub_08:
            st.markdown("")   
            st.markdown(f"<span style='color:BurlyWood; font-size: xx-large; font-weight: bold'>{min_elemperhr}/hour</span>", unsafe_allow_html=True)
    
    with elem_col2:
        fig_elem_perf = px.line( x= pd.DataFrame(elem_hr_result)["User"], y = pd.DataFrame(elem_hr_result)["Per_Houre_Performance"],markers= True)
        fig_elem_perf.update_layout(xaxis_title="User", yaxis_title="Efficiency")
        st.plotly_chart( fig_elem_perf, use_container_width= True)
    
    ## Efficiency vs Creation 
    elem_df =  pd.DataFrame(elem_hr_result).copy()
    elem_df["hours"] = user_elemhour_data[ele_hours]
    fig_elem_scatter =  px.scatter(elem_df, x = slecet_element, y = "Per_Houre_Performance",size = slecet_element, color= "User", hover_name= slecet_element, log_x= True, size_max=60)
    st.plotly_chart(fig_elem_scatter, theme = "streamlit",use_container_width=True)

def eleme_linechrt(elem_selected_df,elem1,elemhr1):
    user_elem_data = elem_selected_df.groupby( by = ["User"], as_index  = False)[elem1].sum()
    elem_hr_result = user_elem_data.copy()
    

    user_elemhr_data = elem_selected_df.groupby( by = ["User"], as_index = False)[elemhr1].sum()
    elem_hr_result["Performance"] = user_elem_data[elem1]/ user_elemhr_data[elemhr1]

    fig_elem_performance_line  = px.line( x = pd.DataFrame(elem_hr_result)["User"], y = pd.DataFrame(elem_hr_result)["Performance"], markers= True, width=350, height=350)
    fig_elem_performance_line.update_layout(xaxis_title="User", yaxis_title="Efficiency" )
    st.plotly_chart(fig_elem_performance_line,use_container_width= True)



tab_structural, tab_arch, tab_plumbing , tab_overall = st.tabs(["Structural","Architectural","Plumbing", "Coordination"]) 
###############################################   File uploaders ##############################################

str_files = st.sidebar.file_uploader(":file_folder: Upload Structure Daily Users' Reports", type=["csv", "xls"], accept_multiple_files=True)

ar_files = st.sidebar.file_uploader(":file_folder: Upload Architecture Daily Users' Reports", type=["csv","xls"], accept_multiple_files= True)

pl_files = st.sidebar.file_uploader(":file_folder: Upload Plumbing Daily Users' Reports", type=["csv","xls"], accept_multiple_files= True)


#######______________________ Structural Tab ___________________________#######

with tab_structural:

    files_names = list()
    all_str_data = pd.DataFrame()  # Create an empty DataFrame to accumulate data from all files

    if str_files:
        for str_file in str_files:
            if str_file is not None:
                filename = str_file.name
                files_names.append(filename)

                df = pd.read_csv(str_file, encoding="ISO-8859-3")
                
                all_str_data = pd.concat([all_str_data, df])  # Concatenate data from each file


    str_dates = all_str_data["Date"].unique()
    str_startdate = str_dates.min()
    st.write(str_startdate)
    str_enddate = str_dates.max()


    col1, col2 = st.columns(2)

    with col1:
        str_startdate = pd.to_datetime(str_startdate)  # Convert to datetime
        str_date1 = st.date_input("Start Date(Strucrure)", str_startdate)

    with col2:
        str_enddate = pd.to_datetime(str_enddate)  # Convert to datetime
        str_date2 = st.date_input("End Date(Structure)", str_enddate)

    all_str_data["Date"] = pd.to_datetime(all_str_data["Date"])



    # # # Filter the DataFrame based on the selected date range
    str_selected_df  = all_str_data[(all_str_data["Date"] >= pd.to_datetime(str_date1)) & (all_str_data["Date"] <= pd.to_datetime(str_date2))]
    str_selected_df_lastdate = all_str_data[all_str_data["Date"] == pd.to_datetime(str_date2)]

    st.write(str_selected_df)
    
    str_option_col1, str_option_col2 = st.columns(2)

    with str_option_col1:
        str_option_st_elem = st.selectbox( "Select Architectural Elements ",( "Column","Beam","Floor","Wall","Stair"))
    with str_option_col2:
        str_option_st_elemhr  = st.selectbox("Select Architectural Element Hours ", ("Column_Hours","Beam_Hours","Floor_Hours","Wall_Hours","Stair_Hours"))

    element_data(str_selected_df,str_selected_df_lastdate,str_option_st_elem,str_option_st_elemhr)
    

############# _____________ Architectural Tab____________________#########

ar_files_names = list()
all_ar_data = pd.DataFrame()  # Create an empty DataFrame to accumulate data from all files

if ar_files:
    for ar_file in ar_files:
        if ar_file is not None:
            ar_filename = ar_file.name
            ar_files_names.append(ar_filename)

            ar_df = pd.read_csv(ar_file, encoding="ISO-8859-4")
            
            all_ar_data = pd.concat([all_ar_data, ar_df])  # Concatenate data from each file

# st.write(all_ar_data)

ar_dates = all_ar_data["Date"].unique()
# st.write(ar_dates)
ar_startdate = pd.to_datetime(ar_dates).min()
# st.write(ar_startdate)
ar_enddate = pd.to_datetime(ar_dates).max()
# st.write(ar_enddate)


with tab_arch:


    ar_col1, ar_col2 = st.columns(2)

    with ar_col1:
        ar_date1 = st.date_input("StartDate(Arch)", ar_startdate)

    with ar_col2:
        ar_date2 = st.date_input("EndDate(Arch)", ar_enddate)

    all_ar_data["Date"] = pd.to_datetime(all_ar_data["Date"])



        # # # Filter the DataFrame based on the selected date range
    ar_selected_df  = all_ar_data[(all_ar_data["Date"] >= pd.to_datetime(ar_date1)) & (all_ar_data["Date"] <= pd.to_datetime(ar_date2))]
    ar_selected_df_lastdate = all_ar_data[all_ar_data["Date"] == pd.to_datetime(ar_date2)]
    st.write(ar_selected_df_lastdate)

    ar_option_col1, ar_option_col2 = st.columns(2)

    with ar_option_col1:
        ar_option_st_elem = st.selectbox( "Select Architectural Elements ",( "Dry_Wall","Room","Floor_Finish","Ceiling","Door"))
    with ar_option_col2:
        ar_option_st_elemhr  = st.selectbox("Select Architectural Element Hours ", ("Dry_Wall_Hours","Room_Hours","Floor_Finish_Hours","Ceiling_Hours","Door_Hours"))

    element_data(ar_selected_df,ar_selected_df_lastdate,ar_option_st_elem,ar_option_st_elemhr)

############_____________________Plumbing tab data __________________########

pl_files_names = list()
all_pl_data = pd.DataFrame()  # Create an empty DataFrame to accumulate data from all files

if pl_files:
    for pl_file in pl_files:
        if pl_file is not None:
            pl_filename = pl_file.name
            pl_files_names.append(pl_filename)

            pl_df = pd.read_csv(pl_file, encoding="ISO-8859-2")
            
            all_pl_data = pd.concat([all_pl_data, pl_df])  # Concatenate data from each file

# st.write(all_ar_data)

pl_dates = all_pl_data["Date"].unique()
pl_startdate = pd.to_datetime(pl_dates).min()
# st.write(ar_startdate)
pl_enddate = pd.to_datetime(pl_dates).max()
# st.write(ar_enddate)


with tab_plumbing:

    pl_col1, pl_col2 = st.columns(2)

    with pl_col1:
        pl_date1 = st.date_input("Start Date1", pl_startdate)

    with pl_col2:
        pl_date2 = st.date_input("End Date1", pl_enddate)

    all_pl_data["Date"] = pd.to_datetime(all_pl_data["Date"])



        # # # Filter the DataFrame based on the selected date range
    pl_selected_df  = all_pl_data[(all_pl_data["Date"] >= pd.to_datetime(pl_date1)) & (all_pl_data["Date"] <= pd.to_datetime(pl_date2))]
    pl_selected_df_lastdate = all_pl_data[all_pl_data["Date"] == pd.to_datetime(pl_date2)]
    st.write(pl_selected_df_lastdate)

    pl_option_col1, pl_option_col2 = st.columns(2)

    with pl_option_col1:
        pl_option_st_elem = st.selectbox( "Select Structural Elements ",( "Pipe","Manhole","Fitting","Equipment","Fixture"))
    with pl_option_col2:
        pl_option_st_elemhr  = st.selectbox("Select Element Hours ", ("Pipe_Hours","Manhole_Hours","Fitting_Hours","Equipment_Hours","Fixture_Hours"))

    element_data(pl_selected_df,pl_selected_df_lastdate,pl_option_st_elem,pl_option_st_elemhr)


with tab_overall:
    
    ###_____Structural linechars____###
    str_lnc_col1, str_lnc_col2, str_lnc_col3, str_lnc_col4, str_lnc_col5 = st.columns(5)
    str_ls = ( "Column","Beam","Floor","Wall","Stair")
    str_ls_hr  = ("Column_Hours","Beam_Hours","Floor_Hours","Wall_Hours","Stair_Hours")
   

    with str_lnc_col1:
        st.write(str_ls[0])
        eleme_linechrt(str_selected_df,str_ls[0],str_ls_hr[0])
    with str_lnc_col2:
        st.write(str_ls[0])
        eleme_linechrt(str_selected_df,str_ls[1],str_ls_hr[1])
    with str_lnc_col3:
        st.write(str_ls[0])
        eleme_linechrt(str_selected_df,str_ls[2],str_ls_hr[2])
    with str_lnc_col4:
        st.write(str_ls[0])
        eleme_linechrt(str_selected_df,str_ls[3],str_ls_hr[3])
    with str_lnc_col5:
        st.write(str_ls[0])
        eleme_linechrt(str_selected_df,str_ls[4],str_ls_hr[4])

        ###_____Architectural linechars____###
    ar_lnc_col1, ar_lnc_col2, ar_lnc_col3, ar_lnc_col4, ar_lnc_col5 = st.columns(5)
    ar_ls = ("Dry_Wall","Room","Floor_Finish","Ceiling","Door")
    ar_ls_hr  = ("Dry_Wall_Hours","Room_Hours","Floor_Finish_Hours","Ceiling_Hours","Door_Hours")
   

    with ar_lnc_col1:
        # st.write(ar_ls[0])
        # st.write(ar_ls_hr[0])
        eleme_linechrt(ar_selected_df,ar_ls[0],ar_ls_hr[0])
    with ar_lnc_col2:
        # st.write(str_ls[0])
        eleme_linechrt(ar_selected_df,ar_ls[1],ar_ls_hr[1])
    with ar_lnc_col3:
        # st.write(str_ls[0])
        eleme_linechrt(ar_selected_df,ar_ls[2],ar_ls_hr[2])
    with ar_lnc_col4:
        # st.write(str_ls[0])
        eleme_linechrt(ar_selected_df,ar_ls[3],ar_ls_hr[3])
    with ar_lnc_col5:
        # st.write(str_ls[0])
        eleme_linechrt(ar_selected_df,ar_ls[4],ar_ls_hr[4])

        ###_____Plumbing linechars____###
    pl_lnc_col1, pl_lnc_col2, pl_lnc_col3, pl_lnc_col4, pl_lnc_col5 = st.columns(5)
    pl_ls = ( "Pipe","Manhole","Fitting","Equipment","Fixture")
    pl_ls_hr  = ("Pipe_Hours","Manhole_Hours","Fitting_Hours","Equipment_Hours","Fixture_Hours")
   

    with pl_lnc_col1:
        # st.write(ar_ls[0])
        # st.write(ar_ls_hr[0])
        eleme_linechrt(pl_selected_df,pl_ls[0],pl_ls_hr[0])
    with pl_lnc_col2:
        # st.write(str_ls[0])
        eleme_linechrt(pl_selected_df,pl_ls[1],pl_ls_hr[1])
    with pl_lnc_col3:
        # st.write(str_ls[0])
        eleme_linechrt(pl_selected_df,pl_ls[2],pl_ls_hr[2])
    with pl_lnc_col4:
        # st.write(str_ls[0])
        eleme_linechrt(pl_selected_df,pl_ls[3],pl_ls_hr[3])
    with pl_lnc_col5:
        # st.write(str_ls[0])
        eleme_linechrt(pl_selected_df,pl_ls[4],pl_ls_hr[4])
    

# def st_elem_piechart(st_elem,st_date):

#     user_st_elem_data_lastdate = str_selected_df_lastdate.groupby( by = ["User"], as_index = False)[st_elem].sum()
#     fig_st_elem_pie = px.pie(user_st_elem_data_lastdate,names="User", values = st_elem, hover_name="User", width=250,height=250, hole=0.5)
#     fig_st_elem_pie.update_traces(textposition='outside', textinfo='percent+label')
#     st.plotly_chart(fig_st_elem_pie, use_container_width=True)



# tab_structural, tab_arch, tab_plumbing = st.tabs(["Structural","Architectural","Plumbing"]) 

# with tab_structural:
#     st.subheader("Structural Data Sheet")
#     st.write( str_selected_df)
#     option_col1, option_col2 = st.columns(2)

#     with option_col1:
#         option_st_elem = st.selectbox( "Select Structural Elements ",( "Column","Beam","Wall","Floor"))
#     with option_col2:
#         option_st_elemhr  = st.selectbox("Select Element Hours ", ("Column_Hours","Beam_Hours","Wall_Hours","Floor_Hours"))



#     st_element_data(option_st_elem,option_st_elemhr)
#     st.divider()
#     st.write(f"<span style='color:BurlyWood; font-size: large; font-weight: Normal'>These graphs show the user performance on different structural element creation </span>", unsafe_allow_html=True)
#     performance_col1,performance_col2,performance_col3,performance_col4 = st.columns(4)
#     with performance_col1:
#         st.markdown(f"<span style='color:Azure; font-size: x-large; font-weight: Normal'>User_Efficiency_Column</span>", unsafe_allow_html=True)
#         st_eleme_linechrt("Column","Column_Hours")

#     with performance_col2:
#         st.markdown(f"<span style='color:Azure; font-size: x-large; font-weight: Normal'>User_Efficiency_Beam</span>", unsafe_allow_html=True)
#         st_eleme_linechrt("Beam","Beam_Hours")
#     with performance_col3:
#         st.markdown(f"<span style='color:Azure; font-size: x-large; font-weight: Normal'>User_Efficiency_Wall</span>", unsafe_allow_html=True)
#         st_eleme_linechrt("Wall","Wall_Hours")
#     with performance_col4:
#         st.markdown(f"<span style='color:Azure; font-size: x-large; font-weight: Normal'>User_Efficiency_Floor</span>", unsafe_allow_html=True)
#         st_eleme_linechrt("Floor","Floor_Hours")
#     st.divider()
#     st.write(f"<span style='color:BurlyWood; font-size: large; font-weight: Normal'>These graphs show the number of different structural element ctreated by different users </span>", unsafe_allow_html=True)
#     data_col1,data_col2,data_col3,data_col4 = st.columns(4)

#     with data_col1:
#         st.markdown(f"<span style='color:Azure; font-size: x-large; font-weight: Normal'>User_Column Data</span>", unsafe_allow_html=True)
#         st_elem_piechart("Column","Date")

#     with data_col2:
#         st.markdown(f"<span style='color:Azure; font-size: x-large; font-weight: Normal'>User_Beam Data</span>", unsafe_allow_html=True)
#         st_elem_piechart("Beam","Date")
    
#     with data_col3:
#         st.markdown(f"<span style='color:Azure; font-size: x-large; font-weight: Normal'>User_Wall Data</span>", unsafe_allow_html=True)
#         st_elem_piechart("Wall","Date")

#     with data_col4:
#         st.markdown(f"<span style='color:Azure; font-size: x-large; font-weight: Normal'>User_Floor Data</span>", unsafe_allow_html=True)
#         st_elem_piechart("Floor","Date")

# ############################################### architectural  file upload & data collect ##############################################
        


# def ar_element_data(slecet_element, ele_hours):
#     ## element data 
#     ## data for pie chart /// Element Created By Users
#         ar_user_elem_data =  ar_selected_df.groupby( by=["User"], as_index = False)[slecet_element].sum()
#         ar_user_elem_data_lastdate = ar_selected_df_lastdate.groupby( by = ["User"], as_index = False)[slecet_element].sum()

#         ar_date_elem_data =  ar_selected_df.groupby( by = ["Date"], as_index = False)[slecet_element].sum()
#         ar_user_elemhour_data =  ar_selected_df.groupby( by = ["User"], as_index = False)[ele_hours].sum()

#         ### max element creator 
#         ar_max_elem_index  =  ar_user_elem_data[slecet_element].idxmax()
#         ar_max_elem_owner =  ar_user_elem_data.loc[ ar_max_elem_index, "User"]
#         ar_max_elem_bycreator = ar_selected_df_lastdate.loc[ar_max_elem_index, slecet_element]
        

#         ### min element creator 
#         ar_min_elem_index  =  ar_user_elem_data[slecet_element].idxmin()
#         ar_min_elem_owner =  ar_user_elem_data.loc[ ar_min_elem_index, "User"]
#         ar_min_elem_bycreator = ar_selected_df_lastdate.loc[ar_min_elem_index, slecet_element]

#         ## per houre performance to model elements 
#         ar_elem_hr_result =  ar_user_elem_data.copy()
#         ar_elem_hr_result["Per_Houre_Performance"]= ar_user_elem_data[slecet_element]/ ar_user_elemhour_data[ele_hours]
        
        
#         ### max performing user 
#         ar_max_elemperhr_user_index = ar_elem_hr_result["Per_Houre_Performance"].idxmax()
#         ar_max_elemperhr_user = ar_elem_hr_result.loc[ar_max_elemperhr_user_index,"User"]
#         ar_max_elemperhr = round(ar_elem_hr_result.loc[ar_max_elemperhr_user_index, "Per_Houre_Performance"])

#         ### min performing user 
#         ar_min_elemperhr_user_index = ar_elem_hr_result["Per_Houre_Performance"].idxmin()
#         ar_min_elemperhr_user = ar_elem_hr_result.loc[ar_min_elemperhr_user_index,"User"]
#         ar_min_elemperhr = round(ar_elem_hr_result.loc[ar_min_elemperhr_user_index, "Per_Houre_Performance"] )

#         elem_col1, elem_col2 = st.columns(2)

#         with elem_col2:
#             st.subheader(" :bar_chart: Element Developed With Time")
#             ar_fig_elem_pie = px.pie(ar_user_elem_data_lastdate, values = slecet_element, names= "User"  , hole=0.5)
#             ar_fig_elem_pie.update_traces(textposition='outside', textinfo='percent+label')
#             st.plotly_chart(ar_fig_elem_pie, use_container_width=True)

#         with elem_col1:
#             st.subheader(":label: Element Created By Users")
#             ar_fig_elem_bar  = px.bar(ar_date_elem_data , x = "Date", y = slecet_element,text = ['{:}'.format(x) for x in ar_date_elem_data[slecet_element]],
#                         template = "seaborn")
#             st.plotly_chart( ar_fig_elem_bar, use_container_width= True)

        
#             elem_col1_01, elem_col1_02 = st.columns(2)

#             with elem_col1_01:
#                 st.markdown("")
#                 st.markdown("")
#                 st.markdown("")
#                 st.markdown(f"<span style='color:Azure; font-size: x-large; font-weight: Normal'>Maximum No. Of Elements Created By:</span>", unsafe_allow_html=True)
#             with elem_col1_02:
#                 st.markdown("")
#                 st.markdown("")
#                 st.markdown("")
#                 st.markdown(f"<span style='color:Azure; font-size: x-large; font-weight: Normal'>Minimum No. Of Elements Created By:</span>", unsafe_allow_html=True)

#             elem_col1_sub_01,elem_col1_sub_02,elem_col1_sub_03,elem_col1_sub_04 = st.columns(4)

#             with elem_col1_sub_01:
#                 st.markdown("")
#                 st.markdown(f"<span style='color:BurlyWood; font-size: xx-large; font-weight: bold'>{ar_max_elem_owner}</span>", unsafe_allow_html=True)

#             with elem_col1_sub_02:
#                 st.markdown("")   
#                 st.markdown(f"<span style='color:BurlyWood; font-size: xx-large; font-weight: bold'>{ar_max_elem_bycreator}</span>", unsafe_allow_html=True)

#             with elem_col1_sub_03:
#                 st.markdown("")
#                 st.markdown(f"<span style='color:OrangeRed; font-size: xx-large; font-weight: bold'>{ar_min_elem_owner}</span>", unsafe_allow_html=True)

#             with elem_col1_sub_04:
#                 st.markdown("")   
#                 st.markdown(f"<span style='color:red; font-size: xx-large; font-weight: bold'> {ar_min_elem_bycreator} </span>", unsafe_allow_html=True)
    
#             elem_col1_03, elem_col1_04 = st.columns(2)

#             with elem_col1_03:
#                 st.markdown("")
#                 st.markdown("")
#                 st.markdown("")
#                 st.markdown(f"<span style='color:Azure; font-size: x-large; font-weight: Normal'>Efficiency_Maximum</span>", unsafe_allow_html=True)
#             with elem_col1_04:
#                 st.markdown("")
#                 st.markdown("")
#                 st.markdown("")
#                 st.markdown(f"<span style='color:Azure; font-size: x-large; font-weight: Normal'>Efficiency_Minimum</span>", unsafe_allow_html=True)

#             elem_col1_sub_05,elem_col1_sub_06,elem_col1_sub_07,elem_col1_sub_08 = st.columns(4)

#             with elem_col1_sub_05:
#                 st.markdown("")   
#                 st.markdown(f"<span style='color:BurlyWood; font-size: xx-large; font-weight: bold'> {ar_max_elemperhr_user} </span>", unsafe_allow_html=True)
#             with elem_col1_sub_06:
#                 st.markdown("")   
#                 st.markdown(f"<span style='color:BurlyWood; font-size: xx-large; font-weight: bold'> {ar_max_elemperhr}/hour</span>", unsafe_allow_html=True)
    
#             with elem_col1_sub_07:
#                 st.markdown("")   
#                 st.markdown(f"<span style='color:BurlyWood; font-size: xx-large; font-weight: bold'>{ar_min_elemperhr_user}</span>", unsafe_allow_html=True)
#             with elem_col1_sub_08:
#                 st.markdown("")   
#                 st.markdown(f"<span style='color:BurlyWood; font-size: xx-large; font-weight: bold'>{ar_min_elemperhr}/hour</span>", unsafe_allow_html=True)
        
#         with elem_col2:
#             ar_fig_elem_perf = px.line( x= pd.DataFrame(ar_elem_hr_result)["User"], y = pd.DataFrame(ar_elem_hr_result)["Per_Houre_Performance"],markers= True)
#             ar_fig_elem_perf.update_layout(xaxis_title="User", yaxis_title="Efficiency")
#             st.plotly_chart( ar_fig_elem_perf, use_container_width= True)
        
#         ## Efficiency vs Creation 
#         ar_elem_df =  pd.DataFrame(ar_elem_hr_result).copy()
#         ar_elem_df["hours"] = ar_user_elemhour_data[ele_hours]
#         ar_fig_elem_scatter =  px.scatter(ar_elem_df, x = slecet_element, y = "Per_Houre_Performance",size = slecet_element, color= "User", hover_name= slecet_element, log_x= True, size_max=60)
#         st.plotly_chart(ar_fig_elem_scatter, theme = "streamlit",use_container_width=True)


# with tab_arch:
#     ar_element_data("Room", "Room_Hours")

