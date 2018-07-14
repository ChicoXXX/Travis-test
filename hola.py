def hola(nombre):
  return ('hola %s' %nombre)
#  print ('bye')

#hola('Chico')
def test_answer():
  assert hola('Chico') == "hola Chico"
