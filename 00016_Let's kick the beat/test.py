class Test(unittest.TestCase):

  def test_how_many_times_trained_enough_with_35_40_32_60_equals_4(self):
    self.assertEquals(how_many_times_trained_enough([35, 40, 32, 60]), 4)

  def test_how_many_times_trained_enough_with_15_45_90_0_equals_2(self):
    self.assertEquals(how_many_times_trained_enough([15, 45, 90, 0]), 2)

