class FileManager:
    def __init__(self, f_name, mode):
        self.f_name = f_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.f_name, self.mode)
            return self.file
        except FileNotFoundError:
            print("Error")
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with FileManager("file.txt", 'r') as f:
    if f:
        print(f.read())