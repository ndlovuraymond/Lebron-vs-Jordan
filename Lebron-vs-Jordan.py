from dash import Dash,dcc,html,callback,Output,Input
from dash import Dash
import pandas as pd
import plotly.express as px

#regular season import
lebron_regular_season = pd.read_csv("lebron_career.csv",parse_dates=["date"])
lebron_totals_regular = lebron_regular_season[["pts","ast","trb","blk","stl","tov"]].sum().to_frame()
lebron_totals_regular.rename(columns={lebron_totals_regular.columns[0]:"Total"},inplace=True)
jordan_regular_season = pd.read_csv("jordan_career.csv",parse_dates=["date"])
jordan_totals_regular = jordan_regular_season[["pts","ast","trb","blk","stl","tov"]].sum().to_frame()
jordan_totals_regular.rename(columns={jordan_totals_regular.columns[0]:"Total"},inplace=True)
#playoffs import
lebron_playoffs = pd.read_csv("lebron_playoffs.csv",parse_dates=["date"])
lebron_totals_playoffs = lebron_playoffs[["pts","ast","trb","blk","stl","tov"]].sum().to_frame()
lebron_totals_playoffs.rename(columns={lebron_totals_playoffs.columns[0]:"Total"},inplace=True)
jordan_playoffs = pd.read_csv("jordan_playoffs.csv",parse_dates=["date"])
jordan_totals_playoffs = jordan_playoffs[["pts","ast","trb","blk","stl","tov"]].sum().to_frame()
jordan_totals_playoffs.rename(columns={jordan_totals_playoffs.columns[0]:"Total"},inplace=True)
#importing finals data
lebron_finals = lebron_playoffs.query("series == 'FIN'")
lebron_total_finals = lebron_finals[["pts","ast","trb","blk","stl","tov"]].sum().to_frame()
lebron_total_finals.rename(columns={lebron_total_finals.columns[0]:"Total"},inplace=True)
jordan_finals = jordan_playoffs.query("series == 'FIN'")
jordan_total_finals = jordan_finals[["pts","ast","trb","blk","stl","tov"]].sum().to_frame()
jordan_total_finals.rename(columns={jordan_total_finals.columns[0]:"Total"},inplace=True)

app = Dash(__name__)

app.layout = html.Div(
children=[
    html.Div(html.H1("Lebron vs Jordan",style={'text-align':'center','color':'white','font-size':'2.5rem',
                                     'font-weight':'bolder','display':'block',
                                      'background-color':'rgb(0,0,0,0.40)','padding':'10px'
                                      ,'border-radius':'5px','margin-bottom':'10px'}),
             id="main-heading"),
        html.Div(children=[html.H2("Cumulative Statistics",style={'text-align':'left',
                        'color':'white','font-size':'2rem','font-weight':'bolder','display':'block',
                        'background-color':'rgb(0,0,0,0.40)','padding':'10px','border-radius':'5px',
                         'margin-top':'0px','margin-bottom':'10px'}),
                         dcc.Dropdown(options=["Regular Season","Playoffs","Finals"],value="Regular Season"
                            ,style={'color':'black','background-color':'rgb(255,255,255,0.40)',
                            'margin-bottom':'10px','font-size':'1.25rem'},id="total-dropdown")
             ],id="sub-heading"),
    html.Div(children=[
    dcc.Graph(id="lebron-stats-total",style={'width':'90%','margin-right':'20px','margin-left':'20px'}),
      dcc.Graph(id="jordan-stats-total",style={'width':'90%','margin-right':'20px'})],id="stats-div")])

@callback(
    Output("lebron-stats-total","figure"),
    Output("jordan-stats-total","figure"),
    Input("total-dropdown","value")
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
          labels={'pts':'Points','ast':'Assists'},
          color_discrete_sequence =['#552583']*len(lebron_totals_regular)
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['pts','ast','trb','blk','stl','tov'],
        ticktext=['Points','Assists','Rebounds','Blocks','Steals','Turnovers'])
        
        jordan_figure=px.bar(jordan_totals_regular,x=jordan_totals_regular.index,y="Total",
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
          color_discrete_sequence =['#552583']*len(lebron_totals_playoffs)
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['pts','ast','trb','blk','stl','tov'],
        ticktext=['Points','Assists','Rebounds','Blocks','Steals','Turnovers'])
        
        jordan_figure=px.bar(jordan_totals_playoffs,x=jordan_totals_playoffs.index,y="Total",
          color_discrete_sequence =['#CE1141']*len(jordan_totals_playoffs)
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['pts','ast','trb','blk','stl','tov'],
        ticktext=['Points','Assists','Rebounds','Blocks','Steals','Turnovers'])
        
        return lebron_figure,jordan_figure
    elif value == "Finals":
        
        total_range = 0 
        lebron_range = lebron_total_finals.max()[0]
        jordan_range = jordan_total_finals.max()[0]
        if jordan_range > lebron_range:
            total_range = jordan_range
        else:
            total_range = lebron_range
            
        lebron_figure=px.bar(lebron_total_finals,x=lebron_total_finals.index,y="Total",
          color_discrete_sequence =['#552583']*len(lebron_total_finals)
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['pts','ast','trb','blk','stl','tov'],
        ticktext=['Points','Assists','Rebounds','Blocks','Steals','Turnovers'])
        
        jordan_figure=px.bar(jordan_total_finals,x=jordan_total_finals.index,y="Total",
          color_discrete_sequence =['#CE1141']*len(jordan_total_finals)
          ).update_layout(
            paper_bgcolor="rgb(0,0,0,0.40)",plot_bgcolor="rgb(0,0,0,0.40)",font={'color':'white'},
            yaxis_range=[0,total_range]
        ).update_xaxes(
        title="Statistical Category",
        tickvals=['pts','ast','trb','blk','stl','tov'],
        ticktext=['Points','Assists','Rebounds','Blocks','Steals','Turnovers'])
        
        return lebron_figure,jordan_figure
        
app.run_server(debug=True,port=8056) 