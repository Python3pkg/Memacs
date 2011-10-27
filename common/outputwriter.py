#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time-stamp: <2011-10-26 15:13:31 awieser>

import time
import codecs
import sys

INVOCATION_TIME = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())

class OutputWriter:
    __handler = None
    
    def __init__(self, file_name=None):
        """
        @param file_name:  
        """
        if file_name != None:            
            self.__handler = codecs.open(file_name, 'w', "utf-8")
            
        self.__write_header()
        
    def write(self, output):
        """
        Write "<output>"
        """
        if self.__handler:
            self.__handler.write(unicode(output))
        else:
            print output
    
    def writeln(self, output):
        """
        Write "<output>\n"   
        """
        self.write(unicode(output) + u"\n")    
    
    def __write_header(self):
        """
        Writes the header of the file
        
        Don't call this function - call instead function close(),
        __init__() does call this function
        """
        self.write_commentln(u"-*- coding: utf-8 -*-")
    
    def __write_footer(self):
        """
        Writes the footer of the file including calling python script and time
        
        Don't call this function - call instead function close(),
        close() does call this function 
        """
        self.writeln(u"* successfully parsed by " + \
                     sys.argv[0] + " at " + INVOCATION_TIME + ".\n\n")
    
    def write_comment(self,output):
        """
        Write output as comment: "## <output>" 
        """
        self.write("## " + output)
        
    def write_commentln(self,output):
        """
        Write output line as comment: "## <output>\n" 
        """
        self.write_comment(output + "\n")
        
    
    def close(self):
        """
        Writes the footer and closes the file
        """
        self.__write_footer()
        if self.__handler != None:
            self.__handler.close()
        