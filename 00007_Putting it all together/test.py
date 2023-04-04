class Test(unittest.TestCase):

  def test_join_strings_super_califragilistic_expialidocious_returns_supercalifragilisticexpialidocious(self):
    self.assertEqual(join_strings(["super", "califragilistic", "expialidocious"]), "supercalifragilisticexpialidocious")
    
  def test_join_strings_empty_list_returns_empty_string(self):
    self.assertEqual(join_strings([]), "")
      
  def test_join_strings_butter_fly_returns_butterfly(self):
    self.assertEqual(join_strings(["butter", "fly"]), "butterfly")

  def test_join_strings_what_s_it_returns_whatsit(self):
    self.assertEqual(join_strings(["what",  "s", "it"]), "whatsit")
