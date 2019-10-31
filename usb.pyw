# python3.6.5

from tkinter import *
from tkinter import ttk
import webbrowser
import speech_recognition as sr
from pygame import mixer


root = Tk()
root.resizable(width=False, height=False)
root.configure(background="white")
root.title('Universal Search Bar')
root.iconbitmap('data/logo4.ico')

style = ttk.Style()
style.configure("TLabel", background="white", foreground ="red", font = "Arial 10 bold")
style.configure("TRadiobutton", background="white", foreground ="red", font = "Arial 10 bold")
style.configure("TEntry", background="white", foreground ="blue", font = "Arial 10 bold")



photo = PhotoImage(file='data/mic.png')

label1 = ttk.Label(root, text='Query:')
label1.grid(row=0, column=0, padx=(15,5), pady=(10, 0))
entry1 = ttk.Entry(root, width=80)
entry1.grid(row=0, column=1, columnspan=4, pady=(10, 0), padx=(0, 5))

btn2 = StringVar()

def callback():
    
    if btn2.get() == 'google' and entry1.get() != '':
        webbrowser.open('http://google.com/search?q='+entry1.get())
        
    elif btn2.get() == 'games' and entry1.get() != '':
        webbrowser.open('http://oceanofgames.com/?s='+entry1.get())

    elif btn2.get() == 'amz' and entry1.get() != '':
        webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords='+entry1.get())

    elif btn2.get() == 'ytb' and entry1.get() != '':
        webbrowser.open('https://www.youtube.com/results?search_query='+entry1.get())

    elif btn2.get() == 'Gmail' and entry1.get() == '':
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

    elif btn2.get() == 'Gmail' and entry1.get() != '':
        webbrowser.open('https://mail.google.com/mail/u/0/#search/'+entry1.get())

    elif btn2.get() == 'music' and entry1.get() != '':
        webbrowser.open('https://www.saavn.com/search/'+entry1.get())

    elif btn2.get() == 'movies' and entry1.get() != '':
        webbrowser.open('https://worldfree4.movie/?s='+entry1.get())

    elif btn2.get() == 'soft' and entry1.get() != '':
        webbrowser.open('https://igetintopc.com/?s='+entry1.get())

    else:
        pass

def get(event):

    if btn2.get() == 'google' and entry1.get() != '':
        webbrowser.open('http://google.com/search?q='+entry1.get())
        
    elif btn2.get() == 'games' and entry1.get() != '':
        webbrowser.open('http://oceanofgames.com/?s='+entry1.get())

    elif btn2.get() == 'amz' and entry1.get() != '':
        webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords='+entry1.get())

    elif btn2.get() == 'ytb' and entry1.get() != '':
        webbrowser.open('https://www.youtube.com/results?search_query='+entry1.get())

    elif btn2.get() == 'Gmail' and entry1.get() == '':
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

    elif btn2.get() == 'Gmail' and entry1.get() != '':
        webbrowser.open('https://mail.google.com/mail/u/0/#search/'+entry1.get())

    elif btn2.get() == 'music' and entry1.get() != '':
        webbrowser.open('https://www.saavn.com/search/'+entry1.get())

    elif btn2.get() == 'movies' and entry1.get() != '':
        webbrowser.open('https://worldfree4.movie/?s='+entry1.get())

    elif btn2.get() == 'soft' and entry1.get() != '':
        webbrowser.open('https://igetintopc.com/?s='+entry1.get())

    else:
        pass

def buttonClick():
    # obtain audio from the microphone
    mixer.init()
    mixer.music.load('data/begin_record.mp3')
    mixer.music.play()

    r = sr.Recognizer()
    r.pause_threshold = 0.7
    r.energy_threshold = 400
    
    with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)

            # recognize speech using Sphinx
            try:
                audio = r.listen(source, timeout=5)
                message =str(r.recognize_google(audio))
                mixer.music.load('data/end_record.mp3')
                mixer.music.play()
                entry1.focus()
                entry1.delete(0, END)
                entry1.insert(0, message)

                if btn2.get() == 'google':
                    webbrowser.open('http://google.com/search?q='+message)
        
                elif btn2.get() == 'games':
                    webbrowser.open('http://oceanofgames.com/?s='+message)

                elif btn2.get() == 'amz':
                    webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords='+message)

                elif btn2.get() == 'ytb':
                    webbrowser.open('https://www.youtube.com/results?search_query='+message)

                elif btn2.get() == 'Gmail':
                    webbrowser.open('https://mail.google.com/mail/u/0/#search/'+message)

                elif btn2.get() == 'music':
                    webbrowser.open('https://www.saavn.com/search/'+message)

                elif btn2.get() == 'movies':
                    webbrowser.open('https://worldfree4.movie/?s='+message)

                elif btn2.get() == 'soft':
                    webbrowser.open('https://igetintopc.com/?s='+message)

                else:
                    pass

            except sr.UnknownValueError:
                entry1.delete(0, END)
                entry1.insert(0, 'Google Speech Recognition could not understand your voice .....')

            except sr.RequestError as e:
                entry1.delete(0, END)
                entry1.insert(0, 'Could not request results from Google Speech Recognition Service !!!')

            else:
                pass    


    
entry1.bind('<Return>', get)

MyButton1 = Button(root, text='Search', width=5, command=callback, foreground ="red", background="white", font = "Arial 10 bold", relief="solid", bd =0)
MyButton1.grid(row=0, column=6, padx=(5, 15), pady=(10, 0))


MyButton2 = ttk.Radiobutton(root, text='Google', value='google', variable=btn2)
MyButton2.grid(row=1, column=1, pady=(5, 10))

MyButton3 = ttk.Radiobutton(root, text='Music', value='music', variable=btn2)
MyButton3.grid(row=1, column=0, sticky=E, pady=(5, 10))

MyButton4 = ttk.Radiobutton(root, text='Amz', value='amz', variable=btn2)
MyButton4.grid(row=1, column=2, sticky=E, pady=(5, 10))

MyButton5 = ttk.Radiobutton(root, text='Ytb', value='ytb', variable=btn2)
MyButton5.grid(row=1, column=2, sticky=W, pady=(5, 10))

MyButton6 = ttk.Radiobutton(root, text='Gmail', value='Gmail', variable=btn2)
MyButton6.grid(row=1, column=3, pady=(5, 10))

MyButton7 = ttk.Radiobutton(root, text='Soft', value='soft', variable=btn2)
MyButton7.grid(row=1, column=4, sticky=W, pady=(5, 10))

MyButton8 = ttk.Radiobutton(root, text='Movies', value='movies', variable=btn2)
MyButton8.grid(row=1, column=4, sticky=E, pady=(5, 10))

MyButton9 = ttk.Radiobutton(root, text='Games', value='games', variable=btn2)
MyButton9.grid(row=1, column=5, columnspan=2, padx=(5, 0), pady=(5, 10))

MyButton6 = Button(root, image=photo, command=buttonClick, bd=0, background='white', overrelief='groove', relief='sunken')
MyButton6.grid(row=0, column=5, padx=(0, 0), pady=(10, 0))

entry1.focus()
root.wm_attributes('-topmost', 1)
btn2.set('google')
root.mainloop()
