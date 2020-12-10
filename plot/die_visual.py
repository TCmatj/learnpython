import pygal
from die import Die

# 创建一个D6
die1 = Die()
die2 = Die(10)
die3 = Die(12)

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die1.num_sides + die2.num_sides + die3.num_sides
for value in range(1,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 and a D12 50,000 times."
x_table = []
for value in range(3,max_result + 1):
    result = str(value)
    x_table.append(result)
hist.x_lables =  x_table
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10 + D12',frequencies)
hist.render_to_file('.//plot//die_visual.svg')