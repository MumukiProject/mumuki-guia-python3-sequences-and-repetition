class Test(unittest.TestCase):

  def test_join_strings_super_califragilistico_espialidoso_devuelve_supercalifragilisticoespialidoso(self):
    self.assertEqual(join_strings("", ["super", "califragilistico", "espialidoso"]), "supercalifragilisticoespialidoso")
    
  
  def test_join_strings_cuatri_motor_devuelve_cuatrimotor(self):
    self.assertEqual(join_strings("", ["cuatri", "motor"]), "cuatrimotor")
    
  def test_join_strings_hola_mundo_con_un_espacio_devuelve_hola_mundo(self):
    self.assertEqual(join_strings(" ", ["hola", "mundo"]), "hola mundo")
    
      
  def test_join_strings_hola_mundo_con_una_coma_devuelve_hola_coma_mundo(self):
    self.assertEqual(join_strings(",", ["hola", "mundo"]), "hola,mundo")
    
    
  
    
    