class RectSection:
    """矩形截面几何特性计算类"""

    def __init__(self, b: float, h: float):
        """
        初始化矩形截面尺寸
        :param b: 截面宽度 (mm)
        :param h: 截面高度 (mm)
        """
        if b <= 0 or h <= 0:
            raise ValueError("截面宽度和高度必须大于 0")
        self.b = b
        self.h = h

    def area(self) -> float:
        """计算截面面积 A (mm^2)"""
        return self.b * self.h

    def moment_of_inertia(self):
        """
        计算惯性矩
        I_x: 绕强轴（水平轴）惯性矩 (mm^4)
        I_y: 绕弱轴（竖直轴）惯性矩 (mm^4)
        """
        I_x = (self.b * self.h ** 3) / 12.0
        I_y = (self.h * self.b ** 3) / 12.0
        return I_x, I_y

    def section_modulus(self):
        """
        计算抵抗矩（截面模量）
        W_x, W_y (mm^3)
        """
        W_x = (self.b * self.h ** 2) / 6.0
        W_y = (self.h * self.b ** 2) / 6.0
        return W_x, W_y

    def radius_of_gyration(self):
        """
        计算回转半径
        i_x, i_y (mm)
        """
        A = self.area()
        I_x, I_y = self.moment_of_inertia()
        i_x = (I_x / A) ** 0.5
        i_y = (I_y / A) ** 0.5
        return i_x, i_y

    def print_summary(self):
        """打印完整的几何特性报告"""
        I_x, I_y = self.moment_of_inertia()
        W_x, W_y = self.section_modulus()
        i_x, i_y = self.radius_of_gyration()

        print(f"=== 矩形截面几何特性报告 ===")
        print(f"截面尺寸 (b × h): {self.b} mm × {self.h} mm")
        print(f"截面面积 (A):     {self.area():.2f} mm²")
        print(f"惯性矩 (I_x):     {I_x:.2e} mm⁴")
        print(f"惯性矩 (I_y):     {I_y:.2e} mm⁴")
        print(f"抵抗矩 (W_x):     {W_x:.2e} mm³")
        print(f"抵抗矩 (W_y):     {W_y:.2e} mm³")
        print(f"回转半径 (i_x):   {i_x:.2f} mm")
        print(f"回转半径 (i_y):   {i_y:.2f} mm")
        print(f"============================")


if __name__ == "__main__":
    # 测试一个常见的柱截面：b=400mm, h=600mm
    column_section = RectSection(b=400, h=600)
    column_section.print_summary()