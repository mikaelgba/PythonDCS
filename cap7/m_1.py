from nose.tools import assert_equal

class UniqueChars(object):

    def has_unique_chars(self, string):

        if(string is None): return False

        list_aux = []
        for letra in string:
            
            if(letra in list_aux): return False
            list_aux.append(letra)
            
        return True

#parte já definida pelo test              
class TestUniqueChars(object):

    def test_unique_chars(self, func):
        assert_equal(func(None), False)
        assert_equal(func(''), True)
        assert_equal(func('foo'), False)
        assert_equal(func('bar'), True)
        print('Sua solução foi executada com sucesso! Parabéns!')

def main():
    
    test = TestUniqueChars()
    try:
        
        unique_chars = UniqueChars()
        test.test_unique_chars(unique_chars.has_unique_chars)
        
    except(NameError): pass

if __name__ == '__main__':
    main()
