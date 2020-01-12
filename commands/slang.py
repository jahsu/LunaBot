def spit_slang(ctx, query):
    str_query = '+'.join(query)
    urban_dic_url = "https://www.urbandictionary.com/define.php?term="
    urban_dic_query = urban_dic_url + str_query
    return urban_dic_query.format(ctx.message)
