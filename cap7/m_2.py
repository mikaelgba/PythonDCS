from nose.tools import assert_equal, assert_raises
import math

class PrimeGenerator(object):

    def generate_primes(self, max_num):

        if(max_num is None): raise TypeError("Erro seu Corno")

        lista_primos = []
        for i in range(max_num): lista_primos.append(True)
        lista_primos[0], lista_primos[1] = False,False
        primo = 2
        
        while(primo <= math.sqrt(max_num)):
            
            self._cross_off(lista_primos, primo)
            primo = self._next_prime(lista_primos, primo)
            
        return lista_primos

    def _cross_off(self, lista_entrada, primo):
        
        for i in range((primo * primo), len(lista_entrada), primo):
            lista_entrada[i] = False
            
    def _next_prime(self, lista_entrada, primo):
        
        next = primo + 1
        while(next < len(lista_entrada) and not lista_entrada[next]):
            next += 1

        return next

class TestMath(object):

    def test_generate_primes(self):
        prime_generator = PrimeGenerator()
        assert_raises(TypeError, prime_generator.generate_primes, None)
        assert_raises(TypeError, prime_generator.generate_primes, 98.6)
        assert_equal(prime_generator.generate_primes(20), [False, False, True, 
                                                           True, False, True, 
                                                           False, True, False, 
                                                           False, False, True, 
                                                           False, True, False, 
                                                           False, False, True, 
                                                           False, True])
        print('Sua solução foi executada com sucesso! Parabéns!')

def main():
    test = TestMath()
    test.test_generate_primes()


if __name__ == '__main__':
    main()
