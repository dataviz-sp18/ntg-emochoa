Accio Title!
================
Erin M. Ochoa
2018 May 29

``` r
clean_book <- function(book){
    local_book <- book
    local_book <- str_to_lower(local_book)
    #local_book <- replace_contraction(local_book)
    local_book <- gsub("'s",'',local_book)
    #local_book <- gsub('[[:punct:] ]+',' ',local_book)
    local_book <- gsub('[[:digit:] ]+',' ',local_book)
    local_book_list <- unlist(str_split(local_book, boundary('word')))
    s.words <- stopwords()
    local_book_list <- local_book_list[!(local_book_list)%in%c(stopwords(),'harry','said')]
    #local_book_clean <- wordStem(local_book_list)
}

dicto <- function(clean_book){
  dicto <- hash()
  for(i in 1:length(clean_book)){
    word <- clean_book[i]
    ct <- dicto[[as.character(eval(word))]]
    if(is.null(ct)){
      dicto[[as.character(eval(word))]] <- 1
    }
    else{
      dicto[[as.character(eval(word))]] <- (ct + 1)
    }
  }
  dicto
}

dicto2df <- function(dicto){
  df <- as.data.frame(hash::values(dicto))
  df <- setDT(df, keep.rownames = TRUE)[]
  colnames(df) <- c('word','freq')
  df
}

book2cloud <- function(book,num){
  clean_book <- clean_book(book)
  dicto <- dicto(clean_book)
  df <- dicto2df(dicto)
  set.seed(1337)
  wordcloud2(df)
  #letterCloud(data = df, word = num,size=2)
  #wordcloud2(df, figPath = '/Users/erin/Desktop/GitHub/emochoa/uc-dataviz/ntg-emochoa/twitter.jpg')
}
```

``` r
books <- c(philosophers_stone,
           chamber_of_secrets,
           prisoner_of_azkaban,
           goblet_of_fire,
           order_of_the_phoenix,
           half_blood_prince,
           deathly_hallows)

clean.ps <- clean_book(philosophers_stone)

#clean.ps
```

### Philosopher's Stone

``` r
cloud.ps <-  book2cloud(philosophers_stone,'1')
cloud.ps
```

![](wordcloud_files/figure-markdown_github/cloud1-1.png)

### Chamber of Secrets

``` r
cloud.cos <-  book2cloud(chamber_of_secrets,'2')
cloud.cos
```

![](wordcloud_files/figure-markdown_github/cloud2-1.png)

### Prizoner of Azkaban

``` r
cloud.poa <-  book2cloud(prisoner_of_azkaban,'3')
cloud.poa
```

![](wordcloud_files/figure-markdown_github/cloud3-1.png)

### Goblet of Fire

``` r
cloud.gof <-  book2cloud(goblet_of_fire,'4')
cloud.gof
```

![](wordcloud_files/figure-markdown_github/cloud4-1.png)

### Order of the Phoenix

``` r
cloud.otp <-  book2cloud(order_of_the_phoenix,'5')
cloud.otp
```

![](wordcloud_files/figure-markdown_github/cloud5-1.png)

### Half-Blood Prince

``` r
cloud.hbp <-  book2cloud(half_blood_prince,'6')
cloud.hbp
```

![](wordcloud_files/figure-markdown_github/cloud6-1.png)

### Deathly Hallows

``` r
cloud.dh <-  book2cloud(deathly_hallows,'7')
cloud.dh
```

![](wordcloud_files/figure-markdown_github/cloud7-1.png)
