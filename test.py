import matplotlib.pyplot as plt

# 模拟数据
time = [2018, 2019, 2020, 2021, 2022]
saved_food = [10, 20, 30, 40, 50]

# 绘制折线图
plt.plot(time, saved_food)

# 设置图表标题并给坐标轴加上标签
plt.title("Saved Food Over Time")
plt.xlabel("Time (months)")
plt.ylabel("Saved Food (kg)")

# 显示图表
plt.show()



# import matplotlib.pyplot as plt

# # 设置粮食消费数据
# food_consumption = [20, 25, 30, 35, 40, 45]

# # 设置对应的年份
# years = [2015, 2016, 2017, 2018, 2019, 2020]

# # 使用 Matplotlib 绘制折线图
# plt.plot(years, food_consumption)

# # 设置图标标题和坐标轴标签
# plt.title('Food Consumption Over the Years')
# plt.xlabel('Year')
# plt.ylabel('Food Consumption (kg)')

# # 显示图表
# plt.show()