#
# Filters file 
#
#
class FilterModule(object):

    def filters(self):
        return {
            'mdtohtml':self.mdtohtml
        }

    def mdtohtml(self, mdtext):
        import mistune
        markdown = mistune.Markdown()
        return markdown(mdtext)
