import unittest
from dominio import Campania
from analisis import separar_datos

class TestProgramaMarketing(unittest.TestCase):

    def test_1_caso_normal(self):
        """Prueba que una campaña con datos perfectos sea válida."""
        # Preparamos una fila simulada
        fila_correcta = {
            'campaign_id': 'camp-123',
            'campaign_type': 'Social Media',
            'budget': '1500.50',
            'conversions': '50',
            'roi': '2.5'
        }
        campania = Campania(fila_correcta)
        
        # Verificamos que es_valida() devuelva True sin lanzar errores
        self.assertTrue(campania.es_valida())
        self.assertEqual(campania.budget, 1500.50)

    def test_2_entrada_invalida(self):
        """Prueba que una campaña con presupuesto negativo lance un ValueError."""
        # Preparamos una fila con un error a propósito (budget negativo)
        fila_con_error = {
            'campaign_id': 'camp-456',
            'campaign_type': 'Email',
            'budget': '-500', # ERROR ACÁ
            'conversions': '10',
            'roi': '1.2'
        }
        campania_mala = Campania(fila_con_error)
        
        # Verificamos que el programa atrape y lance el ValueError
        with self.assertRaises(ValueError):
            campania_mala.es_valida()

    def test_3_propiedad_del_resultado(self):
        """Prueba que separar_datos conserve la cantidad total de registros."""
        # Preparamos una lista con 2 campañas (una buena y una mala)
        datos_mezclados = [
            {'campaign_id': 'ok-1', 'budget': '100', 'conversions': '5', 'roi': '1'},
            {'campaign_id': 'error-2', 'budget': '-50', 'conversions': '2', 'roi': '0'}
        ]
        
        buenas, malas = separar_datos(datos_mezclados)
        
        # Comprobamos que separó 1 para cada lado
        self.assertEqual(len(buenas), 1)
        self.assertEqual(len(malas), 1)
        # buenas + malas = total original
        self.assertEqual(len(buenas) + len(malas), len(datos_mezclados))

if __name__ == '__main__':
    unittest.main()