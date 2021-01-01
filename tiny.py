import json
import pickle
from parserfinal import *


from lex import *


def nonempty_lines():
    file = open("test.txt", "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()
    return line_count

def get_input_from_user(input):
    final_output_token = []
    final_output_value = []
    result = []
    line_count = nonempty_lines()
    lexer = Lexer(input)
    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        final_output_token.append(token.text.lower())
        convert_to_str = token.kind
        convert2 = convert_to_str.name
        token = lexer.getToken()
        final_output_value.append(convert2.lower())
    result.append(final_output_token)
    result.append(final_output_value)
    return result

def main():
    final_output_token1 = []
    final_output_value1 = []
    file = open("test.txt", 'r')
    line_count = nonempty_lines()
    for line in range(0,line_count):
            input = file.readline()
            get_input_from_user(input.upper())


    for i in final_output_value:
        if i != 'newline':
            final_output_token1.append(i)
    for i in range (len(final_output_token1)):
        if final_output_token1[i] == 'semicolon' :
            final_output_token1[i]=';'
        if final_output_token1[i] == 'lessthan' :
            final_output_token1[i] = '<'
        if final_output_token1[i] == 'greaterthan' :
            final_output_token1[i]='>'
        if final_output_token1[i] == 'assign' :
            final_output_token1[i]=':='
        if final_output_token1[i] == 'plus' :
            final_output_token1[i]='+'
        if final_output_token1[i] == 'minus' :
            final_output_token1[i] = '-'
        if final_output_token1[i] == 'mult' :
            final_output_token1[i]='*'
        if final_output_token1[i] == 'div':
            final_output_token1[i]='/'
        if final_output_token1[i] == 'equal':
            final_output_token1[i]='='



    for i in final_output_token:
        if i != '\n':
            final_output_value1.append(i)
    print(final_output_token1)
    print(final_output_value1)
    parse_code = Parser()
    parse_code.set_tokens_list_and_code_list(final_output_token1, final_output_value1)
    parse_code.run()
    nodes_list = parse_code.formate_nodes_table(final_output_value1)
    edges_list = parse_code.edges_table

