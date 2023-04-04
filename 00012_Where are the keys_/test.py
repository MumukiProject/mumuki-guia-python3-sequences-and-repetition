class Test(unittest.TestCase):

  def test_keys_are_in_first_place(self):
    self.assertEquals(where_are_the_keys("🔑🔥👓"), 1, "where_are_the_keys('🔑🔥👓') should be 1")
    
  def test_keys_are_in_second_place(self):
    self.assertEquals(where_are_the_keys("👓🔑🔥"), 2, "where_are_the_keys('👓🔑🔥') should be 2")

  def test_keys_are_in_third_place(self):
    self.assertEquals(where_are_the_keys("🍪🧀🔑"), 3, "where_are_the_keys('🍪🧀🔑') should be 3")

  def test_keys_are_in_fourth_place_with_duplicated_emojis(self):
    self.assertEquals(where_are_the_keys("🍪🍪🍪🔑"), 4, "where_are_the_keys('🍪🍪🍪🔑') should be 4")        