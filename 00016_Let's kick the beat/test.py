class Test(unittest.TestCase):

  def test_how_many_times_trained_enough_with_35_40_32_60_equals_4(self):
    self.assertEquals(how_many_times_trained_enough([35, 40, 32, 60]), 4)

  def test_how_many_times_trained_enough_with_15_45_90_0_equals_2(self):
    self.assertEquals(how_many_times_trained_enough([15, 45, 90, 0]), 2)

  def test_how_many_times_trained_enough_with_15_45_90_equals_1(self):
    self.assertEquals(how_many_times_trained_enough([15, 45, 90]), 1)
    
  def test_how_many_times_trained_enough_with_42_45_43_equals_1(self):
    self.assertEquals(how_many_times_trained_enough([42, 45, 43]), 3)    

