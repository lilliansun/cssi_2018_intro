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
import random
import jinja2



def get_fortune(astro_sign):
    #add a list of fortunes to the empty fortune_list array
    fortunes={
        'Aquarius': "You will have one kid",
        'Pisces': 'You will own two fish',
        'Aires': 'Don\'t spend too much money',
        'Taurus': 'Animals are your friends',
        'Gemini': 'You have a secret twin',
        'Cancer': 'You will have good vibes tomorrow',
        'Leo': 'Don\'t order pizza for five weeks',
        'Virgo': 'Your favorite color will change',
        'Libra': 'You will find happiness',
        'Scorpio': 'You will die from drowning',
        'Sagittarius': 'In two years ,you will get a 100 on a test',
        'Capricorn': 'You will buy two apples tomorrow'
        }

    your_fortune = fortunes[astro_sign]
    return(your_fortune)


#remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = ['jinja2.ext.autoescape'],
    autoescape = 'true'
)

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        # In part 2, instead of returning this string,
        # make a function call that returns a random fortune.
        start_template = jinja_current_directory.get_template(
            "templates/fortune-start.html")
        self.response.write(start_template.render())

    def post(self):
        self.response.write("My post handler")
        end_template = jinja_current_directory.get_template("templates/fortune-result.html")
        user_astro_sign = self.request.get('star-sign')
        fortune = get_fortune(user_astro_sign)
        self.response.write(end_template.render(
                    {"fortune": fortune}))

class HelloHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello World. Welcome to the root route of my app')

class GoodbyeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('My response is goodbye world.')

#the route mapping
app = webapp2.WSGIApplication([
    #this line routes the main url ('/')  - also know as
    #the root route - to the Fortune Handler
    ('/', HelloHandler),
    ('/predict', FortuneHandler),
    ('/farewell', GoodbyeHandler)
     #maps '/predict' to the FortuneHandler

], debug=True)
