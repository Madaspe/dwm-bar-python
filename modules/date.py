from time import strftime


def get_module_text():
    # Must have in all module
    date = strftime("%A, %d. %B %Y %I:%M%p")
    return date


if __name__ == '__main__':
    # Test
    print(get_module_text())