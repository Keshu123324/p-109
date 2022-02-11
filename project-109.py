import random as rand
import plotly.figure_factory as ff
import statistics as s
import plotly.graph_objects as go
import pandas as pd


df=pd.read_csv("StudentsPerformance.csv")
Maths_score=df["math score"].tolist()

#calculating the math_mean, math_median, and math_mode
math_mean=s.mean(Maths_score)
math_mode=s.mode(Maths_score)
math_median=s.median(Maths_score)

print("the math_mean is: ", math_mean)
print("the math_mode is: ", math_mode)
print("the math_median is: ", math_median)

#calculating standard deviation
std_deviation=s.stdev(Maths_score)
print(std_deviation)

#finding 1 standard deviation start and end values
first_std_deviation_start, first_std_deviation_end = math_mean-std_deviation, math_mean+std_deviation
list_data_within_1_std_deviation=[i for i in Maths_score if i > first_std_deviation_start and i < first_std_deviation_end ]
print("percentage of data lies within 1 standard deviation of the math_mean ", len((list_data_within_1_std_deviation)*100)/len(Maths_score))
    
#finding 2 standard deviation start and end values
second_std_deviation_start, second_std_deviation_end = math_mean-(std_deviation*2), math_mean+(std_deviation*2)
list_data_within_2_std_deviation=[i for i in Maths_score if i > second_std_deviation_start and i < second_std_deviation_end ]
print("percentage of data lies within 2 standard deviation of the math_mean  ", len((list_data_within_2_std_deviation)*100)/len(Maths_score))

#finding 3 standard deviation start and end values
third_std_deviation_start, third_std_deviation_end = math_mean-(std_deviation*3), math_mean+(std_deviation*3)
list_data_within_3_std_deviation=[i for i in Maths_score if i > third_std_deviation_start and i < third_std_deviation_end ]
print("percentage of data lies within 3 standard deviation of the math_mean ", len((list_data_within_3_std_deviation)*100)/len(Maths_score))

fig=ff.create_distplot([Maths_score], ["Maths_score"], show_hist=False)
fig.add_trace(go.Scatter(x=[math_mean, math_mean], y=[0,0.17], mode="lines", name="math_mean"))

fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start], y=[0,0.17], mode="lines", name="standard deviation 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end], y=[0,0.17], mode="lines", name="standard deviation 1"))

fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start], y=[0,0.17], mode="lines", name="standard deviation 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end], y=[0,0.17], mode="lines", name="standard deviation 2"))

fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.17], mode="lines", name="standard deviation 3"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.17], mode="lines", name="standard deviation 3"))
fig.show()


