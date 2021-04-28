import psutil


def get_module_text():
    # Must have in all module
    memory = psutil.virtual_memory()
    memory_used = memory.total - memory.available

    return f"MEM: {int(memory_used / 1024 // 1024)}"


if __name__ == '__main__':
    print(get_module_text())
