import wikipediaapi

wiki_client = wikipediaapi.Wikipedia('en')


def query_wiki(ctx, query):
    wiki_page = wiki_client.page(query)
    if wiki_page.exists():
        return wiki_page.fullurl.format(ctx.message)
    else:
        return 'This page does not exist bruh.'.format(ctx.message)
