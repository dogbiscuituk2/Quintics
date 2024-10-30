"""

gtokens = []

def gaccept(token):
    gtokens.pop(0)

def gtokenize(expression):
    token_pattern = r"\\\w+|\{|\}|[^\\\{\}]"
    gtokens.clear()
    for token in re.findall(token_pattern, expression):
        gtokens.append(token)

def gtouch(token):
    # Process an element of the MathTex
    # Point to the next MathTex element
    pass

def gparse_string(s):
    gtokenize(s)
    gparse_expression()

def gparse_expression():
    print('begin expression')
    while gtokens:
        token = gtokens.pop(0)
        match token[0]:
            case '{':
                gparse_expression()
            case '}':
                print('end expression')
                return
            case '\\':
                gparse_function(token)
            case _:
                pass
    print('end expression')

def gparse_block():
    print('begin block')
    gaccept('{')
    gparse_expression()
    print('end block')

def gparse_function(token):
    print('begin function')
    match(token):
        case '\\frac':
            gparse_block()
            print('Intertext!!!')
            gparse_block()
        case _:
            pass
    print('end function')

s = r'x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}'
gtokenize(s)
print(gtokens)
gparse_expression()

"""

"""

    def parse(self, mathTex: MathTex):

        def parse_atom(p: int) -> int:
            print(f" --> atom, p={p}")
            q = p
            while True:
                q += 1
                if q >= n:
                    break
                match s[q]:
                    case '{':
                        self.Level += 1
                    case '}':
                        if self.Level > 0:
                            self.Level -= 1
                        else:
                            break
            atom = s[p+1:q]
            parse_text(p + 1)
            p = q
            print(f"<--  atom, p={p}")
            return p

        def parse_char(p: int) -> int:
            print(f"     char, p={p}")
            c = s[p]
            match c:
                case '_':
                    pass
                case '^':
                    pass
            p += 1
            #print(f"<--  char, p={p}")
            return p

        def parse_func(p: int) -> int:
            print(f" --> func, p={p}")
            p += 1
            q = p
            while q < n and s[q].isalpha():
                q += 1
            word = s[p:q]
            p = q
            match word:
                case 'frac':
                    p = parse_atom(p);
                    p = parse_atom(p);
            print(f"<--  func, p={p}")
            return p

        def parse_text(p: int) -> int:
            print(f" --> text, p={p}")
            while (p < len(s)) and (s[p] != '}'):
                c = s[p]
                match c:
                    case '\\':
                        p = parse_func(p)
                    case '{':
                        level += 1
                    case '}':
                        level -= 1
                    case _:
                        p = parse_char(p)
            print(f"<--  string, p={p}")
            return p

        print("IN parse")
        s = mathTex.tex_string
        n = len(s)
        parse_text(0)

"""