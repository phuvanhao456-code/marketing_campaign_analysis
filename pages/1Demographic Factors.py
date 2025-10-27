import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st 

df = pd.read_csv('https://raw.githubusercontent.com/riodev1310/rio_datasets/refs/heads/main/marketing_campaign.csv')

st.set_page_config(
    page_title="Trực quan hóa dữ liệu các yếu tố nhân khẩu học 'Demographic Factors'",
    page_icon="📚"
)

st.title("📚 Trực quan hóa dữ liệu các yếu tố nhân khẩu học 'Demographic Factors'")

st.header('1) Vẽ biểu đồ cột (histplot) mô tả tình trạng độ tuổi của khách hàng')

# Vẽ biểu đồ cột theo độ tuổi (Age)
plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=20, kde=True, color='seagreen')
plt.title('Phân bố độ tuổi khách hàng')
plt.xlabel('Tuổi')
plt.ylabel('Số lượng khách hàng')
st.pyplot(plt)

st.subheader("2) Vẽ biểu đồ hộp (Boxplot) mô tả tình trạng độ tuổi của khách hàng")

# Vẽ biểu đồ hộp theo độ tuổi
plt.figure(figsize=(8,5))
sns.boxplot(x=df['Age'], color='lightgrey')
plt.title('Phân bố tuổi khách hàng theo (Boxplot)', fontsize=14)
plt.xlabel('Tuổi', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()
st.pyplot(plt)

st.subheader("3) Vẽ biểu cột (Barplot) theo nhóm tuổi")

# Đếm số lượng khách hàng theo nhóm tuổi
age_counts = df['AgeRange'].value_counts().sort_index()
# Vẽ biểu đồ
plt.figure(figsize=(10,6))
sns.barplot(x=age_counts.index, y=age_counts.values, hue=age_counts.index, palette='viridis', legend=False)
# Thêm nhãn số lượng trên đầu cột
for i, v in enumerate(age_counts.values):
    plt.text(i, v + 5, str(v), ha='center', fontsize=10)
plt.title('Số lượng khách hàng theo nhóm tuổi (AgeRange)', fontsize=14)
plt.xlabel('Nhóm tuổi', fontsize=12)
plt.ylabel('Số lượng khách hàng', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
st.pyplot(plt)

st.subheader("3) Vẽ biểu cột (Barplot) theo nhóm trình độ học vấn")

# Đếm số lượng khách hàng theo Education
edu_counts = df['Education'].value_counts()
# Vẽ biểu đồ Bar Chart
plt.figure(figsize=(10,6))
sns.barplot(x=edu_counts.index, y=edu_counts.values, hue=edu_counts.index, palette='viridis', legend=False)
# Thêm nhãn số trên từng cột
for i, v in enumerate(edu_counts.values):
    plt.text(i, v + 5, str(v), ha='center', fontsize=10)
plt.title('Số lượng khách hàng theo trình độ học vấn (Education)', fontsize=14)
plt.xlabel('Trình độ học vấn', fontsize=12)
plt.ylabel('Số lượng khách hàng', fontsize=12)
plt.xticks(rotation=20)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
st.pyplot(plt)

st.subheader("4) Vẽ biểu cột (Barplot) theo nhóm tình trạng hôn nhân")

# Đếm số lượng từng loại trong Marital_Status
marital_counts = df['Marital_Status'].value_counts()
# Vẽ biểu đồ Bar Chart
plt.figure(figsize=(10,8))
sns.barplot(
    x=marital_counts.index,
    y=marital_counts.values,
    hue=marital_counts.index,   # thêm dòng này
    palette='Set2',
    legend=False                # ẩn chú thích
)
# Thêm tiêu đề và nhãn trục
plt.title('Biểu đồ phân bổ tình trạng hôn nhân của khách hàng', fontsize=14)
plt.xlabel('Tình trang hôn nhân', fontsize=12)
plt.ylabel('Số lượng', fontsize=12)
# Hiển thị giá trị trên từng cột
for i, v in enumerate(marital_counts.values):
    plt.text(i, v + 1, str(v), ha='center', fontsize=10)
plt.show()
st.pyplot(plt)

st.subheader("5) Vẽ biểu cột (Boxplot) theo Income")

plt.figure(figsize=(10,6))
sns.boxplot(x=df['Income'], color='skyblue')
plt.title('Biểu đồ Boxplot theo Income', fontsize=14)
plt.xlabel('Income', fontsize=12)
plt.show()
st.pyplot(plt)

st.subheader("6) Vẽ biểu cột (Barplot) theo IncomeRange")

# Đếm số lượng từng khoảng thu nhập
income_counts = df['IncomeRange'].value_counts()
# Vẽ Bar Chart
plt.figure(figsize=(10,6))
sns.barplot(
    x=income_counts.index,
    y=income_counts.values,
    hue=income_counts.index,   # giúp hiển thị màu riêng cho từng cột
    palette='Set2',
    legend=False
)
# Thêm tiêu đề và nhãn
plt.title('Biểu đồ theo Income Range', fontsize=14)
plt.xlabel('Income Range', fontsize=12)
plt.ylabel('Số lượng', fontsize=12)
# Hiển thị giá trị trên cột
for i, v in enumerate(income_counts.values):
    plt.text(i, v + 0.5, str(v), ha='center', fontsize=10)
plt.show()
st.pyplot(plt)

st.subheader("7) So sánh trung bình Kidhome, Teenhome theo Marital Status")

# Gom nhóm và tính trung bình
group_data = df.groupby('Marital_Status')[['Kidhome', 'Teenhome']].mean()
# Vẽ biểu đồ cột
group_data.plot(kind='bar', figsize=(8,6), colormap='Set2')
plt.title('Trung bình số Kidhome và Teenhome theo Marital Status', fontsize=14)
plt.xlabel('Marital Status', fontsize=12)
plt.ylabel('Số trung bình', fontsize=12)
plt.legend(title='Biến')
plt.tight_layout()
plt.show()
st.pyplot(plt)

