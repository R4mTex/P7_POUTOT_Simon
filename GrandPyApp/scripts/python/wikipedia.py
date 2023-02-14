import wikipediaapi


class Wikipedia:

        def wiki_page(query):
            wiki_wiki = wikipediaapi.Wikipedia('fr')
            page_py = wiki_wiki.page(query)
            try:
                if page_py.exists() == True:
                    return {
                        'summary': page_py.summary[0:400], 
                        'url': page_py.fullurl
                        }
                elif page_py.exists() == False:
                    return "La page n'existe pas."
            except:
                return "Une erreur est survenue"
