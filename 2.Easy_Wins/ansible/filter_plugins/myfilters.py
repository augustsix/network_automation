#
# Filters file 
#
#
class FilterModule(object):

    def filters(self):
        return {
            'mdtohtml':self.mdtohtml,
            'find_communities':self.find_communities
        }

    def mdtohtml(self, mdtext):
        import mistune
        markdown = mistune.Markdown()
        return markdown(mdtext)

    def find_communities(self,cmd_output):
        communities = []
        for line in cmd_output:
            communities.add(line.split()[2])
        return communities
