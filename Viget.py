'''
@author: https://github.com/NoeVG
@email: noe-vg@outlook.com
@about: This code is to download videos from youtube, 
        without using modules external to the python API.

        Missing: The url that is obtained only downloads 5 seconds of video
'''

# modules to request working
import urllib.request
from urllib.request import urlopen, unquote

# Set data formats
import datetime


'''
Class that define the methods to:
    - get request from server 
    - parse the request to extract the url videos
    - dowload the video form url
'''
class Viget():

    def __init__(self):
        #setup to video get and save
        self.urlVideo = ""
        self.pathSaveVideo = ""
        self.nameVide = datetime.datetime.today().strftime('%Y-%m-%d %H:%M')
    
    def setUrlVideo(self,urlVideo):
        self.urlVideo = urlVideo

    def setPathSaveVideo(self,pathSaveVideo):
        self.pathSaveVideo = pathSaveVideo

    def parseData(self):
        '''
        Parse data from request to extract the url of the video
        '''
        # Prepare request with a fake agent
        req = urllib.request.Request(
            self.urlVideo, 
            data=None, 
            headers={'User-Agent': 'Mozilla'}
                )
        # Open the stream of the request
        x = urlopen(req )
        raw_data = x.read()
        
        # Decode data to utf8
        raw_data = raw_data.decode('utf8')
        
        # Delete the char u0026 of the url
        raw_data = raw_data.replace("\\u0026", "&")
        
        # Split to extract the url to the ' " ' char
        raw_data = raw_data.split('\"')
        
        # Get the key word mimeType to get the video url
        for index , word in enumerate(raw_data):
            if(word == "mimeType"):
                #print the data of the video url 
                print("----------------------------------------------------------------------------")
                print("[ OK ] Video found")
                print("    [ mimeType ] :",raw_data[index+2].split(';')[0])

                print("    [ + ] url :",raw_data[index-2])
        
    
    def dowloadVideo(self):
        '''
        Missing: The url that is obtained only downloads 5 seconds of video, help !!!! :( 
        '''
        pass

if __name__ == "__main__":
    '''
    Prepare the main funtion and the class Viget
    '''    
    viget = Viget()

    # set the url to test, this copy from youtube player/site
    viget.setUrlVideo("https://www.youtube.com/watch?v=FrPjl_nbJp0")    
    
    # parse the data    
    viget.parseData()