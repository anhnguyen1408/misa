import pandas as pd

# 1. Tạo DataFrame df_students
data = {
    'Name': ['An', 'Bình', 'Cường', 'Dương', 'Hà', 'Hải', 'Lan', 'Minh', 'Ngọc', 'Oanh'],
    'Age': [20, 21, 19, 22, 23, 21, 20, 22, 24, 25],
    'Gender': ['M', 'M', 'M', 'M', 'F', 'M', 'F', 'M', 'F', 'F'],
    'Score': [6.5, 8.0, 4.0, 5.5, 7.5, 3.5, 9.0, 6.0, 4.5, 5.0]
}

df_students = pd.DataFrame(data)

# 2. Hiển thị toàn bộ dữ liệu
print("Toàn bộ dữ liệu:")
print(df_students)

# 3. Hiển thị 3 dòng đầu tiên
print("\n3 dòng đầu tiên:")
print(df_students.head(3))

# 4. Theo index=2 và cột Name
print("\nTên sinh viên tại index=2:")
print(df_students.loc[2, 'Name'])

# 5. Theo index=10 và cột Age (sẽ lỗi vì index chỉ từ 0-9)
print("\nThử truy cập index=10 và cột Age:")
try:
    print(df_students.loc[10, 'Age'])
except KeyError:
    print("Không tồn tại index 10!")

# 6. Hiển thị các cột Name và Score
print("\nCột Name và Score:")
print(df_students[['Name', 'Score']])

# 7. Thêm cột Pass
df_students['Pass'] = df_students['Score'] >= 5

# 8. Sắp xếp theo Score giảm dần
df_sorted = df_students.sort_values(by='Score', ascending=False)
print("\nDataFrame sau khi thêm cột Pass và sắp xếp theo Score giảm dần:")
print(df_sorted)
