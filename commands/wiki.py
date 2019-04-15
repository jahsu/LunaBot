import wikipediaapi

# Can probably do more about th config and also separate this out
wiki_client = wikipediaapi.Wikipedia('en')


def query_wiki(ctx, query):
    str_query = ''.join(query)
    str_query.replace("_", " ")
    wiki_page = wiki_client.page(str_query)
    if wiki_page.exists():
        return wiki_page.fullurl.format(ctx.message)
    else:
        return 'This page does not exist bruh.'.format(ctx.message)
