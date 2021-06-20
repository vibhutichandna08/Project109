import plotly.figure_factory as pf
import pandas as pd
import plotly.graph_objects as go
import statistics

df = pd.read_csv("Project109_data.csv")
data = df["reading score"].tolist()
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
std_deviation = statistics.stdev(data)
print("Mean: {}".format(mean))
print("Median: {}".format(median))
print("Mode: {}".format(mode))
print("Standard deviation: {}".format(std_deviation))
first_std_deviation_start, first_std_deviation_end = mean - \
    std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean - \
    (2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean - \
    (3*std_deviation), mean+(3*std_deviation)
fig = pf.create_distplot([data], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[
              0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 1.1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 1.2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 2.1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 2.2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 3.1"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[
              0, 0.17], mode="lines", name="STANDARD DEVIATION 3.2"))
fig.show()
list_of_data_within_one_std_deviation = [
    result for result in data if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_two_std_deviation = [
    result for result in data if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_three_std_deviation = [
    result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

print("{}% of data lies within one standard deviation".format(
    len(list_of_data_within_one_std_deviation)*100.0/len(data)))
print("{}% of data lies within two standard deviations".format(
    len(list_of_data_within_two_std_deviation)*100.0/len(data)))
print("{}% of data lies within three standard deviations".format(
    len(list_of_data_within_two_std_deviation)*100.0/len(data)))
