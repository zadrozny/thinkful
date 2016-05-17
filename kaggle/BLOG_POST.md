# KAGGLE HOME DEPOT COMPETITION


## THE PROBLEM & THE COMPETITION

The [Home Depot Product Search Relevance Competition](https://www.kaggle.com/c/home-depot-product-search-relevance) asks:

How can we improve the search results on HomeDepot.com? 

A search query should return a (ranked) list of relevant products, given information about those products (individually and collectively).

Specifically, in the context of the competition, how can we predict human evaluators' scores for query-product combinations?


## THE DATA

The Home Depot dataset consists of five files: train.csv, product_descriptions.csv, attributes.csv, sample_submission.csv, and test.csv. 

The train.csv file contains the column headers: id, product_uid, product_title, search_term, and relevance. product_uid's and product_title's may appear multiple times, accompanied by different search_term's. relevance is a (continuous, non-integer) score between 1 and 3, an average of evaluators' scores.

The product_descriptions.csv file consists of product_uid - product_description pairs. Unlike in train.csv (and attributes.csv), there is no duplication of product_uid pairs: each product has one and only one description, corresponding to one and only one row. 
	
Finally, there is an attributes.csv file. On the Home Depot site, these attributes are essentially the bullet points below a product description, with each product containing a different number of bullet points, which correspond to different rows in the file. Some of these bullets are in fact metadata-data pairs (eg, "Material: Galvanized steel"). 

It should be noted that there are many more descriptions in the product_descriptions.csv file than there are titles in train.csv file, ie, many products lack a title. There are 124,428 descriptions (as measured by counting product_uid in product_descriptions.csv) and only 54,667 titles (as measured by counting product_uid in train.csv). This would appear to be an error on the part of the Home Depot.

For a file-by-file and column-by-column description of the data, see DATA_DICTIONARY.ipynb


## THE APPROACH: TARGET, STRATEGY, CHALLENGES

To solve this problem, I sought to maximize for a common metric in informational retrieval, the F1 Score, my target. 

Specifically, F1 is the "harmonic mean between precision recall", or 

	F1 = 2 * ((precision * recall) / (precision + recall))

Here, precision "is the fraction of retrieved documents that are relevant to the query" [[Wikipedia: Precision and Recall](https://en.wikipedia.org/wiki/Precision_and_recall)], equal to: the intersection of relevant documents and retrieved documents, divided by retrieved documents. Recall "is the fraction of the documents that are relevant to the query that are successfully retrieved" [[Wikipedia: Precision and Recall](https://en.wikipedia.org/wiki/Precision_and_recall)], equal to: the intersection of relevant documents and retrieved documents, divided by *relevant* documents.

The strategy consisted of ensembling two machine learning algorithms, Random Forest and Naive Bayes, playing with different features and feature combinations. 

These features (or "vectors") were:

	- EXACT MATCH: between search term (as phrase) and product title, allowing only differences in case
	- OVERLAPPING WORDS: allowing differences in case
	- PERCENTAGE OVERLAPPING WORDS: allowing differences in case
	- Jaccard Distance

These features also included two implementations of the TF-IDF heuristic, with the following bags of words:

	- product descriptions (all) + product titles
	- product titles, descriptions, and attributes


The evaluator scores are heavily biased towards 2's and 3's, as we might expect when dealing with a system that produces better than random results (ie, the system is engineered, so query results should be mostly somewhat or very useful rather than useless).

To adjust for this, I produced a "capped" subset of the data, with an even number of 1's, 2's, and 3's. 


## THE RESULTS

Mean F1 scores for the respective models, on all the data as well as the capped data, were:

|             |   All Data |   Capped  |
|-------------|:----------:|----------:|
|Random Forest|   0.280673 |   0.451411|
|Naive Bayes  |   0.438868 |   0.429971|


The best F1 scores for the respective models, on all the data as well as the capped data, were:

|             | All Data |  Capped   |
|-------------|:--------:|----------:|
|Random Forest|  0.334179|   0.483073|
|Naive Bayes  |  0.327057|   0.449479|



## CONCLUSION

In general, Naive Bayes performed substantially better on the whole / uncapped data set (0.43 vs 0.28), while Random Forest performed somewhat better on the capped data set (0.45 vs 0.42). These results may be distorted somewhat by the inclusion of classifications into two, rather than three, classes. 

As for the best F1 scores, here the differences were less extreme. Random forest performed somewhat better than Naive Bayes on all the data (0.33 vs 0.32), as well as on the capped data (0.48 vs 0.44).

Capping the data -- to ensure a roughly equal number of 1's, 2's, and 3's -- led to the best gains for both the whole and capped dataset.

Three things might improve future predictions: a larger dataset, better features, and / or different models. 


## ACKNOWLEDGMENTS

Many thanks to Kyle Polich for guidance throughout, and to Aaron Foss for help debugging. 
