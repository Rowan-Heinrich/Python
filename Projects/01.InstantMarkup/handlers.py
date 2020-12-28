# handlers.py
# a program for handling paragraphs

class Handler:
	def callback(self, prefix, name, *args):
		# for finding the correct method (start/end/sub).
		# when getattir returns a value a function is called. 
		# for example Handler.callback('start_','paragraph')
		# calls the start-paragraphi method with no arguements.  
		method = getattr(self, prefix+name, None)
		if callable(method): return method(*args)

	def start(self,name):
		# a helper metho for start_
		self.callback('start_',name)

	def end(self,name):
		# a helper metho for end_
		self.callback('end_',name)

	def sub(self,name):
		# returns a function to be used as the replacement
		# function (of re.).
		def subsitution(match):
			result = self.callback('sub_', name, match)
			if result is None: match.group(0)
			return result
		return subsitution

class HTMLRenderer(Handler):
        def start_document(self):
                print('<html><head><title>...</title></head><body>')
        def end_document(self):
                print('</body></html>')
        def start_paragraph(self):
                print('<p>')
        def end_paragraph(self):
                print('</p')
        def start_heading(self):
                print('<h2>')
        def end_heading(self):
                print('</h2')
        def start_list(self):
                print('<ul>')
        def end_list(self):
                print('</ul>')
        def start_listitem(self):
                print('<li>')
        def end_listitem(self):
                print('</li>')
        def start_title(self):
                print('<h1>')
        def end_title(self):
                print('</h1>')
        def sub_emphasis(self, match):
                return '<em>%s</em>' % match.group(1)
        def sub_url(self, match):
                return '<a href="%s">%s</a>' % (match.group(1), match.group(1))
        def sub_mail(self, match):
                return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))
        def feed(self, data):
                print(data)
