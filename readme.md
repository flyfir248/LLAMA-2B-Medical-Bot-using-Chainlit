# **Chainlit Agent Based LLama model**

### User window

![img.png](img.png)

### Question based on text data in the pdf in data folder
##### here we are sourcing it from the 2004 edition of the book : Gale Encyclopedia Of Medicine

![img_1.png](img_1.png)
#### Here the response time highly depends on the Host computer resources as RAM and Processor (Min 8 GB RAM/Ideal 16 RAM).

![img_2.png](img_2.png)
#### Each of the Function calls can be tracked here to give the User a idea of the train of thought/process happening in the Background.

![img_3.png](img_3.png)
#### High lights
1.) Yellow text : This is the LLAMA 2B response.

2.) Pink text : This is the exact source from the ~600 Page Book from where the data was extracted and vectorized.

![img_4.png](img_4.png)
#### Chainlit is powerful as it allows for inbuilt customisations which are similar to streamlit.


![img_5.png](img_5.png)
#### Based on my understanding this can be expanded to other raw and unstructured Data sets as PPTS,Raw Docs,CSVs.
#### This gives a truely intelligent data outputs and is core in our Porject Usecase.

![img_6.png](img_6.png)
#### The Llama model can be replaced by any of the models downloaded from other sources as Huggingface Hub or Github in general.
##### This allows for a wide usecase application.

#### The creativity of the model can be changed or altered in the temperature parameter.

![img_7.png](img_7.png)
#### It also has the added advantage of reiterating ut's search as the old  queries and answers are left in memory.