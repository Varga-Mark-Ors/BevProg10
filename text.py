def main():
    title="Howl's moving castle"
    genre="Japanese animation"
    writer="Miyazaki Hayao"
    date="2004"
    rating="8.2"
    language="Japanese"
    MainC="Sophie"
    duration="119"

    text= """{0} is a {1} film ,written by {2}.
    The film was produced in {3},It's imdb rating is {4}
    The main charachter's name {5} is who is a hatmaker
    the film is {6} mins long. The original language is {7} """

    print(text.format(title,genre,writer,date,rating,MainC,duration,language))
if __name__=="__main__":
    main()