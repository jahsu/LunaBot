import wikipediaapi

# Can probably do more about th config and also separate this out
wiki_client = wikipediaapi.Wikipedia('en')


def print_disambiguation_links(wiki_page):
    page_links = ""
    for title in sorted(wiki_page.links.keys()):
        current_title = "%s: %s" % (title, wiki_page.links[title])
        page_links = page_links + current_title + "\n"
    return page_links


def query_wiki(ctx, query):
    wiki_page = wiki_client.page(query)
    if wiki_page.exists():
        if "disambiguation" in wiki_page.fullurl:
            return print_disambiguation_links(wiki_page).format(ctx.message)
        else:
            return wiki_page.fullurl.format(ctx.message)
    else:
        return 'This page does not exist bruh.'.format(ctx.message)
