"""
Copyright (c) 2016 Gabriel A. Weaver, Information Trust Institute
All rights reserved.

Developed by:             Gabriel A. Weaver, Information Trust Institute
                          University of Illinois at Urbana-Champaign
                          http://www.iti.illinois.edu/

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal with the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimers.
Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimers in the
documentation and/or other materials provided with the distribution.

Neither the names of Gabriel A. Weaver, Information Trust Institute,
University of Illinois at Urbana-Champaign, nor the names of its
contributors may be used to endorse or promote products derived from
this Software without specific prior written permission.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE CONTRIBUTORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS WITH THE
SOFTWARE.
"""
import cptl.requests
import json
import os
import tornado.httpserver
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../index.html")

def make_app():
    settings = {
        "debug": "True",
    }
    handlers = [
        (r'/', MainHandler),
        (r'/api/v1.0.0/analyses$', cptl.requests.AnalysesRequestHandler, dict(config_file="config/server.ini")),
        (r'/api/v1.0.0/analyses/graph_join', cptl.requests.GraphJoinAnalysisRequestHandler, dict(config_file="config/server.ini")),
        (r'/api/v1.0.0/docs/(.*)', tornado.web.StaticFileHandler, {'path': 'static/api/v1.0.0/'}),
        (r'/api/v1.0.0/graphs$', cptl.requests.GraphsRequestHandler, dict(config_file="config/server.ini")),
        (r'/api/v1.0.0/graphs/(.*)', cptl.requests.GraphsRequestHandler, dict(config_file="config/server.ini")),
        (r'/api/v1.0.0/icons$', cptl.requests.IconsRequestHandler, dict(config_file="config/server.ini")),
        (r'/api/v1.0.0/icons/(.*)', cptl.requests.IconsRequestHandler, dict(config_file="config/server.ini")),
        (r'/css/(.*)', tornado.web.StaticFileHandler, {'path': 'static/css/'}),
        (r'/img/(.*)', tornado.web.StaticFileHandler, {'path': 'static/img/'}),        
        (r'/js/(.*)', tornado.web.StaticFileHandler, {'path': 'static/js/'}),        
    ]
    return tornado.web.Application( handlers, **settings )

if __name__ == "__main__":
    app = make_app()
    ssl_options = { "certfile": "keys/localhost.csr",
                    "keyfile": "keys/localhost.key" }
    
    http_server = tornado.httpserver.HTTPServer( app, ssl_options )
    http_server.listen(443)
    tornado.ioloop.IOLoop.instance().start()
            
