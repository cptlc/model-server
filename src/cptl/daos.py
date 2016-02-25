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
import json
import logging

class FilesystemGraphsDAO():
    """
    The FilesystemGraphsDAO is responsible for CRUD operations on a 
       graphs available via the local filesystem.
    """

    model_basedir = None            
    resolver = None              
    
    def create(self):
        """
        Create a new graph

        :return:  returns the new graph's UUID
        """
        raise Exception("method not yet implemented.")

    def retrieve(self, ref_str):
        """
        Retrieve the graph for the given UUID.

        :param uuid_str:  The reference string of the graph to retrieve
        :return:  returns the graph data, empty dict if none
        """
        result = {}
        
        if ( ref_str in self.resolver ):
            graph_file_path = "/".join( [ self.model_basedir, self.resolver[ ref_str ]["graph"] ] )
            graph_file = open( graph_file_path, 'r' )
            graph_data = json.load( graph_file )
            result = graph_data
        else:
            logging.warning("No entry for " + ref + " in resolver")
        
        return result

    def update(self, ref):
        raise Exception("method not yet implemented.")

    def delete(self, ref):
        raise Exception("method not yet implemented.")

    @staticmethod
    def create_dao( model_basedir, resolver_file_name ):
        """
        Create a data access object for graphs

        :param model_basedir:            Base directory for the model to operate upon
        :param resolver_file_name:       Name of the resolver file to use within that model
        """
        fgd = FilesystemGraphsDAO()
        fgd.model_basedir = model_basedir

        resolver_file_path = "/".join([model_basedir, "resolvers", resolver_file_name])
        resolver_file = open( resolver_file_path, 'r' )
        fgd.resolver = json.load( resolver_file )
        
        return fgd
    
