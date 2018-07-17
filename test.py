import vk_api
from my_data import vk_data
import time
import random

#vk_data - a class with your vk information, like as login, password and etc.

def photo(id): #get a photo id of the a user
    avka = vk.photos.get(owner_id=id, album_id='profile', count=1, rev=1)
    return avka
def loyse(ava, id): #like
    z = vk.likes.add(owner_id=id, type='photo', item_id=ava)
    return z


vk_session = vk_api.VkApi(str(vk_data.login), str(vk_data.pswrd))
vk_session.auth()
vk = vk_session.get_api()

girls = vk.users.search(count="""integer number""", city='CITY ID', sex="""1 is female, 2 is male""", age_from=0, age_to=80, has_photo=1) #list of the users
n = girls['items']

for i in n:
    id = i['id']
    array_1 = photo(id)
    some = array_1['items']
    mool = some[0]
    ava = mool['id']
    print(loyse(ava, id))

    time.sleep(random.randint(50, 100)) #random time needs then VK don't block your account





