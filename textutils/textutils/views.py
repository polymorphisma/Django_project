# i have created this file - Shrawansunar
from django.http import HttpResponse
from django.shortcuts import render



MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '

    return cipher

def morse_code_gen(text):
    message = text
    result = encrypt(message.upper())
    
    return result

def index(request):
    return HttpResponse('This is index page')

def about(request):
    return HttpResponse('About page')

def morse_code(request):
    djtext = request.POST.get('text', 'default')
    morse_text = morse_code_gen(djtext)
    params = {'title':'Morse Code', 'head_message':'Your encrypted message is here:', 'converted_text':morse_text}
    return render(request, 'morse_code.html', params)

def main_page(request):
    params = {'morse_code': 'morse_code'}
    return render(request, 'index.html', params)

