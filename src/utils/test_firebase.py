import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('../json/posefect-firebase-adminsdk.json')
firebase_admin.initialize_app(cred,
                              {
                                  'databaseURL': 'https://posefect-b48b9-default-rtdb.firebaseio.com/'
                              })
# firebase_admin.get

def add_data_firebase(foodName):
    # import pandas as pd
    # import firebase_admin
    # from firebase_admin import credentials, firestore
    # cred = credentials.Certificate('./ai-kitchen-helper-firebase-adminsdk.json')
    # firebase_admin.initialize_app(cred,
    #                               {
    #                                   'databaseURL': 'https://ai-kitchen-helper.firebaseio.com/'
    #                               })
    db = firestore.client()
    # doc_ref = db.collection(u'test')
    # Import data
    # df = pd.read_csv(‘PPP_data.csv’)
    # tmp = df.to_dict(orient='records')
    # list(map(lambda x: doc_ref.add(x), 'tmp'))

    # item = Item(name=u'lemon', present=True)
    # doc_ref.add(item.to_dict())

    data = {
        u'name': u'' + foodName,
        u'present': True
    }
    # TODO change it to uuid
    # i = random.randint(1, 1000)
    ref = db.collection(u'test').document(u'I7Uhj1GyTdTs9xlYswgHkGLvJS22').set(data)
    # q = ref.key.set(data)
    # print(q.to_dict())
    # docs = doc_ref.stream()
    # for doc in docs:
    #     print(f'{doc.id} = > {doc.to_dict()}')


add_data_firebase('hello')
