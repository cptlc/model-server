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
import cptl.daos
import ConfigParser
import json
import tornado.web

class GraphsRequestHandler(tornado.web.RequestHandler):

    fgd = None
    
    def initialize(self, config_file):
        Config = ConfigParser.ConfigParser()
        Config.read(config_file)

        section = "GraphsRequestHandler"
        model_basedir = Config.get( section, "model_basedir" )
        resolver_file_name = Config.get( section, "resolver_file_name" )
        self.fgd = cptl.daos.FilesystemGraphsDAO.create_dao(model_basedir, resolver_file_name)
        
    def get(self, uuid=None):

        if (uuid != None):
            graph_data = self.fgd.retrieve( uuid )
            self.write( json.dumps( graph_data, indent=2 ) );
        else:
            self.write( json.dumps( self.fgd.resolver, indent=2 ) );

        self.set_header("Content-Type", "application/json")

