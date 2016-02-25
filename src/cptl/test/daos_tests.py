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
import unittest


class FilesystemGraphsDAOTest(unittest.TestCase):

    fdg = None
    
    def setUp(self):
        Config = ConfigParser.ConfigParser()
        Config.read("config/tests.ini")
        section = "FilesystemGraphsDAOTest"
        
        model_basedir = Config.get( section, "model_basedir" )
        resolver_file_name = Config.get( section, "resolver_file_name" )

        self.fgd = cptl.daos.FilesystemGraphsDAO.create_dao(model_basedir, resolver_file_name)
        
    def test_retrieve(self):
        ref_str = "514d63aa-1fcf-423b-880d-168bac34354f"
        graph_data = self.fgd.retrieve(ref_str)
        self.assertEquals( len(graph_data["nodes"]), 188 )

        
if __name__ == '__main__':
    suite1 = unittest.TestLoader().loadTestsFromTestCase(FilesystemGraphsDAOTest)
    unittest.TextTestRunner(verbosity=2).run(suite1)

