from dash import Dash,dcc,html,callback,Output,Input
from dash import Dash
import pandas as pd
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

#regular season import
lebron_regular_season = pd.read_csv("lebron_career.csv",parse_dates=["date"])
lebron_totals_regular = lebron_regular_season[["pts","ast","trb","blk","stl","tov"]].sum().to_frame()
lebron_totals_regular.rename(columns={lebron_totals_regular.columns[0]:"Total"},inplace=True)
lebron_averages_regular = lebron_regular_season[["pts","ast","trb","blk","stl","tov"]].mean().to_frame()
lebron_averages_regular.rename(columns={lebron_averages_regular.columns[0]:"Total"},inplace=True)
jordan_regular_season = pd.read_csv("jordan_career.csv",parse_dates=["date"])
jordan_totals_regular = jordan_regular_season[["pts","ast","trb","blk","stl","tov"]].sum().to_frame()
jordan_totals_regular.rename(columns={jordan_totals_regular.columns[0]:"Total"},inplace=True)
jordan_averages_regular = jordan_regular_season[["pts","ast","trb","blk","stl","tov"]].mean().to_frame()
jordan_averages_regular.rename(columns={jordan_averages_regular.columns[0]:"Total"},inplace=True)
#playoffs import
lebron_playoffs = pd.read_csv("lebron_playoffs.csv",parse_dates=["date"])
lebron_totals_playoffs = lebron_playoffs[["pts","ast","trb","blk","stl","tov"]].sum().to_frame()
lebron_totals_playoffs.rename(columns={lebron_totals_playoffs.columns[0]:"Total"},inplace=True)
lebron_averages_playoffs = lebron_playoffs[["pts","ast","trb","blk","stl","tov"]].mean().to_frame()
lebron_averages_playoffs.rename(columns={lebron_averages_playoffs.columns[0]:"Total"},inplace=True)
jordan_playoffs = pd.read_csv("jordan_playoffs.csv",parse_dates=["date"])
jordan_totals_playoffs = jordan_playoffs[["pts","ast","trb","blk","stl","tov"]].sum().to_frame()
jordan_totals_playoffs.rename(columns={jordan_totals_playoffs.columns[0]:"Total"},inplace=True)
jordan_averages_playoffs = jordan_playoffs[["pts","ast","trb","blk","stl","tov"]].mean().to_frame()
jordan_averages_playoffs.rename(columns={jordan_averages_playoffs.columns[0]:"Total"},inplace=True)
#importing finals data
lebron_finals = lebron_playoffs.query("series == 'FIN'")
lebron_total_finals = lebron_finals[["pts","ast","trb","blk","stl","tov"]].sum().to_frame()
lebron_total_finals.rename(columns={lebron_total_finals.columns[0]:"Total"},inplace=True)
lebron_averages_finals = lebron_finals[["pts","ast","trb","blk","stl","tov"]].mean().to_frame()
lebron_averages_finals.rename(columns={lebron_averages_finals.columns[0]:"Total"},inplace=True)
jordan_finals = jordan_playoffs.query("series == 'FIN'")
jordan_total_finals = jordan_finals[["pts","ast","trb","blk","stl","tov"]].sum().to_frame()
jordan_total_finals.rename(columns={jordan_total_finals.columns[0]:"Total"},inplace=True)
jordan_averages_finals = jordan_finals[["pts","ast","trb","blk","stl","tov"]].mean().to_frame()
jordan_averages_finals.rename(columns={jordan_averages_finals.columns[0]:"Total"},inplace=True)

# making efficiency statisitics columns to be used for efficiency charts
lebron_regular_season["Field Goals Made"] = lebron_regular_season["fg"]
lebron_regular_season["Field Goals Missed"] = lebron_regular_season["fga"] - lebron_regular_season["fg"]
jordan_regular_season["Field Goals Made"] = jordan_regular_season["fg"]
jordan_regular_season["Field Goals Missed"] = jordan_regular_season["fga"] - jordan_regular_season["fg"]
    
lebron_regular_season["Free Throws Made"] = lebron_regular_season["ft"]
lebron_regular_season["Free Throws Missed"] = lebron_regular_season["fta"] - lebron_regular_season["ft"]
jordan_regular_season["Free Throws Made"] = jordan_regular_season["ft"]
jordan_regular_season["Free Throws Missed"] = jordan_regular_season["fta"] - jordan_regular_season["ft"]
    
lebron_regular_season["Three Made"] = lebron_regular_season["three"]
lebron_regular_season["Three Missed"] = lebron_regular_season["threeatt"] - lebron_regular_season["three"]
jordan_regular_season["Three Made"] = jordan_regular_season["three"]
jordan_regular_season["Three Missed"] = jordan_regular_season["threeatt"] - jordan_regular_season["three"]
    
lebron_playoffs["Field Goals Made"] = lebron_playoffs["fg"]
lebron_playoffs["Field Goals Missed"] = lebron_playoffs["fga"] - lebron_playoffs["fg"]
jordan_playoffs["Field Goals Made"] = jordan_playoffs["fg"]
jordan_playoffs["Field Goals Missed"] = jordan_playoffs["fga"] - jordan_playoffs["fg"]
    
lebron_playoffs["Free Throws Made"] = lebron_playoffs["ft"]
lebron_playoffs["Free Throws Missed"] = lebron_playoffs["fta"] - lebron_playoffs["ft"]
jordan_playoffs["Free Throws Made"] = jordan_playoffs["ft"]
jordan_playoffs["Free Throws Missed"] = jordan_playoffs["fta"] - jordan_playoffs["ft"]
    
lebron_playoffs["Three Made"] = lebron_playoffs["three"]
lebron_playoffs["Three Missed"] = lebron_playoffs["threeatt"] - lebron_playoffs["three"]
jordan_playoffs["Three Made"] = jordan_playoffs["three"]
jordan_playoffs["Three Missed"] = jordan_playoffs["threeatt"] - jordan_playoffs["three"]
    
lebron_finals["Field Goals Made"] = lebron_finals["fg"]
lebron_finals["Field Goals Missed"] = lebron_finals["fga"] - lebron_finals["fg"]
jordan_finals["Field Goals Made"] = jordan_finals["fg"]
jordan_finals["Field Goals Missed"] = jordan_finals["fga"] - jordan_finals["fg"]
    
lebron_finals["Free Throws Made"] = lebron_finals["ft"]
lebron_finals["Free Throws Missed"] = lebron_finals["fta"] - lebron_finals["ft"]
jordan_finals["Free Throws Made"] = jordan_finals["ft"]
jordan_finals["Free Throws Missed"] = jordan_finals["fta"] - jordan_finals["ft"]
    
lebron_finals["Three Made"] = lebron_finals["three"]
lebron_finals["Three Missed"] = lebron_finals["threeatt"] - lebron_finals["three"]
jordan_finals["Three Made"] = jordan_finals["three"]
jordan_finals["Three Missed"] = jordan_finals["threeatt"] - jordan_finals["three"]

#creating dataframes for cumulative shooting
lebron_shooting_totals_regular = lebron_regular_season[["fg","fga","three",
                                                                "threeatt","ft","fta"]].sum().to_frame()
lebron_shooting_totals_regular.rename(columns={lebron_shooting_totals_regular.columns[0]:"Total"},
                                              inplace=True)
jordan_shooting_totals_regular = jordan_regular_season[["fg","fga","three",
                                                                "threeatt","ft","fta"]].sum().to_frame()
jordan_shooting_totals_regular.rename(columns={jordan_shooting_totals_regular.columns[0]:"Total"},
                                              inplace=True)
    
lebron_shooting_totals_playoffs = lebron_playoffs[["fg","fga","three",
                                                                "threeatt","ft","fta"]].sum().to_frame()
lebron_shooting_totals_playoffs.rename(columns={lebron_shooting_totals_playoffs.columns[0]:"Total"},
                                              inplace=True)
jordan_shooting_totals_playoffs = jordan_playoffs[["fg","fga","three",
                                                                "threeatt","ft","fta"]].sum().to_frame()
jordan_shooting_totals_playoffs.rename(columns={jordan_shooting_totals_playoffs.columns[0]:"Total"},
                                              inplace=True)
    
lebron_shooting_totals_finals = lebron_finals[["fg","fga","three",
                                                                "threeatt","ft","fta"]].sum().to_frame()
lebron_shooting_totals_finals.rename(columns={lebron_shooting_totals_finals.columns[0]:"Total"},
                                              inplace=True)
jordan_shooting_totals_finals = jordan_finals[["fg","fga","three",
                                                                "threeatt","ft","fta"]].sum().to_frame()
jordan_shooting_totals_finals.rename(columns={jordan_shooting_totals_finals.columns[0]:"Total"},
                                              inplace=True)

app = Dash(__name__)

app.layout = html.Div(
children=[
    html.Div(html.H1("Lebron vs Jordan",style={'text-align':'center','color':'white','font-size':'2.5rem',
                                     'font-weight':'bolder','display':'block',
                                      'background-color':'rgb(0,0,0,0.40)','padding':'10px'
                                      ,'border-radius':'5px','margin-bottom':'10px'}),
             id="main-heading"),
    #Total Statistics
        html.Div(children=[html.H2("Total Career Statistics",style={'text-align':'left',
                        'color':'white','font-size':'2rem','font-weight':'bolder','display':'block',
                        'background-color':'rgb(0,0,0,0.40)','padding':'10px','border-radius':'5px',
                         'margin-top':'0px','margin-bottom':'10px'}),
                         dcc.Dropdown(options=["Regular Season","Playoffs","NBA Finals"],value="Regular Season"
                            ,id="total-dropdown",
                            searchable=False)
             ],id="sub-heading"),
    html.Div(children=[
    dcc.Graph(id="lebron-stats-total",style={'width':'90%','margin-right':'20px','margin-left':'20px'}),
      dcc.Graph(id="jordan-stats-total",style={'width':'90%','margin-right':'20px'})],id="stats-div"),
# Average statistics
    html.Div(children=[html.H2("Average Career Statistics",style={'text-align':'left',
                        'color':'white','font-size':'2rem','font-weight':'bolder','display':'block',
                        'background-color':'rgb(0,0,0,0.40)','padding':'10px','border-radius':'5px',
                         'margin-top':'0px','margin-bottom':'10px'}),
                         dcc.Dropdown(options=["Regular Season","Playoffs","NBA Finals"],value="Regular Season"
                            ,id="averages-dropdown",searchable=False)],id="sub-heading-avg"),
    html.Div(children=[
    dcc.Graph(id="lebron-stats-averages",style={'width':'90%','margin-right':'20px','margin-left':'20px'}),
      dcc.Graph(id="jordan-stats-averages",style={'width':'90%','margin-right':'20px'})],id="stats-div-avg"),
# Shooting Efficiency
    html.Div(children=[html.H2("Career Efficiency Statistics",style={'text-align':'left',
                        'color':'white','font-size':'2rem','font-weight':'bolder','display':'block',
                        'background-color':'rgb(0,0,0,0.40)','padding':'10px','border-radius':'5px',
                         'margin-top':'0px','margin-bottom':'10px'}),
                         dcc.Dropdown(options=["Regular Season","Playoffs","NBA Finals"],value="Regular Season"
                            ,id="season-dropdown",searchable=False),
                         dcc.Dropdown(options=["Field Goals","Three Pointers","Free Throws"],value="Field Goals"
                            ,id="efficiency-dropdown",searchable=False)]
             ,id="sub-heading-eff"),
    html.Div(children=[
    dcc.Graph(id="lebron-stats-efficiency",style={'width':'90%','margin-right':'20px','margin-left':'20px'}),
      dcc.Graph(id="jordan-stats-efficiency",style={'width':'90%','margin-right':'20px'})],id="stats-div-eff"),
# Cumulative Shooting Statistics
    html.Div(children=[html.H2("Cumulative Shooting Statistics",style={'text-align':'left',
                        'color':'white','font-size':'2rem','font-weight':'bolder','display':'block',
                        'background-color':'rgb(0,0,0,0.40)','padding':'10px','border-radius':'5px',
                         'margin-top':'0px','margin-bottom':'10px'}),
                         dcc.Dropdown(options=["Regular Season","Playoffs","NBA Finals"],value="Regular Season"
                            ,id="cumulative-dropdown",searchable=False)]
             ,id="sub-heading-cumulative"),
    html.Div(children=[
    dcc.Graph(id="lebron-stats-cumulative",style={'width':'90%','margin-right':'20px','margin-left':'20px'}),
      dcc.Graph(id="jordan-stats-cumulative",style={'width':'90%','margin-right':'20px'})],
             id="stats-div-cumulative")
])

@callback(
    Output("lebron-stats-cumulative","figure"),
    Output("jordan-stats-cumulative","figure"),
    Input("cumulative-dropdown","value"),
    allow_duplicate=True
)

def Update_Cumulative(cumulative):
    
    if cumulative == "Regular Season":
        total_range = 0 
        lebron_range = lebron_shooting_totals_regular.max()[0]
        jordan_range = jordan_shooting_totals_regular.max()[0]
        if jordan_range > lebron_range:
            total_range = jordan_range
        else:
            total_range = lebron_range
            
            
        lebron_figure=px.bar(lebron_shooting_totals_regular,x=lebron_shooting_totals_regular.index,y="Total",
          title="Lebron's Cumulative Shooting Statistics",
          color_discrete_sequence =[["#552583","#fdb927","#552583","#fdb927","#552583","#fdb927"]]
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['fg','fga','three','threeatt','ft','fta'],
        ticktext=['Field Goals','Field Goals Attempted',"Three's","Three's Attempted",
                  "Free Throws",'Free Throws Attempted'])
        
        jordan_figure=px.bar(jordan_shooting_totals_regular,x=jordan_shooting_totals_regular.index,y="Total",
          title="Jordan's Cumulative Shooting Statistics",
          color_discrete_sequence =[["#CE1141","white","#CE1141","white","#CE1141","white"]]
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['fg','fga','three','threeatt','ft','fta'],
        ticktext=['Field Goals','Field Goals Attempted',"Three's","Three's Attempted",
                  "Free Throws",'Free Throws Attempted'])
        
        return lebron_figure,jordan_figure
    
    elif cumulative == "Playoffs":
        total_range = 0 
        lebron_range = lebron_shooting_totals_playoffs.max()[0]
        jordan_range = jordan_shooting_totals_playoffs.max()[0]
        if jordan_range > lebron_range:
            total_range = jordan_range
        else:
            total_range = lebron_range
            
            
        lebron_figure=px.bar(lebron_shooting_totals_playoffs,x=lebron_shooting_totals_playoffs.index,y="Total",
          title="Lebron's Cumulative Playoff Shooting Statistics",
          color_discrete_sequence =[["#552583","#fdb927","#552583","#fdb927","#552583","#fdb927"]]
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['fg','fga','three','threeatt','ft','fta'],
        ticktext=['Field Goals','Field Goals Attempted',"Three's","Three's Attempted",
                  "Free Throws",'Free Throws Attempted'])
        
        jordan_figure=px.bar(jordan_shooting_totals_playoffs,x=jordan_shooting_totals_playoffs.index,y="Total",
          title="Jordan's Cumulative Shooting Playoff Statistics",
          color_discrete_sequence =[["#CE1141","white","#CE1141","white","#CE1141","white"]]
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['fg','fga','three','threeatt','ft','fta'],
        ticktext=['Field Goals','Field Goals Attempted',"Three's","Three's Attempted",
                  "Free Throws",'Free Throws Attempted'])
        
        return lebron_figure,jordan_figure
    
    elif cumulative == "NBA Finals":
        total_range = 0 
        lebron_range = lebron_shooting_totals_finals.max()[0]
        jordan_range = jordan_shooting_totals_finals.max()[0]
        if jordan_range > lebron_range:
            total_range = jordan_range
        else:
            total_range = lebron_range
            
            
        lebron_figure=px.bar(lebron_shooting_totals_finals,x=lebron_shooting_totals_finals.index,y="Total",
          title="Lebron's Cumulative Finals Shooting Statistics",
          color_discrete_sequence =[["#552583","#fdb927","#552583","#fdb927","#552583","#fdb927"]]
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['fg','fga','three','threeatt','ft','fta'],
        ticktext=['Field Goals','Field Goals Attempted',"Three's","Three's Attempted",
                  "Free Throws",'Free Throws Attempted'])
        
        jordan_figure=px.bar(jordan_shooting_totals_finals,x=jordan_shooting_totals_finals.index,y="Total",
          title="Jordan's Cumulative Shooting Finals Statistics",
          color_discrete_sequence =[["#CE1141","white","#CE1141","white","#CE1141","white"]]
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['fg','fga','three','threeatt','ft','fta'],
        ticktext=['Field Goals','Field Goals Attempted',"Three's","Three's Attempted",
                  "Free Throws",'Free Throws Attempted'])
        
        return lebron_figure,jordan_figure

@callback(
    Output("lebron-stats-efficiency","figure"),
    Output("jordan-stats-efficiency","figure"),
    Input("season-dropdown","value"),
    Input("efficiency-dropdown","value"),
    allow_duplicate=True
)

def Update_Efficiency(season,efficiency):
    if season == "Regular Season":
        if efficiency == "Field Goals":
            lbj_efficiency = lebron_regular_season[["Field Goals Made","Field Goals Missed"]].mean().to_frame()
            lbj_efficiency.rename(columns={lbj_efficiency.columns[0]:"Total"},inplace=True)
            lbj_figure=px.pie(lbj_efficiency,values="Total",names=lbj_efficiency.index,
                              title="Lebron's Field Goal Efficiency",hole=.4,
                              color_discrete_sequence=["#552583","#fdb927"]).update_layout(
                    paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",
                font={'color':'white'}).update_traces(sort=False)

            jordan_efficiency = jordan_regular_season[["Field Goals Made","Field Goals Missed"]].mean().to_frame()
            jordan_efficiency.rename(columns={jordan_efficiency.columns[0]:"Total"},inplace=True)
            jordan_figure=px.pie(jordan_efficiency,values="Total",names=jordan_efficiency.index,
                              title="Jordan's Field Goal Efficiency",hole=.4,
                              color_discrete_sequence=["#CE1141","white"]).update_layout(
                    paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",
                font={'color':'white'}).update_traces(sort=False)

            return lbj_figure,jordan_figure
        
        elif efficiency == "Three Pointers":
            lbj_efficiency = lebron_regular_season[["Three Made","Three Missed"]].mean().to_frame()
            lbj_efficiency.rename(columns={lbj_efficiency.columns[0]:"Total"},inplace=True)
            lbj_figure=px.pie(lbj_efficiency,values="Total",names=lbj_efficiency.index,
                              title="Lebron's Three Point Efficiency",hole=.4,
                              color_discrete_sequence=["#552583","#fdb927"]).update_layout(
                    paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",
                font={'color':'white'}).update_traces(sort=False)

            jordan_efficiency = jordan_regular_season[["Three Made","Three Missed"]].mean().to_frame()
            jordan_efficiency.rename(columns={jordan_efficiency.columns[0]:"Total"},inplace=True)
            jordan_figure=px.pie(jordan_efficiency,values="Total",names=jordan_efficiency.index,
                              title="Jordan's Three Point Efficiency",hole=.4,
                              color_discrete_sequence=["#CE1141","white"]).update_layout(
                    paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",
                font={'color':'white'}).update_traces(sort=False)
            
            return lbj_figure,jordan_figure
        elif efficiency == "Free Throws":
            lbj_efficiency = lebron_regular_season[["Free Throws Made","Free Throws Missed"]].mean().to_frame()
            lbj_efficiency.rename(columns={lbj_efficiency.columns[0]:"Total"},inplace=True)
            lbj_figure=px.pie(lbj_efficiency,values="Total",names=lbj_efficiency.index,
                              title="Lebron's Free Throw Efficiency",hole=.4,
                              color_discrete_sequence=["#552583","#fdb927"]).update_layout(
                    paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",
                font={'color':'white'}).update_traces(sort=False)

            jordan_efficiency = jordan_regular_season[["Free Throws Made","Free Throws Missed"]].mean().to_frame()
            jordan_efficiency.rename(columns={jordan_efficiency.columns[0]:"Total"},inplace=True)
            jordan_figure=px.pie(jordan_efficiency,values="Total",names=jordan_efficiency.index,
                              title="Jordan's Free Throw Efficiency",hole=.4,
                              color_discrete_sequence=["#CE1141","white"]).update_layout(
                    paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",
                font={'color':'white'}).update_traces(sort=False)
            
            return lbj_figure,jordan_figure 
        
    elif season == "Playoffs":
        if efficiency == "Field Goals":
            lbj_efficiency = lebron_playoffs[["Field Goals Made","Field Goals Missed"]].mean().to_frame()
            lbj_efficiency.rename(columns={lbj_efficiency.columns[0]:"Total"},inplace=True)
            lbj_figure=px.pie(lbj_efficiency,values="Total",names=lbj_efficiency.index,
                              title="Lebron's Field Goal Efficiency",hole=.4,
                              color_discrete_sequence=["#552583","#fdb927"]).update_layout(
                    paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",
                font={'color':'white'}).update_traces(sort=False)

            jordan_efficiency = jordan_playoffs[["Field Goals Made","Field Goals Missed"]].mean().to_frame()
            jordan_efficiency.rename(columns={jordan_efficiency.columns[0]:"Total"},inplace=True)
            jordan_figure=px.pie(jordan_efficiency,values="Total",names=jordan_efficiency.index,
                              title="Jordan's Field Goal Efficiency",hole=.4,
                              color_discrete_sequence=["#CE1141","white"]).update_layout(
                    paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",
                font={'color':'white'}).update_traces(sort=False)

            return lbj_figure,jordan_figure
        
        elif efficiency == "Three Pointers":
            lbj_efficiency = lebron_playoffs[["Three Made","Three Missed"]].mean().to_frame()
            lbj_efficiency.rename(columns={lbj_efficiency.columns[0]:"Total"},inplace=True)
            lbj_figure=px.pie(lbj_efficiency,values="Total",names=lbj_efficiency.index,
                              title="Lebron's Three Point Efficiency",hole=.4,
                              color_discrete_sequence=["#552583","#fdb927"]).update_layout(
                    paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",
                font={'color':'white'}).update_traces(sort=False)

            jordan_efficiency = jordan_playoffs[["Three Made","Three Missed"]].mean().to_frame()
            jordan_efficiency.rename(columns={jordan_efficiency.columns[0]:"Total"},inplace=True)
            jordan_figure=px.pie(jordan_efficiency,values="Total",names=jordan_efficiency.index,
                              title="Jordan's Three Point Efficiency",hole=.4,
                              color_discrete_sequence=["#CE1141","white"]).update_layout(
                    paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",
                font={'color':'white'}).update_traces(sort=False)
            
            return lbj_figure,jordan_figure
        elif efficiency == "Free Throws":
            lbj_efficiency = lebron_playoffs[["Free Throws Made","Free Throws Missed"]].mean().to_frame()
            lbj_efficiency.rename(columns={lbj_efficiency.columns[0]:"Total"},inplace=True)
            lbj_figure=px.pie(lbj_efficiency,values="Total",names=lbj_efficiency.index,
                              title="Lebron's Free Throws Efficiency",hole=.4,
                              color_discrete_sequence=["#552583","#fdb927"]).update_layout(
                    paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",
                font={'color':'white'}).update_traces(sort=False)

            jordan_efficiency = jordan_playoffs[["Free Throws Made","Free Throws Missed"]].mean().to_frame()
            jordan_efficiency.rename(columns={jordan_efficiency.columns[0]:"Total"},inplace=True)
            jordan_figure=px.pie(jordan_efficiency,values="Total",names=jordan_efficiency.index,
                              title="Jordan's Free Throw Efficiency",hole=.4,
                              color_discrete_sequence=["#CE1141","white"]).update_layout(
                    paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",
                font={'color':'white'}).update_traces(sort=False)
            
            return lbj_figure,jordan_figure 
        
    elif season == "NBA Finals":
        if efficiency == "Field Goals":
            lbj_efficiency = lebron_finals[["Field Goals Made","Field Goals Missed"]].mean().to_frame()
            lbj_efficiency.rename(columns={lbj_efficiency.columns[0]:"Total"},inplace=True)
            lbj_figure=px.pie(lbj_efficiency,values="Total",names=lbj_efficiency.index,
                              title="Lebron's Field Goal Efficiency",hole=.4,
                              color_discrete_sequence=["#552583","#fdb927"]).update_layout(
                    paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",
                font={'color':'white'}).update_traces(sort=False)

            jordan_efficiency = jordan_finals[["Field Goals Made","Field Goals Missed"]].mean().to_frame()
            jordan_efficiency.rename(columns={jordan_efficiency.columns[0]:"Total"},inplace=True)
            jordan_figure=px.pie(jordan_efficiency,values="Total",names=jordan_efficiency.index,
                              title="Jordan's Field Goal Efficiency",hole=.4,
                              color_discrete_sequence=["#CE1141","white"]).update_layout(
                    paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",
                font={'color':'white'}).update_traces(sort=False)

            return lbj_figure,jordan_figure
        
        elif efficiency == "Three Pointers":
            lbj_efficiency = lebron_finals[["Three Made","Three Missed"]].mean().to_frame()
            lbj_efficiency.rename(columns={lbj_efficiency.columns[0]:"Total"},inplace=True)
            lbj_figure=px.pie(lbj_efficiency,values="Total",names=lbj_efficiency.index,
                              title="Lebron's Three Point Efficiency",hole=.4,
                              color_discrete_sequence=["#552583","#fdb927"]).update_layout(
                    paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",
                font={'color':'white'}).update_traces(sort=False)

            jordan_efficiency = jordan_finals[["Three Made","Three Missed"]].mean().to_frame()
            jordan_efficiency.rename(columns={jordan_efficiency.columns[0]:"Total"},inplace=True)
            jordan_figure=px.pie(jordan_efficiency,values="Total",names=jordan_efficiency.index,
                              title="Jordan's Three Point Efficiency",hole=.4,
                              color_discrete_sequence=["#CE1141","white"]).update_layout(
                    paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",
                font={'color':'white'}).update_traces(sort=False)
            
            return lbj_figure,jordan_figure
        elif efficiency == "Free Throws":
            lbj_efficiency = lebron_finals[["Free Throws Made","Free Throws Missed"]].mean().to_frame()
            lbj_efficiency.rename(columns={lbj_efficiency.columns[0]:"Total"},inplace=True)
            lbj_figure=px.pie(lbj_efficiency,values="Total",names=lbj_efficiency.index,
                              title="Lebron's Free Throw Efficiency",hole=.4,
                              color_discrete_sequence=["#552583","#fdb927"]).update_layout(
                    paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",
                font={'color':'white'}).update_traces(sort=False)

            jordan_efficiency = jordan_finals[["Free Throws Made","Free Throws Missed"]].mean().to_frame()
            jordan_efficiency.rename(columns={jordan_efficiency.columns[0]:"Total"},inplace=True)
            jordan_figure=px.pie(jordan_efficiency,values="Total",names=jordan_efficiency.index,
                              title="Jordan's Free Throw Efficiency",hole=.4,
                              color_discrete_sequence=["#CE1141","white"]).update_layout(
                    paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",
                font={'color':'white'}).update_traces(sort=False)
            
            return lbj_figure,jordan_figure 
    
@callback(
    Output("lebron-stats-total","figure"),
    Output("jordan-stats-total","figure"),
    Input("total-dropdown","value"),
    allow_duplicate=True
)
def Update_Totals(value):
    if value == "Regular Season":
        
        total_range = 0 
        lebron_range = lebron_totals_regular.max()[0]
        jordan_range = jordan_totals_regular.max()[0]
        if jordan_range > lebron_range:
            total_range = jordan_range
        else:
            total_range = lebron_range
        
        lebron_figure=px.bar(lebron_totals_regular,x=lebron_totals_regular.index,y="Total",
          title="Lebron's Total Regular Season Statistics",
          color_discrete_sequence =['#552583']*len(lebron_totals_regular)
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['pts','ast','trb','blk','stl','tov'],
        ticktext=['Points','Assists','Rebounds','Blocks','Steals','Turnovers'])
        
        jordan_figure=px.bar(jordan_totals_regular,x=jordan_totals_regular.index,y="Total",
          title="Jordan's Total Regular Season Statistics",
          color_discrete_sequence =['#CE1141']*len(jordan_totals_regular)
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['pts','ast','trb','blk','stl','tov'],
        ticktext=['Points','Assists','Rebounds','Blocks','Steals','Turnovers'])
        return lebron_figure,jordan_figure
    elif value == "Playoffs":
        
        total_range = 0 
        lebron_range = lebron_totals_playoffs.max()[0]
        jordan_range = jordan_totals_playoffs.max()[0]
        if jordan_range > lebron_range:
            total_range = jordan_range
        else:
            total_range = lebron_range
            
        lebron_figure=px.bar(lebron_totals_playoffs,x=lebron_totals_playoffs.index,y="Total",
          title="Lebron's Total Playoff Statistics",
          color_discrete_sequence =['#552583']*len(lebron_totals_playoffs)
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['pts','ast','trb','blk','stl','tov'],
        ticktext=['Points','Assists','Rebounds','Blocks','Steals','Turnovers'])
        
        jordan_figure=px.bar(jordan_totals_playoffs,x=jordan_totals_playoffs.index,y="Total",
          title="Jordan's Total Playoff Statistics",
          color_discrete_sequence =['#CE1141']*len(jordan_totals_playoffs)
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['pts','ast','trb','blk','stl','tov'],
        ticktext=['Points','Assists','Rebounds','Blocks','Steals','Turnovers'])
        
        return lebron_figure,jordan_figure
    elif value == "NBA Finals":
        
        total_range = 0 
        lebron_range = lebron_total_finals.max()[0]
        jordan_range = jordan_total_finals.max()[0]
        if jordan_range > lebron_range:
            total_range = jordan_range
        else:
            total_range = lebron_range
            
        lebron_figure=px.bar(lebron_total_finals,x=lebron_total_finals.index,y="Total",
          title="Lebron's Total Finals Statistics",
          color_discrete_sequence =['#552583']*len(lebron_total_finals)
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['pts','ast','trb','blk','stl','tov'],
        ticktext=['Points','Assists','Rebounds','Blocks','Steals','Turnovers'])
        
        jordan_figure=px.bar(jordan_total_finals,x=jordan_total_finals.index,y="Total",
          title="Jordan's Total Finals Statistics",
          color_discrete_sequence =['#CE1141']*len(jordan_total_finals)
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['pts','ast','trb','blk','stl','tov'],
        ticktext=['Points','Assists','Rebounds','Blocks','Steals','Turnovers'])
        
        return lebron_figure,jordan_figure
        
@callback (
    Output("lebron-stats-averages","figure"),
    Output("jordan-stats-averages","figure"),
    Input("averages-dropdown","value"),
    allow_duplicate=True
)

def Update_Averages(value):
    if value == "Regular Season":
        
        total_range = 0 
        lebron_range = lebron_averages_regular.max()[0]
        jordan_range = jordan_averages_regular.max()[0]
        if jordan_range > lebron_range:
            total_range = jordan_range
        else:
            total_range = lebron_range
        
        lebron_figure=px.bar(lebron_averages_regular,x=lebron_averages_regular.index,y="Total",
          title="Lebron's Average Regular Season Statistics",
          color_discrete_sequence =['#552583']*len(lebron_averages_regular)
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['pts','ast','trb','blk','stl','tov'],
        ticktext=['Points','Assists','Rebounds','Blocks','Steals','Turnovers'])
        
        jordan_figure=px.bar(jordan_averages_regular,x=jordan_averages_regular.index,y="Total",
          title="Jordan's Average Regular Season Statistics",
          color_discrete_sequence =['#CE1141']*len(jordan_averages_regular)
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['pts','ast','trb','blk','stl','tov'],
        ticktext=['Points','Assists','Rebounds','Blocks','Steals','Turnovers'])
        return lebron_figure,jordan_figure
    elif value == "Playoffs":
        
        total_range = 0 
        lebron_range = lebron_averages_playoffs.max()[0]
        jordan_range = jordan_averages_playoffs.max()[0]
        if jordan_range > lebron_range:
            total_range = jordan_range
        else:
            total_range = lebron_range
            
        lebron_figure=px.bar(lebron_averages_playoffs,x=lebron_averages_playoffs.index,y="Total",
          title="Lebron's Average Playoff Statistics",
          color_discrete_sequence =['#552583']*len(lebron_averages_playoffs)
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['pts','ast','trb','blk','stl','tov'],
        ticktext=['Points','Assists','Rebounds','Blocks','Steals','Turnovers'])
        
        jordan_figure=px.bar(jordan_averages_playoffs,x=jordan_averages_playoffs.index,y="Total",
          title="Jordan's Average Playoff Statistics",
          color_discrete_sequence =['#CE1141']*len(jordan_averages_playoffs)
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['pts','ast','trb','blk','stl','tov'],
        ticktext=['Points','Assists','Rebounds','Blocks','Steals','Turnovers'])
        
        return lebron_figure,jordan_figure
    elif value == "NBA Finals":
        
        total_range = 0 
        lebron_range = lebron_averages_finals.max()[0]
        jordan_range = jordan_averages_finals.max()[0]
        if jordan_range > lebron_range:
            total_range = jordan_range
        else:
            total_range = lebron_range
            
        lebron_figure=px.bar(lebron_averages_finals,x=lebron_averages_finals.index,y="Total",
          title="Lebron's Average Finals Statistics",
          color_discrete_sequence =['#552583']*len(lebron_averages_finals)
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['pts','ast','trb','blk','stl','tov'],
        ticktext=['Points','Assists','Rebounds','Blocks','Steals','Turnovers'])
        
        jordan_figure=px.bar(jordan_averages_finals,x=jordan_averages_finals.index,y="Total",
          title="Jordan's Average Finals Statistics",
          color_discrete_sequence =['#CE1141']*len(jordan_averages_finals)
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['pts','ast','trb','blk','stl','tov'],
        ticktext=['Points','Assists','Rebounds','Blocks','Steals','Turnovers'])
        
        return lebron_figure,jordan_figure
    
app.run_server(debug=True,port=8050) 
        
app.run_server(debug=True,port=8056) 
