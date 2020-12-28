Readme.txt
This project is to convert a plain-text file to HTML.
This is a possible issue for bloggers who write in XML and need to convert their projects to websites. 

The goal of this project are as follows: 
- The input shouldnt be required to contain artificial codes or tags. 
- you shouldnt be able to deal with both different blocks (such as headings/paragraphs/
list items) and inline text such as emphasized text or URLs. 
- although this implementation deals with HTML, it should be easy to extend to other markup languages. 

TODO & useful tools: 
- [sys.stdin] for reading from the xml file. 
- [iter] iteration over file line items.
- string handling and using generators.
- [re] module for regular expressions & patterns in the XML file. 

Program components: 
- A Parser: an object to read text and manage other classes. 
- Rules: to detect block types and format them appropriately 
- Filters: to deal with in-line elements (using regular expressions)
- Handlers: for the parser to use to produce different kinds of markups. 