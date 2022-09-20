r = "\033[1;31m"
w = "\033[0m"
R = "\033[1;41m"
try:
    import pyfiglet
    from pytube import *
    from tqdm import *
    import time 
except Exception as e:
    print ("ERROR!!",e)
def loadani():
    for i in tqdm(range(40)):
        time.sleep(0.1)
def banner():
    result = pyfiglet.figlet_format("YTInstaller")
    print (result)
try:
    banner()
    usr=input('''
1.mp3
2.mp4
>>''')
    if "2" in usr:
        print ("**********mp4**********")
        link=input("Enter link:")
        resolution=input("Enter resolution:")
        if resolution == "":
            resolution="240p"
        path=input("Enter path:")
        yt = YouTube(link)
        print (r+"Title:",w,yt.title)
        loadani()
        print (R+"This could take a while..."+w)
        YouTube(link).streams.filter(res=resolution).first().download(path)
        print (r+"saved at =>",w,path)
    elif "1" in usr:
        print ("***********mp3***********")
        link3=input("Enter link:")
        path3 =input("Enter path:")
        loadani()
        YouTube(link3).streams.get_audio_only().download(path3)
        print (R+"please rename the extention.change mp4 to mp3")
        print (w,r+"saved at=>",w,path3)
except Exception as g:
    print ("ERROR",g)
