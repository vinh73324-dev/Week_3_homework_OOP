####################################
# Mã sinh viên: 202419018
# Họ tên:       Phạm Văn Vinh
####################################


from model import Employee, SoftwareEngineer, ProjectTeam

def main():
    # 1. Tạo hai Employee bằng hai constructor khác nhau
    print("=== 1. Tạo 2 Employee bằng 2 constructor khác nhau ===")
    e1 = Employee.default()
    e2 = Employee("NV01", "Nguyễn Văn An", 12000000)
    e1.displayInfo()
    e2.displayInfo()

    # 2. Tạo hai SoftwareEngineer bằng hai constructor khác nhau
    print("\n=== 2. Tạo 2 SoftwareEngineer bằng 2 constructor khác nhau ===")
    se1 = SoftwareEngineer("SE01", "Trần Thị Bình", "Python")
    se2 = SoftwareEngineer("SE02", "Lê Hoàng Cường", "C++", 18000000, 4000000)
    se1.displayInfo()
    se2.displayInfo()

    # 3. Tăng lương một nhân sự bằng số tiền cố định
    print("\n=== 3. Tăng lương bằng số tiền cố định ===")
    print("Lương ban đầu của e2:", e2.get_base_salary())
    e2.increaseSalary(3000000)
    print("Lương sau khi tăng 3,000,000:", e2.get_base_salary())

    # 4. Tăng lương một nhân sự khác theo phần trăm
    print("\n=== 4. Tăng lương theo phần trăm ===")
    print("Lương ban đầu của se2:", se2.get_base_salary())
    se2.increaseSalary(10, byPercentage=True)
    print("Lương sau khi tăng 10%:", se2.get_base_salary())

    # 5. Tạo nhóm dự án không có trưởng nhóm
    print("\n=== 5. Tạo nhóm dự án không có trưởng nhóm ===")
    team1 = ProjectTeam("PRJ01", "Hệ thống ERP")
    team1.displayTeam()

    # 6. Thêm một nhân sự vào nhóm bằng addMember(employee)
    print("\n=== 6. Thêm nhân sự vào nhóm bằng addMember(employee) ===")
    res = team1.addMember(e2)
    print("Kết quả addMember(e2):", res)
    team1.displayTeam()

    # 7. Thêm một kỹ sư bằng addMember(employee, true) để đặt làm trưởng nhóm
    print("\n=== 7. Thêm kỹ sư làm trưởng nhóm bằng addMember(se1, True) ===")
    res = team1.addMember(se1, makeLeader=True)
    print("Kết quả addMember(se1, True):", res)
    team1.displayTeam()

    # 8. Thử thêm lại một thành viên đã tồn tại
    print("\n=== 8. Thử thêm lại thành viên đã tồn tại (se1) ===")
    res = team1.addMember(se1)
    print("Kết quả thêm lại se1:", res)

    # 9. Hiển thị danh sách bằng lời gọi đa hình
    print("\n=== 9. Hiển thị danh sách bằng lời gọi đa hình ===")
    for m in team1.get_members():
        m.displayInfo()
        print("Chi phí tháng (calculateMonthlyCost):", m.calculateMonthlyCost())

    # 10. Tính tổng chi phí nhân sự hằng tháng
    print("\n=== 10. Tính tổng chi phí nhân sự hằng tháng ===")
    print("Tổng chi phí hàng tháng của team1:", team1.calculateTotalMonthlyCost())

    # 11. Thử xóa trưởng nhóm hiện tại và kiểm tra thao tác bị từ chối
    print("\n=== 11. Thử xóa trưởng nhóm hiện tại ===")
    leader_id = team1.get_leader().get_id()
    print("Trưởng nhóm hiện tại là:", leader_id)
    res = team1.removeMember(leader_id)
    print("Kết quả xóa trưởng nhóm:", res)

    # 12. Đổi trưởng nhóm rồi xóa người từng là trưởng nhóm
    print("\n=== 12. Đổi trưởng nhóm rồi xóa người từng là trưởng nhóm ===")
    print("Đổi trưởng nhóm sang se2...")
    team1.changeLeader(se2)
    print("Trưởng nhóm mới:", team1.get_leader().get_id())
    res = team1.removeMember("SE01")
    print("Kết quả xóa SE01 (trưởng nhóm cũ):", res)
    team1.displayTeam()

    # 13. Tạo một nhóm thứ hai và thêm một nhân sự đã có ở nhóm thứ nhất
    print("\n=== 13. Tạo nhóm thứ 2 và thêm nhân sự đã có ở nhóm 1 ===")
    team2 = ProjectTeam("PRJ02", "Ứng dụng Di động", leader=se2)
    print("se2 có trong team1 không?:", team1.contains(se2.get_id()))
    print("se2 có trong team2 không?:", team2.contains(se2.get_id()))

    # 14. Hủy nhóm thứ hai bằng cách kết thúc một khối lệnh cục bộ
    print("\n=== 14. Hủy nhóm thứ hai bằng kết thúc khối lệnh cục bộ ===")
    def temp_scope():
        t = ProjectTeam("PRJ_TEMP", "Nhóm tạm")
        t.addMember(se2)
        print("Trong hàm cục bộ: đã tạo và thêm se2 vào PRJ_TEMP")
    temp_scope()
    del team2
    print("Đã hủy team2.")

    # 15. Chứng minh nhân sự của nhóm thứ hai vẫn tồn tại sau khi nhóm bị hủy
    print("\n=== 15. Chứng minh nhân sự vẫn tồn tại sau khi nhóm bị hủy ===")
    print("Thông tin của se2 sau khi team2 bị hủy:")
    se2.displayInfo()
    print("se2 vẫn còn trong team1:", team1.contains(se2.get_id()))

    # Kiểm thử các trường hợp biên
    print("\n=== Kiểm thử các trường hợp biên ===")
    try:
        Employee("", "Nguyễn Văn A", 1000)
    except ValueError as e:
        print("Mã rỗng:", e)

    try:
        Employee("NV02", "", 1000)
    except ValueError as e:
        print("Họ tên rỗng:", e)

    try:
        Employee("NV02", "Nguyễn Văn B", -100)
    except ValueError as e:
        print("Lương âm:", e)

    try:
        SoftwareEngineer("SE03", "Trần Văn C", "")
    except ValueError as e:
        print("Ngôn ngữ rỗng:", e)

    try:
        SoftwareEngineer("SE03", "Trần Văn C", "Python", 1000, -200)
    except ValueError as e:
        print("Phụ cấp âm:", e)

    try:
        e2.increaseSalary(-500)
    except ValueError as e:
        print("Tăng lương âm:", e)

    res = team1.removeMember("MA_KHONG_CO")
    print("Xóa mã không tồn tại:", res)

if __name__ == "__main__":
    main()
