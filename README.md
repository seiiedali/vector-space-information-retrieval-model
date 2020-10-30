# vector space information retrieval model
 This text query system uses vector vector space model for indexing extracted tokens from documents.
 ## Indexing
 Tokens will be parsed through each document text and after some cleaning data(punctuation, white spaces), will be index based on vector space model concepts. Tokenized 
 word are stored in a dictionary with information about their repetition and associated document files. Finally tokens are inserted into another dictionary where their weight on TF-IDF scale are assessed. This data are ready to be any query process.
 ## Query
 After parsing the documents, program would ask you to enter a query up to 4 words. Entered query will be processed in the same way that document were parsed. Final result is ranked related documents which are assessed by Cosine Similarity formula based on TF-IDF values.