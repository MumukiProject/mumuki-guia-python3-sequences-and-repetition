class Test(unittest.TestCase):

  def test_in_a_streak_with_35_40_32_60_equals_True(self):
    self.assertTrue(in_a_streak([35, 40, 32, 60]))
    
  def test_in_a_streak_with_15_45_90_0_equals_False(self):
    self.assertFalse(in_a_streak([15, 45, 90, 0]))
    