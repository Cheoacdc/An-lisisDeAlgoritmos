class QuitException(Exception):
    def __init__(self, message: str = 'User exited current menu'):
        super().__init__(message)
        self.message = message

    def __repr__(self):
        return f'<QuitException: {self.message}>'
