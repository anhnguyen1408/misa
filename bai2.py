import pandas as pd

# 1. Tạo bảng Nhân viên
employee_data = {
    'ID': [101, 102, 103, 104, 105, 106],
    'Name': ['An', 'Bình', 'Cường', 'Dương', None, 'Hạnh'],
    'Age': [25, None, 30, 22, 28, 35],
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR', None],
    'Salary': [700, 800, 750, None, 710, 770]
}

df_emp = pd.DataFrame(employee_data)

# 2. Tạo bảng phòng ban
dept_data = {
    'Department': ['HR', 'IT', 'Finance', 'Marketing'],
    'Manager': ['Trang', 'Khoa', 'Minh', 'Lan']
}

df_dept = pd.DataFrame(dept_data)

# 3. Kiểm tra dữ liệu bị thiếu
print("\nKiểm tra giá trị thiếu:")
print(df_emp.isnull())

# 4. Xoá dòng có hơn 2 giá trị bị thiếu
df_emp = df_emp[df_emp.isnull().sum(axis=1) <= 2]

# 5. Điền giá trị thiếu
df_emp['Name'] = df_emp['Name'].fillna('Chưa rõ')
df_emp['Age'] = df_emp['Age'].fillna(df_emp['Age'].mean())
df_emp['Salary'] = df_emp['Salary'].fillna(method='ffill')
df_emp['Department'] = df_emp['Department'].fillna('Unknown')

# 6. Chuyển kiểu dữ liệu sang int
df_emp['Age'] = df_emp['Age'].astype(int)
df_emp['Salary'] = df_emp['Salary'].astype(int)

# 7. Thêm cột Salary_after_tax
df_emp['Salary_after_tax'] = df_emp['Salary'] * 0.9

# 8. Lọc nhân viên thuộc IT và tuổi > 25
filtered_emp = df_emp[(df_emp['Department'] == 'IT') & (df_emp['Age'] > 25)]
print("\nNhân viên IT và tuổi > 25:")
print(filtered_emp)

# 9. Sắp xếp theo Salary_after_tax giảm dần
sorted_emp = df_emp.sort_values(by='Salary_after_tax', ascending=False)
print("\nBảng nhân viên sắp xếp theo lương sau thuế:")
print(sorted_emp)

# 10. Nhóm theo phòng ban và tính lương trung bình
avg_salary_by_dept = df_emp.groupby('Department')['Salary'].mean()
print("\nLương trung bình theo phòng ban:")
print(avg_salary_by_dept)

# 11. Merge với bảng phòng ban để biết Manager
merged_df = pd.merge(df_emp, df_dept, on='Department', how='left')
print("\nNhân viên với thông tin Manager:")
print(merged_df)

# 12. Thêm 2 nhân viên mới bằng concat
new_employees = pd.DataFrame([
    {'ID': 107, 'Name': 'Phúc', 'Age': 27, 'Department': 'Marketing', 'Salary': 760},
    {'ID': 108, 'Name': 'Quân', 'Age': 29, 'Department': 'IT', 'Salary': 820}
])
# Thêm các cột còn thiếu
new_employees['Salary_after_tax'] = new_employees['Salary'] * 0.9

# Gộp bảng
df_emp_full = pd.concat([df_emp, new_employees], ignore_index=True)
print("\nBảng nhân viên sau khi thêm 2 người mới:")
print(df_emp_full)
