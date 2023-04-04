class Test(unittest.TestCase):

  def test_join_strings_with_empty_string_and_super_califragilistic_expialidocious_returns_supercalifragilisticexpialidocious(self):
    self.assertEqual(join_strings("", ["super", "califragilistic", "expialidocious"]), "supercalifragilisticexpialidocious")
    
  def test_join_strings_with_empty_string_and_butter_fly_returns_butterfly(self):
    self.assertEqual(join_strings("", ["butter", "fly"]), "butterfly")

  def test_join_strings_with_empty_string_and_what_s_it_returns_whatsit(self):
    self.assertEqual(join_strings("", ["what",  "s", "it"]), "whatsit")

  def test_join_strings_with_comma_and_hello_world_returns_hello_comma_world(self):
    self.assertEqual(join_strings(",", ["hello",  "world"]), "hello,world")

  def test_first_example(self):
    self.assertEqual(join_strings(" ", ["Nicki", "Nicole"]), "Nicki Nicole")

  def test_second_example(self):
    self.assertEqual(join_strings(",", ["Esposito", "Lali"]), "Esposito,Lali")

  def test_third_example(self):
    self.assertEqual(join_strings("", ["W", "O", "S"]), "WOS")
