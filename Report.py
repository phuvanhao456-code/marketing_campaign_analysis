import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Tóm tắt & báo cáo phân tích khách hàng và nhóm chiến dịch Marketing",
    page_icon="📚"
)

st.header('📚 Tóm tắt & báo cáo phân tích khách hàng và nhóm chiến dịch Marketing')

st.subheader('1) Tổng quan dữ liệu')

st.write('''
    * Số lượng khách hàng: 2.237
    * Độ tuổi: 28 – 84 tuổi, tuổi trung bình ~55
    * Thu nhập trung bình: ~52.000 USD
    * Phân bố học vấn:
        - Tốt nghiệp đại học chiếm tỷ lệ cao nhất (50%)
        - Tiếp theo là Master (24%), PhD (10%)
    * Tình trạng hôn nhân:
        - Married (39%) và Together (29%) chiếm phần lớn
        - Single chiếm khoảng 17%
''')

st.subheader('2) Hành vi tiêu dùng')

st.markdown("""
<style>
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  border: 1px solid black;
  padding: 8px;
  text-align: left;
}
</style>

<table>
  <tr>
    <th>Chỉ số</th>
    <th>Giá trị trung bình</th>
    <th>Nhận xét</th>
  </tr>
  <tr>
    <td>Mua tại cửa hàng</td>
    <td>5.79 lần</td>
    <td><b>Kênh mua chủ đạo</b></td>
  </tr>
  <tr>
    <td>Mua qua web</td>
    <td>4.09 lần</td>
    <td>Có tiềm năng mở rộng</td>
  </tr>
  <tr>
    <td>Mua qua catalog</td>
    <td>2.66 lần</td>
    <td>Chưa phổ biến</td>
  </tr>
    <tr>
    <td>Số lần truy cập web/tháng</td>
    <td>5.3 lần</td>
    <td>Mức độ quan tâm trung bình</td>
  </tr>
    </tr>
    <tr>
    <td>Tỷ lệ mua hàng có khuyến mãi</td>
    <td>5.3 lần</td>
    <td>Khách hàng <b>ít nhạy cảm với khuyến mãi</b></td>
  </tr>
</table>
""", unsafe_allow_html=True)

st.subheader('Chi tiêu theo danh mục sản phẩm')

st.markdown("""
<style>
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  border: 1px solid black;
  padding: 8px;
  text-align: left;
}
</style>

<table>
  <tr>
    <th>Danh mục</th>
    <th>Mức chi trung bình (USD)</th>
    <th>Ghi chú</th>
  </tr>
  <tr>
    <td>Rượu (Wines)</td>
    <td><b>304</b></td>
    <td><b>Chiếm tỷ trọng cao nhất</b></td>
  </tr>
  <tr>
    <td>Thịt (Meat Products)</td>
    <td><b>165</b></td>
    <td>Nhóm sản phẩm mạnh thứ hai</td>
  </tr>
  <tr>
    <td>Vàng (Gold Products)</td>
    <td><b>52</b></td>
    <td>Cao hơn mức trung bình</td>
  </tr>
    <tr>
    <td>Hoa quả, cá, bánh kẹo</td>
    <td>< 50</td>
    <td>Nhóm phụ, ít quan tâm hơn</td>
</table>
""", unsafe_allow_html=True)

st.subheader('➡️Insight: Khách hàng có xu hướng chi tiêu cao cho rượu vang và thịt, thể hiện phong cách tiêu dùng cao cấp, hướng đến chất lượng hơn giá rẻ.')

st.subheader('4) Nhóm khách hàng nổi bật')

st.write('''
         **Nhóm 1) Nhóm khách hàng giá trị cao (High Value)**
            * Tuổi: 41–60
            * Thu nhập: >70.000 USD
            * Học vấn: Graduation hoặc Master
            * Mua nhiều qua cửa hàng & web
            * Tỷ lệ phản hồi chiến dịch: cao hơn trung bình (≥20%)
         ''')

st.write('''
         **Nhóm 2) Nhóm tiềm năng (Potential Online Buyers)**
            * Tuổi: 31–40
            * Thu nhập: 20K–50K
            * Mua qua website thường xuyên, nhưng tỷ lệ mua thấp
            * Đề xuất: Tăng cường remarketing online, ưu đãi cá nhân hóa
         ''')

st.write('''
         **Nhóm 3) Nhóm ít phản hồi (Low Engagement)**
            * Tuổi >60
            * Mua chủ yếu tại store, ít tương tác web
            * Đề xuất: Tập trung marketing truyền thống hoặc ưu đãi tại cửa hàng
         ''')

st.subheader('5) Hiệu quả chiến dịch quảng cáo')

st.write('''
        * Tỷ lệ phản hồi tổng thể: 14.9%
        * Chiến dịch hiệu quả nhất: Campaign 4 (7.4%)
        * Thấp nhất: Campaign 2 (1.3%)
         ''')

st.subheader('➡️Insight: Cần phân tích sâu hơn nội dung của Chiến dịch 4 để nhân rộng mô hình cho các đợt quảng cáo sau')

st.subheader('6) Tổng hợp Insight chính')

st.write('''
        * ✅ Khách hàng chủ yếu là trung niên, thu nhập khá – cao, học vấn cao.
        * ✅ Rượu vang và thịt là hai nhóm sản phẩm sinh lời cao nhất.
        * ✅ Kênh cửa hàng vẫn chiếm ưu thế, nhưng web và catalog là hướng phát triển tiềm năng.
        * ✅ Chiến dịch quảng cáo đạt hiệu quả vừa phải (15%), cần tăng cá nhân hóa & phân nhóm mục tiêu rõ ràng hơn.
        * ✅ Nhóm tuổi 31–40 là đối tượng nên đầu tư digital marketing mạnh mẽ nhất. 
        ''')

st.subheader('7) Đề xuất hành động')

st.write('''
        * Tăng ngân sách digital cho nhóm tuổi 31–40 với thu nhập 30K–50K.
        * Cải thiện trải nghiệm web, thêm ưu đãi độc quyền online.
        * Phân tầng chiến dịch: 
            - Cao cấp (41–60 tuổi, thu nhập >70K) → Ưu đãi rượu vang, thịt nhập khẩu.
            - Trẻ trung (31–40 tuổi, thu nhập trung bình) → Combo gia đình, khuyến mãi web.
        * Phân tích chi tiết Campaign 4 để xác định yếu tố thành công (nội dung, kênh, thời điểm).
        * Tăng cường các chiến dịch quảng cáo tại điểm bán dành cho nhóm khách hàng lớn tuổi.
        * Gia tăng thêm các chương trình khuyến mãi & khuyến mại cho nhóm khách hàng từ 41-60.
        * Các chương trình bán kèm theo combo sản phẩm, các chương trình VM sản phẩm, bán chéo dựa vào nhu cầu mua sắm của khách hàng.
        * Gia tăng thêm mật độ phủ của các kênh phân phối tại cửa hàng, gia tăng các chương trình chào bán các sản phẩm nhu yếu phẩm thiết yếu.
        ''')



