# Introduction to Python

class Intro:
    def __init__(self) -> None:
        # Numbers
        self.int_32 = 0 # integer
        self.int_64 = 0.0 # float
        self.int_Cx = 0j # complex
        
        # Strings
        self.single_quote = 'Hello World'
        self.double_quote = "ain't working?"
        self.str_esc_1 = '"YES"'
        self.str_esc_2 = "\"YES\" with escape" # escape sequence
        self.str_newln = "\n" # new line escape sequence
        self.str_file = r'C:\some\path' # raw strings
        self.str_multiline = """\
            Something was wrong.... hmmmm
            
            - exit          exit app
            - repair        repair app
            """ # multiline string
        
    
    def print_intro(self):
        # Prints hello python
        print("hello python")
        
    def compute_nums(self, x, y, opr) -> float: 
        match opr:
            case "+":
                return x + y
            case "-":
                return x - y
            case "/":
                return x / y # division, returns float
            case "*": 
                return x * y
            case "**":
                return x ** y # to power, returns float
            case "//":
                return x // y # floor division, returns int
            case "%":
                return x % y # remainder, returns int
    
    def basic_strings(self) -> None:
        pass