import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Graphs
# Enrolments for different terms of the same online course
run = ('run1', 'run2', 'run3')
plt.bar(run, all_run_compare.loc['Enrolments',:])
plt.title('Enrolments')
plt.show()

# Fully Completed the course in differenet run
run = ('run1', 'run2', 'run3')
plt.bar(run, all_run_compare.loc['Fully Completed',:])
plt.title('Fully Completed')
plt.show()

# % Activated Social Enrolments 
run = ('run1', 'run2', 'run3')
plt.bar(run, all_run_compare.loc['% Activated Social Enrolments',:])
plt.title('% Activated Social Enrolments')
plt.show()

# The violinplot of 3 runs‘ data
sns.violinplot(x='run', y='% Completed', data=df, kind='violin')  
plt.show()

# Scatter diagram
sns.lmplot( x="% Completed", y="Visitor Count", data=df, fit_reg=False, hue='run', legend=True, palette="Set1")
plt.show()

# Total Nationalities distribution of 3 run by world map
max_show = int(run_data['Enrolments'].max())
min_show = int(run_data['Enrolments'].min())
country = run_data['Country']
Enrolments = run_data['Enrolments']
a = Map().add('',tuple(zip(country,Enrolments)), 'world')
a.set_global_opts(title_opts=opts.TitleOpts(title='World Map'),
                  visualmap_opts=opts.VisualMapOpts(max_=max_show, min_=min_show,
                                                    is_piecewise=True)
    ).set_series_opts(label_opts=opts.LabelOpts(is_show=False))
a.render_notebook()

