import unittest
from section import RectSection


class TestRectSection(unittest.TestCase):
    def test_basic_properties(self):
        # 验算 200 × 400 的矩形
        sec = RectSection(200, 400)

        # 面积测试：200 * 400 = 80000
        self.assertAlmostEqual(sec.area(), 80000.0)

        # 强轴惯性矩测试：I_x = b * h^3 / 12 = 200 * 400^3 / 12 = 1,066,666,666.67
        I_x, I_y = sec.moment_of_inertia()
        self.assertAlmostEqual(I_x, 200 * 400 ** 3 / 12)


if __name__ == "__main__":
    unittest.main()