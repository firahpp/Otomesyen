# Function / Method

def panggil():
    '''
    method/function tanpa argument/parameter
    '''
    print('oi mau kemana bang?')
    print('aku disini menunggumu.')

def panggil2(nama):
    '''
    method/function dengan argument/parameter
    '''
    print(f'oi {nama} mau kemana bang?')
    print('aku disini menunggumu.')  
    
# panggil2('jajang')  

def tambah2an(a,b):
    c = a + b
    return c
    
# hasil = tambah2an(3,5)

# z = hasil + 10
# print(z)

def kenalan(nama, pekerjaan):    # positional argument
    print(f'halo nama saya {nama}, pekerjaan saya {pekerjaan}')
    
# kenalan('Uno', 'QA')

def kenalan2(nama, *pekerjaan):    # arbitary argument
    if pekerjaan == ():
        kerjaan = 'tidak ada'
    elif pekerjaan != ():
        kerjaan = pekerjaan[0]
    print(f'halo nama saya {nama}, pekerjaan saya {kerjaan}')
    
# kenalan2('jajang','direktur')

def kenalan3(nama='uno',pekerjaan='qa'):
    # print(f'halo nama saya {nama}, pekerjaan saya {pekerjaan}')
    
    return f'halo nama saya {nama}, pekerjaan saya {pekerjaan}'
    
hasil = kenalan3(pekerjaan='direktur')
print(hasil + ' lalala yeyeye')

