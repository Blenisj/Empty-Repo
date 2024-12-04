import plotly.figure_factory as ff
import plotly.graph_objects as go

def create_gantt_chart(user_tasks=None):
    tasks = [
            dict(Task="Planning", Start='2024-11-22', Finish='2024-11-23', Dependencies='-'),
            dict(Task="Initial Prototype Design", Start='2024-11-24', Finish='2024-11-26', Dependencies='Planning'),
            dict(Task="Front-End Development", Start='2024-11-26', Finish='2024-11-28', Dependencies='Initial Prototype Design'),
            dict(Task="Back-End Development", Start='2024-11-29', Finish='2024-11-30', Dependencies='Front-End Development'),
            dict(Task="Testing & QA", Start='2024-12-01', Finish='2024-12-02', Dependencies='Back-End Development'),
            dict(Task="Final Adjustments", Start='2024-12-02', Finish='2024-12-03', Dependencies='Testing & QA'),
            dict(Task="Final Delivery", Start='2024-12-03', Finish='2024-12-03', Dependencies='Final Adjustments')
    ]
    if user_tasks:
        tasks.extend(user_tasks)
    
    fig = ff.create_gantt(tasks, group_tasks=True, show_colorbar=True)
    
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