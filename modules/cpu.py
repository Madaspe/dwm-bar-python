import psutil


def get_module_text():
    # Must have in all module
    return f"CPU: {psutil.cpu_percent()}"


if __name__ == '__main__':
    print(get_module_text())
