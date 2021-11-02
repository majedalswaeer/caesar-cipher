from caesar import encrypt,decrypt,crack

def test_one_encrypt():
    #Arrange
    text='It was the best of times it was the worst of times'
    expected='Lw zdv wkh ehvw ri wlphv lw zdv wkh zruvw ri wlphv'

    #Act
    actual=encrypt(text,3)

    #Assert
    assert actual==expected


def test_two_encrypt():
    #Arrange
    text='It was the best of times it was the worst of times'
    expected='Lw zdv wkh ehvw ri wlphv lw zdv wkh zruvw ri wlphv'

    #Act
    actual=encrypt(text,29)

    #Assert
    assert actual==expected

def test_three_encrypt():
    #Arrange
    text='1234'
    expected='4567'

    #Act
    actual=encrypt(text,3)

    #Assert
    assert actual==expected

def test_one_decrypt():
    #Arrange
    text='4567'
    expected='1234'

    #Act
    actual=decrypt(text,3)

    #Assert
    assert actual==expected

def test_two_decrypt():
    #Arrange
    text='bpyts'
    expected='majed'

    #Act
    actual=decrypt(text,15)

    #Assert
    assert actual==expected

def test_one_crack():
    #Arrange
    text='Sd gkc dro locd yp dswoc sd gkc dro gybcd yp dswoc'
    expected='It was the best of times it was the worst of times, percentage:100.0%'

    #Act
    actual=crack(text)

    #Assert
    assert actual==expected