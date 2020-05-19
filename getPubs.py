import scholarly
import pickle


def buildLine(pub):
    tex = r'\item '
    author = pub.bib['author'].split(' and ')[0].split(' ')[-1]
    if len(pub.bib['author'].split(' and ')) > 0:
        author = author + ' et al.'
    tex += author + r' \textit{'
    tex += pub.bib['title'] + r'}, '
    if 'journal' not in pub.bib.keys():
        pub.bib['journal'] = pub.bib['publisher']
    tex += pub.bib['journal']
    if 'volume' in pub.bib.keys():
        tex += r' \textbf{' + pub.bib['volume'] + r'}'
    tex += '.'
    if 'eprint' not in pub.bib.keys():
        if 'url' in pub.bib.keys():
            pub.bib['eprint'] = pub.bib['url']
    tex += r' \mbox{\href{Avaliable online}{' + pub.bib['eprint'] + '}}'
    return tex


thesis = 'http://orca.cf.ac.uk/77064/12/2015BrienPhD%20(1).pdf'

# Get publications
pubs = scholarly.search_author_id('vGJ6UK8AAAAJ')
pubs.fill()
pubs = pubs.publications

papers = []
for i, pub in enumerate(pubs):
    pub.fill()
    # Skip thesis or preprints
    if 'eprint' in pub.bib.keys():
        if pub.bib['eprint'] == thesis:
            continue
    if 'journal' in pub.bib.keys():
        if 'preprint' in pub.bib['journal']:
            continue
    papers.append(buildLine(pub))

with open('papers.pkl', 'wb') as f:
    pickle.dump(papers, f)
