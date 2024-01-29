with open("poem.txt",'w+') as f:
    f.write('''Twinkle, twinkle, little star

How I wonder what you are

Up above the world so high

Like a diamond in the sky

Twinkle, twinkle little star

How I wonder what you are


When the blazing sun is gone

When he nothing shines upon

Then you show your little light

Twinkle, twinkle, all the night

Twinkle, twinkle, little staR

How I wonder what you are ''')
f=open('poem.txt','r')
a=f.read()
if 'twinkle' in a:
    print('twinkle is present')
    print(a.count('twinkle'))
    print(a.count('Twinkle'))
    print(a.count("I"))
else:
    print('twinkle is absent') 
f.close()