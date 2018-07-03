import pickle
import sqlite3
import numpy as np
import os

# import HashingVectorizer from local dir
from vectorizer import vect

def update_model(db_path, model, batch_size=10000):
	conn = sqlite3.connect(db_path)
	c = conn.cursor()
	c.execute('SELECT * from review_db')
	results = c.fetchmany(batch_size)
	while results:
		data = np.array(results)
		X = data[:, 0]
		y = data[:, 1].astype(int)

		classes = np.array([0, 1])
		X_train = vect.transform(X)
		clf.partial_fit(X_train, y, classes=classes)
		results = c.fetchmany(batch_size)

	conn.close()
	return None

cur_dir = os.path.dirname('C:\\Python_nltk\\sentiment_analysis_flask\\')

clf = pickle.load(open(os.path.join(cur_dir,
				'pkl_objects', 'classifier.pkl'), 'rb'), encoding='latin1')
db = os.path.join(cur_dir, 'reviews.sqlite')

update_model(db_path=db, model=clf, batch_size=1000)

# Uncomment the following lines to update 
# classifier.pkl file permanently.
# pickle.dump(clf, open(os.path.join(cur_dir,
#            'pkl_objects', 'classifier.pkl'), 'wb'),
#             protocol=None)