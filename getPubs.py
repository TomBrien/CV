import scholarly

# Get publications

pubs = scholarly.search_author_id('vGJ6UK8AAAAJ')
pubs = pubs.fill
pubs = pubs.publications