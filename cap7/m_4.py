from nose.tools import assert_equal, assert_raises

class SelectionSort(object):

    def sort(self, data):

        if(data is None): raise TypeError("Erro seu Corno")
        
        if(len(data) < 2): return data
        
        else:
            
            for i in range(len(data)-1):

                menor = i
                for j in range(i + 1, len(data)):

                    if(data[j] < data[menor]):
                        menor = j

                if(data[menor] < data[i]):
                    data[i] = data[menor]
                    data[menor] = data[i]
            
        return data

class TestSelectionSort(object):

    def test_selection_sort(self, func):
        
        print('None input')
        assert_raises(TypeError, func, None)

        print('Input vazio')
        assert_equal(func([]), [])

        print('Um elemento')
        assert_equal(func([5]), [5])

        print('Dois ou mais elementos')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -10]
        assert_equal(func(data), sorted(data))

        print('Sua solução foi executada com sucesso! Parabéns!')

def main():
    
    test = TestSelectionSort()
    try:
        selection_sort = SelectionSort()
        test.test_selection_sort(selection_sort.sort)
        
    except NameError: pass

if __name__ == '__main__':
    main()
