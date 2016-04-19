KAGGLE HOME DEPOT COMPETITION


THE PROBLEM & THE COMPETITION

How can we improve the search results on HomeDepot.com? 

A search query should return a (ranked) list of relevant products, given information about those products (individually and collectively).

Specifically, in the context of the competition, how can we predict human evaluators' scores for query-product combinations?


THE DATA

The Home Depot dataset consists of five files: train.csv, product_descriptions.csv, attributes.csv, sample_submission.csv, and test.csv. 

The train.csv file contains the column headers: id, product_uid, product_title, search_term, and relevance. product_uid's and product_title's may appear multiple times, accompanied by different search_term's. relevance is a (continuous, non-integer) score between 1 and 3, an average of evaluators' scores.

The product_descriptions.csv file consists of product_uid - product_description pairs. Unlike in train.csv (and attributes.csv), there is no duplication of product_uid pairs: each product has one and only one description, corresponding to one and only one row. 
	
Finally, there is an attributes.csv file. On the Home Depot site, these attributes are essentially the bullet points below a product description, with each product containing a different number of bullet points, which correspond to different rows in the file. Some of these bullets are in fact metadata-data pairs (eg, "Material: Galvanized steel"). 

It should be noted that there are many more descriptions in the product_descriptions.csv file than there are titles in train.csv file, ie, many products lack a title. There are 124,428 descriptions (as measured by counting product_uid in product_descriptions.csv) and only 54,667 titles (as measured by counting product_uid in train.csv). This would appear to be an error on the part of the Home Depot.


THE APPROACH: TARGET & STRATEGY

To solve this problem, I sought to maximize for a common metric in informational retrieval, the F1 Score, my target. 

Specifically, F1 is the "harmonic mean between precision recall", or 

	F1 = 2 * ((precision * recall) / (precision + recall))

Here, precision "is the fraction of retrieved documents that are relevant to the query" [Wikipedia], equal to: the intersection of relevant documents and retrieved documents, divided by retrieved documents. Recall "is the fraction of the documents that are relevant to the query that are successfully retrieved" [Wikipedia], equal to: the intersection of relevant documents and retrieved documents, divided by *relevant* documents.

The strategy consisted of ensembling two machine learning algorithms, Random Forest and Naive Bayes, playing with different features and feature combinations. 

These features (or "vectors") were:

	- EXACT MATCH: between search term (as phrase) and product title, allowing only differences in case
	- OVERLAPPING WORDS: allowing differences in case
	- PERCENTAGE OVERLAPPING WORDS: allowing differences in case

These features also included various implementations of the TF-IDF heuristic, with the following bags of words:

	- product descriptions (all) + product titles
	- product descriptions (only those with product titles) + product titles
	- product titles alone (no descriptions)
	- product titles, descriptions, and attributes





Compare to a random toss. 



THE RESULTS



CONCLUSION







ACKNOWLEDGMENTS

Kyle Polich
Aaron Foss

