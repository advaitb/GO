from Bio import Entrez
import time

def search(query):
    Entrez.email = 'advait.balaji@mssm.edu'
    handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax='9999',
                            retmode='xml', 
                            term=query)
    results = Entrez.read(handle)
    time.sleep(2)
    return results

def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'advait.balaji@mssm.edu'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    time.sleep(2)
    return results


with open('/Users/advaitbalaji/Downloads/AdvaitB/XML_Redox.txt', 'a+') as of:
    of.write('<SubcellularProcessDownload>\n')
    results = search('("redox signalling") OR ("redox signaling cascade")')
    time.sleep(10)
    id_list = results['IdList']
    #print(id_list)
    papers = fetch_details(id_list)
    of.write('Total Pubmed Articles: ' +str(len(id_list))+'\n')
    #print(papers)
    time.sleep(10)
    for paper in papers['PubmedArticle']:
        if 'PMID' not in paper['MedlineCitation']:
            pmid = 'NOT AVAILABLE'
        else:
            pmid = paper['MedlineCitation']['PMID']
        if 'ArticleTitle' not in paper['MedlineCitation']['Article']:
            article_title = 'NOT AVAILABLE'
        else:
            article_title = paper['MedlineCitation']['Article']['ArticleTitle']
        journal= paper['MedlineCitation']['Article']['Journal']['Title']
        if 'PubDate' not in paper['MedlineCitation']['Article']['Journal']['JournalIssue']:
            pubdate = 'NOT AVAILABLE'
        else:
            if 'Year' not in paper['MedlineCitation']['Article']['Journal']['JournalIssue']['PubDate']:
                pubdate = 'NOT AVAILABLE'
            elif 'Month' not in paper['MedlineCitation']['Article']['Journal']['JournalIssue']['PubDate']:
                pubdate = 'NOT AVAILABLE'
            else:
                pubdate = paper['MedlineCitation']['Article']['Journal']['JournalIssue']['PubDate']['Year'] + '-' + paper['MedlineCitation']['Article']['Journal']['JournalIssue']['PubDate']['Month']
        if 'Abstract' in paper['MedlineCitation']['Article']:
            abstract = ''.join(paper['MedlineCitation']['Article']['Abstract']['AbstractText'])
        else:
            abstract = 'NOT AVAILABLE'
        of.write('\t<Article>\n')
        of.write('\t\t<PubmedID> '+pmid+ ' </PubmedID>\n')
        of.write('\t\t<ArticleTitle> '+article_title+ ' </ArticleTitle>\n')
        of.write('\t\t<Journal> '+journal+' </Journal>\n')
        of.write('\t\t<PubDate> '+pubdate+ ' </PubDate>\n')
        of.write('\t\t<ArticleAbstract> '+abstract+' </ArticleAbstract>\n')
        of.write('\t</Article>\n')
    of.write('</SubcellularProcessDownload>')
    time.sleep(10)


    #for i, paper in enumerate(papers['PubmedArticle']):
    #   print("%d) %s" % (i+1, paper['MedlineCitation']['Article']['ArticleTitle']))
    # Pretty print the first paper in full
    #import json
    #print(json.dumps(papers[0], indent=2, separators=(',', ':')))