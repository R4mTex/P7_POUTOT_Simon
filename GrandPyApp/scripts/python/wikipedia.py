import wikipediaapi


class Wikipedia:
    def wiki_page(query):
        wiki_wiki = wikipediaapi.Wikipedia('fr')
        page_py = wiki_wiki.page(query)

        try:
            if page_py.exists() is True:
                return {
                    'summary': page_py.summary[0:400],
                    'url': page_py.fullurl
                    }
            elif page_py.exists() is False:
                return "La page n'existe pas."
        except page_py.PageError:
            return "Une erreur est survenue"
