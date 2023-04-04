class Test(unittest.TestCase):

  def test_internals_of_list_4_5_10_2_3_returns_list_5_10_2(self):
    self.assertEquals(internals([4, 5, 10, 2, 3]), [5, 10, 2])
    
  def test_internals_of_list_4_5_10_2_3_9_returns_list_5_10_2_9(self):
    self.assertEquals(internals([4, 5, 10, 2, 3, 9]), [5, 10, 2, 3])
    
  def test_internals_of_list_4_5_10_returns_list_5(self):
    self.assertEquals(internals([4, 5, 10]), [5])
        
  def test_internals_of_list_40_20_returns_list_vacia(self):
    self.assertEquals(internals([40, 20]), [])
    
  def test_extremes_of_list_4_5_10_2_3_returns_list_4_3(self):
    self.assertEquals(extremes([4, 5, 10, 2, 3]), [4, 3])
    
  def test_extremes_of_list_4_3_returns_list_4_3(self):
    self.assertEquals(extremes([4, 3]), [4, 3])
    
  def test_extremes_of_list_1_2_5_returns_list_1_5(self):
    self.assertEquals(extremes([1, 2, 5]), [1, 5])      
