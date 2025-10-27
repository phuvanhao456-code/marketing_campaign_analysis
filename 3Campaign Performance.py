import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 

df = pd.read_csv('https://raw.githubusercontent.com/riodev1310/rio_datasets/refs/heads/main/marketing_campaign.csv')

st.set_page_config(
    page_title="Trực quan hóa dữ liệu hiệu quả chiến dịch marketing (Campaign Performance)",
    page_icon="📚"
)

st.title("📚 Trực quan hóa dữ liệu hiệu quả chiến dịch marketing (Campaign Performance)")

st.header("1) Biểu đồ Heatmap của 5 chiến dịch")

# Các cột campaign
campaigns = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']
# Tính tỷ lệ thành công trung bình của từng campaign
success_rates = df[campaigns].mean().to_frame().T * 100  # nhân 100 để ra %
# Vẽ Heatmap
plt.figure(figsize=(8,2))
sns.heatmap(
    success_rates,
    annot=True, fmt='.1f', cmap='YlGnBu',
    cbar=False, linewidths=0.5,
    annot_kws={'fontsize':12}
)
plt.title('Tỷ lệ thành công (%) của các chiến dịch Marketing', fontsize=14)
plt.yticks([])
plt.xlabel('Chiến dịch (Campaign)', fontsize=12)
plt.show()
st.pyplot(plt)

st.subheader("2) Tỷ lệ khách hàng khiếu nại")

# Tổng hợp khiếu nại của khách hàng
complain_counts = df['Complain'].value_counts()
# Nhãn hiển thị
labels = ['Không phàn nàn', 'Có phàn nàn']
# Vẽ biểu đồ tròn
plt.figure(figsize=(6,6))
plt.pie(
    complain_counts,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    colors=['lightgreen', 'tomato'],
    explode=(0, 0.05),
    shadow=True
)
plt.title('Tỷ lệ khách hàng phàn nàn (Complain)', fontsize=14)
plt.show()
st.pyplot(plt)

st.subheader("3) Phân bố số ngày kể từ lần mua gần nhất")

# Vẽ biểu đồ
plt.figure(figsize=(8,6))
sns.histplot(
    data=df,
    x='Recency',
    bins=20,
    kde=True,
    color='green'
)
plt.title('Phân bố số ngày kể từ lần mua gần nhất (Recency)', fontsize=14)
plt.xlabel('Số ngày kể từ lần mua gần nhất', fontsize=12)
plt.ylabel('Số lượng khách hàng', fontsize=12)
plt.show()
st.pyplot(plt)

st.subheader("4) Tỷ lệ phản hồi của khách hàng thông qua 5 chiến dịch")

# Đếm số lượng khách hàng theo trạng thái phản hồi
response_counts = df['Response'].value_counts()
# Tạo nhãn
labels = ['Không phản hồi', 'Có phản hồi']
# Vẽ biểu đồ tròn
plt.figure(figsize=(6,6))
plt.pie(
    response_counts,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    colors=['lightcoral', 'mediumseagreen'],
    explode=(0, 0.05),
    shadow=True
)
plt.title('Tỷ lệ phản hồi của khách hàng (Response)', fontsize=14)
plt.show()
st.pyplot(plt)
