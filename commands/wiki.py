def query_wiki(ctx, query):
    wiki_link = "https://en.wikipedia.org/wiki/" + '_'.join(query)
    return wiki_link.format(ctx.message)

