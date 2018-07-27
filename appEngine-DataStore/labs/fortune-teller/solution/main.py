#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2
import random
from movie import Movie, Person

def get_fortune():
    fortune_list=['Tomorrow, you will meet a life-changing new friend.',
                  'Fame and Instagram followers are headed your way.',
                  'On the Tuesday after next, an odd meeting will lead to a new opportunity.',
                  'Despite dry skies, bring an umbrella tomorrow.',
                  'A thrilling time is in your immediate future.',
                  'Someone has Googled you recently.',
                  'Stay alert. You will be part of a rescue mission.',
                  'You will beat Watson in a game of Jeopardy. Start studying though']
    return(random.choice(fortune_list))


#remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        start_template=jinja_current_directory.get_template("templates/fortune_welcome.html")
        self.response.write(start_template.render())

    def post(self):
        random_fortune = get_fortune()
        astro_sign = self.request.get('user_astrological_sign')
        my_dict={'the_fortune':random_fortune, 'the_astro_sign':astro_sign}
        end_template=jinja_current_directory.get_template("templates/fortune_results.html")
        #astro_sign = request.form.get('user_astrological_sign')
        self.response.write(end_template.render(my_dict))

class DataDemoHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_directory.get_template("templates/create_movie.html")
        self.response.write(start_template.render())

    def post(self):
        title = self.request.get('movie_title')
        runtime_mins = int(self.request.get('movie_runtime'))
        rating = float(self.request.get('movie_rating'))

        my_movie = Movie(title = title, runtime_mins = runtime_mins, rating = rating)
        my_movie.put()


class PersonHandler(webapp2.RequestHandler):
    def get(self):
        start_template = jinja_current_directory.get_template("templates/create_person.html")
        self.response.write(start_template.render())

    def post(self):
        first_name = self.request.get("person_fname")
        last_name = self.request.get("person_lname")
        occupation = self.request.get("person_occ")
        age = int(self.request.get("person_age"))

        new_person = Person(fname = first_name, lname = last_name, occupation = occupation, age = age)
        new_person.put()

        end_template = jinja_current_directory.get_template("templates/create_person.html")
        results = Person.query().order(Person.fname).fetch()

        self.response.write(end_template.render({'persons':results}))


class DeletePerson(webapp2.RequestHandler):
        def post(self):
            delete_template = jinja_current_directory.get_template("templates/delete_person.html")

            person_key = int(self.request.get("person_key"))
            person_to_delete = Person.get_by_id(person_key)
            person_to_delete.key.delete()

            results = Person.query().order(Person.fname).fetch()

            self.response.write(delete_template.render({
                'fname': person_to_delete.fname,
                'lname': person_to_delete.lname,
                'persons': results,
                }))

app = webapp2.WSGIApplication([
    ('/', FortuneHandler),
    ('/enterdata', DataDemoHandler),
    ('/new_person', PersonHandler),
    ('/delete_person', DeletePerson)
], debug=True)
