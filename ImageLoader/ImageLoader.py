# this is simply app that load all photos from vk album in folder
# WARNING vk api maybe will be changed in the future, so this app maybe will not work in the future

from urllib.request import urlretrieve
import vk, os, time, math

login = 'zhidejkina@gmail.com'
password = 'Black1396'
# appID = '5845299'do not need anymore

session = vk.Session()
vkAPI = vk.API(session)

# sample of adress 'https://vk.com/album-57409266_178241122'
url = input('Enter album name: ')
albumID = url.split('/')[-1].split('_')[1]
ownerID = url.split('/')[-1].split('_')[0].replace('album', '')


photoCount = vkAPI.photos.getAlbums(owner_id = ownerID, album_ids = albumID)[0]['size']

counter = 0
loadPersent = 0
breaked = 0
time_now = time.time()

photosFolder = input('Enter path to save: ')
if photosFolder =='':
    photosFolder = 'album{0}_{1}'.format(ownerID, albumID)
    if not os.path.exists(photosFolder):
        os.mkdir(photosFolder)
        
for i in range(math.ceil(photoCount/1000)):
    photos = vkAPI.photos.get(owner_id = ownerID, album_id= albumID, count = 1000, offset = i*1000)
    for photo in photos:
        counter +=1
        url = photo['src_big'] 
        print('Load photo № {} from {}. Progress: {} %'.format(counter, photoCount, loadPersent ))
        loadPersent = round(100/photoCount*counter, 2)
        try:
            urlretrieve(url, photosFolder + "/" + os.path.split(url)[1])
        except Exception:
            print('Error')
            breaked += 1
            continue