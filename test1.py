import feedparser
import arxiv
from tqdm import tqdm
# from paper import ArxivPaper

# query = "cs.AI+cs.CV+cs.LG+cs.CL"
# client = arxiv.Client(num_retries=10,delay_seconds=10)
# feed = feedparser.parse(f"https://rss.arxiv.org/atom/{query}")
# if 'Feed error for query' in feed.feed.title:
#     raise Exception(f"Invalid ARXIV_QUERY: {query}.")
# papers = []
# all_paper_ids = [i.id.removeprefix("oai:arXiv.org:") for i in feed.entries if i.arxiv_announce_type == 'new']

# search = arxiv.Search(query=query,max_results=150,sort_by=arxiv.SortCriterion.SubmittedDate,sort_order=arxiv.SortOrder.Descending)
# bar = tqdm(total=len(all_paper_ids),desc="Retrieving Arxiv papers")
# for i in range(0,len(all_paper_ids),50):
#     search = arxiv.Search(id_list=all_paper_ids[i:i+50])
#     # batch = [ArxivPaper(p) for p in client.results(search)]
#     batch = [p for p in client.results(search)]
#     bar.update(len(batch))
#     papers.extend(batch)
# bar.close()
# results = client.results(search)
# print(results)

query = "cat:cs.AI OR cat:cs.CV OR cat:cs.LG OR cat:cs.CL AND (ti:ego OR abs:egocentric)"
client = arxiv.Client(num_retries=10,delay_seconds=10)
search = arxiv.Search(query=query,sort_by=arxiv.SortCriterion.SubmittedDate,sort_order=arxiv.SortOrder.Descending)
paper = list(client.results(search))