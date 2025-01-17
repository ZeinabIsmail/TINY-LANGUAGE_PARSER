#from pip._vendor.distlib.compat import raw_input
#def divide_input_into_tokens(input):
   #for i in n:
      #if (i.isdigit()):
        #print("number")

      #elif(i.isalpha()):
        #print("identefire")
      #else:
        #print("assign")
#n =raw_input("enter the syantx: ")
#divide_input_into_tokens(n)///
import enum
import sys


class Lexer:
    def __init__(self, input):
        self.source = input + '\n'  # Source code to lex as a string. Append a newline to simplify lexing/parsing the last token/statement.
        self.curChar = ''  # Current character in the string.
        self.curPos = -1  # Current position in the string.

        self.nextChar()
        pass

    # Process the next character.
    def nextChar(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0'  # EOF
        else:
            self.curChar = self.source[self.curPos]
        return self.curChar
        pass

    # Return the lookahead character.
    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos + 1]
        pass

    #nextChar and peek are helper functions for looking at the next character Invalid token found, print error message and exit.
   # def abort(self, message,):
        #print("Lexing error. " + message)
        #pass
        #self.nextChar()

    #def currentcharacter(self):
        #return self.curChar
        #pass
    #def getthetext(self):
        #thetext = []
        #thetext.append(self.curChar)
        #return thetext
    # Skip whitespace except newlines, which we will use to indicate the end of a statement.
    def skipWhitespace(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r':
            self.nextChar()
            pass

    # Skip comments in the code.
    def skipComment(self):

        if self.curChar == '{':
            while self.curChar != "\n":
                self.nextChar()
        pass

    # Return the next token.
    #It will be called each time the compiler is ready for the next token and it will do the work of classifying tokens
    def getToken(self):
            self.skipWhitespace()
            self.skipComment()
            token = None
            #thetext=[]
            #thetext.append(self.curChar)

            # Check the first character of this token to see if we can decide what it is.
            # If it is a multiple character operator (e.g., !=), number, identifier, or keyword then we will process the rest.
            if self.curChar == '+':
                token = Token(self.curChar, TokenType.PLUS)
            elif self.curChar == '-':
                token = Token(self.curChar, TokenType.MINUS)
            elif self.curChar == '*':
                token = Token(self.curChar, TokenType.MULT)
            elif self.curChar == '/':
                token = Token(self.curChar, TokenType.DIV)
            elif self.curChar == ';':
                token = Token(self.curChar, TokenType.SEMICOLON)
            elif self.curChar == '\n':
                token = Token(self.curChar, TokenType.NEWLINE)
            elif self.curChar == '\0':
                token = Token('', TokenType.EOF)
            elif self.curChar == ')':
                token = Token(self.curChar, TokenType.CLOSEDBRACKET)
            elif self.curChar == '(':
                token = Token(self.curChar, TokenType.OPENBRACKET)
            elif self.curChar == '=':
                token = Token(self.curChar, TokenType.EQUAL)
            elif self.curChar == ':':
                # Check whether this token is = or ==
                if self.peek() == '=':
                    lastChar = self.curChar
                    self.nextChar()
                    #token = Token(self.curChar, TokenType.ASSIGN)
                    token = Token(lastChar + self.curChar, TokenType.ASSIGN)
                #else:

            elif self.curChar == '>':
                # Check whether this is token is > or >=
                if self.peek() == '=':
                    lastChar = self.curChar
                    self.nextChar()
                    token = Token(lastChar + self.curChar, TokenType.GTEQ)
                else:
                    token = Token(self.curChar, TokenType.GT)
            elif self.curChar == '<':
                # Check whether this is token is < or <=
                if self.peek() == '=':
                    lastChar = self.curChar
                    self.nextChar()
                    token = Token(lastChar + self.curChar, TokenType.LTEQ)
                else:
                    token = Token(self.curChar, TokenType.LESSTHAN)
            elif self.curChar == '!':
                if self.peek() == '=':
                    lastChar = self.curChar
                    self.nextChar()
                    token = Token(lastChar + self.curChar, TokenType.NOTEQ)
                else:
                    self.abort("Expected !=, got !" + self.peek())
            elif self.curChar == '\"':
                # Get characters between quotations.
                self.nextChar()
                startPos = self.curPos

                while self.curChar != '\"':
                    # Don't allow special characters in the string. No escape characters, newlines, tabs, or %.
                    # We will be using C's printf on this string.
                    if self.curChar == '\r' or self.curChar == '\n' or self.curChar == '\t' or self.curChar == '\\' or self.curChar == '%':
                        self.abort("Illegal character in string.")
                    self.nextChar()

                tokText = self.source[startPos: self.curPos]  # Get the substring.
                token = Token(tokText, TokenType.STRING)
            elif self.curChar.isdigit():
                # Leading character is a digit, so this must be a number.
                # Get all consecutive digits and decimal if there is one.
                startPos = self.curPos
                while self.peek().isdigit():
                    self.nextChar()
                if self.peek() == '.':  # Decimal!
                    self.nextChar()

                    # Must have at least one digit after decimal.
                    if not self.peek().isdigit():
                        # Error!
                        self.abort("Illegal character in number.")
                    while self.peek().isdigit():
                        self.nextChar()

                tokText = self.source[startPos: self.curPos + 1]  # Get the substring.
                token = Token(tokText, TokenType.NUMBER)
            elif self.curChar.isalpha():
                # Leading character is a letter, so this must be an identifier or a keyword.
                # Get all consecutive alpha numeric characters.
                startPos = self.curPos
                while self.peek().isalnum():
                    self.nextChar()

                # Check if the token is in the list of keywords.
                tokText = self.source[startPos: self.curPos + 1]  # Get the substring.

                keyword = Token.checkIfKeyword(tokText)
                if keyword == None:  # Identifier
                    token = Token(tokText, TokenType.IDENTIFIER)
                else:  # Keyword
                    token = Token(tokText, keyword)
            else:
                # Unknown token!
                print("Unknown token: " + self.curChar)
                token = Token(self.curChar, TokenType.UNKNOWNTYPE)
                pass

            #thetext = self.curChar

            self.nextChar()
            return token



class Token:
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText   # The token's actual text. Used for identifiers, strings, and numbers.
        self.kind = tokenKind   # The TokenType that this token is classified as.
        #print(tokenText)
    @staticmethod
    def checkIfKeyword(tokenText):
        for kind in TokenType:
            # Relies on all keyword enum values being 1XX.
            if kind.name == tokenText and kind.value >= 100 and kind.value < 200:
                return kind

        return None
    #def actualtext(self):
        #tokentext=self.text
        #return tokentext

class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENTIFIER = 2
    STRING = 3
    # Keywords.
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF= 106
    THEN = 107
    END= 108
    WHILE = 109
    REPEAT = 110
    UNTIL = 111
    READ=112
    WRITE=113
    UNKNOWNTYPE=114

    #Operators.
    SEMICOLON =201
    ASSIGN = 202
    PLUS = 203
    MINUS = 204
    MULT = 205
    DIV = 206
    EQEQ = 207
    NOTEQ = 208
    LESSTHAN = 209
    LTEQ = 210
    OPENBRACKET=211
    CLOSEDBRACKET=212
    EQUAL=213
