import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 

df = pd.read_csv('https://raw.githubusercontent.com/riodev1310/rio_datasets/refs/heads/main/marketing_campaign.csv')

st.set_page_config(
    page_title="Trực quan hóa biểu đồ kết hợp (Multi-variable visualizations)",
    page_icon="📚"
)

st.title("📚 Trực quan hóa biểu đồ kết hợp (Multi-variable visualizations)")

st.header("1) Chi tiêu trung bình theo nhóm tuổi")

# Thêm cột total biểu biện chi tiêu tổng cho các sản phẩm MntWines,MntFruits,MntMeatProducts,MntFishProducts,MntSweetProducts,MntGoldProds
df['TotalSpend'] = df['MntWines'] + df['MntFruits'] + df['MntMeatProducts'] + df['MntFishProducts'] + df['MntSweetProducts'] + df['MntGoldProds']

# --- Tính trung bình chi tiêu theo nhóm tuổi ---
age_spend = df.groupby('AgeRange')['TotalSpend'].mean().reset_index()
# --- Vẽ biểu đồ đường ---
plt.figure(figsize=(8,5))
sns.lineplot(x='AgeRange', y='TotalSpend', data=age_spend, marker='o', linewidth=2.5)
# --- Trang trí ---
plt.title('Chi tiêu trung bình theo nhóm tuổi', fontsize=14)
plt.xlabel('Nhóm tuổi (Age Range)', fontsize=12)
plt.ylabel('Chi tiêu trung bình (Total Spend)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
# --- Hiển thị giá trị trên từng điểm ---
for i, row in age_spend.iterrows():
    plt.text(row['AgeRange'], row['TotalSpend'] + 5,
             f"{row['TotalSpend']:.0f}", ha='center', fontsize=10)
plt.show()
st.pyplot(plt)

st.subheader("2) Mối tương quan giữa tổng thu nhập và chi tiêu")

income_spend = df.groupby('IncomeRange')['TotalSpend'].mean().reset_index()
plt.figure(figsize=(8,5))
sns.scatterplot(
    x='IncomeRange',
    y='TotalSpend',
    data=income_spend,
    s=100,
    color='royalblue',
    edgecolor='black'
)
plt.title('Mối tương quan giữa thu nhập và chi tiêu', fontsize=14)
plt.xlabel('Khoảng thu nhập (Income Range)', fontsize=12)
plt.ylabel('Chi tiêu trung bình (Total Spend)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
# Hiển thị giá trị trên từng điểm
for i, row in income_spend.iterrows():
    plt.text(i, row['TotalSpend'] + 30,   # ← tăng từ +5 lên +30
             f"{row['TotalSpend']:.0f}",
             ha='center', fontsize=10, color='black')
plt.show()
st.pyplot(plt)

st.subheader("3) Mối tương quan giữa kênh bán hàng và tổng chi tiêu")

# Chọn các cột liên quan
cols = ['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'TotalSpend']
df_plot = df[cols]
# Thiết lập kích thước biểu đồ
plt.figure(figsize=(10,6))
# Vẽ scatter cho từng kênh
sns.scatterplot(data=df_plot, x='NumWebPurchases', y='TotalSpend', label='Web Purchases', alpha=0.7)
sns.scatterplot(data=df_plot, x='NumCatalogPurchases', y='TotalSpend', label='Catalog Purchases', alpha=0.7)
sns.scatterplot(data=df_plot, x='NumStorePurchases', y='TotalSpend', label='Store Purchases', alpha=0.7)
# Trang trí biểu đồ
plt.title('Mối quan hệ giữa kênh mua hàng và chi tiêu (Total Spend)', fontsize=14)
plt.xlabel('Số lần mua hàng (Number of Purchases)', fontsize=12)
plt.ylabel('Tổng chi tiêu (Total Spend)', fontsize=12)
plt.legend(title='Kênh mua hàng')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
st.pyplot(plt)

st.subheader("4) Tỷ lệ phản hồi của khách hàng theo nhóm tuổi")

# Tạo bảng tần suất theo nhóm tuổi và phản hồi
age_response = df.groupby(['AgeRange', 'Response']).size().reset_index(name='Count')
# Tính tỷ lệ phản hồi theo từng nhóm tuổi (để biểu đồ dễ so sánh)
age_total = df.groupby('AgeRange').size().reset_index(name='Total')
age_response = pd.merge(age_response, age_total, on='AgeRange')
age_response['Percentage'] = (age_response['Count'] / age_response['Total']) * 100
# Vẽ biểu đồ Grouped Bar Chart
plt.figure(figsize=(10, 6))
sns.barplot(
    data=age_response,
    x='AgeRange',
    y='Percentage',
    hue='Response',
    palette='coolwarm'
)
# Trang trí biểu đồ
plt.title('Tỷ lệ phản hồi chiến dịch theo nhóm tuổi (AgeRange vs Response)', fontsize=14)
plt.xlabel('Nhóm tuổi (Age Range)', fontsize=12)
plt.ylabel('Tỷ lệ phản hồi (%)', fontsize=12)
plt.legend(title='Response', labels=['Không phản hồi (0)', 'Có phản hồi (1)'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
st.pyplot(plt)

st.subheader("5) So sánh giữa tình trạng hôn nhân và mức độ chi tiêu theo từng nhóm tình trạng hôn nhân")
plt.figure(figsize=(10,6))
sns.boxplot(
    data=df,
    x='Marital_Status',
    y='TotalSpend',
    hue='Marital_Status',     # thêm dòng này
    palette='coolwarm',
    legend=False,             # tắt chú giải lặp lại
    showmeans=True,
    meanprops={"marker":"o","markerfacecolor":"black","markeredgecolor":"black"}
)
plt.title('Phân bố chi tiêu (TotalSpend) theo tình trạng hôn nhân', fontsize=14)
plt.xlabel('Tình trạng hôn nhân')
plt.ylabel('Tổng chi tiêu (TotalSpend)')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
st.pyplot(plt)

st.subheader("6) Biểu đồ tổng chi tiêu theo trình độ học vấn")
spend_by_edu = df.groupby('Education')['TotalSpend'].sum()
plt.figure(figsize=(7,7))
plt.pie(spend_by_edu, labels=spend_by_edu.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set3'))
plt.title('Tỷ trọng tổng chi tiêu theo trình độ học vấn')
plt.show()
st.pyplot(plt)

st.subheader("8) 10 Nhóm khách hàng có thu nhập trung bình lớn nhất")

seg_table = (
    df.groupby(['IncomeRange', 'AgeRange'])
      .agg(
          Customers=('ID', 'count'),
          Avg_Income=('Income', 'mean'),
          Avg_TotalSpend=('TotalSpend', 'mean')
      )
      .reset_index()
      .sort_values(by='Avg_Income', ascending=False)
)

seg_table['Avg_Income'] = seg_table['Avg_Income'].round(0).astype(int)
seg_table['Avg_TotalSpend'] = seg_table['Avg_TotalSpend'].round(0).astype(int)

st.dataframe(seg_table.head(10), use_container_width=True)
