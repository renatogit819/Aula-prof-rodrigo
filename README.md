# Aula-prof-rodrigo
Atividade-Avaliativa-QA
📄 Estrutura do README.md (Obrigatória)
1. Apresentação
Nome completo
Renato Francelino Da Silva

Curso e semestre
GTI 5NA 5- SEMESTRE 

Um parágrafo com uma breve descrição da sua experiência com a disciplina
Muito boa a disciplina, gostando muito do apeendizado!

2. O que é Quality Assurance (QA)?
Explique com suas palavras o conceito de QA e sua importância no desenvolvimento de software
Uma garantia de qualidade, onde através de ferramentas sao feitos testes, para empresas efetuarem suas atividades com acertividade.

Use uma linguagem simples e acessível, como se estivesse explicando para alguém leigo
Um Perito em qaulidade acertiva



3. Conceitos Aprendidos Durante o Semestre
Escreva um parágrafo explicando o que você aprendeu sobre:
Qualidade em software e cultura de qualidade
Testam o aplicativo em diferentes dispositivos para garantir que funcione bem em todos.

Tipos de testes (unitário, integração, sistema, aceitação, regressão e exploratório)


Planejamento de testes (critérios de aceitação, planos e casos de teste)


Ferramentas de testes utilizadas durante o semestre (Colab, GitHub, etc.)


Automação de testes e integração com CI/CD


Monitoramento e controle de qualidade (uso de métricas, rastreamento de bugs, observabilidade)


4. Ferramentas e Sites Utilizados
Liste todos os sites e ferramentas que você usou durante o curso, por exemplo:

https://reqres.in/
sim 

https://colab.research.google.com/ 
sim

https://github.com/
sim

https://uptimerobot.com/
sim

(outros que desejar incluir)


5. Explicação dos Testes Entregues
Para cada um dos três testes obrigatórios entregues na pasta /testes, responda:
Nome do teste


Objetivo


Qual biblioteca Python foi utilizada
Google Colab

Qual resultado esperado
100%

Link para o arquivo (ex: testes/teste_01.py)
https://colab.research.google.com/drive/1u4nEp5hNE0ZixcMSjN9BpzPk4cCaSjQW?usp=sharing
teste_01 class Calculadora:
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


teste_02 

# Para executar os testes no Colab
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)



Ran 5 tests in 0.011s
Exemplo de formatação:

✅ Teste 01 – Verificação de status da API ReqRes
Biblioteca: Requests


Objetivo: Verificar se o endpoint retorna status HTTP 200


Resultado esperado: Teste passa com sucesso se o status for 200


Arquivo: testes/teste_01.py
https://colab.research.google.com/drive/1u4nEp5hNE0ZixcMSjN9BpzPk4cCaSjQW?usp=sharing


6. Conclusão Final
Escreva um parágrafo com sua reflexão pessoal, respondendo:
O que você aprendeu de mais importante?
TUDO! Vi que o aprendizado de QA é muito importante para q uma(site ou empresa) funcione adequadamente.

Como você enxerga a área de QA no seu futuro profissional?
Pretendo me especializar ainda mais na área para seguir carreira.

Qual ferramenta ou tema mais chamou sua atenção e por quê?
COLAB! Pela facilidade da ferramenta e sempre proporcionar correção em caso de código incorreto


🐍 Requisitos dos Testes Python
Você deve entregar no mínimo três testes desenvolvidos em Python, com as seguintes características:
Estar dentro da pasta /testes


Ter sido feito com base nas atividades vistas em aula


Utilizar bibliotecas como requests, unittest, pytest, entre outras básicas


Estar comentado e com lógica compreensível
