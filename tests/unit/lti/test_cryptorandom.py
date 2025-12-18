import base64

from service_layer.crypto.cryptorandom import CryptoRandom

# pytest tests\unit\lti\test_cryptorandom.py --cov


def test_getRandom():
    """[HASKI-REQ-0028] Ensures LTI state/nonce seeds use unpredictable RNGs (GH-19)."""
    # Act
    result = CryptoRandom.get_random()
    result2 = CryptoRandom.get_random()
    # Assert
    assert result != result2


def test_getrandbits():
    """[HASKI-REQ-0028] Test the getrandbits method."""
    # Arrange
    length = 32
    # Act
    result = CryptoRandom.getrandbits(length)
    result2 = CryptoRandom.getrandbits(length)
    # Assert
    assert result != result2


def test_getrandbytes():
    """[HASKI-REQ-0028] Test the getrandombytes method."""
    # Arrange
    length = 32
    # Act
    result = CryptoRandom.getrandbytes(length)
    result2 = CryptoRandom.getrandbytes(length)
    # Assert
    assert len(result) == length
    assert result != result2

    # Arrange
    length = 64
    # Act
    result = CryptoRandom.getrandbytes(length)
    # Assert
    assert len(result) == length


def test_createuniqueid():
    """[HASKI-REQ-0028] Test the createuniqueid method."""
    # Arrange
    length = 32
    # Act
    result = CryptoRandom.createuniqueid(length)
    result2 = CryptoRandom.createuniqueid(length)
    # Assert
    assert len(result) == length
    assert result != result2

    # Arrange
    length = 64
    # Act
    result = CryptoRandom.createuniqueid(length)
    # Assert
    assert len(result) == length


def test_createuniqueidbase64():
    """[HASKI-REQ-0028] Test the createuniqueidbase64"""
    # Arrange
    length = 32
    # Act
    result = CryptoRandom.createuniqueidbase64(length)
    result2 = CryptoRandom.createuniqueidbase64(length)
    # Assert
    assert len(base64.b64decode(bytes(result, "utf-8"))) == length
    assert result != result2

    # Arrange
    length = 64
    # Act
    result = CryptoRandom.createuniqueidbase64(length)
    # Assert
    assert len(base64.b64decode(bytes(result, "utf-8"))) == length


def test_getrandomstring():
    """[HASKI-REQ-0028] Test the getrandomstring method."""
    # Arrange
    length = 32
    # Act
    result = CryptoRandom.getrandomstring(length)
    result2 = CryptoRandom.getrandomstring(length)
    # Assert
    assert len(result) == length
    assert result != result2

    # Arrange
    length = 64
    # Act
    result = CryptoRandom.getrandomstring(length)
    # Assert
    assert len(result) == length


def test_getrandomstringbase64():
    """[HASKI-REQ-0028] Test the getrandomstringbase64 method."""
    # Arrange
    length = 32
    # Act
    result = CryptoRandom.getrandomstringbase64(length)
    result2 = CryptoRandom.getrandomstringbase64(length)
    # Assert

    # base64.b64decode(result)
    assert len(base64.b64decode(bytes(result, "utf-8"))) == length
    assert result != result2

    # Arrange
    length = 64
    # Act
    result = CryptoRandom.getrandomstringbase64(length)
    # Assert
    assert len(base64.b64decode(bytes(result, "utf-8"))) == length
