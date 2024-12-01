import plotly.figure_factory as ff
import plotly.graph_objects as go

def create_gantt_chart(tasks):
    if not tasks:
        tasks = [dict(Task="Example Task", Start='2023-01-01', Finish='2023-01-02')]
    
    fig = ff.create_gantt(tasks, group_tasks=True, show_colorbar=True)
    
    # Update layout to add grid lines
    fig.update_layout(
        xaxis=dict(
            showgrid=True,
            gridcolor='LightGray',
            gridwidth=1
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='LightGray',
            gridwidth=1
        )
    )
    
    return fig.to_html(full_html=False)