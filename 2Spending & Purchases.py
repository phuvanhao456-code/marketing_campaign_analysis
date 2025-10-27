import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 

df = pd.read_csv('https://raw.githubusercontent.com/riodev1310/rio_datasets/refs/heads/main/marketing_campaign.csv')

st.set_page_config(
    page_title="Trực quan hóa dữ liệu theo hành vi mua hàng & chi tiêu (Spending & Purchases)",
    page_icon="📚"
)

st.title("📚 Trực quan hóa dữ liệu theo hành vi mua hàng & chi tiêu (Spending & Purchases)")

st.header("1) Mức chi tiêu trung bình của khách hàng theo từng nhóm sản phẩm")

# Tạo danh sách các cột sản phẩm
product_cols = [
    'MntWines', 'MntFruits', 'MntMeatProducts',
    'MntFishProducts', 'MntSweetProducts', 'MntGoldProds'
]
# Tính chi tiêu trung bình cho từng loại sản phẩm
avg_spending = df[product_cols].mean().sort_values(ascending=False)

# Vẽ biểu đồ Bar Chart
plt.figure(figsize=(10,6))
sns.barplot(
    x=avg_spending.index,
    y=avg_spending.values,
    hue=avg_spending.index,
    palette='Set2',
    legend=False
)
# Thêm nhãn và tiêu đề
plt.title('Chi tiêu trung bình cho từng loại sản phẩm', fontsize=14)
plt.xlabel('Loại sản phẩm', fontsize=12)
plt.ylabel('Chi tiêu trung bình', fontsize=12)
# Hiển thị giá trị trên đầu cột
for i, v in enumerate(avg_spending.values):
    plt.text(i, v + 1, f'{v:.0f}', ha='center', fontsize=10)
plt.tight_layout()
plt.show()
st.pyplot(plt)

st.subheader("2) So sánh hành vi mua hàng của khách hàng khi có giảm giá và không có giảm giá")
# Các cột liên quan
purchase_cols = ['NumDealsPurchases', 'NumNonDealsPurchases']
# Tính giá trị trung bình
avg_purchase = df[purchase_cols].mean().sort_values(ascending=False)
# Vẽ biểu đồ
plt.figure(figsize=(7,6))
sns.barplot(
    x=avg_purchase.index,
    y=avg_purchase.values,
    hue=avg_purchase.index,
    palette='Set2',
    legend=False
)
# Thêm tiêu đề, nhãn trục và giá trị
plt.title('So sánh hành vi mua hàng có giảm giá và không giảm giá', fontsize=14)
plt.xlabel('Loại hành vi mua hàng', fontsize=12)
plt.ylabel('Số lần mua trung bình', fontsize=12)
for i, v in enumerate(avg_purchase.values):
    plt.text(i, v + 0.1, f'{v:.2f}', ha='center', fontsize=10)
plt.tight_layout()
plt.show()
st.pyplot(plt)

st.subheader("3) So sánh hành vi mua hàng của khách hàng thông qua các kênh bán hàng")

# Tính tổng số lượt mua từng kênh
channels = ['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']
totals = df[channels].sum()
# Tạo Pie Chart
plt.figure(figsize=(7,7))
plt.pie(
    totals,
    labels=['Mua qua Web', 'Mua qua Catalog', 'Mua tại Cửa hàng'],
    autopct='%.1f%%',        # hiển thị phần trăm
    startangle=90,           # xoay cho đẹp
    colors=['#66b3ff','#99ff99','#ffcc99'],  # màu hài hòa
    explode=(0.02, 0.02, 0.02),  # tách nhẹ từng phần ra ngoài
    textprops={'fontsize': 11}
)
plt.title('Tỷ lệ các kênh mua hàng phổ biến', fontsize=14)
plt.show()
st.pyplot(plt)

st.subheader("4) So sánh số lần mua hàng của khách hàng")

# Vẽ biểu đồ
plt.figure(figsize=(8,6))
sns.histplot(
    data=df,
    x='NumAllPurchases',   # cột tổng số lần mua
    bins=20,               # số khoảng chia
    kde=True,              # thêm đường mật độ mượt
    color='cornflowerblue'
)
plt.title('Phân bố số lần mua hàng (NumAllPurchases)', fontsize=14)
plt.xlabel('Số lần mua hàng', fontsize=12)
plt.ylabel('Số lượng khách hàng', fontsize=12)
plt.show()
st.pyplot(plt)
