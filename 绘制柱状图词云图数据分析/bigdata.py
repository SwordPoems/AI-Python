import chardet
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# 加载数据
file_path = 'C:\\Users\\Nymphet\\Desktop\\大数据分析\\MathEdataset.csv'  # 替换为你的CSV文件路径

# 检测文件编码
with open(file_path, 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']
    print(f"Detected encoding: {encoding}")

# 使用检测到的编码读取CSV文件
df = pd.read_csv(file_path, delimiter=';', encoding=encoding)

# 查看数据前几行
print(df.head())

# 检查数据信息
print(df.info())

# 检查缺失值
print(df.isnull().sum())

# 统计每个数学主题的数量
topic_counts = df['Topic'].value_counts()

# 绘制柱状图
plt.figure(figsize=(12, 6))
sns.barplot(x=topic_counts.index, y=topic_counts.values, palette='viridis')
plt.title('Math Topics Distribution')
plt.xlabel('Math Topic')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# 统计每个问题关键字的数量
keyword_counts = df['Keywords'].value_counts()

# 绘制柱状图
plt.figure(figsize=(12, 6))
sns.barplot(x=keyword_counts.index[:20], y=keyword_counts.values[:20], palette='viridis')
plt.title('Top 20 Keywords Distribution')
plt.xlabel('Keyword')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# 生成数学主题词云图
topic_text = ' '.join(df['Topic'])
wordcloud_topic = WordCloud(width=800, height=400, background_color='white').generate(topic_text)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud_topic, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Math Topics')
plt.show()

# 生成问题关键字词云图
keyword_text = ' '.join(df['Keywords'])
wordcloud_keyword = WordCloud(width=800, height=400, background_color='white').generate(keyword_text)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud_keyword, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Keywords')
plt.show()

# 按国家和数学主题的分布
country_topic_counts = df.groupby(['Student Country', 'Topic']).size().unstack().fillna(0)

# 绘制热力图
plt.figure(figsize=(12, 8))
sns.heatmap(country_topic_counts, cmap='viridis', annot=True, fmt='g')
plt.title('Distribution of Math Topics by Country')
plt.xlabel('Math Topic')
plt.ylabel('Country')
plt.show()

# 按问题级别和答案类型的分布
level_answer_counts = df.groupby(['Question Level', 'Type of Answer']).size().unstack().fillna(0)

# 绘制堆叠条形图
level_answer_counts.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Distribution of Answers by Question Level')
plt.xlabel('Question Level')
plt.ylabel('Count')
plt.legend(title='Answer Type')
plt.show()




# 转换Type of Answer为二进制值
df['Type of Answer'] = df['Type of Answer'].map({0: 'Incorrect', 1: 'Correct'})

# 计算每个问题ID和主题的正确回答率
correct_rate_by_question_id_and_topic = df.groupby(['Question ID', 'Topic'])['Type of Answer'].apply(
    lambda x: (x == 'Correct').mean()
).reset_index()

# 获取所有独特的数学主题
topics = df['Topic'].unique()

# 创建一个图表
plt.figure(figsize=(14, 7))

# 对于每个主题，绘制正确回答率随问题ID的变化趋势
for topic in topics:
    topic_data = correct_rate_by_question_id_and_topic[correct_rate_by_question_id_and_topic['Topic'] == topic]
    
    # 绘制该主题的线状图
    plt.plot(topic_data['Question ID'], topic_data['Type of Answer'], marker='', label=topic)

# 设置图表标题和标签
plt.title('Comparison of Correct Answer Rates Over Question IDs by Topic')
plt.xlabel('Question ID')
plt.ylabel('Average Correct Rate')

# 显示图例
plt.legend(title='Math Topics')

# 显示网格
plt.grid(True)

# 显示图表
plt.show()