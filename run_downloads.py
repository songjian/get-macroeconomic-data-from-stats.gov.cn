from cnstats.stats import stats
import csv
import pandas as pd

with open('tasks.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # 读取数据代码和时间段
        data_code = row[0]
        time_period = row[1]
        
        # 执行stats函数
        data = stats(data_code, time_period)
        
        # 添加表头
        header = ['数据名', '数据代码', '日期', '数据']
        
        # 将数据转换为DataFrame格式
        df = pd.DataFrame(data, columns=header)
        
        # 将数据保存到csv文件中
        file_name = f"data/{data_code}.csv"
        df.to_csv(file_name, index=False)



