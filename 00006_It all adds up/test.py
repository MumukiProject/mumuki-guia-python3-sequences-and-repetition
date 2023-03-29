class Test(unittest.TestCase):

  def test_product_of_10_2_3_equals_60(self):
    self.assertEquals(product([10, 2, 3]), 60)

  def test_product_of_3_3_2_4_equals_72(self):
    self.assertEquals(product([3, 3, 2, 4]), 72)

  def test_product_of_8_equals_8(self):
    self.assertEquals(product([8]), 8)

  def test_product_of_1_a_9_equals_362880(self):
    self.assertEquals(product(range(1, 10)), 362880)

  def test_product_of_6_equals_6(self):
    self.assertEquals(product([6]), 6)

  def test_product_of_empty_list_equals_1(self):
    self.assertEquals(product([]), 1)