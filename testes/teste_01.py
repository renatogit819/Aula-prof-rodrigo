class Calculadora:
    def somar(self, a, b):
        return a + b
    
    def subtrair(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b
    
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()
    
    def test_somar(self):
        self.assertEqual(self.calc.somar(2, 3), 5)
        self.assertEqual(self.calc.somar(-1, 1), 0)
        self.assertEqual(self.calc.somar(0, 0), 0)
    
    def test_subtrair(self):
        self.assertEqual(self.calc.subtrair(5, 3), 2)
        self.assertEqual(self.calc.subtrair(-1, -1), 0)
        self.assertEqual(self.calc.subtrair(0, 0), 0)
    
    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(3, 4), 12)
        self.assertEqual(self.calc.multiplicar(-1, 5), -5)
        self.assertEqual(self.calc.multiplicar(0, 10), 0)
    
    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertEqual(self.calc.dividir(9, 3), 3)
        self.assertAlmostEqual(self.calc.dividir(1, 3), 0.333333, places=6)
        
    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

# Para executar os testes no Colab
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)



Ran 5 tests in 0.011s
