def test_tambahtambahan():
    x = 1
    y = 2
    z = x+y
    
    assert z == 3
    
def test_pengurangan():
    x = 2
    y = 3
    
    assert x-y == -1
    
def perkalian(x, y):
     z = x * y
     return z

def test_perkalian():
    hasil = perkalian(2,4)
    
    assert hasil == 7