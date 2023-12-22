#run : python -m pytest automation/unitest.py #

def test_tambahan():
    x = 1
    y = 2
    z = x+y
    
    assert z == 3
    
def test_perkalian():
    a = 20
    b = 10
    c = a*b
    
    assert c == 200
    
def perkalian(d,f):
    g = d*f
    return g

def test_perkalian2():
    hasil = perkalian(2,4) 
    
    assert hasil == 8