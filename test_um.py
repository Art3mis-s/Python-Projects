from um import count

def main():
    test_upper_lower_cases()
    test_sentence_with_um()
    test_space_surroundings()


def test_upper_lower_cases():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_sentence_with_um():
    assert count("Yummi") == 0


def test_space_surroundings():
    assert count("Hello um world") == 1
    assert count("um?") == 1


if __name__ == "__main__":
    main()