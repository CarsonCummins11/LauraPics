import base64
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('images2') if isfile(join('images2', f))]
out = '<!DOCTYPE html><html><head><script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script><style>.center{width: 100vw;height: 100vh;display: flex;align-items: center;justify-content: center;}</style><script>array=['
for f in onlyfiles:
    data = open('images2/'+f, 'rb').read() # read bytes from file
    data_base64 = base64.b64encode(data)  # encode to base64 (bytes)
    data_base64 = data_base64.decode()    # convert bytes to string
    out += '\'<img style="width:300px;"src="data:image/jpeg;base64,' + data_base64 + '">\',' # embed in html

out = out[:-1]
out+= '];$( document ).ready(function() {$("#center").html(array[Math.floor(Math.random() * array.length)]);});</script></head><body><div id="center" class="center"></div></body></html>'

open('index.html','w+').write(out)