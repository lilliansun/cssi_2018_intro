# Copyright 2016 Google Inc.
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

import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello. This is Lilly\'s test app')
#         self.response.write("Enter a number into the url query in the format "
#             "\"?num=____\" to convert to fizzbuzz")
# #
# class FizzBuzz(webapp2.RequestHandler):
#     def get(self):
#         self.response.headers['Content-Type'] = 'text/plain'
#         num = int(self.request.get('num'))
#         if (num%3==0 and num%5==0):
#             response = "fizzbuzz"
#         elif (num%3==0):
#             response = "fizz"
#         elif (num%5==0):
#             response = "buzz"
#         else:
#             response = num
#
#         self.response.write(
#             "{n} converted to fizzbuzz is: {res}".format(n = num, res = response))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    # ('/convert', FizzBuzz)
], debug=True)
