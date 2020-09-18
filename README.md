#### 1



#### 2

##### 2.1

1. NP -> NP PP and Noun -> Adj Noun. These two rules result in infinite (or max_expansion_num in our case) recursion, which leads to long sentences.
2. The probability to have n adj. for a noun is $(1/6)^n$.
3. The weight for NP -> NP PP should be smaller and that for Noun -> Adj Noun should be larger.
4. Lessen the weight for Det. -> every. Because there is less *every* for determiner in regular sentences than *a* and *the*.
5. every chief of staff with a fine delicious perplexed pickle pickled every delicious floor !
   every fine floor kissed the president .
   the pickle kissed a perplexed pickled pickle with a pickle !
   is it true that a floor understood a fine fine pickled pickle ?
   the delicious perplexed sandwich kissed every floor on the pickle in a floor with a fine pickled fine floor on the pickle on a president with the sandwich on a sandwich .
   a floor understood a sandwich .
   is it true that every pickle ate every chief of staff under a chief of staff on the floor ?
   is it true that every pickled pickled delicious floor ate a floor ?
   every perplexed fine president kissed a floor .
   is it true that a perplexed delicious president pickled the floor ?

##### 2.3

6. Add one rule in Root for emphasizing. Add one rule in S for clause to be the subject of one sentence. Add one rule for clause phrases. Add one rule for intransitive verbs. Add one rule for prepositional phrases to describing verbs. Add conjunctions to be used. Add adjective phrases to be described by adverbs (*very*). Add rules for verbs which can be followed by a clause.
7.  Sally on the delicious sandwich or every sandwich or Sally sighed .
   that every floor pickled a desk on a pickled perplexed president with the perplexed desk wanted Sally or a fine floor .
   it perplexed Sally that Sally thought that the fine chief of staff sighed and ate Sally and sighed and pickled a pickle on Sally and thought that a chief of staff sighed .
   the perplexed president sighed .
   every desk perplexed a floor on the delicious fine sandwich .
   Sally sighed and ate a very fine pickled pickled chief of staff .
   a floor sighed and sighed .
   the pickle thought that Sally ate the sandwich .
   a pickled desk and a desk wanted that Sally sighed in every fine pickle .
   the sandwich kissed the pickled chief of staff .
   
#### 4.1
1. I chose the fourth and the fifth phenomena to implement.
The fourth phenomenon is to generate “I wonder” sentences with so-called embedded questions. Since “I wonder” sentences contain wh-word and following embedded questions, I create a phrase called wh-word phrase. 

The fifth phenomenon is use singular and plural forms of verb to generate sentences. So, we set VerbT as verb with s (singular forms) and Verb_base as verb without s (plural forms).And NP_plu stands for noun phrase in plural forms, NP_sin stands for noun phrase in singular forms, VP_plu stands for verb phrase in plural forms and VP_sin stands for verb phrase in singular forms. 
