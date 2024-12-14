class Context():

    level: int = 0 # number of nested braces {}
    sub: int = 0 # number of nested underscores _
    super: int = 0 # number of nested carets ^

    def __init__(self, level: int = 0, sub: int = 0, super: int = 0):
        self.level = level
        self.sub = sub
        self.super = super

    def __str__(self) -> str:
        return f'level={self.level} sub={self.sub} super={self.super}'
    