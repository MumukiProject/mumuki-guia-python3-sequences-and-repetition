class Test(unittest.TestCase):

  def test_juntar_super_califragilistico_espialidoso_devuelve_supercalifragilisticoespialidoso(self):
    self.assertEqual(juntar("", ["super", "califragilistico", "espialidoso"]), "supercalifragilisticoespialidoso")
    
  def test_juntar_lista_vacia_devuelve_string_vacio(self):
    self.assertEqual(juntar("", []), "")
    
  
  def test_juntar_cuatri_motor_devuelve_cuatrimotor(self):
    self.assertEqual(juntar("", ["cuatri", "motor"]), "cuatrimotor")
    
  def test_juntar_hola_mundo_con_un_espacio_devuelve_hola_mundo(self):
    self.assertEqual(juntar(" ", ["hola", "mundo"]), "hola mundo")
    
  
    
    