## problemPractice

Django webapp for daily problem practice in a convenient format

#### Premise
A webapp to submit and practice theory-related questions. Current goal is to have a comprehensive section for training the recognition of the most important discrete math identities.
<br />
Sub-apps are per-topic. First topic is discrete math. Starting with static questions, but hope to get to more clever templates in future versions. No user-submitted latex yet.


#### To Test
Not very exciting at the moment
* Install django in python3, w/ pip3
* python3 manage.py runserver
* Add yourself as a superuser w/ python3 manage.py createsuperuser
* Add entries in admin menu w/ 127.0.0.1:8000/admin/
* Check out site w/ 127.0.0.1:8000/math/
