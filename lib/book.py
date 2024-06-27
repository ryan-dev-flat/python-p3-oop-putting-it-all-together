#!/usr/bin/env python3

class Book:
        def __init__(self, title = "And Then There Were None", page_count = 272):
            self.title = title
            self.page_count = page_count
          
        @property
        def page_count(self):
            """The page_count property"""
            return self._page_count
         
        @page_count.setter
        def page_count(self, page_count):
                """page_count must be an integer" if page_count is not an integer."""
                if isinstance(page_count, int):
                    self._page_count = page_count
                else:
                    raise ValueError("page_count must be an integer.")

            
        def turn_page(self):
            print("Flipping the page...wow, you read fast!")
            
            
            
        # end def
        # end def
        # end alternate constructor
    

    
        