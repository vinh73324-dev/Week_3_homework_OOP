####################################
# Mã sinh viên: 202419018
# Họ tên:       Phạm Văn Vinh
####################################


class Employee:
    """
    Lớp nhân sự cơ bản
    """
    # Constructor nạp chồng thông qua giá trị mặc định
    def __init__(self, id="UNKNOWN", fullName="Unnamed employee", baseSalary=0.0):
        # Kiểm tra dữ liệu đầu vào (Bất biến)
        if not id or not str(id).strip():
            raise ValueError("Mã nhân sự không được rỗng")

        if not fullName or not str(fullName).strip():
            raise ValueError("Họ tên không được rỗng")

        if baseSalary < 0:
            raise ValueError("Lương cơ bản không được âm")

        self._id = str(id).strip()
        self._fullName = str(fullName).strip()
        self._baseSalary = float(baseSalary)

    # Constructor không tham số
    @classmethod
    def default(cls):
        return cls("UNKNOWN", "Unnamed employee", 0.0)

    # Constructor nhận id và fullName
    @classmethod
    def from_id_name(cls, id, fullName):
        return cls(id, fullName, 0.0)

    # Constructor nhận đầy đủ tham số
    @classmethod
    def from_full(cls, id, fullName, baseSalary):
        return cls(id, fullName, baseSalary)

    # Nạp chồng phương thức tăng lương
    def increaseSalary(self, value, byPercentage=False):
        """
        byPercentage = True: Tăng lương theo tỷ lệ phần trăm lương hiện tại
        byPercentage = False (mặc định nếu chỉ truyền 1 tham số): Tăng lương theo số tiền cố định
        """
        if value <= 0:
            raise ValueError("Giá trị tăng phải dương")
            
        if byPercentage is True:
            self._baseSalary += (float(value) / 100.0) * self._baseSalary
        else:
            self._baseSalary += float(value)

    # Getter
    def get_id(self):
        return self._id

    def get_full_name(self):
        return self._fullName

    def get_base_salary(self):
        return self._baseSalary

    def calculateMonthlyCost(self):
        """
        Trả về chi phí nhân sự hàng tháng (mặc định bằng lương cơ bản)
        """
        return self._baseSalary

    def displayInfo(self):
        print(f"ID: {self._id} | Họ tên: {self._fullName} | Lương CB: {self._baseSalary}")

    def __del__(self):
        if hasattr(self, "_id"):
            print(f"Employee {self._id} ({self._fullName}) đã kết thúc vòng đời")


class SoftwareEngineer(Employee):
    """
    Lớp Kỹ sư phần mềm kế thừa công khai từ Employee
    """
    def __init__(self, id="UNKNOWN", fullName="Unnamed employee", primaryLanguage="Unknown",
                 baseSalary=0.0, technicalAllowance=0.0):
        # Kiểm tra dữ liệu riêng của SoftwareEngineer
        if not primaryLanguage or not str(primaryLanguage).strip():
            raise ValueError("Ngôn ngữ lập trình chính không được rỗng")

        if technicalAllowance < 0:
            raise ValueError("Phụ cấp kỹ thuật không được âm")

        # Gọi constructor của lớp cha
        super().__init__(id, fullName, baseSalary)

        self._primaryLanguage = str(primaryLanguage).strip()
        self._technicalAllowance = float(technicalAllowance)

    # Constructor nhận id, name, primaryLanguage
    @classmethod
    def from_id_name_pL(cls, id, fullName, primaryLanguage):
        return cls(id, fullName, primaryLanguage, 0.0, 0.0)

    # Constructor nhận đầy đủ tham số
    @classmethod
    def from_all(cls, id, fullName, primaryLanguage, baseSalary, technicalAllowance):
        return cls(id, fullName, primaryLanguage, baseSalary, technicalAllowance)

    def get_primary_language(self):
        return self._primaryLanguage

    def get_technical_allowance(self):
        return self._technicalAllowance
    
    def calculateMonthlyCost(self):
        """
        Ghi đè: Trả về (lương cơ bản) + (phụ cấp kỹ thuật)
        """
        return self._baseSalary + self._technicalAllowance
    
    def displayInfo(self):
        print(f"ID: {self._id} | Họ tên: {self._fullName} | Lương CB: {self._baseSalary} | Ngôn ngữ chính: {self._primaryLanguage} | Phụ cấp: {self._technicalAllowance}")

    def __del__(self):
        if hasattr(self, "_id"):
            print(f"SoftwareEngineer {self._id} ({self._fullName}) đã kết thúc vòng đời")


class ProjectTeam:
    """
    Lớp Nhóm dự án quản lý danh sách nhân sự tham gia (Quan hệ kết tập - Aggregation)
    """
    # Nạp chồng constructor
    def __init__(self, projectCode, projectName, leader=None):
        if not projectCode or not str(projectCode).strip():
            raise ValueError("Mã dự án không được rỗng")

        if not projectName or not str(projectName).strip():
            raise ValueError("Tên dự án không được rỗng")

        self._projectCode = str(projectCode).strip()
        self._projectName = str(projectName).strip()
        self._leader = None
        self._teams = []

        if leader is not None:
            self._leader = leader
            self._teams.append(leader)

    # Constructor có leader
    @classmethod
    def with_leader(cls, projectCode, projectName, leader):
        return cls(projectCode, projectName, leader)

    def get_project_code(self):
        return self._projectCode

    def get_project_name(self):
        return self._projectName

    def get_leader(self):
        return self._leader

    def get_members(self):
        return list(self._teams)

    def addMember(self, employee, makeLeader=False):
        """
        Thêm nhân sự vào nhóm.
        - Không thêm trùng nhân sự.
        - Nếu makeLeader == True, nhân sự được thêm và trở thành trưởng nhóm.
        - Trưởng nhóm cũ vẫn là thành viên nếu đã có trong nhóm.
        """
        # Nếu employee đã trong team, không thêm tiếp (Bất biến: không trùng ID)
        if self.contains(employee.get_id()):
            return False

        if makeLeader is True:
            self._leader = employee

        self._teams.append(employee)
        return True

    def removeMember(self, employeeId):
        """
        Xóa nhân sự khỏi nhóm theo mã nhân sự.
        - Không được xóa trưởng nhóm khi chưa chọn trưởng nhóm thay thế.
        """
        for i, member in enumerate(self._teams):
            if member.get_id() == employeeId:
                # Bất biến: Không cho phép xóa leader
                if member is self._leader:
                    return False

                del self._teams[i]
                return True

        # Nếu không ai trong team khớp ID, xóa thất bại
        return False

    def changeLeader(self, employee):
        """
        Đổi trưởng nhóm mới:
        - Trưởng nhóm mới phải được thêm vào nhóm nếu chưa phải thành viên.
        """
        if not self.contains(employee.get_id()):
            self._teams.append(employee)
        self._leader = employee

    def contains(self, employeeID):
        for member in self._teams:
            if member.get_id() == employeeID:
                return True
        return False

    def calculateTotalMonthlyCost(self):
        """
        Tính tổng chi phí hàng tháng của toàn nhóm qua lời gọi đa hình
        """
        result = 0.0
        for member in self._teams:
            result += member.calculateMonthlyCost()
        return result

    def displayTeam(self):
        print(f"--- Dự án: {self._projectCode} - {self._projectName} ---")
        if self._leader is not None:
            print(f"Trưởng nhóm: {self._leader.get_full_name()} ({self._leader.get_id()})")
        else:
            print("Trưởng nhóm: Chưa có")

        print("Danh sách thành viên:")
        if not self._teams:
            print("  (Trống)")
        for idx, member in enumerate(self._teams, 1):
            role = " [Trưởng nhóm]" if member is self._leader else ""
            print(f"  {idx}.{role} ", end="")
            member.displayInfo()
        print(f"Tổng chi phí tháng: {self.calculateTotalMonthlyCost()}")

    def __del__(self):
        if hasattr(self, "_projectCode"):
            print(f"ProjectTeam {self._projectCode} đã kết thúc vòng đời")
